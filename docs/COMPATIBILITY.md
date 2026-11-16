## Release claim boundary — Draft 0.103 editorial clarification (non-normative)

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

A published **format specification** is not proof of conformance by a third-party program. An implementer should separately state: profile (`Core 4.3`, `Distributed Session 0.2`, `Production Session 0.2`), operations (read/write/round-trip/execute), preservation of unknown fields, supported external assets, and any fidelity limitations. A JSON document passing a Schema check does not prove musical intent realization, plugin reconstruction, network synchronization, or robot actuation.

Any `D01`–`D05` issuer approval describes publication authority, not an executable compatibility certification. Runtime, independent-parser, DAW/plugin/DSP, WAN, and physical-AI/robot tests are expressly excluded from the release gate and remain unperformed. The adoption candidate files are not modified by this note.

> **Document status: Draft 0.103 editorial review (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

## Draft 0.44 — Vocal cut/interchange disclosure

Inherited 4.2 vocal source records remain byte-structurally valid under 4.3 without generating or changing their Units, Alignments, Voice identities or VocalPerformances. Expanding finite fixed Visits into a new recorded Score is **not** a lossless version-label conversion when source cuts omit some aligned Notes or truncate phoneme/curve spans. Such a writer must explicitly report incomplete associations and its new ID mapping, and must not silently invent missing syllable or phoneme performances. Source-preserving 4.2→4.3 migration does not add any of this derived performance data. See the Draft 0.44 example 15.

# OSTF 4.3 Compatibility and Safe Preservation — Draft

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

1. The `format` remains `OSTF` and serialization UTF-8 JSON with `.ostf` extension. Root `version` is `4.3.0`.
2. All 4.2 root required objects and inherited semantics are retained. 4.3 additions are optional and do not force a new Track, Lyric Voice, or Performance Plan.
3. 4.3 readers select the schema by version, and MUST NOT classify an unknown document as 4.2 merely because inherited properties are familiar.
4. A valid 4.2 source can normally become 4.3 by updating the version *after validating against the final 4.2 specification*. The inherited schema is reconstructed from the officially published 4.2.0 content and matches its public SHA256 exactly; see `SOURCE_RECONCILIATION.md`.
5. Downgrading 4.3 to 4.2 is lossless only if no 4.3 fields, new direction objects, or newly typed references exist. Otherwise loss is explicit and must not overwrite the source without informed author approval.
6. An editor unable to interpret an optional new 4.3 object must preserve it byte-equivalently or structurally non-lossily for a non-lossy save. If safe preservation cannot be guaranteed, refuse that save or offer explicit lossy export.
7. For direction-aware versions, `phrasing` and `vocalFreedom` follow the inherited `type + parameters` shape. Flattened drafts such as `{type:"phrasing",development:"variation"}` are **not** valid 4.3.
8. Performance Plans are opt-in playback views. An application ignoring them MAY play source Notes, but MUST NOT claim to have reproduced the specified expanded performance.
9. An `open` realization is non-deterministic and cannot be round-tripped as concrete Notes unless separately materialized. An absent Instruction is unspecified, never permission to freely improvise.
10. Session records are **not** `.ostf` song objects, and no session profile version is implied by a 4.3 file unless chosen separately.

## Draft 0.40 — `fixed` source Note identity and stochastic state

`fixed` selects authored Note records by source Tick and retains their original 4.2 `enabled`, `probability`, `velocityDeviation`, `velocity`, `releaseVelocity`, and `pitchRole` meanings. The same source Note in several Visits retains one source identity; a performance occurrence is a derived address, not a guaranteed sounding event. Values `0 < probability < 1`, nonzero deviation, or unspecified base velocity prevent an unqualified deterministic MIDI export claim unless resolved/materialized separately. Importing, viewing or changing a Plan does not modify 4.2 fields or create a PRNG/seeding rule. Profile versions and all six Schema files remain unchanged.

## Draft 0.3 editorial additions

The *song Core* remains the same 4.2-derived 127-definition structural model as Draft 0.2. The new note/source-cut semantics clarify a `fixed` Performance Plan interpretation without altering 4.2 Note/MIDI definitions. The separate, optional Session Profile evolves from the Draft 0.1 generic `payload` to Profile 0.2's typed union. These Session profile versions are not wire aliases and require an explicit migrator when converting.

## Draft 0.4 clarification

- A same-Track `ensembleInteraction` with two different explicitly identified Lyric Voice IDs is valid. Draft 0.3's blanket ban on same-Track relationships was an overrestriction; an implementation claiming Draft 0.4 Interaction-aware support must adopt the precise Voice rule.
- Source Notes revisited in a Plan remain one source identity; rendered performance occurrences have derived, Visit-scoped identities only. Materializing fixed performance requires unique new Note IDs in a new document revision.
- Draft Profile 0.2 Snapshots now require an explicit `sessionStatus` and need a Position when `playing`. Draft Profile 0.2 snapshots authored under Draft 0.3 without that field are not implicitly equivalent; require explicit author migration, not silent relabeling.
- The event-ID equality rule compares parsed content trees, not raw byte streams; neither this rule nor the Profile is a cryptographic identity/authentication specification.

## Draft 0.5 companion-profile migration note

The proposed `sessionStarted` subtype and optional `commitmentWindow` extend the **unpublished** Profile 0.2; Profile 0.1 remains a different schema. Existing Profile 0.2 snapshots that omit `commitmentWindow` are valid but **do not** assert complete future committed-phrase coverage. No Core 4.3 migration fields were added in Draft 0.5. The inherited 4.2 baseline must remain unchanged. This is an editorial update only; no robot/network/DAW validation is implied.

## Draft 0.6 separate Profile clarification

Existing OSTF 4.2/4.3 Core documents do not gain Session semantics merely by being upgraded. Profile 0.2 commitments are acceptable only for a separately pinned 4.3 finite Plan Part explicitly marked `open`. This allocation rule does not add/alter Core fields, so unchanged Core 4.3 Schema and 4.2 baseline remain byte-identical. Older example workflows that overlaid a Session phrase on `fixed` source material are not portable under this draft; the Plan author must explicitly mark the Part open and publish a new document revision.

## Draft 0.7 — Web and Session revision pinning

An OSTF 4.3 Core document remains independently versioned from the optional Distributed Session Profile. Within Profile 0.2, `stateRevision` increments represent accepted Session state changes, not OSTF document edits. Replacing a pinned Core `revisionId` is not a compatible in-Session operation. A new published Core revision requires a new Session in Profile 0.2. This editorial rule does not affect the 4.2 → 4.3 Core migration rules or imply backward seek support in Session Profile 0.1.

## Draft 0.10 — Unpublished Profile 0.2 authoring change

Draft 0.9 `visitChanged` objects with only `targetVisitId` lack the newly required authoritative `position`. They MUST NOT be silently interpreted as Draft 0.10 records: require a trusted event-time anchor to be supplied by the author/session authority. Only the **unpublished** Profile 0.2 schema and its example are amended. Profile 0.1 remains distinct; 4.3 Core and inherited 4.2 baseline do not change.

## Draft 0.11 — No new Profile 0.2 fields, stricter semantic interpretation

Earlier unpublished Profile 0.2 Position records with absent `tempoBpm` remain structurally valid (absence does not authorize inventing a source BPM). An earlier `visitChanged` that silently changed `clockDomainId`, or a Position with conflicting `tempoBpm`, is no longer semantically conforming to this Draft 0.11 candidate. Since Profile 0.2 is unpublished, revise those records explicitly rather than silently claiming compatibility. The musical Core Schema, its 4.2 baseline and Profile 0.2 field inventory are unchanged.

## Draft 0.13 — Third-party application production metadata

An OSTF 4.3 score is valid without production metadata. A separate Production Session Profile 0.1.0 MAY be used as a versioned and score-hash-pinned companion for audio channel Mixer control, Bus/Sends and plug-in Device chains; it is not a Core extension nor the Distributed Session Profile. Third-party hosts unable to load the plug-ins SHOULD preserve their descriptors and opaque state asset references, and MUST report loss when making a destructive export. An OSTF-score-only export drops audio mixer and plug-in state and is therefore lossy for the Profile's data. See `PRODUCTION_COMPATIBILITY.md`.

## Draft 0.19 — Cross-profile compatibility boundary

The Core 4.3 schema, Distributed Session Profile 0.2 and Production Profiles 0.1/0.2 remain separately versioned; no new field or migration is introduced by co-binding. When the same original 4.3 Score is supplied to two companion Profiles, the explicit byte digests and declared document/revision identities must agree; the remote selected finite Plan must exist in Core. This is a conditional **joint association** rule, not a new Core authority nor a cross-profile promise of audio, plugin, live transport or robot behavior. Invalid association is rejected non-destructively; an absent original Score allows only comparison of claims, never proof of original-byte identity.

## Draft 0.21 — Version-scoped interchange claims

Core 4.3, Distributed Session Profile 0.2, and Production Session Profile 0.1/0.2 remain independently versioned and selectable. A Core-only tool may work without either Profile; it must **not** claim complete project round-trip if it discarded companion data. A Production Profile reader that preserves only metadata, but not referenced opaque Audio or plug-in-state Asset bytes, may claim **descriptor preservation** but not full source transfer. Preserving opaque state is not equivalent to plug-in execution. Studio Preview is not a completed Score rebind; an edited Score requires a new explicit Production copy and a new Distributed Session identity. Feature and loss labels are explained in `docs/CONFORMANCE.md` and `PRODUCTION_SESSION_PROFILE.md` §27. These are unratified editorial rules, with no Core/schema field changes.

## Draft 0.23 — Link and digest interpretation across versions (editorial)

Core 4.3 has no required hash/canonicalization field. The separately versioned Distributed 0.2 root `scoreSha256` and Production 0.1/0.2 `score.sha256` are original-Score-byte digests. Profile declarations alone cannot prove original Score content when those bytes are missing, even if the two declarations match. The frozen 4.2 manual extract has three unresolvable historical local links, mapped without editing the inherited prose in `COMPLETE_MANUAL.md`. The 4.3 `NEW_FIELDS_COVERAGE.md` does **not** stand in for a full 4.2 field-to-example coverage matrix. No schema or data example is modified in this Draft 0.23 editorial reconciliation.

## Draft 0.24 — Correct family/version discrimination

The Distributed Profile 0.2 has *no* `profileVersion` root key. Its exact root `profile` constant includes `-0.2`, and each record also declares `recordType`. In contrast, Production Profiles 0.1.0/0.2.0 share `profile:"OSTF-Production-Session"` and differ by required `profileVersion`. A Core-only reader must not silently misidentify either as a Score document. An unknown profile/version combination is not a migration instruction. All six structural Schemas and existing examples remain unchanged. Corrected the misleading Production compatibility introduction and clarified stale state-change rejection vs authenticated idempotent retry. No automatic Score/Profile or device-state rewriting is permitted.

## Draft 0.41 — Compatibility of continuous source joins (proposal)

The revised `fixed` Plan-source boundary interpretation does not change 4.2 `notes[]`, MIDI events, Section IDs, or any of the six separately versioned Schemas. It clarifies that a gap/jump or new Visit requires a hard cut, while Section A→B in one fixed Visit may be source-contiguous and sustain a selected Note gate. Serialized Note velocities/probability are unaffected. A downgrade from 4.3 that loses Performance Plans is explicitly lossy; the new note-join interpretation is not silently reconstructed by a 4.2-only reader. This is a D01/D04 editorial candidate, not ratified compatibility or a tested audio crossfade guarantee.


## Draft 0.42 — Targeted MIDI cut/continuity and explicit export

4.2 MIDI `targetNoteId` is preserved unchanged in source Core. A 4.3 fixed Plan can select a controller event by its own Tick without selecting the Note it refers to; a deterministic expanded-MIDI writer MUST NOT silently retarget that event, erase its association, or claim a complete per-note MPE rendition. An eligible selected Note can remain associated across a source-contiguous fixed Section join inside one Visit. Require explicit resolution/diagnostics or refuse an export that cannot preserve the intended association. No 4.2 migration, Schema or raw MIDI format is changed.

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
