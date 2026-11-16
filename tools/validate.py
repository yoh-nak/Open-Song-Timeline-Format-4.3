#!/usr/bin/env python3
"""OSTF 4.3.0 local authoring/reference checker. Not a complete semantic validator.

Requires `jsonschema`. Selected checks here are authoring aids; they are NOT
an interoperability certification, and do not mistake local checks for a DAW, WAN or third-party interoperability certification.
It cannot verify 0.9 cross-record log consistency, score revision immutability,
remote clock state or whether physical performers actually sounded notes.
"""
from __future__ import annotations
import argparse, json, pathlib, sys, hashlib, collections
try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit('Install jsonschema first: python -m pip install jsonschema')

ROOT=pathlib.Path(__file__).resolve().parents[1]

class DuplicateKey(ValueError): pass

def strict_json(path):
    """Reject duplicate keys, non-finite/underflowing numbers and invalid text."""
    import math
    from decimal import Decimal
    def pairs(items):
        obj = {}
        for key, value in items:
            if key in obj:
                raise DuplicateKey('duplicate JSON key ' + repr(key))
            obj[key] = value
        return obj
    def number(text):
        value = float(text)
        if not math.isfinite(value) or (value == 0 and Decimal(text) != 0):
            raise ValueError('non-finite or underflowing JSON number ' + text)
        return value
    def bad_constant(text):
        raise ValueError('non-finite JSON number ' + text)
    text = pathlib.Path(path).read_text(encoding='utf-8')
    data = json.loads(text, object_pairs_hook=pairs, parse_float=number, parse_constant=bad_constant)
    def unicode_check(value):
        if isinstance(value, str):
            value.encode('utf-8', errors='strict')
        elif isinstance(value, dict):
            for key, item in value.items():
                unicode_check(key); unicode_check(item)
        elif isinstance(value, list):
            for item in value:
                unicode_check(item)
    unicode_check(data)
    return data

def overlap(a,b):return max(a[0],b[0])<min(a[1],b[1])
def interval(t):return (t['start'],t['start']+t['duration'])
def validate_43_semantics(doc):
    errors=[]
    def e(path,msg):errors.append(path+': '+msg)
    if doc.get('format')!='OSTF' or doc.get('version')!='4.3.0':return ['root: not OSTF 4.3.0']
    seen={}
    def register(obj,path):
        if not isinstance(obj,dict):return
        ident=obj.get('id')
        if isinstance(ident,str):
            if ident in seen:e(path,'duplicate Core ID '+repr(ident)+' also at '+seen[ident])
            else:seen[ident]=path
    # Core ID indexing here intentionally avoids arbitrary `extensions` and payload keys.
    for key in ['timeline','tracks','lyrics','harmony','phraseLibrary','ensembleInteractions','performancePlans']:
        data=doc.get(key)
        def recurse(v,p):
            if isinstance(v,dict):
                if p.endswith('.document'):return
                register(v,p)
                for k,w in v.items():
                    # Scale targets are typed references, not new Core objects.
                    if p.startswith('harmony.scales[') and k == 'targets':
                        continue
                    if k in ('extensions','data','midi','parameters','sourceRange','requiredPitchRange','scope','capabilities','vocalProfile','refs','ref','target','sourceRef','targetRef'):continue
                    recurse(w,p+'.'+k)
            elif isinstance(v,list):
                for i,w in enumerate(v):recurse(w,p+f'[{i}]')
        recurse(data,key)
    timeline=doc.get('timeline',{})
    sections={x['id']:x for x in timeline.get('sections',[])}
    tracks={x['id']:x for x in doc.get('tracks',[])}
    lyric=doc.get('lyrics',{})
    voices={x['id']:x for x in lyric.get('voices',[])}
    docs={x['id']:x for x in lyric.get('documents',[])}
    lyricphrases={x['id']:x for x in lyric.get('phrases',[])}
    templates={x['id']:x for x in doc.get('phraseLibrary',{}).get('templates',[])}
    plans={x['id']:x for x in doc.get('performancePlans',[])}
    planVisits={p['id']:{v['id']:v for v in p.get('visits',[])} for p in plans.values()}
    duration=timeline.get('duration',0)
    for sec in sections.values():duration=max(duration,sec['start']+sec['duration'])
    def visit_intervals(visit,path):
        if 'sourceRange' in visit:
            r=visit['sourceRange']; i=(r['start'],r['start']+r['duration'])
            if i[1]>duration:e(path,'sourceRange exceeds source timeline')
            return [i]
        ints=[]
        for sid in visit.get('sourceSectionIds',[]):
            if sid not in sections:e(path,'unknown section '+sid);continue
            ints.append(interval(sections[sid]))
        for i in range(len(ints)):
            for j in range(i+1,len(ints)):
                if overlap(ints[i],ints[j]):e(path,'overlapping Section spans in one Visit')
        return ints
    for ti,t in enumerate(doc.get('tracks',[])):
        p=f'tracks[{ti}]'; ds=t.get('directions',[])
        req=t.get('performanceRequirements',{})
        if 'requiredPitchRange' in req:
            r=req['requiredPitchRange']
            if r['lowPitch']>r['highPitch']:e(p,'required pitch range min > max')
            cap=t.get('instrument',{}).get('playablePitchRange')
            if cap and (r['lowPitch']<cap['lowPitch'] or r['highPitch']>cap['highPitch']):e(p,'required pitch range outside authored playablePitchRange')
        for di,d in enumerate(ds):
            path=p+f'.directions[{di}]'
            params=d.get('parameters',{})
            if d['type']=='phrasing':
                for key in ('phraseLengthTicks','onsetGroupsPerQuarter'):
                    x=params.get(key)
                    if x and x['min']>x['max']:e(path,key+' min > max')
                if params.get('motifRef') and params['motifRef'] not in templates:e(path,'motifRef not in phraseLibrary.templates')
            elif d['type']=='vocalFreedom':
                v=voices.get(params.get('voiceId'))
                if not v:e(path,'unknown Lyric Voice');continue
                if v['trackId']!=t['id']:e(path,'Lyric Voice belongs to another Track')
                if params.get('textPolicy')=='alternatives':
                    alternatives=[]
                    for g in params.get('candidatePhraseSets',[]):
                        alternatives.append(tuple(g['phraseIds']))
                        for pid in g['phraseIds']:
                            phrase=lyricphrases.get(pid)
                            if not phrase:e(path,'unknown candidate lyric phrase '+pid)
                            elif phrase['documentId']!=v['documentId']:e(path,'candidate phrase document does not match Voice')
                    if len(set(alternatives))!=len(alternatives):e(path,'candidate phrase sets must differ')
            if d['type'] in ('phrasing','vocalFreedom'):
                for old in ds[:di]:
                    if old['type']!=d['type']:continue
                    if d['type']=='vocalFreedom' and old.get('parameters',{}).get('voiceId')!=params.get('voiceId'):continue
                    if overlap(interval(old),interval(d)):e(path,'overlapping same-kind Direction on Track/Voice')
    for pi,plan in enumerate(doc.get('performancePlans',[])):
        path=f'performancePlans[{pi}]'
        visits=plan['visits']
        if sorted(v['ordinal'] for v in visits)!=list(range(len(visits))):e(path,'ordinals must be contiguous zero-based and unique')
        for vi,v in enumerate(visits):
            vp=path+f'.visits[{vi}]'; ranges=visit_intervals(v,vp)
            seenparts=set()
            for pt in v['parts']:
                tid=pt['trackId']
                if tid in seenparts:e(vp,'duplicate Track part '+tid)
                seenparts.add(tid)
                if tid not in tracks:e(vp,'unknown Track '+tid);continue
                if 'replacesDirectionIds' in pt and 'role' not in pt:e(vp,'replacesDirectionIds requires role')
                replaces=set(pt.get('replacesDirectionIds',[]))
                ds=tracks[tid].get('directions',[])
                for rid in replaces:
                    if not any(d['id']==rid and d['type']=='playingRole' for d in ds):e(vp,'replacesDirectionIds must reference own playingRole Direction '+rid)
                    elif not any(d['id']==rid and d['type']=='playingRole' and any(overlap(r,interval(d)) for r in ranges) for d in ds):e(vp,'replaced playingRole Direction does not intersect this Visit '+rid)
                if 'role' in pt:
                    for d in ds:
                        if d['type']=='playingRole' and d['parameters']['role']!=pt['role'] and any(overlap(r,interval(d)) for r in ranges) and d['id'] not in replaces:
                            e(vp,'conflicting playingRole Direction requires replacesDirectionIds '+d['id'])
    for ii,x in enumerate(doc.get('ensembleInteractions',[])):
        path=f'ensembleInteractions[{ii}]'
        a=x['actorTrackId'];b=x['partnerTrackId']
        if a not in tracks or b not in tracks:e(path,'unknown Track reference')
        if a==b:
            av=x.get('actorVoiceId'); pv=x.get('partnerVoiceId')
            if not av or not pv or av==pv:
                e(path,'same-Track Interaction requires two distinct explicit Lyric Voice IDs')
        if x.get('actorVoiceId') and x.get('actorVoiceId')==x.get('partnerVoiceId'):
            e(path,'actor Voice cannot respond to itself')
        for vid,tid in [('actorVoiceId',a),('partnerVoiceId',b)]:
            if vid in x:
                v=voices.get(x[vid]);
                if not v or v['trackId']!=tid:e(path,'invalid '+vid+' association')
        if 'scope' in x:
            p=x['scope']['performancePlanId'];v=x['scope']['visitId']
            if p not in plans or v not in planVisits.get(p,{}):e(path,'unknown performance Plan/Visit reference')
            elif 'start' in x:
                iv=interval(x)
                if not any(overlap(r,iv) for r in visit_intervals(planVisits[p][v],path+'.scope')):
                    e(path,'interaction source range does not intersect scoped Visit')
        if 'start' in x and x['start']+x['duration']>duration:e(path,'source range exceeds timeline')
    return errors

def _expanded_plan(doc, plan_id):
    """Construct deterministic finite Visit/source layouts (for editorial cross-document checks)."""
    sections = {v['id']:v for v in doc['timeline'].get('sections', [])}
    plans = {p['id']:p for p in doc.get('performancePlans',[])}
    if plan_id not in plans:
        raise ValueError('unknown pinned performancePlanId '+repr(plan_id))
    plan = plans[plan_id]
    offset = 0
    visits = {}
    for v in sorted(plan['visits'],key=lambda v:v['ordinal']):
        pieces=[]
        if 'sourceRange' in v:
            r=v['sourceRange'];pieces=[(r['start'],r['start']+r['duration'])]
        else:
            for sid in v['sourceSectionIds']:
                if sid not in sections:raise ValueError('unknown Section ID '+repr(sid))
                r=sections[sid];pieces.append((r['start'],r['start']+r['duration']))
        segment_positions=[]
        start=offset
        for sr0,sr1 in pieces:
            segment_positions.append((sr0,sr1,offset,offset+(sr1-sr0)))
            offset+=sr1-sr0
        visits[v['id']]={'start':start,'end':offset,'parts':v.get('parts',[]),'segments':segment_positions}
    return plan,visits,offset

def validate_pinned_session(record, doc, pinned_plan_id=None, score_digest=None):
    """Optional development-only cross-document checks. Cannot certify a complete event log."""
    errors=[]
    if record.get('profile')!='OSTF-Distributed-Session-0.2':
        return errors
    ident=doc.get('document',{})
    if record['documentId']!=ident.get('id') or record['revisionId']!=ident.get('revisionId'):
        errors.append('pinned OSTF documentId/revisionId mismatch')
        return errors
    # Draft 0.9: a record pins a Plan even when it has no Position (e.g. prepared).
    # This is not inferred from the only Plan, from a first item, or from an API URL.
    declared_plan=record['performancePlanId']
    if pinned_plan_id and declared_plan!=pinned_plan_id:
        errors.append('record performancePlanId differs from --pinned-plan-id')
    if score_digest is not None and record['scoreSha256']!=score_digest:
        errors.append('E-SESSION-SCORE-DIGEST: OSTF document bytes do not match scoreSha256')
    pinned_plan_id=declared_plan
    try:plan,visits,total=_expanded_plan(doc,pinned_plan_id)
    except ValueError as ex:return [str(ex)]
    tracks={t['id'] for t in doc['tracks']}
    def check_position(pos,where,requires_timed_anchor=False):
        # Draft 0.12: source tempo is indispensable for a playing musical-to-UTC
        # anchor, even when the optional redundancy position.tempoBpm is absent.
        # Prepared/stopped informational positions are not running anchors.
        from decimal import Decimal
        candidates=[item for item in doc['timeline']['tempoChanges'] if item['at']<=pos['sourceTick']]
        if not candidates:
            if requires_timed_anchor or 'tempoBpm' in pos:
                errors.append(where+': E-SESSION-TEMPO-UNRESOLVED: no source Tempo at the musical clock anchor')
        elif 'tempoBpm' in pos:
            effective=max(candidates,key=lambda item:item['at'])['bpm']
            if Decimal(str(pos['tempoBpm']))!=Decimal(str(effective)):
                errors.append(where+': E-SESSION-TEMPO-CONFLICT: tempoBpm disagrees with source OSTF Tempo')
        if pos['performancePlanId']!=record['performancePlanId']:
            errors.append(where+': position pins another Plan than envelope')
        v=visits.get(pos['visitId'])
        if v is None:
            errors.append(where+': unknown Visit')
        elif not any(s0<=pos['sourceTick']<s1 and performance0+(pos['sourceTick']-s0)==pos['performanceTick'] for s0,s1,performance0,_ in v['segments']):
            errors.append(where+': sourceTick, performanceTick and visitId do not map')
    def allocation(tid,tick,duration,where):
        if tid not in tracks:
            errors.append(where+': targetTrackId is not in the pinned OSTF')
            return
        end=tick+duration
        if tick<0 or end>total:
            errors.append(where+': phrase outside finite Performance Plan')
            return
        visit=next((v for v in visits.values() if v['start']<=tick<v['end']),None)
        if not visit or end>visit['end']:
            errors.append(where+': phrase crosses Visit boundary; split and re-propose')
            return
        pt=next((p for p in visit['parts'] if p['trackId']==tid),None)
        actual=pt['realization'] if pt else plan['defaultRealization']
        if actual!='open':
            errors.append(where+': committed session phrase requires open Plan Part, got '+repr(actual))
    def check_committed(c,where):
        allocation(c['targetTrackId'],c['effectivePerformanceTick'],c['phrase']['durationTicks'],where)
    if record['recordType']=='snapshot':
        if 'position' in record:check_position(record['position'],'snapshot.position',record['sessionStatus']=='playing')
        assigned=set()
        for person in record['participants']:
            for tid in person.get('assignedTrackIds',[]):
                assigned.add(tid)
                if tid not in tracks:errors.append('participant '+person['participantId']+': unknown Track '+repr(tid))
        accepted=record.get('committedPhrases',[])
        identities=set();ranges={}
        current_tick=record.get('position',{}).get('performanceTick')
        for i,c in enumerate(accepted):
            path=f'committedPhrases[{i}]';check_committed(c,path)
            k=c['targetTrackId'];r=(c['effectivePerformanceTick'],c['effectivePerformanceTick']+c['phrase']['durationTicks'])
            # Earlier historical accepted phrases may be retained after a forward Visit skip
            # or terminal stop. Such history is not an assertion of present/future assignment.
            still_relevant=record['sessionStatus']!='stopped' and (current_tick is None or r[1]>current_tick)
            if still_relevant and k not in assigned:
                errors.append(path+': still-relevant committed Track has no assigned Participant')
            cid=c['commitEventId']
            if cid in identities:errors.append(path+': duplicate commitEventId in Snapshot')
            identities.add(cid)
            for old in ranges.get(k,[]):
                if overlap(r,old):errors.append(path+': competing accepted phrases overlap on one Track')
            ranges.setdefault(k,[]).append(r)
        if 'commitmentWindow' in record:
            w=record['commitmentWindow']
            if w['endPerformanceTick']>total:
                errors.append('commitmentWindow exceeds expanded finite Plan')
            # Completeness of the phrase set cannot be established without the authority's log.
    else:
        kind=record['kind'];payload=record['payload']
        if kind=='phraseCommitted':
            allocation(payload['targetTrackId'],record['effectivePerformanceTick'],payload['phrase']['durationTicks'],'phraseCommitted')
        if kind=='sessionStateChanged':
            if payload['changeKind']=='sessionStarted':
                check_position(payload['position'],'sessionStarted.position',True)
                if payload['position']['performanceTick']!=record['effectivePerformanceTick']:
                    errors.append('sessionStarted anchor Tick must equal event effectivePerformanceTick')
            if payload['changeKind']=='visitChanged':
                # Draft 0.10: a Visit change re-anchors the mapping from musical Tick to UTC.
                # Without it, an authorized forward skip leaves a remote participant with no
                # defined event-time anchor at the new Visit boundary.
                pos=payload['position']
                check_position(pos,'visitChanged.position',True)
                target=visits.get(payload['targetVisitId'])
                if not target:errors.append('visitChanged references unknown target Visit')
                else:
                    if record['effectivePerformanceTick']!=target['start']:
                        errors.append('visitChanged must target start of pinned Visit')
                    if pos['visitId']!=payload['targetVisitId']:
                        errors.append('visitChanged Position must name the target Visit')
                    if pos['performanceTick']!=target['start']:
                        errors.append('visitChanged Position must anchor target Visit start')
                if record['effectivePerformanceTick']!=pos['performanceTick']:
                    errors.append('visitChanged anchor Tick must equal event effectivePerformanceTick')
        if kind=='turnRequested' and 'requestedVisitId' in payload and payload['requestedVisitId'] not in visits:
            errors.append('turnRequested: unknown requestedVisitId')
        if kind=='cueIssued' and 'targetVisitId' in payload and payload['targetVisitId'] not in visits:
            errors.append('cueIssued: unknown targetVisitId')
    return errors



def session_local_checks(data):
    """Selected record-local checks only; no authoritative event-log replay."""
    errors = []
    record_type = data['recordType']
    if record_type == 'event' and 'resultStateRevision' in data:
        if data['resultStateRevision'] != data['baseStateRevision'] + 1:
            errors.append('resultStateRevision must equal baseStateRevision + 1')
    if record_type == 'snapshot':
        participants = [p['participantId'] for p in data['participants']]
        if len(participants) != len(set(participants)):
            errors.append('duplicate participantId')
        if data['authorityParticipantId'] not in participants:
            errors.append('authorityParticipantId is not a participant')
        position = data.get('position', {})
        if position and position['performancePlanId'] != data['performancePlanId']:
            errors.append('position Plan differs from envelope Plan')
        window = data.get('commitmentWindow')
        if window:
            lo, hi = window['startPerformanceTick'], window['endPerformanceTick']
            tick = position.get('performanceTick')
            if lo >= hi:
                errors.append('commitmentWindow must have positive length')
            if tick is None or not lo <= tick < hi:
                errors.append('position is outside commitmentWindow')
        phrases = [p['phrase'] for p in data.get('committedPhrases', [])]
    else:
        payload = data['payload']
        phrases = [payload['phrase']] if data['kind'] in ('phraseProposed', 'phraseCommitted') else []
        if data['kind'] == 'sessionStateChanged':
            position = payload.get('position')
            if position:
                if position['performancePlanId'] != data['performancePlanId']:
                    errors.append('state-change position Plan differs from envelope')
                if position['performanceTick'] != data['effectivePerformanceTick']:
                    errors.append('position.performanceTick differs from event effective tick')
            if payload['changeKind'] == 'visitChanged' and position:
                if position['visitId'] != payload['targetVisitId']:
                    errors.append('position Visit differs from targetVisitId')
    for phrase in phrases:
        for note in phrase['notes']:
            if note['startTick'] + note['durationTicks'] > phrase['durationTicks']:
                errors.append('phrase Note extends beyond phrase duration')
    return errors


def main():
    parser = argparse.ArgumentParser(description='OSTF 4.3.0: local structure and selected semantic checks, not interoperability certification')
    parser.add_argument('paths', nargs='+', type=pathlib.Path)
    parser.add_argument('--session', action='store_true', help='Read current Distributed Session 0.2 records instead of Core Scores')
    parser.add_argument('--pinned-ostf', type=pathlib.Path, help='Exact Score bytes explicitly supplied for Session reference checks')
    parser.add_argument('--pinned-plan-id', help='Optional expected finite Plan ID; requires --pinned-ostf')
    args = parser.parse_args()
    if args.pinned_ostf and not args.session:
        parser.error('--pinned-ostf requires --session')
    if args.pinned_plan_id and not args.pinned_ostf:
        parser.error('--pinned-plan-id requires --pinned-ostf')
    try:
        schema_name = 'ostf-distributed-session-0.2.schema.json' if args.session else 'ostf-4.3.0.schema.json'
        schema = strict_json(ROOT/'schema'/schema_name)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        pinned = strict_json(args.pinned_ostf) if args.pinned_ostf else None
        digest = hashlib.sha256(args.pinned_ostf.read_bytes()).hexdigest() if args.pinned_ostf else None
        if pinned is not None:
            base_validator = Draft202012Validator(strict_json(ROOT/'schema'/'ostf-4.3.0.schema.json'))
            base_errors = [e.message for e in base_validator.iter_errors(pinned)]
            if not base_errors:
                base_errors = validate_43_semantics(pinned)
            if base_errors:
                raise ValueError('supplied Score fails local checks: ' + '; '.join(base_errors[:10]))
        failed = 0
        for path in args.paths:
            try:
                data = strict_json(path)
                errors = [('/'.join(map(str,e.path)) or '/') + ': ' + e.message for e in validator.iter_errors(data)]
                if not errors:
                    errors += session_local_checks(data) if args.session else validate_43_semantics(data)
                if not errors and pinned is not None:
                    errors += validate_pinned_session(data, pinned, args.pinned_plan_id, digest)
                if errors:
                    failed += 1
                    print('FAIL', path)
                    for error in errors: print(' ', error)
                else:
                    print('PASS — local structure/selected rules only:', path)
            except (OSError, ValueError, KeyError, TypeError, UnicodeError) as error:
                failed += 1
                print('FAIL', path, str(error))
        return int(failed != 0)
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as error:
        print('INPUT ERROR:', error, file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())
