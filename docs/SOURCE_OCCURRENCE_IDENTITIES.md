> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **OSTF 4.3 Draft 0.53 editorial context (unratified).** The heading below preserves the historical origin of this rule set; current adoption remains subject to D01–D05 in [RELEASE_READINESS.md](RELEASE_READINESS.md). No schema change or runtime certification is implied.

## Draft 0.44 — Derived vocal and lyric occurrences (no new source IDs)

For a voice-scoped original 4.2 Alignment, report selection coverage separately for each finite Plan Visit using the selected Note **attack occurrences**; source Lyric Voice, Phrase, Unit, Alignment and VocalPerformance IDs stay stable. For an explicit materialized Score, minted per-occurrence Note IDs require correspondingly valid remapped lyric and performance references, subject to explicit loss reporting. A skipped Note does not turn another source Note into its substitute; continuing vocal curves across contiguous fixed joins does not make a second source Note or VocalPerformance. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.44. This is a D01/D04 editorial candidate, not a playback algorithm.

# Source Note identity and derived performance occurrences — Draft 0.4

## Purpose

One OSTF 4.2/4.3 Note ID denotes one authored source Note. The same source Section can be visited multiple times in an orderedFinite Performance Plan; generated onsets after traversal are distinct *occurrences*, not new source Notes.

## Decision

For an individual fixed Note occurrence during a finite Plan interpretation, the tuple `(performancePlanId, visitId, sourceSegmentOrdinal, sourceNoteId)` is unambiguous if (a) Plan IDs, Visit IDs and source Note IDs are valid and unique, and (b) the source section sequence and Visit ordinal are well defined. The tuple is **derived**; it is not serialized as a second identity authority.

| Layer | Authoritative identity | What can change |
| --- | --- | --- |
| Source score | `notes[].id` in the source Clip | The authored Note may move when the song is edited |
| Visit occurrence | Plan + Visit + ordered selected source segment + source Note | Changes when the Plan's traversal changes; not a Core ID |
| Materialized fixed rendition | Newly minted Core Note ID and new revision | An explicit edit produces a new document |
| Remote session phrase | Profile-specific event/commit and performance position | Not an OSTF Core Note until materialized |

## Example (PPQ 960)

Song has 4 bars `[0,15360)` at 4/4. A source Note `n1` at source Tick `960`, duration `1440` is stored inside Clip `c1`. Visit `head` selects this section starting at performance Tick 0; Visit `solo` selects it again starting at performance Tick 15360. If both parts are fixed, the Note occurs at performance Ticks 960 and 16320, respectively, with different occurrence keys. The source has one Note ID `n1`, not two.

If `solo` uses `realization:"open"`, there is no fixed Note occurrence at Tick 16320 despite the source retaining `n1`. Loading the file still cannot generate a new Note. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` for boundary rules.

## Collision, consent and provenance

No source Note ID is duplicated when a Plan is read or performed. A document-generating program may explicitly render the Plan into a *new* OSTF document: it must generate unique Note IDs for each occurrence, update all relevant references and alignments according to 4.2 rules, and record a new revision with origin information. Do not assume array index or a localized Note label is identity. This appendix specifies interpretation only; it does not define a new Note serialization or an automatic renderer.

## Draft 0.41 — One Note occurrence can span a continuous join

The derived occurrence key `(performancePlanId, visitId, sourceSegmentOrdinal, sourceNoteId)` identifies the selected **attack** segment. If the Note gate continues across adjacent Sections within the same Visit without a source jump, it is still **one** performance occurrence, not a second Note occurrence at the join. For source-cut/restart or new Visit, treat the next source attack as a distinct occurrence. This rule never allocates a new Core ID until an explicit materialized Score revision is authored and must not be confused with MIDI CC or audio/robot-state snapshots.


## Draft 0.42 — MIDI Event occurrence and selected target identity

For one selected MIDI Event, a derived diagnostic key may be `(performancePlanId, visitId, eventSegmentOrdinal, midiEventId)`. If it has `targetNoteId`, associate it with the **selected Note occurrence** whose attack's `sourceSegmentOrdinal` can differ from the event's segment, e.g. a sustained Note across a contiguous Section join. A Note attacked in a skipped or hard-cut source interval does not become a selected occurrence simply because a later targeted Event is present. A deliberately materialized new Score needs fresh Event and Note IDs and a correctly remapped `targetNoteId`; none are minted on Plan read. No implied wire-channel reassignment or MPE rendering is standardized.

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
