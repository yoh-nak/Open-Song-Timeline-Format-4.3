# Draft 0.73 — R04/R11/R13/R14 proposed rule consolidation (UNRATIFIED)

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

For companion Score reference binding, consult the active first-section eight-step decision table in the applicable Core / Distributed Session / Production Session bilingual normative candidate. Historical Draft 0.62–0.72 examples below those new sections are revision context only. Complete authorized Score candidate enumeration and required raw-byte retrieval precede conclusive `MISSING`, `MISMATCH`, `AMBIGUOUS`, or `RESOLVED`. `INVALID`, `UNSUPPORTED`, `NOT_EVALUATED`, and Score-format errors are outside those four statuses. `missing_referent` is a diagnostic detail under `AMBIGUOUS`, not proof of multiple targets. No JSON Schema field or enum is created by these editorial names. D01–D05 remain unsigned.

---

> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.61 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF 4.3 Draft 0.53 — Cross-object semantic rules and diagnostics (UNRATIFIED)

## Draft 0.44 — Stable semantic-rule identifiers (D01/D04 review pending)

The `S` numbers in this document are **stable editorial references**, not JSON
field names, numeric priorities, execution order, or alternative definitions.
The previous Draft 0.43 accidentally reused S13 and S14 for two unrelated
rules. This revision preserves the **earlier** Session identifiers and assigns
unique identifiers to the **later** music rules:

| Identifier | Subject | Publication boundary |
| --- | --- | --- |
| S13 | Distributed Session Profile 0.2 state revision and event acceptance | Separate Session Profile |
| S14 | Distributed Session Profile 0.2 start and commitment-window meaning | Separate Session Profile |
| S21 | Session musical source-tempo resolution | Separate Session Profile |
| **S22** | Consecutive fixed source segments versus hard-cut Notes and MIDI | OSTF 4.3 Core interpretation |
| **S23** | Vocal/lyric selection, phoneme/curve truncation and partial Alignments | OSTF 4.3 Core interpretation |
| **S24** | Voice/Clip-scoped vocal events and expression through source cuts | OSTF 4.3 Core interpretation |

**Cross-reference policy:** quote the **subject** with the exact S number, or
link to its unique heading. References saying only 'S13' for continuous joins
or 'S14' for vocal selection in historical drafts are ambiguous and superseded
by S22 and S23, respectively. Gaps in numbering (e.g. S18–S20) are unassigned;
do not renumber earlier rules to fill them or infer their meaning. Existing
S1–S17 and S21 retain their former identity and meaning. This is a D01/D04
editorial correction, not approval of any rule or a new serialized property.

## Draft 0.25 — Cross-document authority guide (editorial candidate)

For **concrete source values**, OSTF Score Notes/MIDI, Harmony and Lyrics retain their existing 4.2 authorities. A `phrasing` or `vocalFreedom` Direction cannot override saved Notes or text at import. A `performancePlan` Visit computes an occurrence in a **derived** performance coordinate system and cannot mutate Source IDs. An accepted Distributed `phraseCommitted` changes only Session state/history: it is neither evidence of acoustic performance nor a Score/Production write. Production audio Regions/Automation and Mixer/plug-in metadata are separate authored Studio state. No data record grants device, file, network or robot permissions. See `CONFORMANCE.md` Draft 0.25 operation matrix and `SESSION_STATE_MACHINE.md`.

The *failure domain* MUST be distinguished in diagnostics: invalid JSON/Schema identity, invalid typed reference/Plan mapping, unresolved original Score bytes, explicit information-loss export, state-authority rejection, asset-byte unavailability, unsupported interpretation, and execution failure are different outcomes. The last category is outside this format's non-runtime release gate. Never report a preserved descriptor as preserved Asset bytes, or a retained accepted phrase as having sounded. These are pending author adoption, not new JSON fields or a performed runtime check.

---

This document adds a normative-**proposed** editorial checklist for field references and conflicts not expressible in Draft 2020-12 JSON Schema. The 4.3 Schema remains the structural authority. The official 4.2 specification governs inherited semantics.

## S1 — Identity

Every newly authored `phrasing`, `vocalFreedom`, `ensembleInteraction`, `performancePlan`, and `performanceVisit` ID MUST be unique in the Core document ID namespace, separate from string labels, and stable across ordinary edits. Reusing an ID to mean a different event is forbidden. New `ref.type` values resolve to the expected Core object type and MUST NOT resolve by display name.

## S2 — Time

`phrasing`/`vocalFreedom`/source `ensembleInteraction` use absolute nonnegative song ticks in half-open intervals. `sourceRange` and selected Section spans MUST lie in the source song domain. `performanceTick` is computed by concatenating Visit segments in `ordinal` order, with no implicit gap. A repeated source Section is not a new source Section ID; a Visit ID identifies that *occurrence*. Time must not silently be converted to wall clock or bar counts.

## S3 — Direction scopes

A `phrasing` range MUST NOT overlap another `phrasing` range on the same Track. A `vocalFreedom` Direction MUST NOT overlap another `vocalFreedom` range for the same Voice in a Track; different Voices may overlap. Other kinds (e.g., `playingRole`, `improvisation`, `pitchRange`) are independent and retain inherited constraints.

## S4 — Voice ownership

`parameters.voiceId` MUST resolve to an existing Lyric Voice assigned to the enclosing Track. Alternative phrase IDs MUST exist in the correct authored Lyric Document. Candidate lists must be distinct. Selecting an alternative does not mutate established Units, Notes, or Alignment; materialization is a separate authoring action.

## S5 — Interaction refs

Every `ensembleInteraction` MUST reference existing Tracks. Same-Track relationships are permitted only for two distinct, explicitly referenced Lyric Voices both owned by that Track. Any self-Voice relationship is invalid. Optional Voice IDs on different-Track relationships must match their respective Track owners. If `scope` is given, Plan and Visit must exist and be correctly paired. If both source range and scope are given, their intersection with selected Visit source segments must be nonempty. The actor/partner direction must never be guessed from names or Track order. `responseWindowTicks` is a musical offset limit, not a network timeout or absolute wall-clock deadline.

## S6 — Plan source traversal

Each Plan has >=1 Visit with distinct contiguous zero-based ordinals. Every Visit uses exactly one source selector, and every selected source range has positive duration within the source Timeline. Within a Visit, source Sections must not overlap; their authored order determines playback sequence. A Section may recur in other Visits without being copied. Every source cut starts with the active source Tempo, Meter, Key and Harmony context at that source Tick, not the carried end context of a previous segment.

## S7 — Plan role conflict

A Visit-local Part role applies only to that Visit. If a source timed `playingRole` overlaps selected source material and disagrees, the Visit Part MUST explicitly list that source Direction ID in `replacesDirectionIds`. Replacement affects only the Visit, never the source. IDs must belong to that Track and intersect selected Visit ranges. Identical, nonconflicting source role does not need a replacement.

## S8 — Fixed/open/silent authority

`fixed`: use selected existing source Notes/MIDI Events; this can be silence if no events were authored. `open`: concrete performance is not specified for that Part and Visit, even when the source contains Notes; no automatic regeneration or randomization on file load is permitted. `silent`: no part performance in that Visit. Unlisted Tracks obey `defaultRealization`; if `unspecified`, deterministic export MUST report an unresolved plan. The source OSTF remains unchanged regardless of Visit realization.

## S9 — Requirements vs capabilities

`performanceRequirements` describe the source part's **requested** capability. The actual Participant capabilities in the separate Session Profile are advisory reports at session time. Matching, actuator preparation and safety are out-of-Core. An authored required pitch range must fit inside a Track instrument's authored playablePitchRange when one exists.

## S10 — Host / security / migration

No instruction field, URI or event payload may grant authority to fetch, execute commands, change accounts, control actuators or send data externally. Converting 4.3 to 4.2 without losing information is allowed only when no 4.3-only fields, new direction types or new typed ref references exist. Report each removed JSON Pointer for an explicitly lossy export. Automatic version relabeling is not validation.

## S11 — Session state (separate profile)

A **new** state-changing Distributed Profile 0.2 event whose `baseStateRevision` differs from the current authoritative Snapshot revision MUST be rejected for state transition; it is not silently converted into a new `phraseProposed` or re-authorized by timestamp. After exact Session/Score/Plan identity and trusted issuer authorization checks, an already accepted **same `eventId` and equal complete parsed JSON value** is an idempotent no-op, even if its original base revision is now old. Same ID with different parsed content is an integrity conflict. Non-state-changing proposal/observation events never advance `stateRevision`. Musical Tick and clock-domain time are distinct, and uncertain clock confidence must be disclosed. Session Events are never robot actuation commands. The event-ordering authority is `SESSION_STATE_MACHINE.md` §Draft 0.7, table A–F.

## Error classification for implementations

| Code | Meaning |
| --- | --- |
| `E-ID-DUPLICATE` | Nonunique new or inherited Core identity |
| `E-TIME-OUT-OF-BOUNDS` | Source range extends outside source Timeline |
| `E-DIRECTION-OVERLAP` | Incompatible overlapping same-kind Direction |
| `E-VOICE-OWNER` | Voice is not associated with its Track or Lyric Document |
| `E-INTERACTION-REF` | Missing Track/Voice/Plan/Visit reference |
| `E-PLAN-VISIT` | Invalid ordinal, source selector, source overlap or source bounds |
| `E-PLAN-ROLE-CONFLICT` | Unresolved Visit-local / source timed role conflict |
| `E-PART-REALIZATION` | Materialization needed to reproduce open/unspecified content |
| `E-CAPABILITY-CONFLICT` | Requirements and declared playable range contradict |
| `E-DOWNGRADE-LOSS` | 4.3 information cannot be represented in 4.2 Core |
| `E-SESSION-REVISION` | Session state revision mismatch or unaccepted transition |

Codes are proposed interoperable report identifiers, not proof of a fully implemented validator.

## S12 — Explicit note/onset cut authority (Draft 0.3)

For a fixed Plan Part, select only source attacks within `[S,E)`; omit pre-entry lingering attacks rather than synthesizing them. **Do not automatically truncate at every Section boundary**: let a previously selected Note sustain across a source-contiguous join within the same fixed Visit, and truncate at a hard cut (source jump/gap, new Visit, or switch away from fixed) or the authored Note end. Do not duplicate MIDI controller/program/pressure state from before a newly selected hard-cut entry; a continuous join does not itself reinitialize or duplicate MIDI state. Report incomplete state as `E-PLAN-MIDI-STATE-UNKNOWN` when deterministic export depends on it. These rules apply to Plan interpretation only; source Notes remain unchanged. See `NOTE_AND_MIDI_CUT_SEMANTICS.md`.

### Draft 0.40 — Fixed Part source selection versus inherited 4.2 Note state (D01/D04 pending)

A `fixed` Visit Part chooses source Note/MIDI *records* by source Tick; this is separate from whether an inherited 4.2 Note is enabled, passes `probability`, or has a uniquely determined `velocity`. Track/Clip/Note `enabled:false` continues to suppress scheduling, probability between zero and one has no standardized random draw/seed, and a nonzero `velocityDeviation` or unspecified base `velocity` does not fix one actual Note-On velocity. No source Note property is silently reset or duplicated at a Visit boundary. Derived repeat occurrences remain distinguishable from source Note IDs. A fully deterministic Note/MIDI serialization claim must resolve and explicitly materialize these choices in a separate authorized Score revision, with the already-documented MIDI cut-state caveat. This is an unratified clarification of the 4.2 Note model; `E-PLAN-NOTE-STATE-UNRESOLVED` is a suggested report code, not a required JSON property.

## S13 — Profile 0.2 state authority (Draft 0.3)

Profile 0.2 lives outside `.ostf` Core. `phraseProposed` and non-committing events MUST NOT advance authoritative session state; authorized `phraseCommitted` and `sessionStateChanged` MUST advance base revision by exactly one, after the host verifies the declared authority. After authentication and immutable Session/Score/Plan verification, an already accepted event ID with identical **entire parsed event** is an idempotent no-op; same ID/different content is an integrity conflict. A **new** state-changing event with stale `baseStateRevision` is rejected. No implicit reconciliation is permitted. A session record, by itself, is not an actuator command. See `SESSION_STATE_MACHINE.md`.

## S14 — Session Profile 0.2 start and completeness (Draft 0.5)

An authenticated session authority MAY accept `sessionStarted` only for `prepared → playing`, with a pinned finite-Plan Position and `payload.position.performanceTick == effectivePerformanceTick`, advancing the state revision once. A future start anchor does not imply actual sound/actuation. A `sessionStopped` is immediate rather than a future stop reservation; `visitChanged` targets the declared beginning of its Visit when playing. A retained proposal's committed phrase cannot silently change `effectivePerformanceTick`. A Snapshot `commitmentWindow` is an optional asserted complete set of accepted phrase intervals intersecting a bounded half-open performance range as of `stateRevision`; omitted means no completeness guarantee. See `SESSION_STATE_MACHINE.md`.

## S15 — Vocal materialization under cuts (Draft 0.5)

A derived source-note performance occurrence does not mint Lyrics/Voice IDs. If selected fixed Notes are cut and phoneme/expression/Alignment mappings cannot be reproduced faithfully, a consumer claiming deterministic vocal expansion MUST disclose loss/ambiguity or refuse, not invent syllables or claim an exact outcome. See `SPECIFICATION.md`.

## S16 — Session phrase allocation (Draft 0.6; separate Profile 0.2)

Profile 0.2's accepted `midi1Notes` phrase MUST lie completely inside one finite Performance Plan Visit whose target Track is explicitly `open`. Non-open Parts, omitted Parts inheriting the Plan default, Visit crossing, unpinned Plans, and overlapping accepted same-Track phrases MUST be reported; unaccepted proposals do not override Plan intent. See `SESSION_STATE_MACHINE.md` Draft 0.6 section. This does not modify 4.3 Core Schema or the source Notes.

## S17 — Immutable Session score, event acceptance vs execution (Draft 0.7; companion 0.2)

A Profile 0.2 Session pins one OSTF `(documentId, revisionId, performancePlanId)`; a newer Web API resource or altered content under the same revision never silently rebinds it. An accepted `phraseCommitted` is immutable *session history* rather than evidence of sound. Profile 0.2 Visit traversal while playing advances in increasing expanded Performance Tick; backwards seeking requires a new Session or a future explicit profile. Skipped or post-stop future phrases may remain in the accepted log but MUST NOT be claimed as sounded. Event replay identity is checked before rejecting a **new** stale revision. An assignment change cannot silently orphan future accepted phrases or assign motor-execution authorization. Full proposed rules are in `SESSION_STATE_MACHINE.md`, Draft 0.7. No Core Schema fields are added.

## Draft 0.8 — Companion integrity clarifications

Core 4.3 semantic rules have not changed. In the separate unratified Session Profile 0.2, `assignmentChanged` forbids `position` independently from `targetVisitId`; all Session Phrase Notes must fit their parent duration regardless of Snapshot completeness claims; and authenticated exact duplicate replays may be idempotent before stale-revision checks but not before authentication. Historical accepted phrases may survive a stop or skipped Visit without remaining participant assignments and without proving sound. See `SESSION_STATE_MACHINE.md` Draft 0.8.

## Draft 0.10 — Clock anchor at Visit transition

**Draft 0.10 editorial amendment (unratified): a forward Visit transition requires its own clock anchor.** Previously, `visitChanged` carried only `targetVisitId`; a skip over one or more Visits could not convey the corresponding UTC musical anchor. This is a real data-model omission, not proof that a real-time system failed. The separate Profile 0.2 `sessionStateChanged.payload` now requires an existing `position` object for both `sessionStarted` and `visitChanged`. The `visitChanged` object MUST also contain `targetVisitId` and MUST NOT contain `participantId` or `assignedTrackIds`. `assignmentChanged` still forbids both `position` and `targetVisitId`; `sessionStopped` is unchanged.

For an authorized `visitChanged`, `position.visitId` MUST equal `targetVisitId`; `position.performancePlanId` MUST equal the root pinned `performancePlanId`; and `position.performanceTick` MUST equal both `event.effectivePerformanceTick` and the start Tick of the target Visit in the pinned *expanded* finite Plan. `position.sourceTick` MUST map to the **first source segment's first Tick** of that target Visit. `epochUtc` is the estimated clock-domain instant corresponding to this Tick (not the time the event was received); `uncertaintyMs` states uncertainty, not certified WAN synchronization. The event MUST still be authorized, use the frozen source tuple and advance strictly forward in performance Tick under the existing Profile 0.2 rules. In particular, the anchor alone does not authorize physical actuation or assert sounds occurred.

## Draft 0.11 proposed Session Profile 0.2 clock and tempo integrity

The first accepted `sessionStarted.payload.position.clockDomainId` pins the musical Session clock-domain ID. Later `playing` Snapshot positions and `visitChanged` anchors MUST use the same domain; a new domain requires a new Session. Merely matching IDs never proves clock accuracy or identity. Optional `position.tempoBpm` MUST exactly represent the effective source `timeline.tempoChanges` BPM at its mapped `sourceTick` and MUST NOT override the source tempo, including after source Visit cuts. `sessionStopped.effectivePerformanceTick` is an audit/context tick and never a future stop reservation or physical emergency-stop instruction. Full proposed rules and unresolved editorial status: `SESSION_STATE_MACHINE.md` Draft 0.11.

## S21 — Draft 0.12 timed-source tempo requirement (separate Profile 0.2)

`playing` Snapshot Positions and `sessionStarted`/`visitChanged` Event Positions MUST resolve OSTF source Tempo at the anchored `sourceTick`, even if redundant `tempoBpm` is absent. If it is unresolved, report `E-SESSION-TEMPO-UNRESOLVED` rather than fabricating BPM. Within a Visit, ideal score elapsed seconds are the sum of `60 * deltaTicks / (ppq * effectiveBpm)` across step-Tempo and selected source-segment boundaries. Do not bridge source cuts with stale BPM. Profile 0.2 Snapshot `participants` has structural `minItems:1` and the authority still must resolve uniquely. Proposed editorial semantics, not independently verified real-time behavior.

## Draft 0.13 — Additional optional Production Profile authority boundary

For an application that opts into Production Session Profile 0.1.0, source musical participation (`tracks[].enabled`/Clip/Note flags) is **not** the same state as audio Mixer Mute/Solo/Gain/Pan; Core logical MIDI Buses and CC controls are not audio Buses and Mixer automation. Device/Channel/Asset references and acyclic Bus routing must be checked against the byte-pinned score. The Profile's 12 `$defs` remain separate from 4.3 Core 127 `$defs` and Distributed Session Profile 0.2's 16 `$defs`. Host-internal execution, plug-in binary loading and user privileges are outside all format data. See `PRODUCTION_SESSION_PROFILE.md`.

## Draft 0.24 — Exact record-discriminator and revision disposition (editorial candidate)

A data reader MUST select the applicable Schema by the *document's own exact discriminators*, never by an HTTP media type, file extension, directory name, historical Draft heading, or JSON substring. The Core Score uses root `format:"OSTF"` and `version:"4.3.0"`. Distributed 0.1/0.2 Snapshot and Event objects use their own `profile:"OSTF-Distributed-Session-0.1"` / `"OSTF-Distributed-Session-0.2"`, respectively, and `recordType`; **they do not contain `profileVersion`**. Production 0.1.0/0.2.0 uses `profile:"OSTF-Production-Session"` plus mandatory `profileVersion:"0.1.0"` / `"0.2.0"`. These are the existing Schema constants; Draft 0.24 adds no payload fields.

An unknown discriminator combination MUST be reported as unsupported or invalid; a writer MUST NOT silently coerce one profile family into another. A structure that looks like an Event but carries a Production version tag is not a valid Distributed Event. Validate structure and references with the version-matched Schema and the corresponding semantic document. All semantic checks on Event replay operate on duplicate-key-free parsed objects, but Score pinning across Profiles still uses **exact original Score bytes**, not parsed-JSON equality. This deliberate distinction is retained from Draft 0.23.

**Revision acceptance order:** (1) verify and authenticate Session/Score/Plan + issuer, (2) compare authenticated eventId with accepted ledger and reject altered replay / no-op identical replay, (3) for genuinely new state-changing Events enforce the current base revision and single-authority transition, (4) check Visit/Part/clock/etc., then atomically record the accepted state transition. `phraseProposed`, observations and status reports are not silently promoted to state changes. Event acceptance remains non-executable data, not audio output or physical permission.

## S22 — Continuous source join versus hard cut (Draft 0.41, D01/D04 PENDING)

For an ordered pair of selected source intervals in one `performanceVisit`, classify **continuity per Track**. `sourceEnd_i == sourceStart_(i+1)`, adjacent expanded positions, and a resolved `fixed` Part on both sides are jointly necessary for a continuous join. Only such a join may preserve a Note gate selected by the preceding interval and the already selected MIDI controller stream; neither a duplicate Note On nor an artificial Note Off is emitted at the join. A source jump/gap, a new Visit, or any change to an `open`, `silent` or otherwise unresolved Part is a hard cut. A Note beginning precisely at the join belongs only to the next half-open segment. Crossing the continuous join does not change the original Note ID, probability, velocity-deviation or source duration; source map Tempo/Meter/Key/Harmony is re-resolved at each Section boundary even if continuous. The Derived Occurrence key remains attached to the original attack segment. New Source Note replay, acoustic/DSP continuity and external MIDI state reconstruction are separate operations; no new serialized fields, plugin execution or robot actuation is authorized. The exact worked case is `examples/17-fixed-note-source-cut.ostf`.


## Draft 0.42 — Event target association under Source-to-Visit projection (D01/D04 pending)

Selection of MIDI Event records uses Clip-local `event.start` projected into absolute source Tick, then the current fixed Plan's half-open segment. Non-targeted MIDI Events are selected only by their own time. A targeted event's selected Note association MUST resolve through a selected Note attack in the same Visit and a gate continuing to the Event Tick; a source-contiguous fixed join can preserve that occurrence, but a hard cut or skipped pre-entry attack cannot create it. An unresolved target MUST NOT be silently retargeted or stripped of its target to fabricate deterministic MIDI. Preserve source bytes, report the unresolved export decision, and do not infer any MIDI wire ordering between Note On and a same-Tick targeted controller beyond inherited event `order`. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.42 and `examples/17-fixed-note-source-cut.ostf`.

## S23 — Draft 0.43 selected vocal/lyric view (pending D01/D04)

In a finite fixed Visit, voice-scoped 4.2 lyric Alignments and VocalPerformance remain source authority; compute selected Note attack occurrences first. Multi-Note lyric mappings may be partially selected after source cuts; do not describe them as full mappings or forge new Unit/Alignment IDs. Note-scoped phoneme/pitch/expression information may only refer to the selected Note occurrence if the association remains valid for the surviving Note gate. Source-contiguous joins preserve one occurrence; hard cuts may truncate it without authoring a new phoneme or interpolation. Any deterministic vocal materialization is a separate, explicitly disclosed editing operation. Complete meaning and worked data witness: `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.43, `examples/15-vocal-response-phrasing.ostf`.

## S24 — Voice/Clip-scoped 4.2 VocalPerformance projection (Draft 0.45, D01/D04 PENDING)

In a finite `fixed` Performance Plan, a **non-note-targeted** 4.2 `breathEvent`,
`technique` with no `targetNoteId`, or `phonemeEvent` with no `noteId` remains a
Voice/Clip-authored timed item. Its source onset is `clip.start + item.start`
(Clip-local signed Tick converted to absolute Score Tick). It has a selected
**derived occurrence** only if that onset lies within a selected half-open
source segment for the Voice's actual Track in a `fixed` Part. Its effective
range ends at its authored end or the next **hard cut** in that fixed run,
whichever comes first. A source-contiguous fixed join in the same Visit does
not create a second breath/technique/phoneme occurrence; an excluded onset in
a skipped source segment does not become a newly authored item at re-entry.
Multiple Visits may have different derived occurrences of the same source ID.

A `phonemeEvent` lacking `noteId` retains its `unitId` and Voice/Clip ownership;
selection alone MUST NOT manufacture a Note association or an Alignment. A
possible Unit/Alignment association is not the same as a deterministic
note-targeted phoneme mapping. An implementation MUST disclose an unresolved
mapping before claiming fully specified singing export.

A 4.2 `expressionCurve` with **no `targetNoteId`** is Voice/Clip-scoped,
not note-scoped. For multiple points, its source-time function is defined only
between its first and last authored points under the inherited `step`/`linear`
interpolation meaning; outside that source support it is **unspecified**.
For one point, 4.2 defines a constant over the applicable Clip/Voice scope.
The finite Plan projects only the function's intersection with selected fixed
source ranges, evaluating at source Ticks rather than interpolating across
collapsed *expanded-time* jumps. It MUST NOT invent a default (such as `0.5`),
carry stale values from a prior Visit, or store newly synthesized boundary
control points into the source. At a source-contiguous join the piecewise
source function stays continuous where it is authored; at a hard cut or Visit
transition it is re-resolved from the source function without assuming the
previous audible value. Existing 4.2 **note-targeted** expression replacement
rules still take precedence within the selected Note gate: do not add the two
curves or create a competing Note/expression authority.

A selected, Voice/Clip-scoped event may occur during a rest and is **not** proof
that a source Note sounded; 4.2 Voice ownership, original lyric/phoneme timing,
and Plan Part `fixed/open/silent` boundaries remain authoritative. None of
these projections mandates audio output, creates a physical robot command,
or changes a source ID. Materializing an edited fixed rendition requires a
new Score revision, valid rewired identities and explicit timing/phoneme/curve
loss reporting. See `examples/15-vocal-response-phrasing.ostf`. All S24
meanings are unratified proposals, not adopted Core Schema changes.
