> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **OSTF 4.3 Draft 0.53 editorial context (unratified).** The heading below preserves the historical origin of this rule set; current adoption remains subject to D01–D05 in [RELEASE_READINESS.md](RELEASE_READINESS.md). No schema change or runtime certification is implied.

## Draft 0.44 — Derived vocal occurrence and lyric coverage

For a finite `fixed` Visit, apply the selected attack/gate rules first, then resolve 4.2 Lyric Voice/Unit/Alignment and Note-scoped VocalPerformance references in source coordinates. A skipped attack can make a multi-Note Alignment partial even though the original `lyrics.alignments[]` is valid. A continuous fixed join retains one selected vocal Note occurrence; a hard cut can truncate the surviving gate without silently rewriting phoneme events or curves. Do not infer vocal-synthesis or syllable completeness from a derived selection. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.44 and example 15. This candidate remains unratified (D01/D04).

# OSTF 4.3 — Source and expanded Performance time

## Draft 0.44 — Rule ID disambiguation (D01/D04 PENDING)

`SEMANTIC_RULES.md` previously used the identifiers S13 and S14 twice, once
for Distributed Session semantics and again for later Core music semantics.
To prevent incompatible implementations, the earlier S13 and S14 remain
**Session-only**, and the later fixed continuous-join and fixed vocal/lyric
rules are uniquely identified as **S22** and **S23**. S21 remains the
source-tempo Session rule. Rule numbers are documentary cross-references,
not JSON fields or a priority order. See the canonical ID table and the
published corrections in `PUBLISHER_RELEASE_DECISIONS.md`.
Publisher adoption and English/Japanese editorial review are still required;
no Schema, 4.2 inherited field, runtime claim or license changes are made.

A 4.3 Performance Plan is a **non-mutating interpretation** of existing OSTF source Sections/Track contents. It never creates an independent authoritative source Timeline.

## Coordinates

- `sourceTick`: absolute Tick position in the original 4.3 document, consistent with `ppq`.
- `performanceTick`: concatenated playthrough Tick position; derived by expanding Visit source intervals.
- `visitId`: unique ID for one occurrence within the `performancePlanId`.
- For a source segment `[S, S+L)` in a Visit whose expanded segment begins at `P`, `performanceTick = P + (sourceTick - S)` for sourceTick in the segment.

If the song has `ppq=960`, a 4/4 bar is 3840 ticks. Source sections A `[0,3840)` and B `[7680,11520)` yield Visit source A,B with performance A `[0,3840)` and performance B `[3840,7680)`. The gap `[3840,7680)` in source is omitted rather than copied.

## Context on segment boundaries

Each new segment resolves effective **source** tempo, meter, key, chord and scale context at its own source start. A segment boundary is a **continuous join** for a fixed Track only if the previous source end equals the next source start within the same Visit and expanded positions are adjacent. Source map reevaluation occurs even at a continuous join (an authored change exactly at the boundary takes effect there). Source jumps/backward repeats, Visit transitions and changes from `fixed` to `open`/`silent` are **hard cuts** for the fixed source stream. Applications must not carry skipped source-map state or invent smoothing ramps between disconnected segments.

## Overlaps and nonrepresentable cases

Two selected Section spans within one Visit MUST NOT overlap, even if they carry different IDs. To play the same Section twice, author two Visits (or distinct nonoverlapping source Sections). Open parts cannot be rendered as deterministic MIDI just because source Notes exist. Visit-local role supersession only applies via `replacesDirectionIds` when a time-scoped playingRole would otherwise conflict.

## Sessions and remote robots

A Session Snapshot may carry `performancePlanId`, `visitId`, `sourceTick`, and `performanceTick`. Session time mapping is extra data and needs a coherent clock-domain sample and uncertainty. Tempo does not by itself synchronize wall-clock clocks. Network transport and physical actuator planning are outside `.ostf` Core.

## Note/MIDI events at cuts (Draft 0.3 decision)

A `fixed` Part deterministically **selects eligible source attack records** in its half-open source intervals, but inherited 4.2 Note enable/probability/velocity-deviation state may still leave actual sounding outcomes unresolved. A Note attacked within an interval may sustain across subsequent **contiguous source segments within the same fixed Visit**, without artificial Note Off/On at the join; truncate its gate only at its authored end or the next hard cut. Notes whose attacks precede the selected entry are NOT retriggered. MIDI control/program state before a hard-cut entry is not reconstructed without an explicit independent policy; a continuous join does not itself reset/reemit selected controllers. Disclose unresolved state. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` for the current proposed event table.

## Draft 0.40 — Finite Visit repeat versus probabilistic performance

A repeated Visit selects an eligible source Note again using a **new derived performance occurrence**, never a second Core Note identity. If an inherited Note declares `0 < probability < 1` or a nonzero `velocityDeviation`, the fixed source selection is stable but the **audible/sent MIDI outcome is not fully determined** by the OSTF document; no rule mandates reusing or redrawing stochastic outcomes per Visit. A writer making a fully deterministic playback claim must explicitly materialize the chosen outcome in a new Score revision without carrying unresolved probability/deviation forward. Disabled Track/Clip/Note state remains effective and does not imply an `open` Part.

## Draft 0.12 — Piecewise ideal timing for remote performance

For a selected source interval of `n` ticks with effective source tempo `b` BPM, ideal elapsed seconds equal `60*n/(ppq*b)`. A remote Profile 0.2 running Position must resolve source Tempo at the anchor Tick. Step-Tempo changes and boundaries between selected source segments divide integration intervals: re-evaluate the source at each segment start rather than carrying a BPM through a cut, and do not account for omitted source Tick gaps. A Visit change uses a new explicit UTC clock anchor. This does not determine actual WAN/audio/robot timing.

## Draft 0.18 — Studio Region/Automation projection (source vs expanded performance)

The companion **Production Session Profile 0.2** reuses original score-global **source Tick** for its `audioRegions` and Automation. A finite Plan maps each selected `[S,E)` to an expanded `[Q,Q+(E-S))` but does **not** author Visit-local mixer states. Compute all Automation values at the original `t`, including earlier points in omitted source ranges; re-evaluate on every Visit re-entry, and never carry the last mix setting from a different Visit. This *value lookup* is distinct from the MIDI cut event rule, which does not synthesize earlier CC/Program events.

For native Region audio, the ideal source-frame position at `t` is derived from the **original source tempo map from Region start**; skipped source durations are counted for *asset-frame lookup* but are **not appended** to the expanded Performance Plan timeline. For fit audio, map the same `t` against the Region's original normalized Tick position. Truncation intersects source half-open intervals, does not restart fades or assets, and creates no implicit crossfade. Complete proposed normative wording is `PRODUCTION_SESSION_PROFILE.md` §24. These are semantic descriptions, not host-specific renderer algorithms or live-network timing claims.

## Draft 0.41 — Worked source-join witness (unratified)

`examples/17-fixed-note-source-cut.ostf` selects Section One `[0,3840)` followed by Section Two `[7680,11520)` and Section Three `[11520,15360)` **inside one Visit**, then revisits One. In the first Visit: One maps to expanded `[0,3840)`, Two to `[3840,7680)` and Three to `[7680,11520)`. One→Two is a **hard cut** (source jump 3840→7680); a Note attacked at 3600 for 960 ticks terminates at source3840 (expanded end3840). Two→Three is a **continuous join** (source11520→11520, same fixed Track); a Note attacked at 11280 for 720 ticks maps to expanded `[7440,8160)` and is *not* split or retriggered at expanded Tick7680. A Note attacked exactly at source11520 belongs to Three once. The later Visit selecting One starts at expanded Tick11520 and is a fresh hard cut, independent of earlier Visit audio or MIDI state. This witness does not model an actual audio renderer or prove probabilistic note realization.


## Draft 0.42 — Targeted MIDI event during a continuous Note occurrence

A MIDI Event's selected source time and a targeted Note's selected attack time are distinct. For a fixed Plan, derive Event occurrence from its own selected source segment; resolve `targetNoteId` to a selected Note occurrence active at that Tick within the same continuous fixed run. A Note begun in skipped source music has no such occurrence, even when its MIDI Event lies in a selected Section; do not silently retarget or reinterpret the Event. At a source-contiguous join, an existing Note occurrence remains active but no second Note On is made. `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.42 is the detailed proposal. The source Score and all IDs remain unchanged.

## Draft 0.45 — Voice/Clip-wide vocal data under finite fixed Plans (S24, UNRATIFIED)

The inherited 4.2 VocalPerformance model also permits **non-note-targeted**
`breathEvents`, `techniques` without `targetNoteId`, `phonemeEvents` without
`noteId`, and `expressionCurves` without `targetNoteId`. These do not become
Note-scoped simply because the same Voice has a Lyric Alignment. For each
finite `fixed` Plan Visit, select a discrete item's original onset from the
Clip-relative time converted to absolute Score Tick; a skipped onset stays
unselected, a contiguous fixed join keeps one ongoing occurrence, and a hard
cut ends any selected ongoing item. An unbound phoneme retains its Unit and
Voice attribution but cannot be claimed as a fully specified Note/phoneme
association. Voice/Clip-wide curves are projected from their *source-time*
interpolation on selected segments, never by extrapolating missing values,
carrying a prior Visit's value, or rewriting 4.2 source points. A single-point
curve is constant over the applicable Clip/Voice scope; multi-point curves are
unspecified outside their authored point span. Existing note-targeted curves
replace overlapping Voice/Clip values where 4.2 defines such replacement;
they are not summed. Neither an audible rendering nor the automatic creation
of new Units/Alignments/Notes is specified. See `SEMANTIC_RULES.md` S24 and
the updated `examples/15-vocal-response-phrasing.ostf`. This is an editorial
D01/D04 proposal only.
