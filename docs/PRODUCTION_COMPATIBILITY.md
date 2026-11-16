> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF 4.3 / Production Session Profiles 0.1 and 0.2 — Compatibility and migration

**Candidate editorial guidance. Not a ratified or independently tested interchange standard.**

## A. Three independent versioned documents

1. OSTF Score Core `format:"OSTF"; version:"4.3.0"` is authoritative for source Timeline, Harmony, Track/Clip/Note, Lyrics, MIDI and musical Directions/Plans.
2. The companion *Production Session Profile* `profile:"OSTF-Production-Session"; profileVersion:"0.1.0"` optionally records audio mixer settings, devices, resources and host automation; it is not in the Core `extensions` field.
3. The companion *Distributed Session Profile 0.2* is selected by `profile:"OSTF-Distributed-Session-0.2"` (with `recordType:"snapshot"` or `"event"`); it has **no** `profileVersion` property. It separately describes remote participants, live session state and performance proposals. Production Profile 0.1.0/0.2.0 is instead selected by `profile:"OSTF-Production-Session"` **plus** the required `profileVersion`. Joint binding to the same Score is opt-in, byte-pinned and read-only, not implied by either profile alone (Production §25).

A 4.3 score without a Production Profile remains fully valid. A Production Profile may be preserved without being renderable. Each Profile references the pinned Score; Score does not link back to a particular Profile.

## B. Supported lossless editorial operations

- Existing Core 4.2 score to Core 4.3: according to inherited compatibility rules, do not infer mixer, plug-in or solo/mute settings.
- Import to a standalone host: retain all profile channel/Device IDs, state asset bytes and unknown `hostExtensions` even if the host cannot instantiate effects or audio buses.
- Copy/edit a Production Profile only: the score hash stays unchanged; changes to a score must be treated as a **new pinned score** and reconciled explicitly.
- Export to OSTF score only: all `channels`, `devices`, `assets`, `automation` and `hostExtensions` will be **lost**, so a writer claiming no loss MUST preserve the separate Profile or report the loss.

## C. When full production equivalence is impossible

The Profile is NOT a full DAW project format. Version 0.1 intentionally omits full audio regions, waveforms, clip fades/warping, exact signal graph including sidechains, virtual device GUIs, platform-specific plug-in binary processing and implicit installation. An exporter to DAWproject can be useful for richer DAW project data but must report unmapped fields, resources and permission constraints. An OSTF plus a DAWproject resource can coexist but must not silently become one authoritative format.

## D. Missing plug-ins and portability

A third-party reader without a plug-in host should preserve state **without attempting to load**. If `onUnavailable` is `preserveAndBypass` or `preserveAndSilence`, that indicates a degraded representation, not musical or timbral equivalence. Returning to a capable host may restore vendor state if the plug-in is present and compatible; state restoration is never guaranteed by Profile format conformance. Allowed relative Asset URIs must resolve beneath the directory containing the Production Profile JSON after the strict single-pass URI path checks and symlink resolution of Production §23. No standardized OSTF production project ZIP or archive root is defined (§28). Retain/check original-byte SHA-256 when the referenced Asset is actually supplied. External HTTPS resources must not be fetched just by parsing JSON.

## E. Solo/Mute precedence

- Core `enabled` determines whether authored score material participates at all.
- Production `mute` applies only at the audio channel; `solo` and `soloSafe` are mixer audition flags.
- A `mute` automation lane can change the authored audio channel mute state at source Tick. It does not rewrite Core note states, nor MIDI CC7/10/11/91/93 events.
- Host-specific Solo semantics, pre-fader sends and sidechains may be irreproducible; warn and preserve rather than silently flattening.

## F. Conformance statements

Label claims precisely: `Core 4.3 Reader`, `Production Profile 0.1 Reader`, `Production Profile 0.1 Writer`, `Device-State-Preserving Reader`, `Production Plug-in Host Adapter`. No claimed role implies a third-party VST3/CLAP/DAW/robot runtime test. All new Profile semantics and ownership/licensing require explicit publisher ratification before public release.

## Draft 0.14 — Production Session Profile 0.2 compatibility and loss (candidate)

The 0.1 and 0.2 Schemas coexist and are selected by exact `profileVersion`; they are not aliases. The musical Score 4.3 is untouched by either profile and carries only music-level authority. Inherited 0.1 Channel/Device/Send/Automation semantics are unchanged; 0.2 adds optional audio-only Channels, audio Regions and sidechain metadata.

A 0.1 → 0.2 upgrade can be a version-token edit after explicit validation; it MUST NOT fabricate `audioTrack`, `audioRegions`, `sidechainConnections` or audioSource assets. A 0.2 → 0.1 downgrade is lossless **only** if no 0.2-exclusive fields or values are present. Otherwise a non-lossy exporter must preserve the original 0.2 file and its assets or stop; a lossy downgrade MUST name the discarded Channel IDs, audio Region IDs, assets, and sidechain IDs in a report. Audio in the Production Profile is not converted to Score Notes, Core Clips, or VST presets merely by relabelling `profileVersion`.

Before translating to a DAW or DAWproject, report unsupported frame-range editing, native/fit mapping, missing media decoders, sample-rate assumptions, Region Gain/Fade differences, sidechain port mapping and feedback graph restrictions. No portable bit-for-bit audio reproduction is guaranteed, even if the Score and all media hashes match. If production audio and MIDI share a Channel, hosts must disclose any difference in signal summing relative to the declared serial-effects flow. Remote `OSTF-Distributed-Session` snapshots/events never silently rewrite Production Regions or instantiate plug-ins.

Portability classification: `Studio Profile 0.1 Reader/Writer`, `Studio Profile 0.2 Reader/Writer`, `Media-Preserving Importer`, `Sidechain-Reference-Preserving Importer`, `Production Plug-in Host Adapter`. These describe independent capabilities and must not be conflated. A JSON validator is not a DAW, audio DSP renderer or robot controller.


## Draft 0.15 — Profile 0.2 Automation target migration (proposed)

The 0.2 candidate now has three additional typed target branches: `send`, `audioRegion`, `deviceControl`. Its previous `channel` and plug-in numeric `device` target branches are unchanged. The 0.1 Schema is fixed and retains only its original two branches.

When exporting 0.2 to 0.1, **each** new-target automation lane MUST be listed by Automation ID and typed target in the loss report, independent of whether an audio Region or audioSource asset exists; no 0.1 author may silently serialize these as opaque old device parameter IDs. A non-lossy writer preserves the complete original 0.2 file or refuses the write. In contrast, 0.1 to 0.2 can retain the old automation without generating any new lanes. Automation relative to source Tick repeats under finite Plan visits; visit-local mixer/plug-in automation overrides remain outside 0.2.


## Draft 0.16 — Audition selection portability, asset boundary (candidate)

Profile 0.2 adds no new JSON field; it specifies an explicit audition-source eligibility baseline while leaving Profile 0.1 historically unspecified on bus Solo. An upgrade 0.1→0.2 now also requires acknowledging the 0.2 portable Solo/bus selection semantics; a version-token-only upgrade does not guarantee identical native-host audible output. For a host using wet-only Bus Solo or different solo-safe returns, report the difference and preserve all input flags. Track/Clip.enabled only gates Score-derived material, not an independently authored Production audio Region on the same Channel. Channel Mute gates audible post/pre Sends; sidechain followMute is separate and never grants source activation. Symlink escapes from the Production asset directory must be rejected.

## Draft 0.17 — Asset URI portability and Core Plan `silent` scope (candidate)

- Retain exact serialized `assets[].uri` string. A consumer that resolves local asset URI paths MUST perform strict UTF-8 **single-pass per-component percent decoding**, reject encoded parent/directory separators, ambiguous nested escapes, nonportable Windows filename spellings, and symlink escapes. For `%20` filenames, decoded path resolution is permitted but never automatic file access. Unavailable/nonportable names become preservation-and-warning, not arbitrary fallback paths.
- No JSON Schema field is added, and the six existing Schema versions remain pinned. Existing 0.1 files are not silently relabelled as 0.2; the URI guard protects the already stated relative-path confinement rule.
- A Score Plan Part's `realization:"silent"` suppresses Score-derived performance, not an independent Production `audioRegion` on the same bound Studio Channel. Full audible silence requires explicit Production Mute, and hosts unable to represent this distinction MUST disclose it. Production-only `audioTrack` has no Core Plan Part.
- Mixed-content web/DAW exports MUST report failure to resolve an allowed URI path or to preserve the independent Score-vs-Production source distinction. Neither rule is a promise of sound identity or host execution.

## Draft 0.18 — Production Region/Automation source projection and downgrade disclosures (candidate)

Production Profile 0.2 automation applies as a source-Score-Tick **value function** in each finite Performance Plan Visit, not as one evolving latch across concatenated Visits. A 0.2 Writer/exporter MUST preserve authored points from skipped source ranges, because they may determine the value when a Visit later enters a different source interval. The first point of an opaque numeric Device-parameter lane has no portable typed static baseline before it: if vendor state is unavailable, report an unresolved interval rather than fabricate 0/0.5 or using the last value of another Visit.

For native Audio Regions, sample-frame entry offsets depend on the effective **original source** Tempo from the Region start (including omitted source intervals), while the expanded performance clock excludes omitted regions. For fit Audio Regions, original Region-relative Tick determines frame position. A conversion that resets Region playback/fades on every selected source cut, adds an automatic crossfade, or maps source-Tick Automation into an uninterrupted expanded-Playthrough ramp MUST disclose an approximation/loss; it may not label its output lossless. This is a portable authoring/interpretation subset, not a guarantee of a matching DSP sound. No Schema field or version token changed in Draft 0.18; author ratification remains outstanding.

## Draft 0.19 — Optional cross-profile binding with a remote Session

A Production Profile 0.1/0.2 and a Distributed Session Profile 0.2 can refer to one OSTF 4.3 Score without being the same Profile or authorizing shared host state. Compare Production `score.sha256` with Distributed `scoreSha256` and the original `.ostf` byte digest; optional Production document/revision IDs, when present, must match the Distributed required IDs and actual Score; the Distributed `performancePlanId` must resolve in that Score. Production has **no** root `performancePlanId`: do not silently add one or require it. Neither matching Track IDs nor a Participant's remote assignment imply mixer routing, plugin activation, sample playback or a robot actuation grant. Inaccessible Score means identity/Plan claims are not fully verified. See Production Profile §25 and `docs/WEB_INTERCHANGE_PROFILE.md`.

Draft 0.19 adds a data-only optional audit mode to `tools/validate_production_profile.py --distributed ... --score ...`, which checks association claims without changing JSON, downloading content or running a DAW/robot. It is not an independent-interoperability or runtime certificate.

## Draft 0.20 — Explicit score-revision re-binding; old pinned remote Sessions stay immutable

The authoring identity of a Production Profile is its existing Score reference and original-byte `sha256`; changing that digest without reconciling source Tracks and source-Tick media/automation is **not** a lossless upgrade. A score-only authoring edit may preserve the same `document.id` with a *new* `document.revisionId`, but a different `document.id` is a new song association, and same ID/revision with different score bytes is an integrity conflict. The old Production JSON remains pinned to the old score until the author explicitly accepts a separately authored new Production copy. Missing/renamed Track IDs require explicit authored re-map; section/tempo/meter/PPQ edits and Plan changes require manual review of Regions, native audio offsets, Automation and Visit projection. A structurally valid new Production file cannot on its own prove semantic/sonic equivalence; retain original data or disclose named lost objects.

The separate Distributed Session Profile 0.2 cannot be rebound in place. A new Score revision requires a **new sessionId** and new clock/event/Visit/commitment context; old accepted events remain historical records bound to the old score. The optional local `--rebind-target` helper only previews Score identity and source-timing drift, never edits profiles, authorizes host/plugin/robot execution or proves interchange. See Production §26. No new Schema or JSON example fields are introduced, and any claim of a safe production rebind requires explicit author approval of the mapping.

## Draft 0.21 — Full-bundle data preservation versus audio equivalence

The ability to read one OSTF 4.3 Score does **not** mean a third-party host has imported its Production or Distributed Profile. Likewise, preserving a plug-in's identity and state-Asset descriptor does not mean that the state **bytes** arrived, nor that the plug-in can be instantiated. A complete-data round-trip claim requires preserving accessible companion JSON plus all available opaque source Asset bytes or explicitly declaring material unavailable. A Score-only export must identify omitted Studio metadata (channels, plug-in state, audio Regions, Sidechains, Automation, assets) and all remote Session fields not separately preserved. Unknown production metadata must never be silently recast as a MIDI control or Core event.

On an explicit Score Revision rebind, reconcile all present `score` identity fields and exact-byte hash in a **new Profile copy**, and report any source-Tick meaning or Asset mismatch. An old `score.sourceUri` is advisory, not identity or fetch permission. The companion Distributed Session requires a new Session ID, not just a new pinned hash. This is non-runtime editorial guidance; see Production §27 for its proposed normative contract.

## Draft 0.22 — What is (and is not) an OSTF Production 'bundle'

The developer release ZIP with its `PACKAGE_MANIFEST.json` is **not** a standardized user-project interchange container. Production Profile 0.2 defines separate JSON and Asset references, not a standard archive layout or universally round-trippable host-project format. Any claims of lossless 'whole-project' exchange MUST identify the concrete supplied Score, versioned Profiles and actual Asset byte streams preserved; an absent, never-supplied companion is not evidence of deletion, and a retained descriptor is not evidence that its bytes were present. Score and Asset integrity hashes cover their defined original bytes, never outer ZIP or web-response metadata. See `PRODUCTION_SESSION_PROFILE.md` §28. This is an unratified editorial clarification and changes no Schema.
