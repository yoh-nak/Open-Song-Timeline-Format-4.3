> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# Migration: OSTF 4.2.0 → 4.3.0 — Draft

## Upgrade

- Parse and validate using the **final 4.2 schema**; do not use a 4.3 schema merely to pretend 4.2 input is valid.
- Preserve all 4.2 data with stable IDs, musical ticks, notes, lyric alignments, and provenance.
- Change only root `version` to `4.3.0`, then check structural and semantic validity.
- Do **not** infer new `phrasing`, `vocalFreedom`, `ensembleInteractions`, `performancePlans`, or `performanceRequirements` from ordinary Track names, style tags or phrases.

## Downgrade

- If any 4.3 features are present, a 4.2-only writer cannot claim lossless downgrade without a separate preservation container and openly documented semantics.
- If a Plan has been materialized, record new concrete source Notes and revised provenance only after explicit author action; it is NOT an ordinary lossless downgrade of an unmaterialized Plan.
- Remove 4.3-only properties from a copy only after reporting exact lost JSON Pointers, retaining the 4.3 original.

## Known Draft risks

The inherited 4.2.0 schema matches the officially published SHA256 exactly. Its source authentication is documented in `SOURCE_RECONCILIATION.md`. The new 4.3 semantics remain editorial Draft; 4.2 compatibility is not evidence of external implementation compatibility.

## Draft 0.3 version separation

Song Core: 4.2.0→4.3.0 adds optional song-level fields and optional Direction/Track properties. No old Note/MIDI/Lyric structure is redefined. Session Profile JSON is **separately versioned**, and a Session Profile 0.1 object is not a valid Profile 0.2 object merely by relabeling its `profile`; field-specific conversion and authority validation are needed. 4.3→4.2 lossy export must list every removed new root/Track/Direction/ref property as a JSON Pointer rather than guessing behavior.

## Draft 0.4 further boundary clarification

4.2 migration does not synthesize Lyric Voices, ensemble relationships, repeated Note identities or Session event state. In 4.3, the same Track may be both actor and partner only if two distinct pre-existing Lyric Voice IDs are present; this is an opt-in 4.3 semantic interpretation, not a 4.2 migration step. Materializing a finite Plan into a new fixed OSTF must allocate new Note identities in a new document revision and preserve lineage where possible. The separate Session Profile 0.2 Snapshot lifecycle field is not part of the `.ostf` migration at all.
