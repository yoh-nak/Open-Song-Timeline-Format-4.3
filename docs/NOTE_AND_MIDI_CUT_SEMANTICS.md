> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **OSTF 4.3 Draft 0.53 editorial context (unratified).** The heading below preserves the historical origin of this rule set; current adoption remains subject to D01–D05 in [RELEASE_READINESS.md](RELEASE_READINESS.md). No schema change or runtime certification is implied.

# Performance Plan fixed-mode boundary and continuous-join semantics — Editorial candidate 0.41

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

## Draft 0.43 — Fixed vocal, lyric and expression references across finite Plan selection (D01/D04 PENDING)

This **candidate semantic rule** does not change the inherited 4.2 Lyrics or VocalPerformance schemas, does not introduce a vocal renderer and does not redefine the authority of `lyrics.alignments` or `clips[].vocalPerformances[]`. It concerns only a **derived fixed-Plan selection view**, not the validity of the original source Score.

1. **Voice ownership precedes expansion.** Resolve each authored `lyrics.voices[].id` to its source `trackId` and `documentId`. Resolve each voice-scoped `lyrics.alignments[]` to source Unit/Note IDs under the 4.2 rules before examining the selected Performance Plan. Never infer a Voice from a Track name, infer an Alignment from proximity, or allocate a new source lyric ID merely because a Section is repeated.
2. **Selected vocal Note occurrences.** For a `fixed` Visit, first select source Note attacks with the same half-open source-section, clip-local-to-source-Tick, enabled and continuous/hard-cut rules defined for Notes in Drafts 0.40–0.42. Each selected Note's **derived** occurrence is keyed by Plan, Visit, attack segment and source Note ID. The same Unit or Phrase may refer to multiple derived occurrences in different Visits without creating new source Unit, Phrase or Alignment identities. A `vocalFreedom` Direction still denotes intent, not an override of fixed authored lyrics and Notes.
3. **Alignment coverage is not all-or-nothing source validity.** For a given Visit, an Alignment is *fully selected* only if **all** its referenced source Note attacks have eligible occurrences in that Visit and all Units resolve to the correct authored Voice/Document. If some but not all referenced Note attacks are selected, it is *partially selected*; if none is selected, it has no selected vocal Note occurrence. The original source Alignment remains valid and unchanged in every case. An export must not silently label partial melisma or incomplete many-to-many mappings as fully reproduced lyrics.
4. **Time-scoped vocal event/curve association.** Phoneme events with a source `noteId`, and note-scoped pitch/expression curves or techniques, may be associated with a derived Note occurrence **only** when the referenced source Note attack is selected and its surviving gate covers the relevant time. An event/curve in skipped source music is not inserted as a new live event merely because a later segment selects the same Lyric Unit. A selected Note crossing a continuous fixed join retains **one** occurrence; its original associated curves or phoneme timing remain authored source data, not re-triggered at the join. An untargeted breath or Clip-level expression may be associated by its own selected source time, but that selection alone does not prove the audible breath/phrase was realized.
5. **Hard cuts and partial spans.** A source Note's gate may end at a hard cut before its original end; an authored phoneme event or pitch/expression curve may then extend past the surviving gate. Do **not** claim the complete syllable, phoneme sequence, pitch contour or vocal technique has been reproduced. A renderer/exporter must explicitly disclose such unavailable/partial spans and its target-specific clipping/omission/approximation policy, or decline the conversion. It must not silently reassign the remaining phoneme to a different Note or create a new authoritative Alignment.
6. **Materialization is explicit.** Exporting an expanded deterministic vocal Score requires new concrete Note IDs and remapped Voice/Unit/Alignment and per-Clip VocalPerformance references wherever affected; do not reuse source IDs across materialized Note occurrences. When any necessary phoneme timing, many-to-many lyric association or cut expression is unresolved, label the conversion lossy or refuse it. The mere presence of a Voice/Direction never guarantees that a synthesizer can reproduce the original audio.

**Static witness — `examples/15-vocal-response-phrasing.ostf`:** Visit `call-response-visit` selects A `[0,3840)`, jumps to B `[7680,11520)`, then joins contiguous C `[11520,15360)`; Visit `call-reprise-visit` selects A again. `lead-a-hold` attacks at 3600 but its authored phoneme event ends at 4200 and a pitch-curve point occurs at 4200, both outside the surviving gate ending at the A→B hard cut at 3840. `lead-omitted-gap` attacks at 7400 in skipped material; `align-with-partial` mentions it alongside the selected `lead-b-carry` attack at 11280, so it is a **partial** Alignment in the first Visit rather than a new fully resolved melisma. The `lead-b-carry` gate and its associated pitch/expression curve extend from B through the B→C **continuous join** without a duplicate onset; its original source phoneme timing is not replayed at the join. The reprise of A is a separate derived Note/lyric occurrence with the same source IDs. All identities and original lyric text remain unmodified. No vocal playback or renderer conformance is claimed.


This document clarifies `docs/SPECIFICATION.md` §13. It does not modify OSTF source Notes or Clips.

## Draft 0.42 — Note-targeted MIDI event association across finite Plan cuts (D01/D04 PENDING)

The inherited 4.2 `targetNoteId` on Control Change, Pitch Bend, Channel Pressure, and Poly Pressure is a **semantic association with an authored source Note**, not a substitute for MIDI channel/pitch wire semantics. It is NOT a new source Note or guaranteed per-note actuator routing. This proposal applies to a **derived fixed-Plan selection view**, not to validating or rewriting original 4.2 events.

1. Compute each MIDI event's source position using `clip.start + midiEvent.start`; select its original record exactly once if that source Tick lies in an eligible half-open source segment of the current `fixed` Part and Visit. An event exactly at an adjacent source boundary belongs to the next segment. Events in skipped source gaps are not synthesized or copied as a state checkpoint.
2. An **untargeted** event remains a channel/bus-scoped authored source event, selected solely by its own source Tick. Its prior MIDI Program/CC/Bend state at a hard-cut entry can still be unknown; do not invent a snapshot.
3. A **targeted** event only has a resolvable *Visit-local Note association* when the referenced source Note has an eligible selected attack occurrence whose gate is still within the same continuous fixed run at that event's Tick. A Note attacked in the skipped region is **not** selected merely because its later targeted event lies inside a selected segment. The continuous-join rule may carry a selected target Note into the following contiguous Section without creating a duplicate Note occurrence.
4. When the referenced Note has no eligible active occurrence, is disabled, or has a potentially suppressed Note-On due to probabilistic realization, the event is **not automatically reinterpreted as an untargeted channel event, assigned to a different Note, or claimed to be a deterministically rendered per-note gesture**. The source event bytes remain intact. A deterministic expanded-MIDI writer must make and disclose an explicit omit/preserve/approximation policy or decline the conversion. This caveat is especially important for MPE member channels and multi-timbral routing. A derived source-selection preview may label such an event `unresolved_target` without declaring the original Score structurally invalid.
5. A selected targeted event carries the original `targetNoteId` in source documents. For expanded *diagnostic* views, associate it with the selected **derived Note occurrence** `(performancePlanId, visitId, sourceAttackSegmentOrdinal, sourceNoteId)`; its own MIDI-event occurrence may use `(performancePlanId, visitId, eventSegmentOrdinal, midiEventId)`. These are computed addresses, never new Core IDs. Event and Note ordinals may differ for a sustained Note across a continuous join. Explicit materialization into a new Score needs fresh Core IDs and rewritten valid target references; none is created by merely reading a Plan.
6. The existing 4.2 MIDI `order` resolves ordering among same-Tick MIDI Events only under its inherited rules. This amendment does NOT invent a universal Note-On versus controller ordering at an identical Tick or mandate a plug-in/MPE playback policy. Report unresolved ordering instead of inventing a deterministic MIDI wire sequence.

**Worked static witness — `examples/17-fixed-note-source-cut.ostf`:** In the first Visit, `target-prior-note-selected` at source 3750 is associated with source Note `cut-shortened` in Section One. `ctrl-omitted-gap` at 4000 is not selected. On the source jump to Section Two, `program-on-source-entry` at 7680 is included once, while `target-prior-note-not-selected` at 7800 references the unselected `cut-pre-sustain` attack at 7400 and therefore has no selected target occurrence. At the continuous Two→Three source join, `controller-on-contiguous-join` at 11520 is selected once and `target-across-contiguous-join` at 11760 remains associated with the already-selected `carry-across-contiguous-join` Note attacked in Two. The later One Visit supplies separate derived occurrences for One; it does not reuse the first Visit's MIDI state. These cases are a **non-executing data interpretation example**, not a DAW/robot test or new serialized requirement.


## Draft 0.41 — Source-continuity classification (UNRATIFIED)

A source segment remains a half-open *attack selector*. It is not always a hard release boundary. For each Track in one Visit, a **continuous join** between consecutive segments exists only if the prior source end `E` equals the next source start `S_next`, the two expanded intervals are adjacent, and that Track resolves to `fixed` on both sides. A **hard cut** applies at every source jump/gap, at every Visit transition, or when the Track realization changes away from `fixed`. The existence of adjacent Source Section IDs alone is insufficient if their actual Tick ranges do not join.

| Source material | At entry / join | At exit / cut | Interpretation |
| --- | --- | --- | --- |
| Note On `t < S`, Note Off `> S` and no prior selected occurrence | Do **not** synthesize a new Note On | No event from that source attack | A newly selected source segment does not reconstruct prior note-on history |
| Note selected in preceding source segment, crossing a **continuous** join | Keep already selected gate, no duplicate attack | Release at authored end or the maximal continuous `fixed` run end, whichever comes first | Sustained legato across adjacent Sections of one Visit |
| Note selected in preceding segment, crossing a **hard cut** | No reattack | Release at cut boundary | Disconnected source or Visit/realization transition |
| Note On `t = S` or `S < t < E` | Include once if eligible and enabled according to inherited Note state | May extend across continuous joins, never across a hard cut | Half-open membership and source Note state are separate |
| Note On `t = E` | Excluded by preceding segment | Following segment may include once if it starts at `E` | No duplicate Note On at a boundary |
| MIDI event `t < S`, not previously selected | Do not synthesize | N/A | No hidden CC/Program/Bend state checkpoint |
| MIDI event selected in previous segment at continuous join | Keep event stream/state in time order; do not replay | State persists only within the continuous fixed run | A continuous join does not itself reset controllers |
| MIDI event selected at or after a hard cut | Include only events within the newly selected source interval | Previous controller state is not implicitly recreated | Missing initial state must be disclosed |
| Tempo/Key/Meter/Harmony at every source start | Re-resolve effective source map | Source discontinuity still resets context | Source music maps are always authoritative, not carried from skipped time |

**No implicit acoustic continuity:** Source Note gate continuity does not standardize synth release tails, MPE/plug-in state, vocal phoneme synthesis, region fades or physical actuation. These remain outside finite-Plan Note/MIDI selection. The `sourceSegmentOrdinal` portion of an occurrence key identifies the segment of the **original attack**, even if its sustained gate passes into a later continuous segment; do not create a second occurrence at the join.

### Draft 0.40 — Note eligibility, source state and stochastic realization (UNRATIFIED)

The Note-On rows above describe **source-event eligibility**, not a promise of audible output. Once a Note attack is selected by the half-open source interval, preserve the inherited 4.2 data and honor `track.enabled`, `clip.enabled` and `note.enabled` before scheduling any event. Disabled source objects remain authored data; `fixed` never converts them into `open` or `silent` Plan Parts.

A selected `note.probability:0` cannot produce a Note-On; `0 < probability < 1` cannot be rendered as a reproducible inclusion/exclusion choice from OSTF alone (the format does not define a PRNG stream or per-Visit draw semantics). Unspecified probability means 1. A nonzero `velocityDeviation` and unspecified `velocity` likewise cannot be described as a uniquely authored concrete outgoing velocity. `velocityDeviation` is a 4.2 relative *endpoint*, not an OSTF-wide sampling algorithm. Repeated source Note IDs preserve one source identity but need not yield identical stochastic sounding results on repeated Visits.

A **deterministic event-selection map** can be produced from a `fixed` Plan even when its **deterministic performance realization** is unresolved. Exporters must state that distinction. To author a fully determined output, make an explicit new Score revision containing chosen Note occurrences with distinct Note IDs, definite Note-On velocities and resolved note states; do not overwrite or silently flatten the original 4.2 probability/velocity settings. An unresolved preceding MIDI controller/Program state remains a separate limitation, even when all Note state is deterministic. Proposed diagnostic example: `E-PLAN-NOTE-STATE-UNRESOLVED` (documentation-only, not a serialized required error code).

**Controller state warning.** A Program Change/Pitch Bend/CC earlier than the selected segment might be vital to rendering. The Plan format does not guarantee a state checkpoint for each cut. Implementations claiming deterministic external rendering MUST surface unresolved state rather than invent it. For MPE, multi-bus and vendor external synths, compatibility is target-specific.

**Rest and silence.** When a Visit Part is `open` or `silent`, it intentionally suppresses selected fixed material in *that Visit only*. Generated Session Profile phrases may be accepted for an `open` Part separately, but MUST NOT be represented as authored OSTF Core Notes until explicit materialization.

**Source vs expanded time.** Each Visit is a sequence of ordered, non-overlapping source segments. A segment with source start `S`, length `L`, and performance start `P` maps any source Tick `t∈[S,S+L)` to `P+(t-S)`. If source Tempo changes, timing in seconds must integrate the actual source tempo map over each selected segment; never assume one BPM over a composite Visit.

**Error/report identifiers (new proposals):** `E-PLAN-NOTE-CUT-UNSUPPORTED`, `E-PLAN-MIDI-STATE-UNKNOWN`, `E-PLAN-UNSPECIFIED-PART`, `E-PLAN-TIME-MAP-INVALID`. The report identifiers are documentation only until an implementation claims diagnostic conformance.

## Draft 0.4: Source Note versus repeated performance occurrence

For a Clip-local Note, first compute `sourceNoteStart = clip.start + note.start` using inherited 4.2 timing. The source selector tests this absolute Tick, never the Clip-relative Tick. A negative Clip-local Note start is legal when the resulting source start remains valid; it does not cause a synthetic Note-On at any cut boundary.

Repeated finite Visits never duplicate the source identity. To distinguish emitted events without changing Core, use a **derived** occurrence key `(performancePlanId, visitId, sourceSegmentOrdinal, sourceNoteId)`. When a Plan is explicitly materialized into a new fixed song, allocate new Core Note IDs and a new document revision for the emitted occurrences; retain origin references in provenance where possible. This key is diagnostic/implementation-local and never substitutes for a source ID or the existing Core ref vocabulary.

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
