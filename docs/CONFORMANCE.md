# Draft 0.73 — Reference binding precedence decision cases (documentary examples only)

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

| Companion / authorized candidate scenario | Expected diagnostic |
|---|---|
| Malformed mandatory pin (even when candidate collection is empty) | INVALID |
| Unsupported profile version (even when Score exists) | UNSUPPORTED |
| Candidate enumeration incomplete, matching bytes already inspected | NOT_EVALUATED |
| Complete candidate list but one required Score unreadable | NOT_EVALUATED |
| Explicitly scoped empty complete candidate set | MISSING |
| One complete Score stream whose bytes represent newer Score only | MISMATCH |
| Matching Score bytes but invalid JSON/Core structure | Score format error |
| Valid matching Score, required Track missing | AMBIGUOUS + missing_referent |
| Valid matching Score, two different objects satisfy required referent | AMBIGUOUS + nonunique_referent |
| Two physical copies with identical bytes and unique referents | RESOLVED |
| Valid matching Score and all semantic referents uniquely resolved | RESOLVED |

These are *editorial cases*, not executed interoperability tests. No new wire-field statuses. If a historical example disagrees, Draft 0.73's current proposed decision order controls this review candidate, pending D01–D03 publisher ratification.

---

# Draft 0.72 — Capability claims: documentary examples, NOT executed tests

| Product claim | Acceptable scope statement | Unsupported inference |
|---|---|---|
| Score 4.3 reader | Reads declared fields; states unknown-field behavior | Can edit or preserve all fields |
| Score 4.3 round-trip | Preserves declared original data under disclosed operations | Produces identical musical performance |
| Production Session import | Interprets declared mixer and device metadata | Restores absent plugins or identical DSP |
| Distributed Session parsing | Reads participation, events and references | Delivers network events or safe robotic motion |
| `NOT_EVALUATED` Score binding | Evaluation incomplete in declared authorized scope | Missing globally or digest matched conclusively |

No runtime or independent interoperability testing was performed to substantiate these example claims. Adoption status D01–D05 is PENDING.

---

# Draft 0.71 — Documentary binding-decision examples (NOT execution tests)

| Authorized inspection state | Diagnostic | Caveat |
| --- | --- | --- |
| Enumeration incomplete; verified matching Score observed | `NOT_EVALUATED` | Do not infer completion from a matching candidate |
| Enumeration complete; one required Score unreadable | `NOT_EVALUATED` | Do not silently omit unreadable candidate |
| Complete authorized set empty | `MISSING` | Only for declared scope |
| Complete set contains byte candidates; none matches pinned SHA-256 | `MISMATCH` | Different revision remains a mismatch |
| Complete set, exact digest match, required Track absent | `AMBIGUOUS` | External detail: `missing_referent` |
| Complete set, exact digest match, duplicate required referent | `AMBIGUOUS` | External detail: `nonunique_referent` |
| Complete set, digest match, all required referents unique | `RESOLVED` | No runtime guarantee or authorization |
| Explicitly narrowed candidate scope; complete within narrower scope | Reassess for narrower scope | Disclose dropped candidate scope and any fetch failures |
| Invalid or unsupported Profile | `INVALID` / `UNSUPPORTED` | Outside binding stage |

**Precedence clarification:** The Draft 0.70 conditional RESOLVED exception under incomplete enumeration is withdrawn. This is a documentary proposal, not a passed test. The diagnostic names introduce no JSON properties.

---

# Draft 0.69 — Scope-limited reference diagnosis casebook (UNRATIFIED)

| Case | Candidate Score bytes authorized *and actually accessible* for this evaluation | Proposed result | Important limitation |
|---|---|---|---|
| A | None | `MISSING` | Only within the evaluated candidate scope; not global nonexistence |
| B | One newer revision, digest differs | `MISMATCH` | No implicit rebind to the new revision |
| C | Several candidates, all digests differ | `MISMATCH` | Multiple mismatches do not imply ambiguous matching identity |
| D | Identical digest-matched byte copies | Continue structural/referent checks | Duplicated storage paths do not create multiple Score identities |
| E | Digest-matched bytes with invalid Score JSON/schema | Score-format error | Never call the binding `RESOLVED` |
| F | Valid digest-matched Score; required Track absent | `AMBIGUOUS` + `missing_referent` | Detail distinguishes absence from plurality |
| G | Valid digest-matched Score; required referent occurs more than once | `AMBIGUOUS` + `nonunique_referent` | No first-match-by-array-order fallback |
| H | Authorized URL or cache key but byte retrieval not performed/possible | `not_evaluated` / `unknown` at operation level | Neither verified `MISSING` nor `MISMATCH`; no fifth binding state |
| I | Valid matching Score with all required referents unique | `RESOLVED` | Scope-bounded reference success, not execution or authenticity |

These are interpretation examples, **not tests or new serialized fields**. Candidate authorization, bytes availability and actual assessment scope must be disclosed in a diagnostic claim. A later assessment over a larger authorized set can yield a different result without invalidating the accurately scoped earlier report. D01–D05 remain pending. Independent parser, DAW, DSP/plugin, network/WAN and physical robot tests are excluded and unperformed.

---

# Draft 0.68 — corrected editorial case matrix (NOT EXECUTED)

| Case | Authorized Score byte candidates | Pin / required referents | Proposed result |
| --- | --- | --- | --- |
| A | None | Valid companion pin | `MISSING` |
| B | Only newer revision bytes | None match pin | `MISMATCH` (supersedes the historical Draft 0.62 `MISSING` example) |
| C | Several byte-distinct candidates | No digest matches | `MISMATCH` |
| D | Two file paths, byte-identical Score | Digest matches; all referents unique | `RESOLVED` |
| E | A matching Score | Score content malformed | Score format error, not `RESOLVED` |
| F | A matching valid Score | Required Track resolves to zero objects | `AMBIGUOUS` + `missing_referent` |
| G | A matching valid Score | Required Visit resolves to two objects | `AMBIGUOUS` + `nonunique_referent` |
| H | A matching valid Score | Multiple required referents fail differently | `AMBIGUOUS` + all diagnostic details |
| I | A matching valid Score | All required referents uniquely resolve | `RESOLVED` (not execution proof) |
| J | Any | Missing required companion pin | Format failure before binding states |

This matrix is a **documentary conformance expectation**, not an executed conformance suite. The historical Draft 0.62 table is retained for change traceability but must not be implemented as the current resolution precedence. No serialized fields, Schema constraints or tools have been changed.

---

# Draft 0.67 — Required-referent distinction (editorial cases; NOT executed)

| Preconditions | Proposed summary | Diagnostic detail (non-serialized) |
| --- | --- | --- |
| Profile invalid / version unsupported | INVALID / UNSUPPORTED (outside four) | Format or version issue |
| Original Score bytes unavailable | MISSING | Missing *Score bytes*, not internal Track/Plan |
| Authorized Score candidates available, none match pinned raw SHA | MISMATCH | No silent rebind |
| Digest matched, required Track has zero matching objects | AMBIGUOUS | `missing_referent` |
| Digest matched, required Visit has two valid matches | AMBIGUOUS | `nonunique_referent` |
| Digest matched, all required references uniquely resolve | RESOLVED | No execution guarantee |

These are interpretation examples, not automated test outcomes. The previous historical Draft 0.64 wording is superseded *as a recommended clarification* only upon publisher adoption.

---

# Draft 0.66 — Conformance claim gate (proposal only)

A product must not call itself unqualified “OSTF 4.3 fully compatible” solely because it parses a Score document. A meaningful claim includes the family and exact version, which operations work, whether unknown fields survive a read→write cycle, and whether companion Score pins remain exact after any serialization. Editing or exporting an unsupported field without loss reporting is not a lossless capability. This is a documentary policy proposal and does not certify any product.

---

# Draft 0.64 — Reference diagnosis boundary cases (editorial, not executed)

| Input state | Editorial result | Required disclosure |
| --- | --- | --- |
| Companion has no required pin or unsupported Profile version | INVALID / UNSUPPORTED (outside four binding states) | Companion version/format issue |
| Recognized Profile has valid pin; no authorized Score bytes | MISSING | Exact Score bytes unavailable |
| Recognized Profile has valid pin; authorized Score exists, all digests differ | MISMATCH | Do not auto-rebind to another revision |
| A digest-matched Score cannot be parsed as its declared Score format | Score format error (outside successful reference resolution) | Structural failure; not RESOLVED |
| Matching Score is parseable, but required Plan or Track reference is absent | AMBIGUOUS (unresolved semantic referent) | Report the actual missing referent |
| Matching Score is parseable; all required references resolve uniquely | RESOLVED | Reference binding only; no execution guarantee |

These are proposed reading rules for editorial review. They are not independent parser tests, nor executed conformance fixtures. D01–D05 are pending.

---

# Draft 0.63 — Candidate deterministic binding precedence (UNRATIFIED)

The following are **editorial examples only**, not executed tests:

| Authorized candidate bytes and references | Expected editorial classification | Reason |
| --- | --- | --- |
| No original Score bytes supplied, only a matching filename | MISSING | File naming is not a byte pin |
| Two different revisions available; neither hashes to pin | MISMATCH | Quantity of wrong candidates does not imply ambiguous pin |
| Multiple path copies with exact same original bytes; identifiers and referents valid | RESOLVED | One byte identity, many paths |
| Matching Score bytes available but the pinned `performancePlanId` does not resolve | AMBIGUOUS / unresolved referent | Digest alone does not resolve the semantic reference |
| Matching Score bytes and all required Plan, Track, Visit and range references resolve | RESOLVED | Complete binding resolution, without execution guarantee |
| Missing/invalid required pin or unknown required Profile version | Outside four states | Schema/format/version error first |
| Matching revision exists by displayed title but not by raw-byte digest | MISMATCH | Human-readable name cannot overwrite byte mismatch |

When a required field's Schema validation fails, do not mask that error as a reference-resolution state. If several diagnostics apply, report the earliest decisive failure and retain the full evidence; do not silently rebind. These illustrative outcomes require publisher adoption under D01–D03 and R04/R11/R13/R14. No new wire fields or operational test claims.

---

# Draft 0.62 — Bound Score resolution outcome table (UNRATIFIED)

| Observed input | State | Claim / safe response |
| --- | --- | --- |
| Exact Score bytes available and digest matches companion pin | RESOLVED | May process binding; does not establish audible execution |
| Original Score not available, only newest revised Score | MISSING | Preserve old pin; require explicit recovery or reassociation |
| Candidate Score bytes exist but digest differs | MISMATCH | Do not auto-rebind; report difference and retain original association |
| Distinct candidate identities cannot be disambiguated | AMBIGUOUS | Do not guess by name/path/order; require explicit selection |
| Multiple files containing identical bytes matching expected digest | RESOLVED | Same byte identity despite multiple filenames |
| Profile still pinned to old Score and old bytes archived | RESOLVED for old binding | Do not silently redirect to edited Score |
| Explicit rebind to revised Score but referenced Track/Visit removed | Rebind rejected/unresolved | Retain original association and request repair |

These labels are **documentation guidance**, not new required serialized fields or runtime-certified error codes. The proposed prohibitions and optional read-only treatment must be adopted by the publisher under R04/R11/R13/R14 and D01–D03.

---

# Draft 0.61 — Orphaned companion and interrupted-export cases (PROPOSED)

| Condition | Publication-level interoperability interpretation |
| --- | --- |
| Old-pinned Profile retained; original Score bytes also retained | Old-version Profile/Score pair remains identifiable; it is *not* automatically rebound to new Score |
| Old-pinned Profile retained; original Score overwritten and no archived original exists | Companion is orphaned/unresolved; cannot claim a coherent round trip of that pair |
| New Score committed; one selected companion rebinding fails | New Score may exist; failed companion remains old-bound or unresolved; entire bundle is *not* an atomic successful export |
| Temporary writes completed but final commit/rename uncertain | Result status is unknown until exact committed bytes and links are established; no success claim |
| Byte-identical old Score still available under another filename | Identity can still resolve by exact bytes; filename alone is not an identity guarantee |

These cases clarify Draft 0.60's rebinding procedure; no new JSON field, universal backup strategy, or tested transaction behavior is introduced. R04/R11/R13/R14 and D01–D03 are unsigned.

---

# Draft 0.60 — Rebind/export decision table (PROPOSED, not a tested implementation)

| Operation | Required editorial outcome before claiming consistent export |
| --- | --- |
| Change only Score formatting; Production and Distributed still pin old digest | Do **not** auto-update pins; exported set is not mutually rebound |
| Edit Notes, preserve opaque fields, explicitly choose one Profile for rebind | Check that Profile’s old digest and every referenced ID/range still resolve; leave all unselected Profiles pinned to original |
| Edit/delete a Track referenced by Session or Production | Reject that Profile’s rebind or present an explicit repair operation; do not silently drop its references |
| Unable to update all selected files together | Do not claim transaction success; preserve originals and report partial/failed output state |
| No edit; exact Score bytes preserved | Referencing Profile can retain the old pinned identity; this does not prove DSP or physical playback |

This is an editorial decision table, not proof that the packaged tools enforce these conditions. Reference: six bilingual Draft 0.60 candidate sections; ballots R04/R11/R13/R14. All D01–D05 are pending.

---

# Draft 0.59 — Normative source-of-truth and identity decision examples (PROPOSED; unsigned)

The following decisions close an editorial ambiguity without introducing JSON fields. These are **candidate** interpretations for R04/R11/R13/R14 and require publisher D01–D04 adoption.

| Input / action | Identity and preservation result | Safe capability wording |
| --- | --- | --- |
| Original Score bytes imported read-only; no export | Source digest unchanged; companion pinned Profiles retain their original association | “Score read/import (listed subset)” |
| Score exported with equivalent musical events but different serialized bytes | New SHA-256 means **new byte identity**; linked Profiles remain pinned to the old bytes until explicitly rebound | “Score re-serialized; existing pins not automatically transferred” |
| Unknown optional Score fields round-tripped verbatim while known notes edited | Report which bytes/JSON subtrees were preserved; do not call a changed Score byte-identical | “Known Score fields edited; unknown fields preserved as stated” |
| Unknown optional fields discarded on save | Loss must be identified; unchanged known notes do not make this lossless | “Partial Score export with disclosed omissions” |
| Production plug-in descriptor retained but binary preset or installed plug-in missing | Descriptor preservation is **not** asset-byte preservation or playable restoration | “Production metadata retained; dependency missing” |
| Session phrase committed without observation of audio/actuator action | Accepted event is session history only | “Session commitment recorded; execution unverified” |

**Boundary decision:** byte identity, semantic musical equivalence, recognized-field preservation, opaque-field retention, and audio/actuator reproduction are different propositions. A claim of one never proves the others. A digest is computed over the exact referenced bytes, not over normalized JSON, unless a separate explicit canonicalization convention is formally adopted. A proposed implementation SHOULD report loss outside OSTF; this draft defines no serialized loss-report requirement. Documentation examples and tools cannot override the versioned Schemas and publisher-approved normative texts. English and Japanese normative interpretations must agree before adoption.

**Release decision:** R01–R14 and D01–D05 all remain **PENDING**; this table is not a sign-off, test result or interoperability certification.

---

# Draft 0.58 — Narrow capability claim decision procedure (PROPOSED; unsigned)

A publisher evaluating a third-party implementation's OSTF support claim should record these decisions **for each operation** (read, retain, edit, export, play, synchronize, restore):

1. Identify the precise versioned family: Score Core 4.3.0, Distributed Session 0.2, or Production Session 0.2. Importing one does **not** imply support for another.
2. Identify the operation and supported data subset. Parsing is not round-trip retention; metadata retention is not executable restoration; an accepted Session event is not proof of audio output or physical actuation.
3. Compare incoming and outgoing data preservation. If unsupported optional fields are omitted or changed, disclose that scope rather than claim a lossless round trip. If companion Profiles pin the original serialized Score, a new Score digest requires an explicit rebinding decision, not automatic identity equivalence.
4. Differentiate a stored external asset URI from stored bytes, and a plugin descriptor from an installed executable processor. Neither dependency's availability is guaranteed by JSON validity.
5. Word the claim narrowly: e.g., "Score 4.3.0 read/import; Production Session unsupported; no assertion of audio equivalence." Do not use "OSTF 4.3 fully compatible" without specifying supported families, operations and known losses.

**Negative cases:** a Score-only importer claiming complete project round-trip; an exporter that silently discards vocal intent or plugin descriptors; a Production importer claiming sound matching without the target plugin; a Session recorder claiming a robot executed a committed event. Such claims are misleading even when imported JSON is structurally valid.

**Status:** This procedure interprets proposed R11/R13/R14 and is editorial guidance pending D01–D04 ratification. It introduces no new serialized fields, certified conformance class, automated test result or requirement for an OSTF-formatted loss-report object.

---

# Draft 0.56 — Conformance claim approval boundary (publisher proposal)

The proposed R01–R14 decisions are now indexed in `PUBLISHER_RELEASE_DECISIONS.md`; no new conformance class or required serialized report is introduced. A third-party's operation-specific claim can only describe explicitly handled families/versions and which supplied content it keeps; it must not imply audio fidelity, network authorization, robot safety, or universal preservation. An editorial publisher GO does **not** certify an independent implementation. If a corresponding normative duty is unsettled, it remains a candidate even if the decision ledger suggests ADOPT.

# Draft 0.55 — editorial capability/loss-reporting edge-case matrix (R14; proposed)

The following outcomes apply to **claims**, not to validator certification or additional JSON Schema requirements. All are pending publisher adoption.

| Scenario | Permitted narrow statement | Statement requiring more evidence or disclosure |
| --- | --- | --- |
| Reads 4.3 Score but ignores optional intents | “Score 4.3 import of stated fields” | “Full 4.3 performance interpretation” |
| Edits notes and discards unsupported 4.3 metadata | “Partial Score editor; dropped fields disclosed” | “Lossless Score round-trip” |
| Same notes, different Score bytes | “New serialized Score; rebind requires explicit action” | “Existing Session and Production pins automatically stay valid” |
| Imported Session committed phrase | “Committed Session event recorded” | “Phrase actually sounded / robot executed it” |
| Imported Production descriptor but plug-in absent | “Plug-in metadata retained; DSP unavailable” | “Plug-in restored / matching audio obtained” |
| External asset URI retained, bytes unavailable | “Asset reference retained, content missing” | “Self-contained project / full asset preservation” |
| Score plus one Profile converted, other omitted | “Partial multi-family export, omitted family reported” | “Full OSTF project export” |

Suggested **out-of-band loss report** (not an OSTF Schema extension): `family`, `version`, `operation`, `preserved`, `transformed`, `omitted`, `unavailableDependencies`, `sourceDigestBefore`, `sourceDigestAfter`, and `rebindDecision` as applicable. These are reporting concepts, *not mandated property names or a normative JSON payload*. If a consumer has no way to surface such a report, it must limit its advertised capabilities accordingly.

This is the R14 editorial decision candidate. No released implementation or real-time system is claimed to have been tested.

# Draft 0.54 — Third-party capability declaration and preservation contract (proposal, NOT RATIFIED)

An OSTF product must not advertise one ambiguous universal "4.3 supported" promise. **A capability claim describes an operation on an identified family and version, not a blanket certification of every Profile, asset, plug-in, or performance.** The declarations below are proposed editorial guidance for D01–D03/D04 review; they do not assert any implementation has passed tests and do not add Schema keys.

| Declaration scope | Minimum accurate claim | A claim that MUST NOT follow automatically |
| --- | --- | --- |
| Score Core 4.3 import | Can parse the exact 4.3.0 family/shape and report unsupported semantic features | Complete interpretation of optional performance intent, audio reproduction, or edits |
| Score Core 4.3 author/edit | Can save the stated edited fields and disclose other records discarded or changed | Lossless whole-Score preservation unless the entire supplied Score survives |
| Distributed Session 0.2 record/import | Can preserve the versioned Session snapshot/events and Score binding | WAN sync, identity authentication, real-time collaboration, robot execution |
| Production Session 0.2 import | Can retain mixer/device/routing/automation descriptions and referenced asset descriptors | Matching DAW sound, installed plug-ins, executable plug-in state, asset bytes present |
| Core + Profiles package interchange | Can exchange explicitly enumerated supplied Score, Profile and actual asset bytes | Implicit merging of multiple authority domains or universal DAW project format |

## Proposed operation-level preservation ledger

A publisher or host making a specific *non-lossy* operation claim should identify input family versions, exact supplied components, operation, output components, intentionally omitted components, and unresolved external dependencies. This is a recommended reporting convention, **not a new mandatory JSON property**.

1. **Read-only inspection:** Do not imply that merely displaying data updates the referenced Score, commits a Distributed event, or restores a plug-in.
2. **Score-only rewrite:** Report preservation of supplied Score fields, and do not imply preservation of an unsupplied companion Session/Profile/asset. Byte-rewriting changes Score SHA-256 even if notes are semantically unchanged.
3. **Production import without asset bytes:** Distinguish preserved descriptors from missing binaries. No plug-in install, state recreation, audio render, or network fetch is implied.
4. **Session snapshot/event conversion:** Preserve event identity, chronology and Score pinning as authored or disclose loss; acceptance/commitment is not a sound or physical-act observation.
5. **Partial export:** Identify each omitted family, unsupported optional object and dropped provided asset instead of labeling the combined document "lossless".

## Proposed conflict resolution order

**Family/version selection first** → authoritative versioned Schema shape → corresponding normative family specification and exact-field semantics → cross-family binding and loss reporting → examples/implementation notes as illustrations. An example or tool output cannot silently override a normative definition. English/Japanese normative duties must be reconciled before D04 rather than selecting whichever translation happens to be convenient. Score Notes and MIDI events, remote Session state, and Production mixer settings retain distinct authority. These rules remain **unratified** until D01–D03 are expressly adopted.


---

# Draft 0.53 — authoritative current-edition clarification (editorial, unratified)

The active review edition in this package is **Draft 0.53**; retained older Draft headings are historical change notes only. The serialized Core `4.3.0`, Distributed `0.2`, and Production `0.2` identities are **not** Draft numbers. If a historical passage appears to conflict with a current norm, report the exact contradictory clauses for D01–D03 publisher disposition rather than choosing the latest heading by chronology. This edition neither adds fields nor alters source data.

---

# OSTF 4.3 — Third-party Conformance and Authority Guide (Draft 0.51)

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

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

## Draft 0.43 — Vocal/lyric projection capability disclosure (publisher review pending)

A 4.3 Reader may preserve 4.2 Lyrics/Voices/VocalPerformance verbatim without implementing a finite-Plan vocal materializer. A Plan-aware inspection can report selected Note occurrences, complete/partial/absent Alignment coverage, and source phoneme/curve overlap beyond hard-cut Note gates; this is neither exact singing synthesis nor a guarantee of lossless export. A writer that materializes Visits must remap affected Core Notes and all dependent Lyric/VocalPerformance references, or disclose and decline unsupported transformations. Source Score ownership stays with 4.2 Lyrics/Note/VocalPerformance; no Distributed/Production or Web Profile authorizes physical or audible execution. D01/D04 adoption pending; example 15 illustrates this precise boundary.



## Draft 0.40 — Fixed Note-state interoperability boundary (unratified)

The complete OSTF 4.2 Note model has `enabled`, `probability` and `velocityDeviation` alongside authored `velocity` and optional release/pitch-role metadata. In a `fixed` Plan, a reader can derive eligible Note identities and times deterministically, but **not** assert a fully deterministic outgoing MIDI sequence when probability or velocity outcomes are unresolved. Multiple Visits give new derived performance occurrences without minting source Note IDs. To publish a deterministic expanded Score, materialize chosen outcomes explicitly with unambiguous velocities, under a new revision; preserve the original rather than deleting probability or rewriting the original automatically. `examples/25-source-note-repeated-visits.ostf` now contains one source Note with both inherited stochastic fields to illustrate this distinction; no Profile/Schema definition changes. Publisher sign-off D01 and D04 is pending.

## Draft 0.40 — Unambiguous current-edition labels (editorial; unratified)

A **current-edition** banner (`Current edition: Draft N` / `現行編集版：Draft N`)
identifies the editorial copy being reviewed, **not** a serialized `version`,
`profile`, or `profileVersion`, nor publisher approval. The leading H1 of a
current normative/reference document and its explicit current-edition banner
MUST agree on editorial Draft number. Earlier `## Draft N` addenda are
**historical proposals**, not alternative current authorities. A mismatch is
an editorial defect to correct and re-review under D04; do not resolve a
substantive semantic contradiction by preferring the newest displayed label.

`python tools/validate.py --audit-doc-editions` now separately checks the
precise value of the current-edition banner and the leading H1 (including
Japanese), detects multiple banners, and enforces the current release-gate
header. Draft 0.38's check incorrectly passed a Draft 0.37 banner when a
nearby title said Draft 0.38; this false negative has been corrected. This
change does not update JSON Schema, imply independent interoperability,
ratify semantics, authorize remote execution, or close D01–D05.

## Draft 0.38 — Current-edition and historical-text interpretation (editorial candidate; not adopted)

The **current review edition is Draft 0.49**. A `Draft 0.x` label on a retained addendum or in a quotation is *editorial history*, not a different serialized `version` or `profileVersion`. Primary EN/JA specifications have a current-edition heading; **only** [`RELEASE_READINESS.md`](RELEASE_READINESS.md) states the current D01–D05 release decision. The presence of historical MUST/SHOULD language does not make a proposal formally adopted.

When an implementer finds an inherited or historical rule that appears to conflict with the current candidate:

1. Identify the exact JSON family and serialized version, then the corresponding versioned Schema.
2. Quote both conflicting passages with document paths, headings and the affected stable IDs/fields. Distinguish *structural permission* from *cross-object semantic requirements* before declaring a contradiction.
3. **Do not infer a precedence from Draft number, file order, language, or example chronology.** Mark the contested operation unresolved for D01–D04 publisher review. Preserve the input non-destructively or refuse an unsafe save; provide an explicitly labelled lossy alternative only with consent.
4. Correct the EN and JA candidate prose together after an editorial decision, without rewriting the official inherited 4.2 Schema/manual or inventing a behavior for unrelated feature subsets.

A locally successful editorial audit or a current-edition banner is **not** D01–D05 approval, independent-format interoperability evidence, a license grant, or robot/DAW operation. This is documentation-only work.

---

## Draft 0.37 — Normative document map and conflict triage (editorial; unratified)

**Use the exact serialized family/version first.** Do not derive a Schema or features from a file extension, URL, product title or the chronological number of a Draft subheading. The table below is an *index to existing proposed authorities*, not a new hierarchy that overrides the versioned schemas.

| Data family and exact selector | Structural authority | Candidate semantic authority | What remains outside its authority |
| --- | --- | --- | --- |
| Score `.ostf` with `format:"OSTF"`, `version:"4.3.0"` | `schema/ostf-4.3.0.schema.json` | `docs/SPECIFICATION.md`, `docs/SEMANTIC_RULES.md`, `docs/PERFORMANCE_TIMELINE.md`, `docs/NOTE_AND_MIDI_CUT_SEMANTICS.md`; inherited 4.2 meanings stay unchanged | Session participation, Production Mixer, external API, plug-in/robot execution |
| Published Score `version:"4.2.0"` | `schema/ostf-4.2.0.schema.json` | Inherited 4.2 source as pinned in `docs/SOURCE_RECONCILIATION.md` | 4.3-only Directives/Plans; no automatic forward-version reinterpretation |
| Distributed records, `profile:"OSTF-Distributed-Session-0.1"` or `"OSTF-Distributed-Session-0.2"` | Exact `schema/ostf-distributed-session-{0.1,0.2}.schema.json` | 0.2: `docs/SESSION_PROFILE.md` and `docs/SESSION_STATE_MACHINE.md`; 0.1 historical scope stays distinct | Writing Score Notes, studio mixing, WAN clock guarantees, physical actuation |
| Production records, `profile:"OSTF-Production-Session"` and `profileVersion:"0.1.0"` or `"0.2.0"` | Exact `schema/ostf-production-session-{0.1,0.2}.schema.json` | `docs/PRODUCTION_SESSION_PROFILE.md`, `docs/PRODUCTION_COMPATIBILITY.md` | Score composition, Session Event admission, plug-in/DSP compatibility guarantees |

**Interpretation sequence:** (1) classify exact family and version; (2) validate that version's Schema; (3) resolve document-local references and the actual supplied source Score bytes when required; (4) apply only the matching family-specific semantic rules; (5) if companions are present, evaluate their *separate* links to the same exact source Score rather than merging their authorities; (6) describe unsupported semantics, missing Asset bodies, revisions and losses by the requested operation. `docs/COMPLETE_MANUAL.md` and `docs/PARAMETER_REFERENCE.md` are explanatory and field-reference companions, not independent authorities capable of overriding the Schema.

**Conflict disposition for D01–D04:** if two proposed normative texts disagree, mark the contested operation **unresolved** and escalate the two exact file/section references for publisher amendment. Neither newer Draft number, Markdown order, example content, array order nor a host default is an implicit tie-breaker. A difference between a Schema's permitted *shape* and a stricter cross-object semantic requirement is not automatically a contradiction: structural and semantic checks cover different rules. Examples and authoring helpers do not expand what the normative text permits. The profile families can remain independently valid while cross-binding is unresolved. **Nothing in this index authorizes an API fetch, event commit, plug-in launch, audio rendering or robot movement.**

**Current status:** proposed editorial consolidation only; no JSON shape/field change and no publisher ratification. D01–D05 remain PENDING, and excluded runtime/independent checks remain unperformed.

## Draft 0.36 — Current reader handoff and evidence map (editorial consolidation)

This section **indexes existing proposals**. It does not add a new Core/Profile property, endorse execution, or replace the existing full specifications. A third-party product SHOULD disclose the exact *family/version/operation* before claiming a capability.

| Input set actually supplied | Immutable identity to examine | What can be stated from data alone | What must **not** be inferred |
| --- | --- | --- | --- |
| OSTF Score alone | `format:"OSTF"`, `version:"4.3.0"` (or exact inherited version) | Source Score parse, semantics for supported fields, preserved bytes if actually retained | Studio plugin graph, live Session/robot state, or ability to regenerate intentions |
| Score + Production 0.1/0.2 | `score.sha256` vs exact bytes of the supplied `.ostf`; optional `documentId`/`revisionId` when authored | Pinned source association; authored mixer/plug-in descriptors, referenced media metadata | Missing asset bytes, plugin load/licensing, DSP equivalence, any live actuator authority |
| Score + Distributed 0.2 | `scoreSha256` plus `documentId`/`revisionId`, `performancePlanId`, exact Profile discriminator | Declared participants, chosen finite Plan, session-state/event record meanings, subject to reference checks | Accepted phrase automatically saved as Score Notes; accepted event actually sounded; robot permissions |
| Score + both Profiles | All of the above pins independently checked against **the same supplied Score bytes** | Compatible *record association* across three independent data owners | Implicit Participant→Production Channel binding; silent updates of either companion or the Score |
| Profile supplied without Score bytes | Only profile-declared IDs and digests | Metadata preserved with an unresolved source dependency | Verified Score/Plan/Track identity or any ability to author a new matching digest |
| Score reserialized / revised | New actual raw-byte SHA-256, explicit revision/ownership decisions | A new Score byte identity; a rebind **proposal** until explicitly authored | Reusing old hash pins, reviving an old Distributed session ID or rewiring production routing automatically |

**Data-only review recipe for D04:** confirm all six exact-version Schemas remain mapped in `EXAMPLES_GUIDE.md`; inspect `22-pinned-session-aaba.ostf` together with `session/03-snapshot-02.json` and `production/03-audio-regions-sidechain-02.json`; confirm that the raw-byte Score SHA is exactly matched by both companions; distinguish descriptor-only Asset preservation from actual supplied media bytes; review explicit-loss and unsupported-feature reporting. This is an editorial cross-reference checklist, not evidence of independent implementations or runtime success. When two normative drafts contradict each other, report the conflict for D01–D04 resolution rather than inventing a rule.

## Draft 0.33 — Transaction boundaries for third-party OSTF software (UNRATIFIED)

**Purpose.** An import, preview, Score save, collection export, Profile edit, Session event commit, and project publication are distinct *operations*. Passing one operation's checks is not permission to silently perform another. This is normative **proposal** for D01–D04 publisher review; it adds no JSON fields, executable command model, mandatory report wire format or multi-document atomic transaction protocol.

| Requested operation | Permitted result / authority | Must not silently perform | Required disclosure if incomplete |
| --- | --- | --- | --- |
| Parse or inspect Score | Read exact `format`/`version`, build view; allow `not_evaluated` for unsupported semantics | Generate Notes; edit companion Profile; load plug-ins; fetch remote Asset; authorize robot movement | Unknown semantics, unsupported version, unresolved references |
| Preview a prospective edit | Provide proposed target IDs / source-Tick impact without modifying saved document | Rewrite Notes, lyric links, Production Automation, or Session event history | Exact affected objects, ambiguity, unverified assumptions |
| Save a Score without touching others | Write valid Score in explicitly selected revision/scope | Retarget pinned Distributed Session or Production Profile when original Score bytes change | Digest change, unmodified companion pins, resulting stale-binding status |
| Save or rebind Production companion | Explicitly author new companion binding to supplied Score revision and recomputed original-byte SHA-256 | Mutate source Score or presume referenced plug-in/audio Asset bytes exist | Asset availability, Track/tempo/Plan review, omitted or approximated data |
| Accept Distributed Session event | Apply authorized event to version-pinned *session state* only under the Session Profile state-machine rules | Persist new Score Notes, rewrite source Audio Regions, change robot actuator state | Conflict/retry disposition, state Revision, unexecuted/rendering status |
| Export selected files | Preserve exactly the selected requested collection scope, separately inventorying supplied Asset bytes | Claim complete collection losslessness when supplied companion files or Asset bodies are omitted | Family/version, omitted stable IDs, missing body bytes, partial/lossy status |
| Publish an OSTF standard or bundle | Publisher separately approves exact final distribution bytes and rights | Interpret package build, static checks or license template as actual publication approval | D01–D05 and excluded runtime/independent verification status |

**Failure isolation:** Rejecting one write or event MUST NOT leave a partial *accepted* event-state mutation or falsely report Score/Profile persistence. A multi-document save with partial success requires a component-by-component outcome; this proposal does not mandate a filesystem/API rollback mechanism. If the app cannot guarantee the requested non-lossy scope, it must refuse that claim or offer a separately consented partial/lossy export. Reading alone must never infer a permission to update or execute.

**Interoperability boundary:** `sourceTick` and `performanceTick` are different spaces; a fixed Score Note, a production Automation event, and a Distributed phrase proposal do not become the same authoritative event by sharing a Track ID and time. Only explicit, versioned conversion or authoring may create new Score data. An authenticated accepted Session event is still not evidence of sounding notes or of physical robot execution.

**Status:** all rules above are requested for **publisher D01–D04 review**. They are not signed, accepted, runtime-tested, or a mandatory serialized report schema.

---

## Draft 0.32 — Original-byte identity versus information preservation (unratified editorial decision)

**Three separate assertions must not be conflated:**

| Assertion | Required evidence | What it does not guarantee |
| --- | --- | --- |
| **Original-byte Score identity** | SHA-256 of the exact supplied UTF-8 `.ostf` document bytes, bound to the referenced Score and checked before any parse/rewrite | JSON semantic equality, audio playback or external-source authorization |
| **Score meaning-preserving export** | Correct versioned structure, identities, references and original authored musical content, with unsupported optional information retained or losses disclosed | The resulting byte sequence is unchanged (formatting, key order and escaping may differ) |
| **Collection/Asset byte-complete preservation** | Inventory and exact retention of all *actually supplied* Score/Profile documents and supplied opaque Asset byte streams, according to explicitly requested collection scope | Playable plug-ins, same rendered audio, robotic execution or retention of never-supplied Asset bodies |

**Critical binding rule:** JSON parse-and-serialize may preserve the same musical values while changing raw Score bytes. If Score bytes change, the old `scoreSha256` / `score.sha256` is not valid for the newly serialized Score, even when semantic content is judged unchanged. A Writer MUST NOT silently reuse an old companion digest. It must either (a) preserve the original Score bytes unchanged; (b) explicitly create/rebind appropriate companion records with the newly computed digest under the applicable revision and session rules; or (c) decline the operation / issue a clearly labelled partial or lossy output with scope disclosure. A revision or distributed Session must never be silently rewritten merely to make a hash check pass. There is no portable canonical-JSON hashing algorithm in Score Core 4.3.

**External delivery:** HTTP compression and transport headers are not part of the hashed Score bytes. If decoded resource bytes are unavailable, a URI, ETag, digest declaration or visually equal JSON is not proof of Score-byte identity. The implementation must report `not_evaluated` / unresolved binding instead of manufacturing certainty.

This is a **proposed D01–D04 editorial clarification**, not a Schema change, automatic publication approval, required serialized reporting field or completed interoperability validation.

---

## Draft 0.30 — Cross-family authority / conflict disposition for independent hosts (PROPOSAL)

The following **editorial decision table** reconciles the existing candidate semantics without adding serialized fields. It is a **candidate for D01–D04 adoption**, not a completed standard amendment. A validator accepting JSON structure is not thereby entitled to perform the operation.

| Situation | Authoritative input | Permissible non-executing response | Forbidden shortcut |
| --- | --- | --- | --- |
| Score fixed Notes versus `phrasing` or `improvisation` | Score `tracks[].clips[].notes[]`, MIDI events | Preserve fixed events; treat Directions as hints for a *separately requested* generation | Regenerate Notes merely by loading a file |
| Distributed `phraseCommitted` versus Score Note data | Distributed event history for *session commitment*; Score Notes for stored arrangement | Retain committed event without modifying Score; materialize via an explicit new Score revision and report scope | Equate session acceptance with Score write permission |
| Production Audio Region versus Score Plan `silent` | Score Plan governs Score-derived performance; Production governs independent audio Regions | Preserve Audio Region; apply explicit Production mute when present | Mute all Studio audio solely because the musical Track is `silent` |
| Core MIDI CC versus Production channel automation | Distinct independent control domains | Preserve both; report unresolved host mapping if numeric controllers and mixer values cannot be mapped unambiguously | Replace a CC stream with a Production gain/pan lane or vice versa |
| Distributed Plan/Score pins versus newly edited Score | Original-byte Score digest plus explicit document/revision/Plan identity | Refuse implicit rebinding; request a new bound Profile/new session identity after review | Reuse a stale SHA or Track-name matching as an implicit update |
| Production state descriptor versus actual plug-in bytes | Descriptor and actually supplied Asset bytes are independently authoritative | Preserve supplied descriptor; disclose unavailable bytes separately | Claim sound/state restoration from URI/hash alone |
| Source Region/automation versus a repeated `visit` | Source Score Tick for authored data, expanded performance Tick for occurrence | Resolve each Visit from its source interval; report approximation/truncation | Carry state from the previous Visit or treat an omitted source range as played |
| Same-family authored directives that conflict | Version-specific formal meaning rules, not array order | Report `semantic_conflict`, preserve source, refuse affected action | Guess last-wins precedence |

**Diagnostic precedence for a single attempted operation:** parse and exact family/version selection first; Schema validation second; reference, digest and authority checks third; semantic-conflict and operation-support checks fourth; supplied-byte/preservation analysis fifth; execution support is a *separate* claim. Reporting one failure class does not suppress other verified failures. A host MAY report several diagnostics. This is an implementer reporting convention; no mandatory JSON report encoding, processing API, or plugin host behavior is prescribed.

**Partial/export contract:** identify the requested scope and the components actually supplied; the absence of an optional companion not supplied is not loss. Omitting supplied Profile bytes or Asset bytes in an output called *full collection lossless* is loss. An output containing descriptors but not the previously supplied Asset body cannot claim byte-complete preservation. Report exact affected IDs/paths where available; never manufacture unsupported values or a replayed physical action.

**Release decision:** These descriptions remain pending D01–D04 publisher/editorial adoption, with D05 rights/license authorization separately pending. Excluding execution tests does not change the need for those decisions.

---

## Draft 0.29 — Diagnostic and conformance reporting contract (proposed; not a new serialized Score/Profile field)

A third-party host must distinguish **validity**, **reference resolution**, **operation support**, **data preservation**, and **execution capability**. No host may infer support merely from successful JSON parsing. This editorial proposal does not mandate a particular CLI/UI/API shape; the following names are portable diagnostic *categories*, not new JSON Schema enums or additions to `.ostf` files.

| Category | Example | Decision / safe outcome |
| --- | --- | --- |
| `invalid_document` | Wrong family/version discriminator or JSON Schema failure | Reject the claimed conformant input; do not reinterpret as an older version |
| `unresolved_reference` | Missing Track, Voice, Section, Visit, device, asset or external Score | Report exact stable target ID/path; do not guess from names or array order |
| `semantic_conflict` | Incompatible authoritative Directions, duplicate session event ID with different content, invalid routing graph | Reject affected interpretation/transition; do not silently select last-wins |
| `unsupported_semantics` | Host reads a known Profile but cannot interpret sidechain or open solo instructions | Preserve when non-lossy writing; report unsupported behavior separately from invalid data |
| `missing_asset_bytes` | Plug-in URI/hash descriptor exists but referenced bytes were not provided | Preserve descriptor as supplied; never say media/plug-in state bytes or sound have been restored |
| `explicit_loss` | Score-only export excludes supplied Production Region or Session record | Identify omitted family, scope, stable IDs and assets; use distinct partial/lossy export or refuse |
| `stale_binding` | Production or Distributed Profile points at a different Score revision/hash | Require explicit rebind/new Session; do not mutate by matching Track names |
| `execution_unverified` | Robot/plug-in/DAW execution not assessed | Do not certify sound, safety or physical behavior merely from structurally valid data |

**Minimum useful report for a requested operation:** exact document family/version and operation name; outcome (`accepted`, `accepted_with_disclosure`, `rejected`, or `not_evaluated`); category, affected stable IDs and JSON Pointer / source path where available; what input bytes were actually supplied; whether information is preserved, omitted, approximated or unresolved; and an explicit distinction between static data checks and unperformed runtime/independent verification. This is a *reporting convention*, not a new file format or required persisted report Schema. Implementations may use their own diagnostics transport/representation.

**Authority rule:** The Score determines saved music; Distributed events determine only Session state; Production determines Studio state. Neither a warning nor an accepted Session event grants physical actuation, plug-in execution, URL fetching or Score modification. If two proposed normative documents contradict, report the conflict and request publisher resolution instead of inventing cross-document precedence. `D01–D05` publication approvals remain pending.

### Examples of report decisions (not normative JSON fixtures)

- A Score-only editor opens an otherwise valid 4.3 Score with unknown optional Directions: valid input, `unsupported_semantics` for interpretation, but non-lossy save is permissible only if the untouched Directions and all supplied Score information are truly preserved.
- A Production Profile references a missing plug-in state blob: `missing_asset_bytes`, not `invalid_document` merely for lack of downloaded bytes, unless an applicable structural or reference rule independently fails.
- A Studio-to-Score-only export omits the **supplied** Production Profile: valid partial export with `explicit_loss`, never full-collection lossless output.
- A remote state-changing Event has a new event ID but stale base Revision: `semantic_conflict` and rejection; an authenticated, identical already-accepted replay may be an idempotent no-op under Distributed 0.2 rules.

This proposed diagnostic taxonomy is a quality-of-interchange recommendation. It is **not evidence that any external host implements or passes it**, and does not add a mandatory conformance test to the user's runtime-test-exempt release gate.

---

## Draft 0.28 — Interchange/save transaction contract (unratified editorial candidate)

The following is guidance for **one requested save/export transaction**, not a new serialized object, a ZIP project standard, or a requirement for an audio/AI runtime. It specializes the supplied-input-set distinction in Draft 0.27. Record the transaction's **requested scope**, **actually supplied input components**, **preservation status** and **loss disclosures** before making any non-lossy claim.

| Scenario | Supplied input | Requested output | Accurate claim | Required caveat / action |
| --- | --- | --- | --- | --- |
| A. Score-only edit | Score; neither companion Profile was supplied | Revised Score | Score-only preservation (if all supplied Score information is retained) | Do not fabricate companion Profiles or call their absence a loss |
| B. Score-only export from studio | Score + Production Profile + two actual Asset byte streams | Score only | Partial / lossy **collection export**, even if Score is preserved | Identify omitted Production/Profile stable IDs and both omitted Asset streams; never call it full-session lossless |
| C. Descriptor-only plug-in exchange | Score + Production Profile carrying state Asset URI/digest; binary bytes were NOT supplied | Score + Profile preserving URI/digest | Descriptor-preserving, not asset-byte-complete | Mark Asset bytes as *not supplied*, not *successfully preserved*; do not invent a plug-in preset |
| D. Full supplied-data preservation | Score + actually supplied Distributed/Production records + supplied Asset byte streams | Complete collection retaining supplied records and bytes | Eligible to claim collection preservation (subject to actual non-lossy semantics) | Rebind all Score hashes/references on explicit revision change; does not imply executable plug-ins or synchronized robots |
| E. Remote committed phrase | Score + Distributed event with accepted `phraseCommitted` | Saved Score without explicit materialization | Core Score unchanged; remote event/history retained only if corresponding supplied Session record is retained | No implicit modification of Core Notes or Production Audio Regions |

**Decision procedure (proposed):** (1) identify the exact family/version of each *supplied* document; (2) validate the target operation's scope; (3) inventory supplied Asset bytes separately from descriptors; (4) decide whether the output includes each supplied component and semantics; (5) report omitted, unresolved, approximated, and externally dependent elements using stable IDs and source paths when available; (6) if a non-lossy result cannot be produced, decline that operation or request informed acceptance of a separately labeled partial/lossy export. A report about omitted data is not a replacement for an actually lossless save.

Companion `score.sha256` / `scoreSha256` pins the **original OSTF UTF-8 file bytes**, not a canonicalized JSON tree; relabeling a revised Score without rebuilding permitted companion bindings is not a valid shortcut. Old session state, event IDs, physical-device grants and plug-in execution permission cannot be transferred by merely copying matching Track IDs. These are editorial interpretations pending D01–D05; software quality and security tests are explicitly outside the user-requested release gate.

---

## OSTF 4.3 Draft 0.27 — Conformance scope and retained historical feature proposals

## Draft 0.27 — Minimum third-party implementation declaration (editorial candidate)

A product MUST NOT use a single unqualified label such as “OSTF 4.3 compatible” as a substitute for describing which **document family, exact version, and operation** it actually implements. Suggested human-readable declaration (NOT a new JSON payload or a machine-certified compatibility badge):

| Reported item | Example statement | Avoid claiming |
| --- | --- | --- |
| Score | Score 4.3.0: parse, validate known semantics; write only if all supplied optional information can be preserved | “All 4.3 functionality” from successful JSON parsing |
| Distributed | Distributed 0.2: parse records; preserve event history; no live protocol/runtime implementation | Valid WAN clock sync or safe robot operation |
| Production | Production 0.2.0: preserve channels, devices, assets descriptors; unresolved external bytes disclosed | Identical plug-in sound, license to run proprietary software, full asset round-trip |
| Version / omission | Distributed 0.1 is a *different* version, not an alias for 0.2; absent never-supplied Profile is allowed | Treating missing optional companion records as corrupt Score data |

For the **non-lossy** claim, define the operation's *input set*: (1) the supplied Score JSON bytes/objects, (2) each supplied companion Profile, and (3) each supplied external Asset byte stream. A preserved **reference** to an Asset is not preserved **bytes**; neither is an Asset absent from the input set an omission by the Writer. If any input component is intentionally dropped or approximated, the output MUST be clearly labeled as a **lossy or partial export** and the impacted stable IDs/JSON pointers reported. A host MAY decline the non-lossy save instead.

This table describes interchange **claims**, not an obligation to develop an audio engine, WAN controller, plug-in host or robot. It does not guarantee identical sound or musical improvisation from the same abstract directions. The author/publisher must still adopt or amend this editorial candidate before a normative release.

---

## Historical Draft 0.26 — Document-family acceptance and scope reporting (editorial candidate)

A third-party host may implement a subset of this interchange system. A **supported exact document family/version** is a different statement from a successfully loaded plug-in, reconstructed sample, valid live network session or robot execution. The following is a current navigation/diagnostic decision table; it introduces **no new on-disk JSON field or permission**.

| Incoming record | Exact discriminator to inspect | Required authority for structural checks | Portable scope of a read operation |
| --- | --- | --- | --- |
| OSTF Score 4.3 | `format:"OSTF"` and `version:"4.3.0"` | `schema/ostf-4.3.0.schema.json` | Musical source; does not imply either optional Session Profile exists |
| OSTF Score 4.2 | `format:"OSTF"` and `version:"4.2.0"` | `schema/ostf-4.2.0.schema.json` | Inherited source; 4.3 fields MUST NOT be silently grafted onto it |
| Distributed Session 0.2 | `profile:"OSTF-Distributed-Session-0.2"` and typed `recordType` | `schema/ostf-distributed-session-0.2.schema.json` | Pinned, proposed/accepted session state; has **no `profileVersion` discriminator** |
| Production Session 0.1/0.2 | `profile:"OSTF-Production-Session"` plus **required** `profileVersion:"0.1.0"` or `"0.2.0"` | Exact matched `ostf-production-session-0.1/0.2.schema.json` | Authored studio settings/media references; not plug-in execution |
| Unknown/unsupported version or family | No known exact discriminator | No safe fallback Schema | Preserve as uninterpreted data if possible, or refuse a non-lossy edit; NEVER silently reinterpret as older known revision |

For every imported family, an application SHOULD distinguish **(a)** malformed/unknown format, **(b)** valid document with unresolved references or missing pinned Score bytes, **(c)** accepted readable data with an unsupported meaning, **(d)** stored metadata for absent external Asset bytes, **(e)** loss disclosed during export, and **(f)** an out-of-scope execution failure. A non-lossy Writer MUST NOT convert (b)–(d) into invented objects or assume missing Asset bytes exist; if full preservation is unavailable it MUST refuse the lossless claim or offer an explicitly agreed lossy output. A Score-only export is not automatically a lossless combined Score+Production+Distributed export when those companion records were supplied.

If the exact Schema and semantic documents give irreconcilable instructions, an implementation MUST preserve the submitted data and report a **specification conflict for publisher resolution**, not silently assert a precedence that changes musical intent. The inherited 4.2 authority applies to inherited fields; Score semantics are in `SPECIFICATION.md`/`SEMANTIC_RULES.md`, Distributed event state in `SESSION_STATE_MACHINE.md`, Studio state in `PRODUCTION_SESSION_PROFILE.md`. A publisher review is still required before these candidate MUST/SHOULD rules become the adopted standard.

**Status:** no Profile capability, successful live actuation, copyright permission or publisher ratification is granted by this table. All runtime/independent implementation checks remain outside the user-requested release gate, not "passed."

---

## Draft 0.25 — Portable data authority and honest feature claims (proposed)

**Status:** publication candidate, not an adopted normative standard. These rules are a current review layer over the shipped 4.3/companion schemas; original 4.2 meanings and six schema bytes are unchanged. This section resolves ambiguity for products that read the Score, remote Sessions and Studio Production documents *together*.

### A. Explicit data and operation layers

| Layer / source | Portable authority | What it does NOT authorize |
| --- | --- | --- |
| OSTF 4.3 Score `timeline` and `harmony` | Authored musical structure / harmonic context | Audio clock master, physical control |
| Score `tracks[].clips[].notes[]` and `midiEvents[]` | Authored fixed musical performance | Automatic improvisation from Directions |
| Score `lyrics`, Voice / Alignments, `vocalPerformances` | Authored lyric ownership, Note links, vocal expression | Replacing Note or text sources by inference |
| Score Track Directions, Interactions, Plans and Requirements | Intent, Visit order, abstract constraints/capability *requirements* | Audio/video DSP, robot capability certification |
| Distributed Session 0.2 accepted Event ledger / Snapshot | Session state and *accepted* performance proposals anchored to pinned Score bytes / Plan | Mutating the OSTF Score, automatic audible output, permission to actuate |
| Production Session 0.2 channels, Devices, Region / Automation / Assets | Authored Studio mix and media/plug-in **descriptors**; actual asset bytes only when supplied | Granting rights to install/run plug-ins or treating CC as mixer faders |
| Web API / host / robot controller | Transport, authentication and actual execution decisions (external to OSTF) | Changing the authored musical data by pretending that the JSON itself is a command |

**Companion identity:** an original Score byte digest asserted by both companion Profiles is a *binding check*, not a signature or permission. An absent companion Profile is *not* an omitted required Score field; it may be deliberately absent. A companion provided but dropped during claimed combined-data export is an explicit loss. A referenced Asset whose bytes were not supplied is **unavailable material**, not preserved media. Revisions and re-binding require newly authored records, not silent hash substitution.

### B. Version-scoped capability claims and failure reporting

A third-party product claiming any OSTF capability SHOULD publish each supported `(record family, exact version, operation)` separately; examples: `Score 4.3 parse`, `Score 4.3 non-lossy write`, `Distributed 0.2 event-ledger preservation`, `Production 0.2 media-byte preservation`, `Studio source-selection semantics`. An importer that can **parse** JSON but cannot preserve unknown or unsupported data MUST NOT advertise a non-lossy Writer. Processing one Profile does not imply the others.

| Given operation | Allowed data-only claim | Must be reported or refused |
| --- | --- | --- |
| Read 4.3 Score only, no Profiles supplied | Score parsing and supported musical semantics | No implicit mixer, robot or remote Session reconstruction |
| Read production Profile with plugin-state descriptor but unavailable bytes | Descriptor and unresolved-asset preservation | Do not claim a complete plug-in-state round trip |
| Write Score-only from supplied Score + Production + Distributed | Explicitly partial Score export | Production and remote records are omissions if not separately retained |
| Persist accepted remote `phraseCommitted` | Distributed Session state/history only | Do not claim concrete Score Notes were inserted or acoustically performed |
| Create a revised Score and carry Studio settings | Rebind **proposal** until explicitly authored new Profile pin and reviewed source timing | Silent same-Session migration; implicit source-tick shifting |
| Host cannot faithfully implement a mixer graph/automation | Input preservation or labeled lossy approximation | No undisclosed routing or bypass changes, no DSP-equivalence claim |
| Session data refers to Score by ID and hash but Score bytes not supplied | Declared identity comparison only | Do not claim the real Score/Plan/Track was verified |

Loss reports SHOULD identify stable object IDs or JSON Pointers, classify `omitted`, `approximated`, `unavailable`, `unsupported`, `unresolved`, or `not-executed`, and say whether source bytes were retained. This is a proposed **reporting vocabulary**, not new serialized Core/Profile fields. A *failed* non-lossy write and an *accepted* explicitly lossy export are not interchangeable outcomes.

### C. Reference precedence and no-inference rule

Structural shape is governed by the **exact versioned JSON Schema**; inherited 4.2 semantics remain authoritative for inherited fields; novel 4.3 musical meanings are described by `SPECIFICATION.md` and `SEMANTIC_RULES.md`; remote event admission is described by `SESSION_STATE_MACHINE.md`; Studio data by `PRODUCTION_SESSION_PROFILE.md`. This matrix helps a reader navigate; it does **not** silently resolve genuinely conflicting documents. If a cross-document claim contradicts its authority, an implementer MUST report the conflict and preserve source data, not invent a priority or change a version marker. Japanese-language descriptions are pending editorial equivalence approval.

Only the author/publisher can adopt these proposed normative rules and grant publication rights. Static examples and bundled CC0/MIT draft texts do not constitute an approval or third-party/runtime certification.

---

## Draft 0.24 — Exact interchange record identification and non-executable authority

The following table is an **editorial interoperability proposal** based on the shipped Schema constants, not new JSON fields or proof of software operation.

| Document | Discriminator values in the JSON | Additional selector | Exact Schema |
| --- | --- | --- | --- |
| Music Score 4.3 | `format:"OSTF"`, `version:"4.3.0"` | No companion `profile` required | `schema/ostf-4.3.0.schema.json` |
| Distributed Session 0.1 | `profile:"OSTF-Distributed-Session-0.1"` | `recordType:"snapshot"` or `"event"`; **no `profileVersion`** | `schema/ostf-distributed-session-0.1.schema.json` |
| Distributed Session 0.2 | `profile:"OSTF-Distributed-Session-0.2"` | `recordType:"snapshot"` or `"event"`; **no `profileVersion`** | `schema/ostf-distributed-session-0.2.schema.json` |
| Production Session 0.1 | `profile:"OSTF-Production-Session"` | `profileVersion:"0.1.0"` | `schema/ostf-production-session-0.1.schema.json` |
| Production Session 0.2 | `profile:"OSTF-Production-Session"` | `profileVersion:"0.2.0"` | `schema/ostf-production-session-0.2.schema.json` |

A Reader MUST NOT select a schema solely from a `.json` extension, Web API URL, name containing "0.2", or a guessed version. `profileVersion` is not part of Distributed Profile 0.2 and is forbidden by its closed Snapshot/Event objects. Production 0.2 **requires** `profileVersion`. A writer that does not support the declared version must preserve the input without silently relabeling it, or decline a purported non-lossy save.

**Event replay and stale transitions** are different outcomes. Once the issuer is authenticated and the pinned Score/Session/Plan are verified, exact accepted same-ID/same-content replays are no-ops; modified same-ID content is an integrity conflict. A genuinely new state-changing Event at an old `baseStateRevision` MUST be rejected; it does **not** become an approved proposal. The original Score byte SHA-256 is a separate identity test and is not an event canonicalization or authentication mechanism. See `SESSION_STATE_MACHINE.md` and `SEMANTIC_RULES.md`.

**Conformance wording:** "record syntax recognized" does not mean "combined Score and both Profiles bound"; "data preserved" does not mean "plugs loaded", "event accepted" does not mean "sound produced", and none of these authorize a robot. Claim version and supported operation separately. The user's excluded runtime/third-party tests have not been performed or certified.

---

## Historical Draft 0.23 — versioned, bounded interoperability claims

**Draft only; no independent implementation certification.** A vendor's capability declaration SHOULD identify exactly which of these it supports: OSTF Core `4.3.0` parsing/writing; Distributed Profile `0.2` Snapshot/Event parsing/semantic handling; Production Profile `0.1` or `0.2` parsing/writing; preserving the actual separately supplied opaque Asset bytes; and optional rendering/network/physical execution. These are distinct, opt-in claims. Conformance to one Profile does not require, imply or grant support for the other, and a data-preserving reader is not a plug-in or robotic engine.

**Source authority:** JSON Schema is the structural authority for each **explicitly versioned document**; the relevant `SPECIFICATION.md`, `SESSION_STATE_MACHINE.md`, and `PRODUCTION_SESSION_PROFILE.md` are the respective *proposed* semantic authorities. The companion Profile schemas are not part of `.ostf` Core. The English 4.3 text is the most complete candidate reference; the Japanese texts are pending final parallel editorial review. An apparent contradiction MUST be documented and resolved by the maintainer before a final interchange claim, never silently arbitrated by file date, JSON array order, the development ZIP layout or a historical README heading. Examples illustrate data but do not override Schema or proposed normative semantics.

**No standard outer container:** There is no normative OSTF 4.3 full-studio archive format. The distribution ZIP is not a claim of studio-project preservation or interoperability. A full-supplied-data collection claim requires an explicit inventory of preserved Score, Profiles and Asset bytes; asset descriptors alone do not imply byte availability. See Production §28.

---

## Draft 0.23 — Current data claims and frozen-source navigation

A **single Core Score document** is not a complete production bundle by implication. To make any multi-document claim, separately identify (a) supplied Score bytes, (b) optionally supplied Production Profile, (c) optionally supplied Distributed Profile, and (d) opaque Asset **actual bytes**, not merely their descriptors. **Only the exact supplied Score bytes** permit a companion SHA-256 verification claim. Absent Score bytes, identical declared SHA-256 values permit only a weaker "declarations agree" report; an application MUST NOT claim validated Track/Plan binding. Distributed `phraseCommitted` modifies the Session ledger, not Core or Production files. New Score bytes require an explicit new revision, separate Production re-binding and, for remote performance, a new Session.

The three obsolete intra-package links in the **frozen verbatim 4.2 appendix** of `COMPLETE_MANUAL.md` are deliberately preserved for provenance. Their safe 4.3-package substitutes are listed **before that appendix** in the current manual. A static documentation link check MUST distinguish the frozen source from new 4.3 authored content. These notes do not grant publisher ratification, license rights, a new JSON field, canonicalized JSON, standardized studio archive, or runnable DAW/robot capability.

---

## Historical proposal definitions (unratified)

Conformance must be claimed by operation and feature; JSON parse success is **not** interoperability.

| Profile | Required ability | Not implied |
| --- | --- | --- |
| Core Reader | Parse full known 4.3 schema, resolve IDs and preserve unsupported optional Core | Realize open phrases |
| Core Writer | Emit valid 4.3 JSON without silent data loss | Understand every musical intent |
| Direction-aware | Interpret declared inherited and new Track Directions, respect scope/overlap/authority | A high-quality solo generator |
| Ensemble-aware | Resolve directed Track/Voice Interaction references | Synchronous remote jam |
| Plan-aware | Deterministically expand finite source-visit mappings and preserve inherited enabled/probability/velocity-deviation state; distinguish eligible Notes from certain-sounding Notes | Guaranteed identical rendered performances without explicit stochastic realization |
| Vocal-aware | Resolve lyric ownership/Voice/Alignment; handle `vocalFreedom` | Singing synthesis or independent export |
| Requirement-aware | Assess abstract track performance requirements | Robot safety certification |
| Session-profile-aware | Parse separate session snapshots/events and versioned state; enforce local authority checks | WAN latency guarantee, actuator execution |

**Normative conformance diagnostics** should distinguish structural schema errors; invalid references; ambiguity/conflicting directions; missing capabilities; non-materialized open content; unsupported scope/clock; lossy downgrade; external-format mapping approximations.

**Readiness note:** No conformance tests are claimed in this draft. Runtime validation is explicitly excluded from the user's release-readiness criterion, but editorial schema/spec/source consistency is not.

## Draft 0.3 boundary-reporting requirement

A Plan-aware exporter claiming fully deterministic expanded musical playback MUST (1) apply the specified source-start/half-open selection and note-gate clipping, (2) detect unresolved inherited 4.2 Note states (disabled state, `0 < probability < 1`, nonzero `velocityDeviation`, or absent `velocity` when concrete velocity is required) rather than claim that a `fixed` Part is guaranteed sound, (3) detect when a cut requires external MIDI/program/controller state not determined by the Plan, and (4) not assert that `open` or `unspecified` Parts were completely rendered without additional authored material. Fixed *event selection* is not a complete guaranteed playback outcome. A Profile 0.2-aware session consumer MUST enforce typed event payload meaning and reject stale/unauthorized revision transitions; this does not certify any WAN or robot performance.

## Draft 0.5 semantic clarification for implementers

- Ensemble-aware readers MUST accept a same-Track Interaction when two different `lyrics.voices` IDs on that Track are explicit. They MUST reject same-Track relationships lacking them and self-Voice relationships. This is a cross-reference semantic rule, not a JSON Schema field-type change.
- Plan-aware readers MUST distinguish source Note IDs from generated Visit occurrences. Plan expansion cannot duplicate the Core Note namespace without a separate explicit materialization action and a new revision.
- Distributed Session Profile 0.2 Snapshot-aware readers MUST read the required `sessionStatus`; `playing` requires `position`. Event idempotency compares parsed JSON content, not whitespace-dependent bytes. A Profile 0.2 reader written for previous Draft 0.3 is not automatically Draft 0.5-conformant.
- None of these declarations implies DAW, robot, independent parser or real-time network testing. They are candidate normative obligations for feature-aware software only.

## Draft 0.5 additional Session Profile claim

A Profile 0.2 Reader that recognizes `sessionStarted` must validate the required Position and the base/next-revision relationship before it claims state-transition awareness. A Snapshot Reader must not infer complete future committed Session phrases from `committedPhrases` unless an explicit, truthful `commitmentWindow` covers the target interval. An implementation that cannot establish that completeness against authoritative logs must avoid a late-join-complete claim. None of these statements certifies real network, audio, robotic or safety execution.

## Draft 0.7 — Companion profile semantic claims

A Session Profile 0.2-aware consumer claiming acceptance semantics MUST distinguish: replay of an already accepted identical Event (no-op), a new Event with a stale `baseStateRevision` (rejected), a conflict when an `eventId` matches but content differs (rejected), and actual rendering/actuation (not attested by Session state). A Session adapter claiming Plan-aware collaboration MUST keep its OSTF Score/Revision/Plan pin fixed throughout the Session, refuse backwards `visitChanged`, and avoid treating skipped or post-stop accepted phrases as if they had sounded. An `assignmentChanged` does not change accepted phrase identities or grant execution rights. These are *candidate* feature-conformance obligations; this package provides no independent conformance certification.

## Draft 0.8 — Companion Profile authoring obligations (not third-party certification)

A future Profile 0.2 writer must not emit `position` in an `assignmentChanged` payload. Readers must validate every retained Session Phrase's Note containment independently of any `commitmentWindow`. A host must authenticate and validate pinned Session/Score identity before acknowledging duplicate Event IDs; no incoming JSON is robot actuation permission. Historical accepted phrases do not certify current performer assignment or physically sounded notes. This describes proposed minimum meaning, not a claim of tested interoperability.

## Draft 0.9 Session Profile awareness (editorial candidate)

A consumer claiming **separate Profile 0.2 Draft 0.9** support MUST parse root `performancePlanId`/`scoreSha256` on every Snapshot and Event (including unpositioned `prepared`), resolve the named finite Plan, require nested Position Plan equality, and compare the declared SHA-256 with the actual original source bytes when the score is available. Reading an arbitrary documentId/revisionId with a different original-byte digest is a source conflict, not successful interoperability. SHA-256 is not authentication or robot permission. This is a proposed conformance definition, not an assertion that an independent implementation has passed it.

## Draft 0.10 — Remote Visit anchor data obligations

A Profile 0.2-aware writer/reader claiming support for this Draft MUST require a `position` on both `sessionStarted` and `visitChanged` state-change Events and ensure `visitChanged` Position is anchored to the target Visit start in the pinned OSTF Plan. These are proposed *data semantics*, not evidence of synchronized WAN or physical-AI operation. Core 4.3 remains at 127 schema definitions; Profile 0.2 remains at 16.

## Draft 0.11 candidate Session conformance clarifications

A Profile 0.2 Session-aware consumer that claims cross-record state interpretation MUST reject a change of `clockDomainId` after an authoritative `sessionStarted` without creating a new Session. With a pinned OSTF score, any present `position.tempoBpm` MUST agree with the effective source tempo at `position.sourceTick`; a missing source tempo cannot be inferred from the Session. Treat `sessionStopped.effectivePerformanceTick` as audit context rather than as a delayed stop. These are editorial semantics, not an independent network/robot/DAW conformance result.

## Draft 0.12 — Clock-anchor source completeness (proposal)

A Profile 0.2-aware consumer claiming timed `playing` Snapshots or start/Visit-change positions MUST find an effective positive source BPM at the mapped source Tick from the byte-pinned OSTF score, even if the optional `tempoBpm` field is absent. It MUST reject unresolved anchors with `E-SESSION-TEMPO-UNRESOLVED`, and preserve piecewise step-Tempo/source-cut semantics for ideal musical scheduling. A structurally conforming Snapshot has at least one declared participant; authority identity still requires semantic resolution. These claims do not certify WAN wall-clock alignment, sound, servo behavior or robot safety.

## Draft 0.13 — Independent third-party studio Profile conformance

A separate Profile 0.1 Reader MAY claim structural and selected semantic support without being a plug-in host. A Profile Writer MUST serialize stable Channel/Device/Asset identities and known standard mix fields without silently dropping unknown opaque state/assets in a non-lossy mode. A plugin-state-host Adapter can claim separate restoration support **only with appropriate external evidence**; Profile parsing by itself does not establish VST3/CLAP/AU/AAX execution, license, sound fidelity or DAWproject compatibility. The stateful remote Distributed Session Profile 0.2 is a different format with unrelated participants and clock semantics. See `PRODUCTION_SESSION_PROFILE.md` and `PRODUCTION_COMPATIBILITY.md`.

## Draft 0.14 — Production Profile 0.2 conformance labels (proposal)

`Production Profile 0.1 Reader/Writer` and `Production Profile 0.2 Reader/Writer` are **different claims**. 0.2 adds a mono/stereo audio source/region model and sidechain detector routing; readers can declare `Audio-Region-Preserving` or `Sidechain-Reference-Preserving` without claiming playback. A standalone third-party host can implement Core Score decoding, 0.2 data reading and vendor-plugin hosting independently. A successful static Schema/semantic reference check only certifies the specific evaluated fields; it does not prove waveform parity, decoder support, DAWproject conversion or VST/CLAP state round-trip.


## Draft 0.16 — optional portable Production Profile audition claim

A `Production Profile 0.2 Data Reader/Writer` preserves authored channel flags, enabled Sends, Audio Regions and Sidechains; this role does **not** assert acoustic audition equivalence. An implementation that additionally claims `Production Profile 0.2 Portable Audition Selection` MUST follow §22 source-selection rules for current source Tick, including the reachability of Solo buses, source-vs-bus SoloSafe distinction and source-state separation; deviations due to a native DAW mixer MUST be disclosed. This claim does not imply plug-in loading, host DSP tests, sample-identical rendering or security certification. These are **draft candidate** conformance labels, not ratified statuses.

## Draft 0.19 — Cross-Profile Binding Reader (optional and additive)

An implementation may separately claim `OSTF 4.3 Cross-Profile Binding Reader` if it (a) already supports relevant versions of the production, remote and Core data documents; (b) requires the exact pinned Score to establish original-byte equality with both profile hashes; (c) resolves explicit document/revision IDs, source Track IDs and the selected finite Plan; (d) rejects inconsistent association without silently modifying any original JSON. This is **not** an additional requirement on applications supporting only one Profile. Claiming association without the pinned score must be labeled *unverified*, even if declared hashes match. Production channel routing and remote physical actuation are outside this conformance label. The bundled local optional `--distributed --score` authoring check is not an independent conformance certification.

## Draft 0.20 — Revision-Rebinding Preview versus authored conversion

An optional `OSTF 4.3 Score-Rebinding Preview` claim is limited to reading original/new Score files, comparing byte hashes and explicit revision lineage, and flagging missing Core Track references plus relevant changes to PPQ, Sections, Tempo/Meter and finite Performance Plans. Such a preview MUST NOT claim that the Production Profile was migrated, that MIDI/Region/Automation was re-timed, or that a new Distributed Session was started. A `Production Profile Rebinding Writer` is a **separate** and stronger claim requiring a newly authored Profile copy, correct new Score pin, valid references, explicit musician/author source-time reconciliation and reporting of any features lost. Neither role implies DSP fidelity or DAW/plugin/WAN/robot testing. The bundled `--rebind-target` action is read-only static authoring assistance and never an independent conformance certificate. See `PRODUCTION_SESSION_PROFILE.md` §26.

## Draft 0.21 — Release-quality feature and preservation claims (editorial candidate)

A software vendor SHOULD publish a **version-scoped operation matrix**, separately indicating whether it can (1) parse/validate a supplied Core/Profile record, (2) preserve that record and any referenced exact bytes without loss, (3) interpret the specified musical/production/session meanings, and (4) render audio, exchange network state, or actuate physical performers. These are distinct claims; none follows automatically from another.

| Interchange situation | Claim available after data-only conformance | Claim NOT established |
| --- | --- | --- |
| OSTF Score 4.3 reader preserves unsupported optional semantic fields | Non-destructive Score preservation | Correct improvisation generation |
| Production 0.2 reader retains plug-in descriptors + actual opaque state Asset bytes | Data/asset-preserving import | Plug-in instantiation, sound fidelity, license validity |
| Production 0.2 reader retains descriptors but lacks the referenced asset bytes | Metadata/descriptor preservation only | Complete source bundle round-trip |
| OSTF 4.3 Score-only writer exports from a combined bundle | Partial export with explicit loss disclosure | Non-lossy full project exchange |
| Production rebind helper compares original/new Score revisions | Authoring preview/report | Rebinding completed, automatic audio re-timing |
| Distributed 0.2 reader stores Session Events | Event-data preservation | Clock synchronization, event acceptance by authority, physical actuation |

An explicit **loss disclosure** SHOULD cite affected stable source IDs and say whether material was omitted, approximated, unavailable, bypassed or left uninterpreted. Such report labels are not Core/Profile Schema fields. Unknown optional data MUST be retained in a non-lossy Writer or the Writer must refuse and offer a clearly lossy copy. A new Score byte digest requires explicitly updated dependent Profile pins; a new Score revision cannot silently reuse a live Distributed Session. Details: `PRODUCTION_SESSION_PROFILE.md` §27 and `PRODUCTION_COMPATIBILITY.md`.

**Status: unratified Draft 0.21 editorial candidate.** This matrix is for honest third-party feature claims, not runtime/DAW/WAN/robot test certification. The user's release gate excludes those tests; licensing and publisher adoption remain open.


## Draft 0.35 — Version-specific sample routing and support claims (editorial proposal)

This is an **evidence index for the included fixture files**, not an assertion that a third-party implementation passes interoperability or runtime tests. Route a document by its declared family and exact version **before** interpreting musical content, session authority, or production parameters. The model must not treat unknown versions as synonyms for a supported version.

| Family and exact discriminator | Included schema | Fixture inventory |
| --- | --- | --- |
| `format: OSTF`, `version: 4.3.0` | `schema/ostf-4.3.0.schema.json` | `examples/*.ostf` |
| `format: OSTF`, `version: 4.2.0` | `schema/ostf-4.2.0.schema.json` | Baseline schema retained; these 4.3 example files must **not** be relabelled 4.2 |
| `profile: OSTF-Distributed-Session-0.1` plus `recordType` | `schema/ostf-distributed-session-0.1.schema.json` | `examples/session/01-snapshot.json`, `02-event.json` |
| `profile: OSTF-Distributed-Session-0.2` plus `recordType` | `schema/ostf-distributed-session-0.2.schema.json` | `examples/session/*-02.json` |
| `profile: OSTF-Production-Session`, `profileVersion: 0.1.0` | `schema/ostf-production-session-0.1.schema.json` | `examples/production/01-...json`, `02-...json` |
| `profile: OSTF-Production-Session`, `profileVersion: 0.2.0` | `schema/ostf-production-session-0.2.schema.json` | `examples/production/03-...json` |

**Operation-scoped evidence:** a successful JSON parse does not prove semantic conformance; an application that preserves unknown bytes is not thereby able to interpret Session events or render a plug-in chain. For each version/family, an implementation should report separately whether it can (1) parse structurally, (2) resolve Score/Profile references, (3) preserve *actually supplied* data losslessly, (4) interpret music/session/production semantics, and (5) execute audio or physical actions. No execution capability follows merely from a valid JSON file. The bundled local checkers are authoring aids and are **not** independent interoperability proof.

The inventory was derived directly from the included `examples/` files for this draft; it is not an exhaustive matrix of every permitted object or optional feature. A missing example is **not** a ban on a valid schema-defined feature. Existing 4.2 source semantics are inherited and remain authoritative where not explicitly extended. This is a proposed D01–D04 documentation clarification, not a new serialized field or a newly adopted standard.

### Exact included JSON fixture inventory

| Example | Family | Selector |
| --- | --- | --- |
| `examples/01-minimal.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/02-guitar-solo.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/03-jazz-comping.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/04-aaba-performance-plan.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/05-rnb-vocal-open.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/06-scat.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/07-vocal-alternatives.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/08-gospel-response.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/09-techno-variation.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/10-physical-robot-requirements.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/11-harmony-plus-phrasing.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/12-visit-scoped-response.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/13-fixed-notes-and-directions.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/14-tempo-map-reentry.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/15-vocal-response-phrasing.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/16-inherited-comprehensive-core.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/17-fixed-note-source-cut.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/18-visit-role-override.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/19-concurrent-voice-directions.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/20-phrasing-with-motif-reference.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/21-visit-and-range-intersection.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/22-pinned-session-aaba.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/23-range-visit-and-label.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/24-intra-track-voices-response.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/25-source-note-repeated-visits.ostf` | Score Core | `OSTF` / `4.3.0` |
| `examples/session/01-snapshot.json` | Distributed Session | `OSTF-Distributed-Session-0.1` / `snapshot` |
| `examples/session/02-event.json` | Distributed Session | `OSTF-Distributed-Session-0.1` / `event` |
| `examples/session/03-snapshot-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/session/04-phrase-proposed-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/05-phrase-committed-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/06-snapshot-after-commit-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/session/07-session-state-change-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/08-turn-request-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/09-cue-issued-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/10-performance-observed-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/11-participant-status-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/12-snapshot-prepared-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/session/13-snapshot-stopped-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/session/14-session-stopped-event-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/15-prepared-to-playing-event-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `event` |
| `examples/session/16-playing-after-start-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/session/17-late-join-complete-window-02.json` | Distributed Session | `OSTF-Distributed-Session-0.2` / `snapshot` |
| `examples/production/01-track-mixer-plugin-chain.json` | Production Session | `OSTF-Production-Session` / `0.1.0` |
| `examples/production/02-unavailable-plugin.json` | Production Session | `OSTF-Production-Session` / `0.1.0` |
| `examples/production/03-audio-regions-sidechain-02.json` | Production Session | `OSTF-Production-Session` / `0.2.0` |

## Draft 0.41 — Continuous-join interpretation claim (D01/D04 pending)

A consumer claiming **fixed finite-Plan source-note interpretation** should distinguish (a) source-discontinuous cuts, (b) source-contiguous Section joins inside one fixed Visit, and (c) hard cut at Visit boundaries. The latter is a deliberate editorial conservatism, not a statement about whether a specific DAW can legato across a programmed section. It should preserve the selected gate across (b) without a duplicate attack or release; it must release at (a) and (c) and must not invent controller snapshots. The candidate note-state stochastic rules from Draft 0.40 remain separate. A `Plan-aware` conformance claim is about **interpreting authored source selections and their boundaries**, not about actual synth tails, audio-DSP fidelity, WAN synchronization, deterministic PRNG decisions, or robotics. `tools/validate.py --explain-plan-joins` is an optional local explanatory aid, not a mandatory Report Schema, independent validator, or runtime evidence.


## Draft 0.42 — Note-targeted MIDI selection capability boundary (D01/D04 pending)

A Plan-aware application should distinguish **(i)** source-interval event selection, **(ii)** selected Note occurrence and gate continuity, **(iii)** target association resolution, **(iv)** concrete MIDI state/Note-On realization, and **(v)** external synth/MPE playback. These are not interchangeable conformance claims. A selected `targetNoteId` event whose Note attacked in an omitted interval must be reported as an unresolved export policy, not silently treated as an untargeted channel event. The static example 17 pairs an unresolved target at source Tick7800 with a resolvable cross-join target at source Tick11760. A fully determined MIDI claim still needs concrete velocity/probability decisions and any necessary prior controller state. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` for detailed proposed rules.

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


## Draft 0.70 — Candidate-set completeness editorial decision table (not test results)

| Observed authorized candidate evidence | Allowed diagnostic (only within described scope) |
| --- | --- |
| Search/retrieval incomplete, no bytes inspected | NOT_EVALUATED (external status) |
| Complete search/retrieval, zero Score candidates | MISSING |
| Complete search/retrieval, candidate bytes present, no hash matches | MISMATCH |
| Verified Score hash, required Track absent | AMBIGUOUS + missing_referent |
| Verified Score hash, required referent nonunique | AMBIGUOUS + nonunique_referent |
| Verified Score hash, all required referents uniquely resolved | RESOLVED |
| Incomplete search, one match but uncertain uniqueness of referent | NOT_EVALUATED with partial evidence; do not guess |
| Invalid version/profile discriminator | INVALID or UNSUPPORTED before binding |

NOT_EVALUATED and diagnostic suffixes are *reporting terminology* only, not serialized fields or new Schema enum values. This table is a proposed documentary interpretation, not execution/interop test evidence.


## Draft 0.76 — superseded incomplete-scope exception (editorial case, not a test result)

A reader has an authorized candidate directory containing two Score file references. It retrieves one matching Score and hashes its raw bytes. The other authorized candidate fails to download. **Result: `NOT_EVALUATED`**, not `RESOLVED`, even if the first Score's Track/Plan references can be resolved. After authorized scope enumeration **and all candidate byte retrieval** finish, re-evaluate against the full set to determine MISSING/MISMATCH/AMBIGUOUS/RESOLVED. This rule supersedes the historical Draft 0.70 conditional RESOLVED sentence and is consistent with Draft 0.71/0.73. This is an editorial hypothetical, not a successfully executed test.
