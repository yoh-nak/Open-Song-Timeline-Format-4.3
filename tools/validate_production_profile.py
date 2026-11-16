#!/usr/bin/env python3
"""Draft 0.21 local authoring aid (behavior unchanged) for optional OSTF Production Session Profile 0.1/0.2.

Structural + selected semantic authoring checks only. No plugin loading, DAW/robot
execution, vendor interoperability, or independent runtime verification is claimed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import pathlib
import re
import sys
import urllib.parse
import wave
from collections import Counter

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Please install requirements.txt (jsonschema>=4.20,<5)")


# Strict parser from the companion local authoring utility.
from validate import strict_json

def err(msg: str):
    return f"E-PRODUCTION: {msg}"


def is_number(v):
    return type(v) in (float, int) and math.isfinite(v)


def safe_asset_uri(uri: str):
    """Interpret a bundle-relative Asset URI only once, identically across hosts.

    Percent encoding is decoded exactly once as strict UTF-8, independently in
    each POSIX path segment. An encoded separator, dot segment, Windows-reserved
    path or residual percent sign is rejected rather than ambiguously treated
    by different URI and file-system APIs. This is an authoring check, NOT a
    guarantee of safe arbitrary filesystem/HTTP access or a full security audit.
    """
    if not isinstance(uri, str) or not uri:
        return False, None, "empty or non-string asset URI"
    if any(ch.isspace() or ord(ch) < 32 or ord(ch) == 127 for ch in uri):
        return False, None, "whitespace/control characters require portable percent encoding"
    if '\\' in uri:
        return False, None, "backslash is not a portable URI path separator"
    try:
        parsed = urllib.parse.urlsplit(uri)
    except ValueError:
        return False, None, "malformed asset URI"
    if parsed.scheme:
        if parsed.scheme.lower() != 'https' or not parsed.netloc or not parsed.hostname or parsed.username or parsed.password:
            return False, None, "only authorized HTTPS external assets without embedded credentials are supported"
        return True, None, None  # never auto-fetch; the host must authorize it.
    if parsed.netloc or uri.startswith('/') or ':' in uri or '?' in uri or '#' in uri:
        return False, None, "unsafe or non-portable relative asset URI"
    decoded=[]
    for encoded_segment in uri.split('/'):
        if not encoded_segment or re.search(r'%(?![0-9A-Fa-f]{2})', encoded_segment):
            return False, None, "empty segment or malformed percent escape in asset URI"
        try:
            segment = urllib.parse.unquote_to_bytes(encoded_segment).decode('utf-8', 'strict')
        except UnicodeDecodeError:
            return False, None, "percent encoding must decode to valid UTF-8"
        if segment in ('.','..') or any(c in segment for c in '/\\<>:"|?*%'):
            return False, None, "dot segment, disguised separator, reserved character or ambiguous nested encoding"
        if segment != segment.strip(' ') or segment.endswith('.'):
            return False, None, "leading/trailing spaces or trailing dots are not portable across hosts"
        if any(ord(c) < 32 or ord(c) == 127 for c in segment):
            return False, None, "decoded control characters in URI segment"
        stem=segment.split('.',1)[0].upper()
        if stem in {'CON','PRN','AUX','NUL'} or re.fullmatch(r'(COM|LPT)[1-9]',stem):
            return False, None, "Windows-reserved filename in cross-platform asset URI"
        decoded.append(segment)
    return True, '/'.join(decoded), None


def source_selection_at_tick(data, tick):
    """Pure, illustrative 0.2 audition-source selection (NOT audio rendering).

    Compute Send.enabled effective values from static values and step automation.
    The graph is directed from source channels toward audible output channels.
    SoloSafe buses only preserve selected audio through host-side bus solo gating;
    they do not independently select unrelated source channels.
    """
    channels = data['channels']
    by_id = {c['id']: c for c in channels}
    send_switches = {}
    for a in data.get('automation', []):
        t = a['target']
        if t['kind'] == 'send' and t['parameter'] == 'enabled':
            value = None
            for pt in a['points']:
                if pt['atTick'] <= tick:
                    value = pt['value']
                else:
                    break
            if value is not None:
                send_switches[t['sendId']] = value
    graph = {}
    for c in channels:
        targets = []
        if c.get('outputChannelId') in by_id:
            targets.append(c['outputChannelId'])
        for send in c.get('sends', []):
            enabled = send_switches.get(send['id'], send['enabled'])
            if enabled and send['targetChannelId'] in by_id:
                targets.append(send['targetChannelId'])
        graph[c['id']] = targets
    solo = {c['id'] for c in channels if c['kind'] != 'master' and c['solo']}
    solo_bus = {c['id'] for c in channels if c['kind'] == 'bus' and c['solo']}
    sources = [c for c in channels if c['kind'] in ('track', 'audioTrack')]
    def reaches_solo_bus(start):
        visited = set()
        pending = [start]
        while pending:
            x = pending.pop()
            if x in visited:
                continue
            visited.add(x)
            if x in solo_bus:
                return True
            pending.extend(graph.get(x, ()))
        return False
    selected = [c['id'] for c in sources if not solo or c['solo'] or c['soloSafe'] or reaches_solo_bus(c['id'])]
    return {'sourceTick': tick, 'soloChannelIds': sorted(solo),
            'selectedSourceChannelIds': selected,
            'note': 'Selection only; mixer mute, score source enablement, regions, FX and acoustic output are not calculated.'}


def semantic_validate(data, profile_path, score_path=None):
    errors=[]
    channels=data['channels']; devices=data.get('devices',[]); assets=data.get('assets',[])
    automate=data.get('automation',[])
    audio_regions=data.get('audioRegions',[])
    sidechains=data.get('sidechainConnections',[])
    c_by={c['id']:c for c in channels}; d_by={d['id']:d for d in devices}; a_by={a['id']:a for a in assets}
    for label,vals in [('channels',[c['id'] for c in channels]),('devices',[d['id'] for d in devices]),('assets',[a['id'] for a in assets]),('automation',[a['id'] for a in automate]),('sends',[sd['id'] for c in channels for sd in c.get('sends',[])]),('audioRegions',[a['id'] for a in audio_regions]),('sidechainConnections',[x['id'] for x in sidechains])]:
        dup=[k for k,n in Counter(vals).items() if n>1]
        if dup: errors.append(err(f"duplicate {label} IDs: {dup}"))
    if len([c for c in channels if c['kind']=='master']) != 1:
        errors.append(err('exactly one channel.kind=master required'))
    for c in channels:
        ident=c['id']
        if c['kind']=='track':
            if 'trackId' not in c: errors.append(err(f'{ident} track channel needs trackId'))
        elif 'trackId' in c: errors.append(err(f'{ident} non-score-bound channel must not have trackId'))
        if c['kind']=='master':
            if 'outputChannelId' in c: errors.append(err('master must not have outputChannelId'))
        elif 'outputChannelId' not in c:
            errors.append(err(f'{ident} must have outputChannelId'))
        elif c['outputChannelId'] not in c_by or c_by[c['outputChannelId']]['kind'] not in ('bus','master'):
            errors.append(err(f'{ident} output must resolve to bus/master'))
        if c.get('outputChannelId') == ident: errors.append(err(f'{ident} cannot route to itself'))
        seen_inst=0
        for i,did in enumerate(c['deviceIds']):
            if did not in d_by:errors.append(err(f'{ident} has missing device {did}'));continue
            d=d_by[did]
            if d['role']=='instrument':
                seen_inst+=1
                if i!=0 or c['kind']!='track':errors.append(err(f'{ident} instrument must be first device on a track channel'))
        if seen_inst>1:errors.append(err(f'{ident} can have at most one instrument device'))
        for sd in c.get('sends',[]):
            tgt=c_by.get(sd['targetChannelId'])
            if not tgt or tgt['kind']!='bus':errors.append(err(f'{ident} send target {sd["targetChannelId"]} must be an existing bus'))
            if tgt and tgt['id']==ident:errors.append(err(f'{ident} send cannot target itself'))
    mapped=[c.get('trackId') for c in channels if 'trackId' in c]
    if len(set(mapped))!=len(mapped):errors.append(err('one source OSTF Track may map to at most one score-bound track channel'))
    used_ids=[did for c in channels for did in c['deviceIds']]
    if len(set(used_ids))!=len(used_ids):errors.append(err('same Device cannot be placed in multiple channel chains'))
    for d in devices:
        if d['id'] not in used_ids:errors.append(err(f'orphan device {d["id"]} not in a channel chain'))
        ref=d.get('stateAssetId')
        if ref and (ref not in a_by or a_by[ref]['purpose']!='pluginState'):
            errors.append(err(f'device {d["id"]} stateAssetId not a pluginState asset'))
    # Only 0.2 admits recording-only audio channels. The owner of a sidechain target
    # is determined by its unique appearance in an ordered Device chain.
    owners={did:c['id'] for c in channels for did in c['deviceIds']}
    occupied_ports=set()
    for link in sidechains:
        source=c_by.get(link['sourceChannelId'])
        target=d_by.get(link['targetDeviceId'])
        owner=owners.get(link['targetDeviceId'])
        if not source or source['kind']=='master':
            errors.append(err(f'sidechain {link["id"]} source must be a non-master channel'))
        if not target or target['role']!='effect' or owner is None:
            errors.append(err(f'sidechain {link["id"]} target must resolve to an owned effect device'))
        if owner==link['sourceChannelId']:
            errors.append(err(f'sidechain {link["id"]} self/feedback channel source is unsupported'))
        port=(link['targetDeviceId'],link['targetPortId'])
        if port in occupied_ports:
            errors.append(err(f'sidechain {link["id"]} targetPort already has a source; mix the keys explicitly on a bus'))
        occupied_ports.add(port)
    for region in audio_regions:
        chan=c_by.get(region['channelId'])
        asset=a_by.get(region['sourceAssetId'])
        if not chan or chan['kind'] not in ('track','audioTrack'):
            errors.append(err(f'audioRegion {region["id"]} must target a track or audioTrack channel'))
        if not asset or asset['purpose']!='audioSource':
            errors.append(err(f'audioRegion {region["id"]} must reference an audioSource asset'))
        else:
            if region['sourceStartFrame']+region['sourceFrameCount']>asset['frameCount']:
                errors.append(err(f'audioRegion {region["id"]} source frame selection is beyond the declared audio asset'))
            if chan and chan['audioChannels']!=asset['audioChannels']:
                errors.append(err(f'audioRegion {region["id"]} channel count mismatch; implicit downmix/upmix is not standardized'))
        if region.get('fadeInTicks',0)+region.get('fadeOutTicks',0)>region['durationTicks']:
            errors.append(err(f'audioRegion {region["id"]} fade interval sum exceeds region duration'))
    for c in channels:
        path=set();current=c
        while current and current['id'] not in path:
            path.add(current['id']);target=current.get('outputChannelId')
            if not target:break
            current=c_by.get(target)
        if current and current['id'] in path and current.get('outputChannelId'):
            errors.append(err(f'cycle in output routing from {c["id"]}'))
    # Output+send union graph must be acyclic for this introductory portable profile.
    graph={c['id']:([c['outputChannelId']] if c.get('outputChannelId') in c_by else [])+[s['targetChannelId'] for s in c.get('sends',[]) if s['targetChannelId'] in c_by] for c in channels}
    visiting=set();visited=set()
    def dfs(x):
        if x in visiting:return True
        if x in visited:return False
        visiting.add(x)
        if any(dfs(n) for n in graph[x]):return True
        visiting.remove(x);visited.add(x);return False
    # A sidechain is not audible output routing, but it can participate in a DSP
    # dependency cycle. The 0.2 portability subset forbids feedback loops.
    for link in sidechains:
        if link['sourceChannelId'] in graph and link['targetDeviceId'] in owners:
            graph[link['sourceChannelId']].append(owners[link['targetDeviceId']])
    if any(dfs(k) for k in graph):errors.append(err('combined output/send/sidechain routing dependency cycle detected'))
    for asset in assets:
        ok,local,reason=safe_asset_uri(asset['uri'])
        if not ok:
            errors.append(err(f'asset {asset["id"]}: {reason}'));continue
        if local:
            root=profile_path.parent.resolve()
            f=root/local
            # Reject symlink escapes as well as lexical traversal.
            if not f.is_file():errors.append(err(f'asset {asset["id"]} missing local file {local}'))
            elif not f.resolve().is_relative_to(root):
                errors.append(err(f'asset {asset["id"]} escapes Production Profile directory through symbolic link'))
            else:
                bs=f.read_bytes()
                if hashlib.sha256(bs).hexdigest()!=asset['sha256']:
                    errors.append(err(f'asset {asset["id"]} sha256 mismatch'))
                if 'byteLength' in asset and asset['byteLength']!=len(bs):
                    errors.append(err(f'asset {asset["id"]} byteLength mismatch'))
                if asset['purpose']=='audioSource' and asset.get('mediaType') in ('audio/wav','audio/x-wav','audio/wave'):
                    try:
                        with wave.open(str(f),'rb') as wav:
                            actual=(wav.getframerate(),wav.getnframes(),wav.getnchannels())
                        declared=(asset['sampleRateHz'],asset['frameCount'],asset['audioChannels'])
                        if actual!=declared:
                            errors.append(err(f'audioSource {asset["id"]} WAV frame metadata mismatch: declared={declared}, actual={actual}'))
                    except (wave.Error,EOFError,OSError) as ex:
                        errors.append(err(f'audioSource {asset["id"]} WAV decode/metadata failure: {ex}'))
        # HTTPS resource bytes are not downloaded automatically.
    if score_path:
        bs=score_path.read_bytes()
        if hashlib.sha256(bs).hexdigest()!=data['score']['sha256']:
            errors.append(err('score raw-byte sha256 mismatch'))
        try:score=json.loads(bs)
        except Exception as e:errors.append(err(f'score JSON parse: {e}'));score={}
        if score.get('format')!='OSTF' or score.get('version')!=data['score']['formatVersion']:
            errors.append(err('score format or version does not match source'))
        tids={x['id'] for x in score.get('tracks',[])}
        for c in channels:
            if c['kind']=='track' and c.get('trackId') not in tids:
                errors.append(err(f'channel {c["id"]} refers to a missing OSTF Track'))
        doc=score.get('document',{})
        if 'documentId' in data['score'] and data['score']['documentId']!=doc.get('id'):
            errors.append(err('score documentId mismatch'))
        if 'revisionId' in data['score'] and data['score']['revisionId']!=doc.get('revisionId'):
            errors.append(err('score revisionId mismatch'))
        ppq=score.get('ppq')
        timeline=score.get('timeline',{})
        tempo_changes=sorted(timeline.get('tempoChanges',[]),key=lambda v:v.get('at',0))
        # For native/fit audio, mapping Tick to actual seconds requires authored
        # source tempo. Do not fabricate 120 BPM or inherit a skipped Visit Tempo.
        for region in audio_regions:
            applicable=[t for t in tempo_changes if t.get('at',0)<=region['startTick']]
            if not applicable or not is_number(applicable[-1].get('bpm')) or applicable[-1]['bpm']<=0:
                errors.append(err(f'audioRegion {region["id"]} has no valid effective source OSTF Tempo at its startTick'))
        boundary=max([section['start']+section['duration'] for section in timeline.get('sections',[])]+[clip['start']+clip['duration'] for track in score.get('tracks',[]) for clip in track.get('clips',[])]+[0])
        if boundary:
            for a in automate:
                if any(pt['atTick']>boundary for pt in a['points']):
                    errors.append(err(f'automation {a["id"]} point beyond source duration'))
    seen_targets=set()
    for a in automate:
        tgt=a['target']
        kind=tgt['kind']
        param=tgt.get('parameter')
        if kind=='channel':
            if tgt['channelId'] not in c_by:errors.append(err(f'automation {a["id"]} has missing channel'))
            is_bool=param=='mute'
        elif kind=='device':
            if tgt['deviceId'] not in d_by:errors.append(err(f'automation {a["id"]} has missing device'))
            is_bool=False
        elif kind=='deviceControl':
            if tgt['deviceId'] not in d_by:errors.append(err(f'automation {a["id"]} has missing device control'))
            is_bool=True
        elif kind=='send':
            send_ids={sd['id'] for channel in channels for sd in channel.get('sends',[])}
            if tgt['sendId'] not in send_ids:errors.append(err(f'automation {a["id"]} references missing send'))
            is_bool=param=='enabled'
        elif kind=='audioRegion':
            if tgt['audioRegionId'] not in {r['id'] for r in audio_regions}:
                errors.append(err(f'automation {a["id"]} references missing audio Region'))
            is_bool=param=='mute'
        else:
            errors.append(err(f'automation {a["id"]} has unknown target kind'))
            is_bool=False
        expected_type='boolean' if is_bool else 'number'
        if a['valueType']!=expected_type:
            errors.append(err(f'automation {a["id"]} target {kind}.{param} requires valueType {expected_type}'))
        identity=json.dumps(tgt,sort_keys=True)
        if identity in seen_targets:errors.append(err(f'duplicate automation target {identity}'))
        seen_targets.add(identity)
        vals=[p['atTick'] for p in a['points']]
        if len(vals)!=len(set(vals)) or vals!=sorted(vals):
            errors.append(err(f'automation {a["id"]} atTick values must be strictly increasing'))
        if a['valueType']=='boolean' and a['interpolation']!='step':
            errors.append(err(f'automation {a["id"]} boolean interpolation must be step'))
        for p in a['points']:
            v=p['value']
            if a['valueType']=='boolean' and type(v)!=bool:
                errors.append(err(f'automation {a["id"]} boolean value expected'))
            if a['valueType']=='number' and not is_number(v):
                errors.append(err(f'automation {a["id"]} numeric value expected'))
            if is_number(v) and kind in ('channel','send','audioRegion'):
                if param=='pan' and not (-1<=v<=1):errors.append(err(f'automation {a["id"]} pan out of range'))
                if param=='gainDb' and not (-120<=v<=24):errors.append(err(f'automation {a["id"]} gainDb out of range'))
            if is_number(v) and kind=='device' and not (0<=v<=1):
                errors.append(err(f'automation {a["id"]} normalized plugin parameter out of range'))
    return errors


def check_joint_score_association(production, distributed, pinned_score_bytes):
    """Draft 0.19 opt-in *data association*, not host/session permission.

    Assumes both documents have passed their own structural checks, and that
    original Score bytes are available. No network/asset/plugin access.
    """
    problems=[]
    digest=hashlib.sha256(pinned_score_bytes).hexdigest()
    ps=production['score']
    if ps['sha256'] != distributed['scoreSha256'] or digest != ps['sha256']:
        problems.append('E-CROSS-PROFILE-SCORE-HASH: original OSTF bytes and both declared digests differ')
    try:
        doc=json.loads(pinned_score_bytes)
    except (UnicodeDecodeError,json.JSONDecodeError) as ex:
        return problems+['E-CROSS-PROFILE-DOCUMENT: original score cannot be parsed: '+str(ex)]
    if doc.get('format')!='OSTF' or doc.get('version')!='4.3.0':
        problems.append('E-CROSS-PROFILE-DOCUMENT: original source is not OSTF 4.3.0')
    identity=doc.get('document',{})
    if distributed['documentId'] != identity.get('id'):
        problems.append('E-CROSS-PROFILE-DOCUMENT: Distributed documentId does not match original Score')
    if distributed['revisionId'] != identity.get('revisionId'):
        problems.append('E-CROSS-PROFILE-REVISION: Distributed revisionId does not match original Score')
    if 'documentId' in ps and ps['documentId'] != distributed['documentId']:
        problems.append('E-CROSS-PROFILE-DOCUMENT: Production and Distributed documentId differ')
    if 'revisionId' in ps and ps['revisionId'] != distributed['revisionId']:
        problems.append('E-CROSS-PROFILE-REVISION: Production and Distributed revisionId differ')
    matching_plan=[p for p in doc.get('performancePlans',[]) if p.get('id')==distributed['performancePlanId']]
    if not matching_plan or matching_plan[0].get('mode')!='orderedFinite':
        problems.append('E-CROSS-PROFILE-PLAN: remote Plan must resolve to orderedFinite Core Plan')
    tracks={t['id'] for t in doc.get('tracks',[])}
    for ch in production.get('channels',[]):
        if ch['kind']=='track' and ch.get('trackId') not in tracks:
            problems.append(f'E-CROSS-PROFILE-TRACK: Production channel {ch["id"]} references missing Core Track')
    if distributed.get('recordType')=='snapshot':
        for participant in distributed.get('participants',[]):
            for track in participant.get('assignedTrackIds',[]):
                if track not in tracks:
                    problems.append(f'E-CROSS-PROFILE-TRACK: remote participant {participant["participantId"]} references missing Core Track {track}')
    elif distributed.get('recordType')=='event':
        target=distributed.get('payload',{}).get('targetTrackId')
        if target is not None and target not in tracks:
            problems.append(f'E-CROSS-PROFILE-TRACK: remote event references missing Core Track {target}')
    return problems


def preview_score_revision_rebind(production, original_bytes, candidate_bytes, score_schema):
    """Conservative, read-only, non-lossless Score edit preview.

    This tool does NOT create or approve a Production Profile/Session migration;
    score metadata and schema checks are not proof of musical equivalence.
    """
    problems=[]
    old_digest=hashlib.sha256(original_bytes).hexdigest()
    new_digest=hashlib.sha256(candidate_bytes).hexdigest()
    report={
        'status':'REVIEW_REQUIRED',
        'profile_unchanged':True,
        'original_score_sha256':old_digest,
        'candidate_score_sha256':new_digest,
        'bytes_changed': old_digest!=new_digest,
        'remote_session_action':'NEW_SESSION_REQUIRED_IF_SCORE_CHANGED',
        'lossless_migration_certified':False,
    }
    try:
        old=json.loads(original_bytes.decode('utf-8','strict'))
        new=json.loads(candidate_bytes.decode('utf-8','strict'))
    except (UnicodeDecodeError,json.JSONDecodeError) as ex:
        return dict(report,status='BLOCKED',reason='E-REBIND-SCORE-INVALID: '+str(ex)),[str(ex)]
    schema_validator=Draft202012Validator(score_schema)
    for which,doc in (('old',old),('candidate',new)):
        errs=list(schema_validator.iter_errors(doc))
        if errs:
            problems.append(f'E-REBIND-SCORE-INVALID: {which} Score fails 4.3 structure: {errs[0].message}')
    for which,doc in (('old',old),('candidate',new)):
        if doc.get('format')!='OSTF' or doc.get('version')!='4.3.0':
            problems.append(f'E-REBIND-SCORE-INVALID: {which} is not OSTF 4.3.0')
    old_identity=old.get('document') or {}
    new_identity=new.get('document') or {}
    old_id, new_id=old_identity.get('id'),new_identity.get('id')
    old_rev, new_rev=old_identity.get('revisionId'),new_identity.get('revisionId')
    report['old_document_id']=old_id
    report['candidate_document_id']=new_id
    report['old_revision_id']=old_rev
    report['candidate_revision_id']=new_rev
    if production['score']['sha256']!=old_digest:
        problems.append('E-REBIND-SCORE-HASH: Production does not pin the supplied original Score bytes')
    if 'documentId' in production['score'] and production['score']['documentId']!=old_id:
        problems.append('E-REBIND-IDENTITY: authored old Production document ID mismatch')
    if 'revisionId' in production['score'] and production['score']['revisionId']!=old_rev:
        problems.append('E-REBIND-IDENTITY: authored old Production revision ID mismatch')
    if not old_id or not new_id or old_id!=new_id:
        problems.append('E-REBIND-IDENTITY: same-song revision lineage needs matching explicit document.id')
    if not old_rev or not new_rev:
        problems.append('E-REBIND-IDENTITY: same-song revision lineage needs both revisionId values')
    if old_digest!=new_digest and old_rev==new_rev:
        problems.append('E-REBIND-REVISION-REUSE: changed source bytes may not reuse revisionId')
    old_tracks={t['id'] for t in old.get('tracks',[]) if isinstance(t,dict) and 'id' in t}
    new_tracks={t['id'] for t in new.get('tracks',[]) if isinstance(t,dict) and 'id' in t}
    referenced={ch['trackId'] for ch in production.get('channels',[]) if ch.get('kind')=='track' and 'trackId' in ch}
    missing=sorted(referenced-new_tracks)
    report['production_track_refs_missing_in_candidate']=missing
    if missing:
        problems.append('E-REBIND-TRACK-UNRESOLVED: '+', '.join(missing))
    report['ppq_changed']=old.get('ppq')!=new.get('ppq')
    old_time=old.get('timeline') or {}; new_time=new.get('timeline') or {}
    report['sections_changed']=old_time.get('sections')!=new_time.get('sections')
    report['tempo_changes_changed']=old_time.get('tempoChanges')!=new_time.get('tempoChanges')
    report['meter_changes_changed']=old_time.get('meterChanges')!=new_time.get('meterChanges')
    report['performance_plans_changed']=old.get('performancePlans')!=new.get('performancePlans')
    report['source_tick_review_required']=any(report[k] for k in ('ppq_changed','sections_changed','tempo_changes_changed','meter_changes_changed'))
    report['visit_projection_review_required']=report['source_tick_review_required'] or report['performance_plans_changed']
    report['native_audio_frame_mapping_review_required']=bool(report['tempo_changes_changed'] or report['ppq_changed'])
    report['author_action']='Review source Tick mappings and musical meaning; explicitly author a new Production copy with new Score hash and matching identity. Do not mutate old files.'
    if problems:
        report['status']='BLOCKED';report['issues']=problems
    elif old_digest==new_digest:
        report['status']='UNCHANGED_BYTES';report['author_action']='No Score content re-pin is needed; this does not certify Production sound or remote Session state.'
    return report,problems


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('profile',type=pathlib.Path)
    p.add_argument('--score',type=pathlib.Path,help='Path to exact original score .ostf bytes')
    p.add_argument('--distributed',type=pathlib.Path,help='Optional Distributed Session Profile 0.2 Snapshot/Event to compare with this Production Profile (requires --score)')
    p.add_argument('--rebind-target',type=pathlib.Path,help='Read-only comparison against candidate new OSTF Score revision (requires --score with original bytes; never writes/migrates)')
    p.add_argument('--explain-audition', action='store_true',
                   help='Print portable 0.2 source-selection model (not audio rendering)')
    p.add_argument('--at-tick', type=int, default=0,
                   help='Original Score source Tick for selection example, default 0')
    args=p.parse_args()
    if args.distributed and args.score is None:
        p.error('--distributed requires --score with exact original OSTF bytes')
    if args.rebind_target and args.score is None:
        p.error('--rebind-target requires --score with the Production Profile original pinned Score bytes')
    root=pathlib.Path(__file__).resolve().parents[1]
    data=strict_json(args.profile)
    version=data.get('profileVersion')
    if version != '0.2.0':
        sys.exit('This release utility accepts Production Profile 0.2.0 only; use the historical distribution for 0.1.0')
    schema_file='ostf-production-session-0.2.schema.json'
    schema=json.loads((root/'schema'/schema_file).read_text())
    errs=list(Draft202012Validator(schema).iter_errors(data))
    if errs:
        for e in errs:print('E-SCHEMA:',e.message,file=sys.stderr)
        sys.exit(1)
    e=semantic_validate(data,args.profile,args.score)
    if args.distributed:
        try:
            distributed=strict_json(args.distributed)
            remote_schema=json.loads((root/'schema'/'ostf-distributed-session-0.2.schema.json').read_text(encoding='utf-8'))
            remote_errors=list(Draft202012Validator(remote_schema).iter_errors(distributed))
            if remote_errors:
                e.extend(err(f'E-CROSS-PROFILE-REMOTE-SCHEMA: {x.message}') for x in remote_errors)
            elif distributed.get('profile') != 'OSTF-Distributed-Session-0.2':
                e.append(err('E-CROSS-PROFILE-REMOTE-VERSION: expected Distributed Session Profile 0.2'))
            else:
                e.extend(err(x) for x in check_joint_score_association(data,distributed,args.score.read_bytes()))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as ex:
            e.append(err('E-CROSS-PROFILE-INPUT: '+str(ex)))
    if args.rebind_target and not e:
        try:
            full_schema=json.loads((root/'schema'/'ostf-4.3.0.schema.json').read_text(encoding='utf-8'))
            preview, preview_errors=preview_score_revision_rebind(data,args.score.read_bytes(),args.rebind_target.read_bytes(),full_schema)
            print('READ-ONLY REBIND PREVIEW:',json.dumps(preview,ensure_ascii=False,sort_keys=True))
            e.extend(err(x) for x in preview_errors)
        except (OSError,UnicodeDecodeError,json.JSONDecodeError) as ex:
            e.append(err('E-REBIND-INPUT: '+str(ex)))
    for msg in e:print(msg,file=sys.stderr)
    if e:sys.exit(2)
    if args.explain_audition:
        if args.at_tick < 0:
            sys.exit('--at-tick must be nonnegative')
        if version == '0.2.0':
            print('AUDITION MODEL:', json.dumps(source_selection_at_tick(data, args.at_tick), ensure_ascii=False))
        else:
            print('AUDITION MODEL: Profile 0.1 retains historical host-dependent Solo behavior; no 0.2 selection rule inferred.')
    if args.distributed:
        print('CROSS-PROFILE BINDING DATA CHECK PASS:', args.distributed, '(not hardware routing, independent interoperability or permissions)')
    if args.rebind_target:
        print('REBIND PREVIEW ONLY: no Score, Production Profile or remote Session was edited')
        print('ORIGINAL PROFILE STATIC CHECK PASS:',args.profile,'(candidate re-bind still requires author review; no migration happened)')
    else:
        print('LOCAL AUTHORING PASS:',args.profile,'schema & selected semantic checks (NOT runtime interoperability)')


if __name__=='__main__':main()
