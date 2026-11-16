> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF Distributed Session Profile 0.2 — Proposed state/event semantics (Draft 0.53 editorial edition; no Schema changes)

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

**Scope.** Separate JSON records, never added to `.ostf`. The 0.2 proposal replaces 0.1's arbitrary event payloads with a seven-kind typed event union. It does **not** standardize transports, latency guarantees, robot control, security identities or singer/FX/audio interoperability.

## Event authority and state revisions

- Every event names `sessionId`, `documentId`, `revisionId`, `issuerParticipantId`, `eventId`, `baseStateRevision`, `effectivePerformanceTick` and typed `kind/payload`. Its pinned OSTF document/revision MUST match the current authoritative Snapshot.
- `eventId` is an idempotency key: receiving an identical event twice MUST NOT apply it twice. Same `eventId` with a different **parsed JSON content tree** MUST be treated as an integrity conflict; different insignificant whitespace or JSON object key order alone MUST NOT cause a conflict. JSON array order and actual values remain significant. Parsers MUST reject duplicate JSON object keys before comparing. This equality rule is for replay/idempotency, not a digital signature, and does not define a cryptographic canonical byte format.
- `phraseProposed`, `turnRequested`, `cueIssued`, `performanceObserved` and `participantStatus` carry **no** `resultStateRevision` and cannot mutate authoritative session state merely by being received.
- `phraseCommitted` and `sessionStateChanged` are the only 0.2 state-changing kinds. They MUST contain `resultStateRevision = baseStateRevision + 1` and MUST be accepted only from the session's declared `authorityParticipantId`, subject to independently enforced authentication/authorization. An event with stale base revision is never auto-applied; reconciling it requires an explicit new decision.
- Acceptance MUST be deterministic in authoritative revision order, not the arrival order or UTC message timestamp. Participants may suggest content or a turn but cannot assert commitment by changing the event kind locally without authority.
- The meaning of `effectivePerformanceTick` depends on the Event kind: an intended phrase/boundary position for scheduling kinds, an observed/context tick for observational kinds, and audit context only for immediate `sessionStopped`. A late musical proposal is NOT automatically executed in the past; host policy may reject or negotiate a new request. The comprehensive Draft 0.11 rule below supersedes older blanket "requested future boundary" wording.

## Snapshots and late join

A Profile 0.2 Snapshot MUST include `sessionStatus` (`prepared`, `playing`, or `stopped`), all participant identities, assigned Track IDs, current `stateRevision`, and `authorityParticipantId`. A **playing** Snapshot MUST include `position` (pinned Plan/Visit/source/performance ticks, clockDomainId, epochUtc, uncertainty); **prepared** and **stopped** MAY omit it. An omitted position in a stopped Snapshot does not mean performanceTick 0. The lifecycle status is session-wide authoritative state, never inferred from the latest `participantStatus` report. Earlier Draft 0.4 Profile 0.2 snapshots without this mandatory field need an explicit editorial migration decision, not silent guessing. `committedPhrases[]` contains self-contained session phrases needed for an active or future horizon. To claim faithful complete historical replay, a service must retain *all* committed past phrases in a separate durable log or complete snapshot; a live subset alone is insufficient.

The authority identifier must resolve to exactly one participant. Participant IDs must be unique. Each `assignedTrackIds[]` member MUST resolve to a pinned OSTF Track; multiple participants may be assigned the same Track unless the host enforces exclusive scheduling. Assignment does not itself authorize actuation. `position` must map to the referenced `performancePlanId/visitId/sourceTick` under the chosen finite Plan; `performanceTick` is derived from the Plan and is not separately invented. The `epochUtc` timestamp refers to the instant the displayed `performanceTick` was estimated in the named `clockDomainId`, with `uncertaintyMs` as the application's stated uncertainty bound. Providing a timestamp does not establish synchronized clocks; external clock discipline is mandatory for timed physical cooperation.

## Typed event payloads

| Kind | Fields in `payload` | Meaning |
| --- | --- | --- |
| `phraseProposed` | `proposalId`, `targetTrackId`, `phrase` | A candidate only; not the authoritative song or a scheduled actuation |
| `phraseCommitted` | `proposalId`, `targetTrackId`, `phrase` | Approved session realization; self-contained content for late join, not an OSTF file edit |
| `turnRequested` | `targetTrackId`, `requestedRole`, optional `requestedVisitId` | Request only |
| `cueIssued` | `cueId`, optional `targetVisitId` | Musical cue, not a robot command |
| `performanceObserved` | `observedParticipantId`, `sourceTrackId`, `confidence` and optional `features` | Observation with uncertainty; not authoritative note transcription |
| `participantStatus` | `participantId`, `availability`, optional `message` | Report only |
| `sessionStateChanged` | `changeKind` + required subtype fields | Accepted visit change, track assignment or stop; requires authority |

The minimal session Phrase 0.2 representation is `midi1Notes`: a finite `durationTicks` plus one or more `{startTick,durationTicks,pitch,velocity}` notes relative to the event's effectivePerformanceTick. Values use integers and MIDI 1.0 0–127 pitch / 1–127 velocity. Each Note MUST start at or after zero and finish no later than phrase `durationTicks`, unless a future Profile version explicitly adds tails. The phrase DOES NOT represent full OSTF Clips, Notes with SoundSlots, program state, MPE, lyrics, phonetics, audio, or physical motion; these remain future optional profile versions or separate agreed adaptations.

A committed phrase MUST match the proposal's `proposalId`, `targetTrackId` and content if the proposal is known. If not retained, the committed record is self-contained but host policy must still verify authority and absence of conflicting allocations. Committed phrases are bound to the exact effective performance position and track, not to a source Document Note ID. They do not mutate Core `tracks[].clips[]` unless a user authorizes explicit materialization into a new OSTF document revision.

## Session conflicts

When two accepted state-change Events claim the same `baseStateRevision`, **at most one** may advance the state to the next revision. The rest are rejected and may be resubmitted against the new revision. No last-writer-wins timestamp ordering. For a proposed phrase that overlaps already committed phrase intervals for the same Track, the Profile 0.2 authority MUST reject that new commitment; this version does not define replacement, deletion or automatic mixing. A distinct future Session or versioned extension would be needed for such a change. `sessionStateChanged` subtype payload must contain the fields defined in the Schema; event reception does not itself grant an actuator permission.

## Security and physical-AI separation

A Profile Event is a musical data assertion. Robot motor kinematics, safety, authentication, permission, time synchronization, jitter/latency handling, fail-safe actions and E-stop remain independently enforced in the robot controller and session service. Future extensions must preserve this boundary. Literal text/URLs/JSON within a file or event are untrusted inputs, never executable orders.

## Profile migration

Profile 0.1 and 0.2 are separately identified. A 0.1 payload with unconstrained object content is not automatically a valid 0.2 typed event. An explicit migrator may convert when the content satisfies the appropriate 0.2 payload and can establish a `documentId/revisionId` pair and session authority; otherwise preserve it as 0.1 rather than guessing.

## Draft 0.4: Lifecycle and stopped-session semantics

`sessionStateChanged(changeKind:"sessionStopped")` is a committed state transition by the declared session authority. After accepting it, the next authoritative Snapshot MUST report `sessionStatus:"stopped"`. A stopped Snapshot is not a ready-to-play actuation instruction. No new future phrase commitment can be adopted in a stopped Session without a separately specified new Session or lifecycle reinitialization; Profile 0.2 does not define a `resume` event. `participantStatus` reports individual availability and cannot change `sessionStatus`. A prepared Snapshot has no necessarily established playback clock; a playing Snapshot has an explicit Position and timing uncertainty.

## Draft 0.4: Temporal and event identity nuance

A Snapshot's `stateRevision` is a monotonic authoritative version, not a measure of musical Tick. Delayed network messages MAY arrive out of order; the `eventId` and `baseStateRevision` determine idempotency and whether a state change may be adopted. A serialized JSON property order and whitespace have no authority; content identity is the duplicate-key-free parsed JSON value. `effectivePerformanceTick` does not license scheduling after the safe window, and no payload is authorized robot motor control.

## Draft 0.5 editorial amendment — Explicit start and commitment coverage

The authoritative proposal in `SESSION_STATE_MACHINE.md` closes the absent `prepared → playing` transition by adding `sessionStateChanged(changeKind:"sessionStarted",position:...)`. It also adds optional Snapshot `commitmentWindow` to distinguish complete future accepted phrase coverage from a list that is merely partial. This is an in-draft amendment, not a published Profile 0.2 change. The full subtype and state rules in that amendment override any abbreviated earlier examples in this document when they differ. A proposed future `sessionStopped` is NOT a scheduled state change in 0.2; it is an immediate host-observed stop, and no parse or remote packet performs physical E-stop control. A committed phrase linked to a known proposal MUST preserve the proposed effective performance Tick in addition to content and Track.


## Draft 0.6 — Committed phrase allocation against the pinned OSTF Plan

**Proposed normative rule (not yet publisher-ratified):** An authoritative `phraseCommitted` event can produce a *supplemental session performance* only for an `open` Plan Part. It MUST NOT silently layer over a `fixed` Part, make sound on a `silent` Part, or interpret `unspecified` as open. Resolution uses `targetTrackId`, the accepted `effectivePerformanceTick`, the finite `phrase.durationTicks`, and the **pinned** Performance Plan. A Part's explicit `realization` takes precedence over that Plan's `defaultRealization` for its own Track in that Visit. A Plan Track omitted from `parts[]` with default `fixed`, `silent`, or `unspecified` is not an `open` target.

Both the phrase start and its entire half-open interval `[effectivePerformanceTick, effectivePerformanceTick + durationTicks)` MUST lie inside the finite expanded Plan and inside one Visit with `realization:"open"` for the target Track. Crossing an intra-Visit source Section boundary is permitted because a Visit defines one contiguous expanded musical span; crossing a Visit boundary is **not** permitted in Profile 0.2. Split and re-propose at the boundary instead of silently dropping or clipping Notes. Proposals may describe other targets, but the authority MUST reject an incompatible commitment until the source plan/revision is explicitly edited and all participants re-pin the new document revision. This release has no ad-hoc `fixed` overdub/replacement semantics.

A Session MUST have a uniquely pinned finite Plan before accepting any phrase commitment. **As amended in Draft 0.9**, every Snapshot/Event carries the binding at root `performancePlanId` and `scoreSha256`, including `prepared` Snapshots that omit musical `position`. An optional prepared Position gives a clock estimate but is **not** necessary to identify the pinned Plan. `sessionStarted` supplies the required first playing Position; its nested Plan ID MUST match the root binding. The source document, revision, digest and Plan stay pinned throughout the Session: Profile 0.2 defines no in-place Plan switch.

At an authoritative Snapshot `stateRevision`, every retained `committedPhrases[]` entry MUST also be consistent with the pinned Plan and target's `open` Visit Part. The same `commitEventId` MUST NOT appear twice, and two distinct accepted committed-phrase intervals MUST NOT overlap on the same Track. A `phraseCommitted` event creates an immutable accepted session phrase; Profile 0.2 does not define replacement, revocation or layer mixing. A later revision that changes a commitment requires a future versioned event type or a new Session, never an implicit overwrite. The authority MUST check the Track is assigned to at least one Session Participant at acceptance; this is not authorization for physical actuation.

**Separation from Core:** None of these checks modifies authored OSTF Notes, or reclassifies a Core fixed Note as a Session phrase. Unaccepted proposals and non-authoritative observed events are not guaranteed performance. These rules are cross-document semantic obligations; JSON Schema alone cannot inspect the external pinned `.ostf` or historical state.

Recommended diagnostic names: `E-SESSION-PLAN-UNPINNED`, `E-SESSION-PART-NOT-OPEN`, `E-SESSION-PHRASE-CROSSES-VISIT`, `E-SESSION-ACCEPTED-PHRASE-CONFLICT`, `E-SESSION-PIN-MISMATCH`. These are editorial candidates and not a certification of any runtime.

## Draft 0.7 — Score pinning, forward-only playback, commitment finality and replay ordering

**Editorial status: proposed normative amendment; publisher ratification pending.** These rules refine the *unpublished* Profile 0.2. They do not add any field to the 4.3 Core or to Profile 0.2, and they are not an implementation of a clock, transport, or robotic controller.

### A. Session score/revision pinning

1. The first authoritative Snapshot for a Session pins `sessionId`, `documentId`, `revisionId` and (when musical scheduling or playback is claimed) one finite OSTF `performancePlanId`. This pin is invariant throughout the Session. An HTTP GET for a newer revision, a participant changing its cached `.ostf` file, or a changed server alias MUST NOT silently change the active Session source.
2. Every subsequent Snapshot and Event MUST identify the same `sessionId`, `documentId` and `revisionId`; `position.performancePlanId`, when present, MUST equal the pinned Plan. If two different source document contents are presented under the same `(documentId, revisionId)`, a consumer MUST report an integrity conflict and MUST NOT continue claiming that its source-to-performance mapping is shared. This Profile does not impose a canonical hash or URL scheme: hosts must ensure equivalent pinned source content using their own authenticated revision/integrity controls.
3. Changing the Score, replacing the Plan, rebasing source Notes or adopting a newly revised remote JSON document requires a **new Session** for Profile 0.2. Merely incrementing Session `stateRevision` cannot rebind the underlying musical score.

### B. Atomic event admission order and idempotency

For an incoming state-changing Event, a Session authority SHOULD apply the following logically atomic checks, in this order. All are necessary before accepting a new state Revision:

| Step | Decision | Failure handling |
| --- | --- | --- |
| 1 | Parse/validate a duplicate-key-free typed Event, resolve its Session, verify the pinned Score identity, then authenticate and authorize its issuer against trusted Session state | Fail closed; no event-ledger acceptance information is exposed to unauthenticated senders |
| 2 | Check the authenticated `eventId` against the retained event ledger and compare the **whole parsed event value** | Identical already accepted Event is an **idempotent no-op** even when its base revision is now stale; same ID with altered content is an integrity conflict |
| 3 | For a **new** state-changing Event, require `baseStateRevision` to match the current authoritative revision | Reject stale/new conflicting event; no last-writer-wins |
| 4 | Check lifecycle, Visit mapping, target Track/Part allocation, accepted future-phrase conflicts, and any host scheduling lead-time policies | Reject or negotiate a **new** future proposal/command; never silently shift an accepted event |
| 5 | Require `resultStateRevision = baseStateRevision + 1`, then append one accepted event and publish the resulting Snapshot atomically | Either both log/state advance once or neither does |

Non-state-changing events are still untrusted; they MUST NOT mutate the authoritative Snapshot when merely received. After authentication and Score/Session identity verification, replay detection precedes the stale-revision test so that delayed identical network retries are harmless, while genuinely new stale events remain rejected. Authentication MUST NOT be bypassed simply because a replayed ID is known. A host that has lost the relevant event identity ledger MUST NOT claim that an unknown retransmission is an accepted new action.

### C. Monotonic expanded musical time and Visit changes

- In a `playing` Session, accepted `visitChanged` transitions MUST point to the **start Tick of a later Visit** in the same pinned finite Plan. Its expanded `effectivePerformanceTick` MUST be greater than the current authoritative observed `position.performanceTick` at admission; equal/past Tick, backward seek and a move back to a previous Visit are not specified in Profile 0.2 and MUST be rejected. This is an intentionally conservative rule; a new Session or future version may represent rewind/rehearsal behavior explicitly.
- Forward skips to a later Visit MAY be accepted if the authority can safely establish its new musical/clock anchor. Previously committed phrases located in skipped expanded Tick intervals remain in the immutable event ledger, **but are not asserted to have sounded**. A `commitmentWindow` continues to report accepted phrase records as-of revision, not guaranteed acoustic playback.
- No `visitChanged` is accepted in `prepared` or `stopped`, and this Profile defines no `paused`, `resume` or same-Session score-rebinding transition. Accepting a future Tick never guarantees that remotely observed wall clocks or physical actuators reached it.

### D. Accepted-phrase immutability and terminal stop

- A valid `phraseCommitted` creates an immutable accepted *Session* phrase at its explicit Track, single Visit and expanded Tick range. It does not convert a source Note into a new Note, does not start a robot, and is not overwritten by another phrase. Profile 0.2 has **no** phrase cancellation, deletion, replacement, extension, layers or overdub event. A musical correction requires a new Session or an explicitly versioned future extension; changing local playback after acceptance does not rewrite the ledger.
- A `sessionStopped` commits the terminal `stopped` state immediately. Previously committed phrases whose time lies after that stop are retained as historical acceptance records but **MUST NOT be represented as performed after stop**. Local actuator safety and actual termination remain external; the profile does not claim remote E-stop completion.
- A Session Snapshot can omit old or irrelevant phrases when it makes no completeness claim, but an included `commitmentWindow` MUST truthfully include **every accepted** phrase intersecting that window at its `stateRevision`, even if a later Visit skip made an event non-sounding. The Snapshot alone cannot certify actually sounded notes.

### E. Track assignment changes versus performance commitments

- An accepted `assignmentChanged` modifies a declared Participant's `assignedTrackIds`, **not** the Track identity or its accepted Session phrases. Participant `kind`, capabilities, availability and assignment do not imply that a robot is ready, authorized or uniquely selected to actuate.
- At acceptance of a `phraseCommitted`, the target Track MUST have at least one assigned Participant (as already required in Draft 0.6). An `assignmentChanged` MUST NOT remove the last assigned Participant for a Track that has *still-relevant future accepted phrases* without an explicit conflict decision; Profile 0.2 does not define a phrase revocation or performer-transfer acknowledgement. In this conservative candidate, **reject such an assignment change** and require the service to settle participant replacement through a separately authorized/new-Session decision.
- If more than one Participant is assigned to the same Track, the Profile does not decide which one actually renders/actuates. Execution routing and non-duplication are host-level decisions; Snapshot assignment alone cannot establish a completed performance.

### F. Examples of expected disposition (not additional fields)

| Sequence | Interpretation |
| --- | --- |
| An accepted commit is retransmitted after `stateRevision` advanced | Same event ID and same JSON value → idempotent no-op, not a second commit |
| Same event ID with altered `effectivePerformanceTick` | Integrity conflict; do not reschedule silently |
| A new commit has an older `baseStateRevision` | Reject as stale, even if its target audio event lies in the future |
| HTTP endpoint serves changed song content under the same revision | Integrity conflict; no auto-rebase of Plan or Tick |
| Authority requests a backward Visit | Reject for Profile 0.2; begin a new Session to rehearse |
| A forward Visit skip bypasses accepted phrases | Retain acceptance records; do not claim skipped phrases sounded |
| The Session stops before a future accepted phrase begins | Keep ledger; do not claim performance after stop |
| Assignment removes the only performer for an unplayed committed Track | Reject the assignment change; use a new explicit resolution path |

**Proposed diagnostics:** `E-SESSION-SCORE-DRIFT`, `E-SESSION-EVENT-ID-CONFLICT`, `E-SESSION-STATE-STALE`, `E-SESSION-BACKWARD-VISIT`, `E-SESSION-FUTURE-PHRASE-UNASSIGNED`, `E-SESSION-PHRASE-AFTER-STOP-CLAIM`. These are editorial reporting labels, not evidence of a complete validator or runtime interoperability.

## Draft 0.8 — Subtype exclusivity, event equality and Note-containment clarifications

**Unratified candidate amendment.** This section corrects a genuine structural bug in the *unreleased* Profile 0.2 Schema and clarifies the already intended Session meaning. The Core 4.3 Schema is unchanged.

1. A `sessionStateChanged` Event with `payload.changeKind:"assignmentChanged"` MUST contain `participantId` and `assignedTrackIds`; it MUST NOT contain either `targetVisitId` or `position`. The earlier Schema mistakenly used `not` with *both* `required:["targetVisitId"]` and `anyOf:[...]`, allowing `position` unless `targetVisitId` was also present. That condition is replaced with `not:{"anyOf":[{"required":["targetVisitId"]},{"required":["position"]}]}`. This fixes one subtype branch without adding a new definition or a new field. At the time of Draft 0.8, `sessionStarted` was the only subtype carrying `position`; Draft 0.10 supersedes this by requiring `position` for `visitChanged` as well, with the target Visit and `sessionStopped` neither changes assignments nor provides a future clock anchor.
2. Every `phrase` in **every** Event or Snapshot MUST contain Notes with `note.startTick + note.durationTicks <= phrase.durationTicks`. This holds even when a Snapshot lacks `commitmentWindow` or is `stopped`. `commitmentWindow` affects completeness *claims*, not the validity of each retained phrase. A note that crosses the phrase end is not silently truncated or accepted; the author must submit a new valid phrase.
3. An idempotent retry MUST pass trusted authentication/authorization and immutable Session/Score identity checks **before** a service confirms prior acceptance or exposes event-ledger state. Only after those checks can an already accepted identical Event bypass the stale `baseStateRevision` test. An untrusted matching `eventId` is not authorization to act, query the ledger or replay a physical gesture.
4. Whole parsed-event equality ignores JSON object property order and insignificant whitespace; it preserves array order and decoded string scalar values (no implicit Unicode normalization). JSON numbers are compared by their exact mathematical decimal values (for example `1` and `1.0` are equal), distinct from Boolean `true`/`false`; a consumer unable to compare without lossy numeric coercion MUST reject an ambiguous retry rather than claim equality. Duplicate object keys, non-finite numbers and invalid JSON are rejected. This is **not** a signature/canonical-byte format; authenticated transport and physical safety remain outside the Profile.
5. A stopped Snapshot MAY retain a committed historical Track phrase when no Participant is still assigned to that Track. A playing Snapshot MAY retain a phrase wholly behind its current authoritative performance position after a forward skip. Such records still obey identity, Note containment and accepted-phrase conflict rules. The "do not remove the last performer" condition applies to **still-relevant future commitments**, not to every historical record after stop/skip. No retained record proves acoustic output.

**Draft diagnostics:** `E-SESSION-ASSIGNMENT-POSITION`, `E-SESSION-PHRASE-NOTE-OVERFLOW`, `E-SESSION-UNAUTHENTICATED-REPLAY`, `E-SESSION-AMBIGUOUS-REPLAY-VALUE`. These are specified editorial outcomes, not independent interoperability evidence.

## Draft 0.9 — Normative candidate: immutable source bytes and explicit Plan binding

**Gap fixed:** A previously valid `prepared` Snapshot could omit `position` and therefore did not identify *which* Performance Plan was pinned. A Session Event also lacked a top-level Plan identifier. Naming `(documentId,revisionId)` alone is insufficient to detect two different JSON scores being served under the same human-readable Revision label. This amendment applies **only to the unpublished separate Profile 0.2**, not OSTF 4.3 Core or historical Profile 0.1.

1. Every Profile 0.2 `snapshot` and `event` MUST include a root `performancePlanId` identifying a *finite* `performancePlans[].id` in the pinned OSTF score, and a root `scoreSha256` matching `^[0-9a-f]{64}$`. Both are mandatory even on `prepared` and `stopped` Snapshots without `position` and on non-state-changing Events. The authoritative Session binding is now the tuple `(sessionId, documentId, revisionId, performancePlanId, scoreSha256)`; a Session cannot change any member of that tuple.
2. The digest is SHA-256 of the **exact byte sequence of the UTF-8 `.ostf` document artifact** used as the Session score: for HTTP responses this is the resource representation after decoding any HTTP Content-Encoding, before JSON parsing, Unicode normalization, whitespace changes or serialization. A BOM, if present in the original bytes, is included. Any byte change (even semantically equal JSON reformatting) changes the pinned artifact digest; this profile intentionally pins *artifact bytes*, not a musical-equivalence hash. A reserialized source must be an explicitly new Revision / Session binding, not an invisible refresh.
3. Every included `position.performancePlanId` (Snapshot or `sessionStarted` payload) MUST equal root `performancePlanId`. A positioned record MUST resolve its Visit and Tick mapping in that Plan. An absent `position` means only that no current clock anchor is asserted, **not** that the Plan is unpinned. The authority MUST verify the root Plan exists and is finite **before accepting any Session commitment**; do not infer a Plan from array order or from a lone available Plan.
4. An Event submitted to an authority MUST be authenticated as before, then matched to the full pinned source tuple (including Plan and exact byte digest) **before** prior Event-ID replay information is revealed. Same-ID parsed JSON equality remains the proposed idempotency rule; an altered Plan or digest is an integrity conflict, not a harmless retry. A content digest **does not authenticate the source or the participant**, validate licensing, or authorize robot actuation; those controls remain external.
5. Earlier **unpublished** Profile 0.2 Draft 0.8 payloads lacking root `performancePlanId`/`scoreSha256` are not 0.9-conformant; their authors must explicitly select and byte-pin the intended score. Versioned Profile 0.1 is separately preserved and must not be relabeled as 0.2. This draft amendment precedes formal publication, but application claims must identify which exact Profile 0.2 draft they accept.

**Diagnostics:** `E-SESSION-PLAN-UNPINNED`, `E-SESSION-POSITION-PLAN-MISMATCH`, `E-SESSION-SCORE-DIGEST`, `E-SESSION-SCORE-DRIFT`, `E-SESSION-REPLAY-PIN-CONFLICT`. A format parser can validate the digest syntax and mandatory presence; verifying it against the *actual score artifact* requires source access. Neither operation demonstrates live timing or physical performance.

## Draft 0.10 — Authoritative Visit-change clock re-anchor

**Draft 0.10 editorial amendment (unratified): a forward Visit transition requires its own clock anchor.** Previously, `visitChanged` carried only `targetVisitId`; a skip over one or more Visits could not convey the corresponding UTC musical anchor. This is a real data-model omission, not proof that a real-time system failed. The separate Profile 0.2 `sessionStateChanged.payload` now requires an existing `position` object for both `sessionStarted` and `visitChanged`. The `visitChanged` object MUST also contain `targetVisitId` and MUST NOT contain `participantId` or `assignedTrackIds`. `assignmentChanged` still forbids both `position` and `targetVisitId`; `sessionStopped` is unchanged.

For an authorized `visitChanged`, `position.visitId` MUST equal `targetVisitId`; `position.performancePlanId` MUST equal the root pinned `performancePlanId`; and `position.performanceTick` MUST equal both `event.effectivePerformanceTick` and the start Tick of the target Visit in the pinned *expanded* finite Plan. `position.sourceTick` MUST map to the **first source segment's first Tick** of that target Visit. `epochUtc` is the estimated clock-domain instant corresponding to this Tick (not the time the event was received); `uncertaintyMs` states uncertainty, not certified WAN synchronization. The event MUST still be authorized, use the frozen source tuple and advance strictly forward in performance Tick under the existing Profile 0.2 rules. In particular, the anchor alone does not authorize physical actuation or assert sounds occurred.

Earlier **unpublished** Draft 0.9 Profile 0.2 `visitChanged` payloads containing only a Visit ID are not conformant to this Draft 0.10 proposal: an author must re-anchor explicitly from trusted session/score/clock information. Do not invent a wall-clock instant or copy `epochUtc` from an earlier Visit without an authoritative calculation. Profile 0.1 remains a different versioned draft. OSTF 4.3 Core and its 4.2 baseline are not modified. Proposed diagnostics: `E-SESSION-VISIT-ANCHOR-MISSING`, `E-SESSION-VISIT-ANCHOR-MISMATCH`, `E-SESSION-VISIT-SOURCE-START`. These are semantic editorial rules, not evidence of robot, network or independent-parser conformance.

## Draft 0.11 — Clock-domain continuity, source tempo authority, and event-position semantics (UNRATIFIED)

This amendment applies **only** to the separate unpublished Distributed Session Profile 0.2; no new OSTF 4.3 Core musical fields are introduced. It clarifies already present `position.clockDomainId`, `position.tempoBpm`, `position.epochUtc`, `position.sourceTick`, and Event `effectivePerformanceTick`. Independent parser, WAN, DAW, robot, clock-accuracy and acoustic tests are excluded from the user-requested release gate and are **not** asserted complete.

### A. One authoritative clock domain per playing Session

1. An authorized `sessionStarted` MUST establish the Session's authoritative **musical clock domain** using `payload.position.clockDomainId`. The clock domain is an opaque ID, not a network endpoint, UTC synchronization protocol, device address, or cryptographic identity.
2. Every later authoritative `visitChanged.payload.position.clockDomainId` and every `playing` Snapshot `position.clockDomainId` in the **same** Session MUST equal the established ID. A `stopped` Snapshot MAY retain the last observation of this domain. A `prepared` Snapshot's optional Position does **not** establish a running clock domain. A conflicting domain value MUST be rejected as `E-SESSION-CLOCK-DOMAIN-MISMATCH`; the Profile has no clock-domain-switch event. Re-establishing a new clock domain requires a **new Session** or future versioned protocol.
3. No participant can establish a shared clock by merely writing the same `clockDomainId`. The value is a reference to an externally established common clock, and all real synchronization, error bounds and physical scheduling remain the implementation's responsibility.
4. A `visitChanged` MAY re-anchor `epochUtc` and `uncertaintyMs` at its target Visit while keeping `clockDomainId` unchanged. The timestamp corresponds to the Position's explicitly mapped expanded Tick; it MUST NOT be interpreted as message arrival time or as proof of synchronous sound.

### B. OSTF Tempo is the sole musical tempo authority

1. For any Position at a mapped source Tick `S`, the **effective source tempo** is the `bpm` of the final OSTF `timeline.tempoChanges[]` event with `at <= S`, following the inherited 4.2 step-tempo interpretation. Tempo is re-evaluated after every source segment/Visit jump. There is no interpolated ramp across a cut.
2. `position.tempoBpm` is **optional descriptive redundancy**. If present, its mathematical numeric value MUST equal the effective source tempo at `position.sourceTick`; it MUST NOT override, transpose, rescale or silently correct the source timeline. On a mismatch, reject the record as `E-SESSION-TEMPO-CONFLICT` before publishing it as authoritative musical-clock state.
3. When there is no effective source Tempo event at/before `S`, the tempo is **unresolved**. Do not invent a BPM from `position.tempoBpm`, the preceding Visit, a default constant, or an external performance engine and claim Core-conformant synchronization. The author should explicitly define the source tempo at or before each Visit entry, using a **new authored OSTF revision** as necessary. Profile `position.tempoBpm` cannot repair a missing source Tempo event.
4. A constant tempo across all source Visits does not need duplicate Position messages solely for this reason. A `visitChanged` still needs its own `position` clock anchor as defined in Draft 0.10. Numeric equality is semantic equality of JSON numbers (e.g. 120 and 120.0), not a fuzzy acoustical or floating-point tolerance assertion.

### C. `effectivePerformanceTick` is event-type dependent

- For `phraseProposed` and `phraseCommitted`, it identifies the proposed/committed phrase **start** in expanded music time. For `sessionStarted` and `visitChanged`, it MUST equal `payload.position.performanceTick` under the existing strict Visit rules.
- For `turnRequested` and `cueIssued`, it identifies the requested musical context/boundary; host policy may reject a stale or unschedulable request. For `performanceObserved` and `participantStatus`, it is a **reported musical context**, not an instruction to schedule robotic motion.
- For `sessionStateChanged(changeKind:"sessionStopped")`, it is an **audit/context tick only**; it MUST NOT be treated as a future stop reservation or as evidence of the actual acoustic/motor stop time. The authoritative stop is the accepted state transition. A received network JSON record is never an emergency-stop command. The event may carry `0` even if no playing position was ever established (e.g. prepared-to-stopped). No precise physically observed stopping Tick is implied.
- These are distinctions in the semantics of the existing mandatory property, not new event types or required fields. There is still no resume, rewind, clock-domain switch or actuator command in Profile 0.2.

**Authoring diagnostic examples (not standalone fixture files):** A `visitChanged` carrying `position.clockDomainId:"clock-B"` after `sessionStarted` pinned `"clock-A"` is rejected even when its Visit and Ticks match. A Position with `tempoBpm:121` for a pinned score whose effective source tempo is 120 BPM is rejected; omitting `tempoBpm` is valid and leaves the inherited OSTF tempo authoritative. A `sessionStopped` Event with `effectivePerformanceTick:0` is *not* a future stop scheduled at Tick 0.

**Ratification status:** proposed; author/publisher adoption, bilingual final text and CC0/MIT rights permission remain open. These semantics do not certify WAN synchronization or robot execution.

## Draft 0.12 — Running clock anchors require resolved source tempo (UNRATIFIED)

The mandatory `position` of a `playing` Snapshot and the mandatory `position` of a `sessionStarted` or `visitChanged` Event assert a *timed musical anchor*. Such an anchor MUST resolve a positive effective source Tempo at its `sourceTick` from the pinned OSTF `timeline.tempoChanges` (last event with `at <= sourceTick`). A missing `position.tempoBpm` **does not** authorize an assumed tempo: if no source Tempo exists, reject the timed anchor as `E-SESSION-TEMPO-UNRESOLVED`. A present `tempoBpm` remains redundant and MUST match the source value exactly as already required in Draft 0.11. This changes no Core song field and does not force every ordinary `.ostf` document to contain a Tempo event.

A `prepared` or `stopped` Snapshot MAY retain an optional `position` without being a running-clock assertion; if it has no effective source Tempo, a reader MUST NOT infer a schedulable musical-to-UTC continuation from it. Any present `tempoBpm` is still subject to Draft 0.11's equality requirement and MUST NOT repair absent source Tempo. Starting a Session with unresolved Tempo requires a newly *authored* OSTF revision that supplies it; `sessionStarted` MUST NOT invent a fallback tempo or silently rewrite the pinned source digest.

### Ideal tick-to-time integration after an anchor

For an interval of `n` ticks at source tempo `b` BPM and song resolution `ppq` ticks per quarter note, the ideal musical duration in seconds is `60 * n / (ppq * b)`. When walking **forward from an explicit authoritative Position** to a later performance Tick *within the same Visit*, split the path at every source Tempo change and selected source-segment boundary, re-evaluate the effective **source** Tempo at every segment entry, and sum these ideal durations piecewise. An omitted source range contributes **no** time; the prior segment's Tempo MUST NOT leak across a cut. If any traversed interval has no effective Tempo, the musical-time mapping for that interval is unresolved; implementations MUST NOT claim an inferred UTC performance deadline. The next `visitChanged` carries a fresh anchor, not an implicit extrapolation across an unobserved network transition.

This integration describes the **ideal score-time schedule**, not a remotely verified clock, time-server guarantee, sound-onset measurement or physical-actuation authorization. `uncertaintyMs`, communication latency, oscillator drift, servo delay and fail-safe behavior remain outside `.ostf` and cannot be certified from JSON.

### Minimum authority participant

Every Profile 0.2 Snapshot MUST contain at least one `participants[]` member, enforced structurally in Draft 0.12. Existing semantics still require `authorityParticipantId` to resolve to exactly one unique participant. No Participant's mere presence grants login, network or physical actuation rights.

**Illustrative negative (not a new file):** a Profile 0.2 `sessionStarted` Position with `sourceTick:0` and no `position.tempoBpm` is still invalid when its byte-pinned source OSTF has its earliest authored Tempo event at Tick 960, leaving Tick 0 without an effective Tempo. An unpositioned `prepared` Snapshot referring to that score is structurally valid (provided its pinned Plan and participant IDs are valid), but it cannot advance to `playing` without authoritative source Tempo. A Snapshot with `participants:[]` is now structurally invalid.

**Publisher status:** editorial proposal, not ratified. The author must approve this stricter timed-anchor meaning and companion Schema constraint along with previous 4.3 rules. No WAN, robot, DAW or independent-parser test is asserted.
