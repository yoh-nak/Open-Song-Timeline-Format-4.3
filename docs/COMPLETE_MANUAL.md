# OSTF 4.3.0 — Complete Implementation Manual

**Formal release edition · 2026-11-16** · [日本語](COMPLETE_MANUAL.ja.md) · [Core reference](PARAMETER_REFERENCE.md) · [All examples](EXAMPLES_GUIDE.md)

This manual covers the full inherited Core, all 4.3 additions and both current companion profiles. The schema-derived references enumerate every field, constraint and alternative. The adopted normative sources govern cross-object meaning; this manual does not invent fields or certify an application. [Edition guide](RELEASE_READINESS.md) explains historical labels in the frozen adopted sources.

## Navigation

- [Release model and quick start](#release-model-and-quick-start)
- [Full inherited musical model](#full-inherited-musical-model)
- [OSTF 4.3 musical-intent authoring](#ostf-43-musical-intent-authoring)
- [Finite performance plans and boundaries](#finite-performance-plans-and-boundaries)
- [Distributed Session 0.2](#distributed-session-02)
- [Production Session 0.2.0](#production-session-020)
- [Editing, interchange and implementation workflow](#editing-interchange-and-implementation-workflow)
- [Publication, coverage and local tools](#publication-coverage-and-local-tools)

## Release model and quick start

There are three independent artifacts. A **Core Score** is a `.ostf` file with `format="OSTF"` and `version="4.3.0"`. A **Distributed Session** record is JSON with `profile="OSTF-Distributed-Session-0.2"`. A **Production Session** is JSON with `profile="OSTF-Production-Session"`, `profileVersion="0.2.0"`. A file extension or name never substitutes for these discriminators. A companion cannot be merged into the Core root as extra fields.

Use [01-minimal.ostf](../examples/01-minimal.ostf) as a starting document. Required roots are `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, and `resources`. Empty valid collections are permitted; absence of advanced data is not an instruction to generate it. A valid 4.2 Score can be promoted using the 4.3 version when its unchanged fields remain valid; no new 4.3 structures need to be fabricated.

### Root-object map

| Object | Responsibility |
|---|---|
| `song` | Titles, genres/moods/languages, key/scale, credits, rights, melody/lyric selections |
| `timeline` | Global duration, Sections, tempo, meter, key changes, bar origin |
| `harmony` | Chord contexts, optional voicings, timed scale contexts and typed targets |
| `tracks` | Instruments, Clips, Notes, MIDI, vocal performance and Track Directions |
| `soundSlots`, `drumKits` | Document-local percussion/event identities and optional MIDI maps |
| `lyrics` | Documents, Phrases, Units, Alignments and explicitly assigned Voices |
| `resources`, `contributors` | External descriptors and credit identities, not retrieval permission |
| `document`, `provenance` | Revision identity, parent/source records and declared edit history |
| `relativePhrases`, `generation` | Derived relationships and explicit generation intent |
| `presentation`, `localization` | Non-musical presentation metadata and stable-ID translations |
| `phraseLibrary`, `clipChoices` | Phrase templates/instances and explicit take choices |
| `midi` | Logical buses; never physical devices or ports |
| `extensions` | Verbatim retained legacy/third-party envelopes; Core remains authoritative |
| `ensembleInteractions`, `performancePlans` | Optional ensemble intent and finite source playthroughs |

Read known fields without deleting unsupported material. Build typed indexes rather than indexing every `id` string as a new object: `harmony.scales[].targets[].id`, generic `ref.id` and localization targets are references. Scope rules distinguish Core IDs, document/revision identities and companion IDs. Display names are not lookup keys.

### Time and units

`ppq` is ticks per quarter note; it is an integer in 1–960000. Global contexts use the source song timeline. Clip positions are global; Note/MIDI/vocal event positions are Clip-local where specified. A negative local onset can be valid when its absolute song time remains nonnegative. Ranges are half-open: `[start, start+duration)`. Do not confuse MIDI pitch (0–127), relative vocal cents, MIDI bend words (0–16383), normalized expression (0–1), audio frames, milliseconds or performance ticks.

For PPQ=960, a quarter note is 960 ticks. Source tempo maps determine elapsed time piecewise; a performance-plan repetition does not change the source tempo map. Labels, bars, seconds and filenames do not redefine the tick coordinate system.

## Full inherited musical model

The following material integrates the complete inherited Core implementation guidance, including ordinary notes/MIDI, metadata, derived information, lyrics and 4.2 singing representation. The historical version numbers in this section explain inheritance; all examples in this release use Core 4.3.0. Distribution-specific links and audit commands have been updated for the current package. These chapters are followed by the 4.3-specific and companion implementation instructions.

# Inherited Core implementation chapters (4.2 baseline)

Open Song Timeline Format (OSTF) 4.2.0 is an open, DAW-independent JSON interchange format for structured songs, harmony, arrangement, lyrics, MIDI-ready performance data, and track-level semantic performance directions.

This manual is the implementation-oriented guide for reading, writing, validating, preserving, editing, merging, migrating, playing, and generating with OSTF 4.2.0. For exact field names, requiredness, numeric bounds, enums, and object shapes, use [`PARAMETER_REFERENCE.md`](PARAMETER_REFERENCE.md). For normative Track Direction semantics and version rules, use [`SPECIFICATION.md`](SPECIFICATION.md). The structural authority is [`../schema/ostf-4.2.0.schema.json`](../schema/ostf-4.2.0.schema.json).

## Part I — Foundation

## 1. What OSTF 4.2 is

OSTF is a structured-song interchange format. It preserves song metadata, harmony, arrangement, lyrics, MIDI-ready performance and semantic Track Directions without becoming a DAW project. Version 4.2 preserves all 4.1 Core fields and adds optional phonetics, voice profiles and per-clip vocal performance metadata. None of those additions is mandatory for instrumental music. AI or humans can author the format directly; no dedicated Max for Live device is required.

## 2. What OSTF 4.1 is not

OSTF is not a plug-in preset format, audio-session archive, device-state container, operating-system MIDI-port map, or replacement for a DAW project. Physical ports, USB device names, DAW routing graphs, plug-in binary state, audio routing, SysEx, MIDI clock/MTC/MMC, and MIDI 2.0 UMP are outside Core 4.1.

Applications may keep those details in host-local state. They should not invent portable Core fields for host-only information.

## 3. File format and extension

OSTF 4.2 files are UTF-8 JSON documents with the `.ostf` extension. The root declares `format: "OSTF"` and `version: "4.2.0"`. Do not emit comments, trailing commas, duplicate properties, non-finite numbers or unpaired Unicode surrogates. Unicode display text is preserved. A reader may accept a UTF-8 BOM, but writers should emit plain UTF-8.

## 4. Required root objects

Every 4.1 document contains ten required root fields: `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, and `resources`.

Other Core objects such as `contributors`, `drumKits`, `document`, `relativePhrases`, `generation`, `presentation`, `phraseLibrary`, `clipChoices`, `localization`, `provenance`, and document-level `midi` are optional.

## 5. Structural authority and semantic authority

The JSON Schema defines structural validity: object shape, required fields, enum members, numeric ranges, and most local constraints. The specification and this manual define semantic rules that cannot be expressed cleanly in JSON Schema, such as reference resolution, ownership, overlap rules, migration behavior, and safe preservation.

A document can pass JSON Schema and still be semantically invalid if its references or cross-object relationships are inconsistent.

## 6. Version handling

Select semantics by the declared version. A 4.1-only reader must not assume a 4.2.0 document is 4.1.0. A reader that explicitly supports 4.2 may perform compatibility playback while preserving optional unsupported data. A valid 4.1 document can be migrated by changing only the root version; no vocal metadata is inferred. Never silently relabel data just to pass a schema.

## 7. PPQ and global musical time

`ppq` is the number of ticks per quarter note. OSTF stores musical timeline positions as integer ticks. Time is not stored as seconds and is not fundamentally stored as bar numbers.

All absolute timeline objects—including Sections, Tempo changes, Meter changes, Key changes, Chords, Harmony Scale contexts, Clips, and Track Directions—share the same document PPQ.

## 8. Half-open time ranges

Timed ranges use the half-open convention `[start, start + duration)`. Two objects may meet exactly at a boundary without overlapping.

This rule is especially important for same-type Track Directions and timed Harmony Scale contexts.

## 9. Absolute versus local time

Timeline-level objects use absolute document ticks. Clips have an absolute `start`, while Note and MIDI-event `start` values are stored inside the Clip and may be signed. This allows pickups and pre-roll material relative to a Clip.

An implementation should not convert between local and absolute positions without preserving exact tick values.

## 10. IDs

Core IDs are stable document-local identifiers. They are not display names. IDs should remain stable when the same logical object is moved or edited, and new IDs should be created when an independent copy is created.

Never resolve references by array index, visible name, localized label, or inferred musical role.

## 11. Global Core ID uniqueness

Core object IDs participate in a shared document namespace unless the specification explicitly says otherwise. A Note ID must not collide with a Track ID, Chord ID, Direction ID, or other Core ID.

Reference objects reuse IDs but do not create new identity. Validators must distinguish references from object declarations.

## 12. References

Generic Core references use `{ "type": ..., "id": ... }`. The type vocabulary includes Sections, Tracks, Clips, Notes, Chords, Scales, Sound Slots, Drum Kits, lyric objects, Resources, metadata objects, MIDI Buses, MIDI Events, Lyric Voices, and 4.1 Track Directions.

References must resolve by ID to an object of the declared type.

## 13. Unknown data and preservation

A non-lossy editor must preserve supported Core data that it does not actively edit. Unknown vendor Direction data and legacy extension payloads must not disappear merely because an application cannot interpret them.

If safe preservation is impossible, the application should refuse destructive overwrite or clearly offer an explicitly lossy export.

## 14. Authority boundaries

OSTF deliberately separates several kinds of truth. Harmony describes musical harmonic context. Notes and MIDI Events describe concrete stored performance. Track Directions describe how a Track should be performed, interpreted, or generated. Generation records process/history/intention. Presentation describes non-musical display metadata.

Do not store the same concept in several competing locations.

## Part II — Song, Timeline, Key, Scale, Harmony

## 15. Song metadata

`song.title` is the only required Song field. Optional fields include subtitle, description, alternate titles, credits, genres, key, song-level scale, languages, primary lyric document, moods, rights, and multiple melody-track declarations.

Original authored text is authoritative. Localization adds display translations without replacing source text.

## 16. Alternate titles

Alternate titles have stable IDs and title text. Array position is not identity. Use them for established alternate names, not UI-transient aliases.

## 17. Genres

Genres are song-local open tags with stable IDs and authored names. OSTF does not impose one genre taxonomy. An optional external URI may point to an external vocabulary but is never auto-dereferenced or authoritative over the local label.

## 18. Moods

Moods are authored descriptive tags. They are not generation presets, probabilities, or automatic emotional analysis results. They may also carry an optional external vocabulary URI.

## 19. Languages

`song.languages` records relevant language tags for the work. It does not replace language fields on lyric documents and does not imply that every textual field has been translated.

## 20. Contributors and credits

`contributors[]` defines stable song-local identities. `song.credits[]` assigns roles to those contributors. One contributor can receive multiple credit roles without duplicating identity records.

Credit `role` is an open semantic token. `label` can provide display wording when needed.

## 21. Rights

`song.rights` is an authored rights statement. OSTF never infers ownership, permission, copyright status, or license validity. `rightsHolderIds` reference Contributor IDs.

The existence of a license URI is descriptive data, not a guarantee that the license applies correctly.

## 22. Timeline

`timeline` contains Sections, Tempo changes, Meter changes, optional Key changes, optional total duration, and optional bar origin. These objects share the global PPQ timebase.

A Reader should build the timeline before interpreting time-dependent Harmony, Clips, or Directions.

## 23. Sections

Sections have stable IDs, names, starts, and positive durations. `role` is an open authored role such as `intro`, `verse`, `chorus`, `bridge`, or a custom term.

Sections may overlap if an application intentionally models nested or alternative structure, unless a higher-level workflow imposes stricter rules.

## 24. Tempo changes

Tempo changes are step changes at absolute ticks and store BPM as a positive numeric value. The first event is normally at tick zero, although the schema does not use Tempo changes to encode ramps.

Tempo changes do not rewrite musical tick positions.

## 25. Meter changes

Meter changes store numerator, denominator, and optional beat grouping. `beatGroups` is useful for meters such as 7/8 grouped 2+2+3.

Meter describes metrical interpretation; it does not change the PPQ unit.

## 26. Bar origin

`timeline.barOrigin` allows display systems to choose a bar-count origin without changing stored positions. It is metadata for bar numbering, not a second timing coordinate system.

## 27. Key

A Key can be `tonal`, `atonal`, or `unspecified`. Tonal Keys require a spelled tonic and mode string. Atonal and unspecified Keys do not carry tonic/mode.

Mode strings are open. Applications must preserve unknown modes rather than silently rewriting them to major or minor.

## 28. Initial Key and Key changes

The initial Key belongs at `song.key`. Changes after tick zero belong in `timeline.keyChanges[]`. Key changes use positive ticks so tick zero does not have two competing authorities.

A Key change persists until another Key change or the end of the document.

## 29. Song-level Scale

`song.scale` is an explicit song-level scale definition with stable ID, tonic, and pitch-class intervals relative to the tonic. It is distinct from the Key object and distinct from timed Harmony Scale contexts.

The interval set includes 0 and uses unique pitch classes 0–11.

## 30. Chords

Harmony Chords have ID, start, duration, and label. A Writer may store only the label, or may also provide structured root, intervals, bass, and voicing.

When `root` or `intervals` is used, both are required together. The label remains authored text and should not be regenerated unnecessarily.

## 31. Chord intervals

Chord intervals may extend beyond one octave, allowing explicit tensions. Interval 0 must be present in structured interval lists.

Applications should not flatten all chord semantics to a fixed transposition of pitch classes if the authored chord spelling or label carries meaningful information.

## 32. Slash bass

`bass` stores the authored chord bass pitch class independently from root. A slash bass is harmony information, not automatically a concrete bass-line Note.

## 33. Chord voicing

A Chord may carry a `voicing` snapshot of MIDI-style pitches and optional velocities. Voicing is descriptive harmonic realization, not a Track Clip and not an automatic playback sequence.

Concrete arrangement notes still belong in Tracks.

## 34. Timed Harmony Scale contexts

`harmony.scales[]` stores timed harmonic or analytical scale contexts. These objects may overlap only when the intended analytical model can tolerate ambiguity; array order never defines precedence.

They are not automatic performance instructions. OSTF 4.1 Track Directions can reference them explicitly when a generator should follow them.

## 35. Scale targets

A timed Scale may explicitly target a Section, Track, Clip, Chord, or Note by ID. The target narrows its analytical context; it does not make that Scale a Track Direction.

## 36. Harmonic authority versus improvisation authority

A scale that describes the harmony and a scale chosen as an improvisational pitch vocabulary can differ. For example, a song may remain in A minor while a Guitar Direction requests A-minor pentatonic only for an interlude.

Do not overwrite Harmony merely to express a performance strategy.

## Part III — Tracks, Clips, Notes, Sound Slots, Drums

## 37. Tracks

Tracks have stable ID, name, Clips, and optional role, Instrument, enabled state, Track type, preferred view, Sound Source, Drum Kit, MIDI interpretation, localized names, and 4.1 Directions.

A Track is a logical musical lane, not a DAW mixer channel.

## 38. Track roles

`track.role` is the authored default role for the whole Track. The vocabulary is open. OSTF 4.1 `playingRole` Directions can temporarily override its interpretation for a range.

## 39. Track types

`trackType` is `melodic`, `drum`, or `mixed`. It is a structural/editorial hint. A melodic Track cannot declare `drumKitId`.

## 40. Preferred view

`preferredView` can request `auto`, `pianoRoll`, or `drumGrid`. It is a display preference, not musical authority.

## 41. Instrument

`instrument.name` is required when an Instrument object is present. Optional family and localized names support display and classification without defining a standardized instrument ontology.

4.1 adds optional `playablePitchRange` as an authored pitch capability.

## 42. Sound Source

`soundSource` is an informational rendering class or opaque destination hint. It can be unassigned, GM1, external MIDI, plug-in, or host managed.

It does not bind a physical port, load a plug-in, or carry plug-in state.

## 43. Clips

Clips have stable ID, absolute start, positive duration, concrete Notes, and optional MIDI Events. Note and event starts are local to the Clip.

Moving a Clip should normally preserve its internal local timing.

## 44. Notes

A Note addresses either a pitch or a Sound Slot ID, never both. Pitch Notes use MIDI-style 0–127 pitch numbers. Sound-slot Notes address logical percussion targets.

Notes are the authoritative stored Note events. Note On/Off messages are not duplicated into `midiEvents[]`.

## 45. Note velocity

`velocity` is optional and uses 1–127. Absence means unspecified, not automatically 100 or 127. Applications may use a playback default but must not write back an invented value unless the user chooses it.

## 46. Release velocity

`releaseVelocity` stores optional Note-Off velocity 0–127. It is distinct from Note-On velocity.

## 47. Enabled state

`enabled:false` preserves a Note but suppresses scheduling/playback. It is not the same as deleting the Note and is not the same as `probability:0`.

## 48. Probability

`probability` is 0.0–1.0. Omission means full probability. OSTF does not standardize a shared random-number sequence, so deterministic interchange requires materializing the chosen result as concrete Notes.

## 49. Velocity deviation

`velocityDeviation` describes an optional relative variation endpoint and requires `velocity`. The resulting velocity must remain in 1–127.

## 50. Pitch role

Pitch Notes may declare `pitchRole:"musical"` or `pitchRole:"fixedTrigger"`. Fixed triggers represent exact MIDI keys such as keyswitches and should not be transposed or treated as musical-pitch evidence.

Sound-slot Notes do not use `pitchRole`.

## 51. Sound Slots

Sound Slots are stable logical percussion targets. Equal names or MIDI mappings do not merge different slot IDs.

A Slot may carry a legacy MIDI-note hint, an explicit MIDI mapping, localized names, and an open role.

## 52. MIDI mapping for Sound Slots

`midiMapping.standard` is `gm1` or `custom`. GM1 percussion mappings are constrained to GM percussion key range. Custom mappings use any MIDI 1.0 note 0–127.

Mapping is an external output mapping, not the slot's identity.

## 53. Drum Kits

A Drum Kit is a named ordered list of global Sound Slot IDs. It does not define samples, plug-in presets, choke groups, or kit-local remapping.

Track `drumKitId` references one Drum Kit.

## Part IV — Lyrics, Melody Relationships, Resources, Localization

## 54. Lyrics model

Lyrics are separated into Documents, Phrases, Units, Alignments, and optional Voices. This separation allows text to be shared across several melody/vocal tracks without duplicating the authored lyric document.

## 55. Lyric Documents

A Lyric Document has stable ID and optional title/language. It is the textual document identity used by Phrases and Lyric Voices.

## 56. Lyric Phrases

Phrases reference a Lyric Document and store text plus optional pronunciation and optional timed range. Timing is optional; text identity does not depend on timing.

## 57. Lyric Units

Units subdivide a Phrase and may also carry pronunciation and optional timing. Applications may choose word-, syllable-, mora-, or other unit granularity according to the authored data.

## 58. Lyric Alignments

Alignments connect one or more Lyric Unit IDs to one or more concrete Note IDs. Alignment does not copy Note timing into lyric text and does not replace the Notes.

## 59. Multiple Melody Tracks

`song.melodyTrackIds` explicitly identifies multiple melody Tracks. `primaryMelodyTrackId` may identify one primary melody without implying that other melody Tracks are secondary or disposable.

Names such as “Lead Vocal” are not substitutes for explicit IDs.

## 60. Lyric Voices

A Lyric Voice explicitly relates one Track to one Lyric Document and may declare an open role such as lead, harmony, backing, unison, double, counter, adlib, or response.

Several Voices may reference the same Lyric Document.

## 61. Voice-specific alignment

`lyricAlignment.voiceId` makes an alignment specific to one Lyric Voice. When present, aligned Units should belong to that Voice's document and aligned Notes should belong to that Voice's Track.

## 62. Primary lyric document

`song.primaryLyricDocumentId` is an explicit preferred lyric-document reference. It does not delete or hide other lyric documents.

## 63. Resources

Resources point to external audio, MIDI, text, or other files using URI strings. Optional SHA-256 may identify exact bytes.

A Resource URI is data. Readers should not automatically fetch or execute external resources without the application's normal security and permission model.

## 64. Localized names

Several Core objects support `localizedNames` directly for simple display-name translation. The original source name remains authoritative.

Language-tag dictionaries must preserve independently authored translations.

## 65. Standard Localization object

The root `localization` object supports structured translation entries for approved textual fields on stable Core targets. It uses explicit targets and dependency status.

Localization must not target arbitrary musical values or rewrite source metadata.

## 66. Legacy extensions

`extensions` exists for preserved third-party or older compatibility payloads. Standard first-party Core information should not be hidden only in extensions.

Unknown extensions should be preserved if an editor claims non-lossy round-trip behavior.

## Part V — Derived and Advanced Core

## 67. Status and dependencies

Several advanced Core objects use `status` plus `dependencies`. Status is `current`, `stale`, or `unverified`. Dependencies can apply to the whole document, no dependency, or explicit object references.

Applications should not pretend stale derived information is current after editing its dependencies.

## 68. Relative Phrases

`relativePhrases` records relationships between concrete Notes and chord-tone or scale-degree contexts. It does not replace concrete pitch Notes.

A relative assignment identifies the concrete Note, basis, context ID, anchor pitch, index, and chromatic offset.

## 69. Generation

`generation` records generation process/history/intention. A Generation Process stores generator identity, input references, output references, protected Notes, optional target range, and optional intent.

Loading a file never re-runs generation automatically.

## 70. Generation Intent

Generation Intent may describe genre names, mood names, groove intent, prompt text, and seed. These are descriptive process metadata and do not overwrite `song.genres`, `song.moods`, or concrete Notes.

Prompt text is untrusted document content and is not permission to execute external actions.

## 71. Groove Intent

Groove Intent can describe a name or a long/short subdivision weighting with `unitTicks`. It is an intent record, not a playback transformation that must be re-applied to already stored Notes.

## 72. Presentation

`presentation` stores optional role definitions, Section-role assignments, and appearance colors. Presentation never changes musical semantics.

An editor may ignore colors while preserving them.

## 73. Role definitions and role colors

Role Definitions create stable custom presentation roles. Appearance can color generic roles, custom role IDs, or specific target objects.

Color uses six-digit hexadecimal RGB text.

## 74. Phrase Library

Phrase Library stores reusable templates and materialized instances. Template Notes are not played by themselves. Concrete Track Notes remain playback authority.

## 75. Phrase templates

A Phrase Template has ID, duration, and template-local source Notes. Source Notes can carry the same note-state properties as concrete Notes but remain template content.

## 76. Phrase instances

A Phrase Instance links a Template to a concrete Clip, repeat count, transpose amount, and Note mapping. Velocity and note-state linkage modes define how explicit refresh operations treat those values.

Loading a document does not refresh or regenerate an instance automatically.

## 77. Clip Choices

`clipChoices` groups alternative Clip candidates and records a selected candidate or `null`. Candidate identity is stable; selection is not inferred from which Clips happen to be enabled.

## 78. Document identity

The optional `document` object records an opaque document ID, revision ID, parent revisions, and creator/modifier software. It supports revision lineage without imposing a network service.

## 79. Provenance

Provenance records non-executable historical assertions such as create, import, conversion, edit, transpose, merge, and generation actions. Provenance is not a composer credit and does not prove authorship.

## 80. Transpose provenance

A transpose Provenance Record may store semitone count and before/after Key snapshots. `semitones` is only legal for the transpose action.

## Part VI — MIDI Performance Layer

## 81. MIDI principle

OSTF stores Notes as Notes and stores controller/program/pitch/pressure streams separately as MIDI Events. It is not a JSON serialization of raw MIDI Note On/Off messages.

## 82. Logical MIDI Buses

Document-level `midi.buses[]` defines portable logical MIDI destinations. Each Bus has its own channel namespace.

A Bus is not a physical OS port or DAW destination. The Host maps a logical Bus to its own environment.

## 83. MIDI channels

MIDI channels are 1–16 in OSTF user-facing numeric form. Program numbers remain wire-style 0–127 as defined by the Schema; applications that display 1–128 must convert explicitly.

## 84. Track MIDI modes

A Track MIDI object uses `singleChannel`, `multiChannel`, or `mpe` mode. Single-channel mode requires one channel. Multi-channel mode leaves channel assignment to Notes/Events. MPE mode requires an MPE zone declaration.

## 85. Control Change

Control Change Events store controller number, value, optional channel, optional order, and optional per-note target where permitted. They remain separate from Notes.

## 86. Bank Select

Bank Select uses standard CC 0 and CC 32 Events. OSTF does not create a separate Bank event type. Applications should preserve same-tick ordering with Program Change when order matters.

## 87. Program Change

Program Change stores program 0–127. A UI showing programs 1–128 must convert to and from the wire value explicitly rather than writing the display value directly.

## 88. Pitch Bend

Pitch Bend stores the full 14-bit value. Do not collapse it to 7-bit or convert it to arbitrary floating-point normalization in the file.

## 89. Channel Pressure

Channel Pressure stores one pressure value for a MIDI channel. In MPE it may also be associated semantically with a targeted Note according to the authored event/channel relationship.

## 90. Polyphonic Key Pressure

Poly Pressure stores channel, pitch, and pressure value and may identify a target Note. It is distinct from Channel Pressure.

## 91. Channel Mode

Channel Mode messages use the standard MIDI controller-number/value representation with event type `channelMode`.

## 92. Same-tick order

MIDI Events may carry signed `order` values to provide deterministic ordering when several Events share a start tick. Array order is not a substitute for explicit order when wire-order semantics matter.

## 93. MPE zones

MPE settings declare a lower or upper zone plus member-channel count. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously.

## 94. MPE Notes

In an MPE Track, member-channel Notes store their actual MIDI channel. MPE does not require a separate MPE Note type.

## 95. Per-note MPE expression

Pitch Bend, CC, or Pressure events may use `targetNoteId` as defined by the 4.0 performance model. Targeted events should resolve to a concrete Note in the appropriate musical context.

Do not invent MPE-only duplicate event types.

## 96. Multiple MIDI buses

The same MIDI channel number may appear independently on different logical Buses. `(bus, channel)` is the relevant routing context, not channel alone.

## Part VII — OSTF 4.1 Track Directions

## 97. Why Track Directions exist

MIDI can store concrete performance control but is poor at storing higher-level semantic instructions such as “improvise with A-minor pentatonic for this interlude” or “act as the soloist for these four bars.” Track Directions provide a typed Core location for those instructions.

They are semantic instructions, not a second MIDI stream.

## 98. One timeline, not a Track-specific timeline

`tracks[].directions[]` does not create another clock or independent Track timeline. Every Direction is positioned on the same global OSTF timebase.

Range Standard Directions use `start` and `duration`. Vendor Directions may also be point-timed with `at`.

## 99. Standard Direction types

OSTF 4.1 standardizes three range Direction types: `improvisation`, `playingRole`, and `pitchRange`. `vendor` is the controlled extension mechanism.

The 4.1 vocabulary is intentionally small so instrument-specific technique taxonomies can mature before becoming Core.

## 100. Improvisation Direction

`improvisation` defines pitch-vocabulary guidance for generation or interpretation. It does not change Song Key, Chords, or Harmony Scale contexts.

It requires a `pitchSource` and explicit `adherence` policy.

## 101. `effectiveKeyScale`

This pitch source derives a canonical pitch collection from the effective Key and Key changes. 4.1 defines mappings for major, minor, dorian, phrygian, lydian, mixolydian, and locrian.

Atonal, unspecified, and unknown mode strings remain unresolved rather than being guessed.

## 102. `songScale`

This source uses explicit `song.scale`. It is invalid semantically if the Song has no explicit Scale. A Writer must not invent one just to satisfy the Direction.

## 103. `harmonyScales`

This source references authored `harmony.scales` IDs and is intended for chord-scale or jazz-style operation. The referenced Scale objects keep their own timing authority.

Referenced scale contexts must not overlap each other inside the same Improvisation Direction range, and array order is never precedence.

## 104. `explicitScale`

This source embeds a Direction-local pitch collection. It is the standard solution for a temporary pentatonic or blues vocabulary that should not become a Harmony assertion.

For example, an A-minor song can give only the Guitar an A-minor-pentatonic `explicitScale` during an eight-bar solo.

## 105. `adherence`

`strict` means generated pitches should stay within the chosen pitch vocabulary. `preferred` makes that vocabulary primary while allowing intentional passing tones, approaches, ornaments, or other outside notes.

No implicit default is defined; the Writer must state the intended policy.

## 106. Playing Role Direction

`playingRole` temporarily changes Track role interpretation for a range. A Guitar whose default role is accompaniment can become `solo` during an interlude and automatically return to the Track default after the range ends.

The role string is open and must be preserved even if unknown.

## 107. Pitch Range Direction

`pitchRange` constrains or prefers a temporary register with `lowPitch`, `highPitch`, and explicit `constraint` (`strict` or `preferred`). It is an instruction to a generator or performer-aware system, not a new Note range inside existing concrete Notes.

## 108. Instrument playable pitch range

`instrument.playablePitchRange` declares a non-timed authored capability. It can distinguish, for example, a 5-string Bass that reaches Low B from a more limited instrument setup.

A timed `pitchRange` Direction must stay inside a declared playable range.

## 109. Why tuning/fret/string models are not Core 4.1

Playable pitch capability is broadly interoperable; exact string count, tuning, fret geometry, fingering, and technique taxonomies are much more instrument- and application-specific. 4.1 deliberately leaves them outside Standard Core.

They can be explored with Vendor Directions or future versions.

## 110. Vendor Range Directions

A Vendor Direction uses `type:"vendor"` plus a stable reverse-domain-style namespace, name, optional version, and arbitrary JSON object `data`. Range Vendor Directions use `start` and `duration`.

`org.ostf` and descendants are reserved for OSTF-defined use.

## 111. Vendor Point Directions

Vendor Directions may use a single absolute `at` position instead of a range. This allows experimentation with point concepts such as breath cues or one-shot gestures without prematurely standardizing them.

## 112. Unknown Vendor Directions

Unsupported Vendor Directions may be ignored behaviorally but must be preserved by a non-lossy Writer. Software must not reinterpret a Vendor payload as a Standard Direction merely because names look similar.

## 113. Natural-language instruction

Any Direction may include optional `instruction` text for human or AI-readable nuance. Structured Core parameters remain authoritative if the text conflicts with them.

`instruction` is untrusted document data. It is not executable code, permission for file/network/account actions, or privileged instructions to an AI system.

## 114. Direction overlap

Different Standard Direction types may overlap. Same-type Standard range Directions on one Track must not overlap for `improvisation`, `playingRole`, or `pitchRange`.

4.1 defines no hidden priority, last-wins behavior, or array-order precedence.

## 115. Directions and concrete Notes

Concrete Notes and MIDI Events remain authoritative for deterministic playback. A Direction does not invalidate existing Notes merely because they do not satisfy it.

Generation or regeneration from Directions must be an explicit application/user action, not an automatic consequence of loading the file.

## Part VIII — Reading, Writing, Editing, Merging, Migration

## 116. Reader implementation order

A robust Reader should: parse JSON; verify `format` and `version`; select the matching Schema; validate structure; build the global ID index; resolve references; build Timeline/Harmony; build Tracks/Clips/Notes; resolve Lyrics and advanced Core; then interpret MIDI and Track Directions according to supported capabilities.

Do not derive identities from names before reference resolution.

## 117. Writer principles

A Writer should preserve stable IDs, preserve unsupported optional Core data, avoid inventing omitted values, emit valid references, and use atomic save where practical.

A Writer must not silently normalize open vocabularies into its own preferred terms.

## 118. Safe deletion

Before deleting a Core object, an editor should find all references to it. Deletion may affect Harmony Scale targets, lyric alignments, generation records, presentation objects, phrase instances, clip choices, MIDI targets, or Directions.

Offer a repair plan instead of leaving dangling references.

## 119. Moving Tracks and Clips

Moving a Track does not change absolute timing because Track order is not time. Moving a Clip changes the Clip start while preserving its local Note and MIDI-event starts unless the editing operation explicitly changes them.

Track Directions belong to the Track and use absolute document time, so arrangement edits should move them consistently when the user moves the musical range they describe.

## 120. Section editing

Resizing or moving Sections does not automatically stretch unrelated Notes, Chords, or Directions. An editor must define the user's intended reflow operation explicitly.

Do not infer a global ripple edit merely because one Section duration changed.

## 121. Merge

Merge must operate by stable IDs and explicit conflict rules. Two objects with the same display name are not automatically the same object.

Track merge includes Clips, Notes, MIDI configuration, and Track Directions as part of that Track's authored state.

## 122. Atomic save

For files on disk, a safe Writer should write a complete new file, validate it, and then replace the previous file atomically where the platform supports that operation. This reduces corruption risk.

## 123. 4.0 to 4.1 migration

A valid 4.0 document can become 4.1 without inventing any new data. The minimal migration is an explicit version change after validation.

Do not infer Directions, playable ranges, solo roles, or pentatonic choices from Track names, Notes, Genre, or common practice unless the user explicitly asks for such inference.

## 124. 4.1 to 4.0 downgrade

Downgrade is lossless only when no 4.1-only Core data exists. `tracks[].directions`, `instrument.playablePitchRange`, and references of type `trackDirection` cannot be represented in 4.0 Core.

A lossy exporter must disclose what will be removed and must not silently claim round-trip preservation.

## 125. Compatibility Playback

A 4.1-aware Player may ignore optional Directions that it cannot execute while still playing concrete Note/MIDI content. It should distinguish “unsupported behavior” from “missing data.”

A 4.0-only Player is not automatically a 4.1 Compatibility Player.

## 126. Unknown future versions

A 4.2 implementation must not assume 4.3 or 5.x has unchanged semantics. Refuse unsupported destructive writes or use an explicitly preservation-only mode. Recognition of a future version is not established merely by ignoring unknown keys.

## Part IX — Validation and Conformance

## 127. Structural validation

Use `schema/ostf-4.2.0.schema.json` with JSON Schema Draft 2020-12. Structural validation should happen before semantic reference checks.

The bundled validator performs both stages.

## 128. Semantic validation

Semantic validation includes global ID uniqueness, reference resolution, Track Direction overlap, playable-range relationships, Harmony Scale references, lyric relationships, MIDI Bus references, Phrase Library mappings, Clip Choice references, and other cross-object rules.

A production implementation may add stricter domain checks as long as it does not reject valid Core data merely because the application lacks a feature.

## 129. Reader conformance

A conforming Reader recognizes 4.2 explicitly, uses its structure and semantics, resolves typed references and distinguishes musical authority. Lyrics are not Notes; Directions are not Harmony; vocal pitch is not ordinary MIDI Bend. Unsupported optional behavior may be ignored for playback only if the source data remains preserved.

## 130. Writer conformance

A conforming Writer emits structurally and semantically valid Core data, preserves unsupported information in non-lossy mode, and does not silently invent or discard meaningful fields.

## 131. Compatibility Player conformance

A Compatibility Player explicitly recognizes 4.1 and may skip unsupported Direction execution. It must still preserve those Directions if it saves the document non-lossily.

## 132. Direction-aware generator conformance

A generator should declare which Direction types and pitch-source modes it actually supports. It must not claim `harmonyScales` support if it cannot resolve referenced Scale IDs and timing.

It must not claim `strict` adherence if it knowingly emits outside pitches without another explicit authored rule.

## 133. Validation versus musical quality

Validation proves format correctness, not musical quality. A structurally valid improvisation instruction can still lead to a poor musical phrase. Musical generation quality belongs to the implementing application.

## Part X — Common implementation mistakes

## 134. Do not duplicate Note On/Off into MIDI Events

Notes remain in `notes[]`. MIDI controller/program/pitch/pressure streams remain in `midiEvents[]`.

## 135. Do not store physical ports as MIDI Bus identity

Logical Buses are portable document-local routing identities. Physical/virtual host port assignments are environment state.

## 136. Do not store Program display numbers directly

If a UI displays 1–128, convert explicitly to stored Program 0–127.

## 137. Do not reduce Pitch Bend to 7-bit

Store the specified 14-bit value.

## 138. Do not create MPE-only duplicate event types

Use the existing MIDI Event types plus channel and target-note relationships.

## 139. Do not treat Harmony Scale as a hidden improvisation command

A Harmony Scale describes analytical/harmonic context. Use an `improvisation` Direction when a Track should actively use a pitch vocabulary for generation.

## 140. Do not turn Directions into a second timeline

Directions use the shared OSTF timebase. There is no independent Track clock.

## 141. Do not resolve conflicts by array order

If the specification says an overlap is invalid, report it. Do not silently apply last-wins behavior.

## 142. Do not execute document text

Prompts, Instructions, URIs, identifiers, Vendor data, and Provenance descriptions are document data. They are not application commands or permission to perform external actions.

## 143. Do not discard unsupported 4.2 information on save

Preserve inherited data and optional phonetics, profiles and vocal performances. If preservation is not possible, refuse a non-lossy overwrite or offer an explicitly lossy export with a separate filename.

## Part XI — Practical implementation patterns

## 144. Simple single-channel piano

Use one melodic Track, one or more Clips, pitch Notes, a logical MIDI Bus if routing is relevant, and `singleChannel` MIDI mode. No Direction is required unless a semantic generation/performance instruction is authored.

## 145. Multi-timbral track

Use `multiChannel` Track MIDI mode and explicit Note/Event channels. Do not set a single Track channel in this mode.

## 146. External synth collection

Use multiple logical MIDI Buses or Tracks as needed, with optional `soundSource.kind:"externalMidi"` informational identifiers. Keep physical device mapping in Host state.

## 147. MPE synth

Declare a logical Bus, `mpe` Track mode, MPE zone, member-channel Notes, and ordinary MIDI Events for expression. Use `targetNoteId` where the 4.0 model requires explicit Note association.

## 148. Lead plus harmony vocals

Declare both melody Tracks, define one or more Lyric Documents, define Lyric Voices linking Tracks to Documents, and optionally use voice-specific Alignments.

## 149. Call and response

Separate lead and response Tracks and Lyric Voices. Use open `role` values such as `lead` and `response`; do not infer role from Track names.

## 150. Popular-music solo

Keep the Song Key/Harmony intact. On the solo Track, use `playingRole:"solo"` and an `improvisation` Direction with `explicitScale` or `effectiveKeyScale` for the relevant range.

## 151. Jazz solo

Author timed Harmony Scale contexts and reference them from the soloist's `harmonyScales` pitch source. Keep scale timing in Harmony and solo intent in the Direction.

## 152. Five-string bass

Declare `instrument.playablePitchRange` to include Low B. Add a temporary `pitchRange` Direction only when the arrangement should prefer or require a narrower register.

## 153. Standard vocal breath events and vendor cues

For portable 4.2 breath timing, use `clips[].vocalPerformances[].breathEvents` with an explicitly assigned Voice. A vendor Direction remains available for application-specific cues but must not become a competing authoritative standard breath timeline. Do not automatically migrate historic vendor payloads by guessing their meaning.

## 154. AI-assisted generation

Use structured Direction parameters for interoperable constraints and optional `instruction` for nuance. Keep AI model-specific settings in Vendor data or external application state rather than forcing them into Standard Core.


# Part XII — Complete 4.2 vocal workflow

This part integrates all optional 4.2 semantics into the same manual as the inherited Core. Read it before implementing a singing adapter; melodic roles alone never authorize vocal assignment.

## 1. Purpose

OSTF 4.2 provides a neutral interchange representation, allowing AI or humans to author OSTF directly and separate adapters to translate explicitly assigned vocal content into singing-synthesizer project formats. Examples of *potential* targets include UFDATA, SVP, USTX, VPR/VSQX and CCS. Mentioning a target is **not** a claim of implemented or tested support. OSTF does not provide audio synthesis, vendor voicebanks, proprietary synthesizer APIs or a dedicated vocal Max for Live device.

## 2. OSTF 4.1 Core preservation

- Existing `ppq`, `timeline`, `harmony`, `tracks[]`, `clips[]`, `notes[]`, `midiEvents[]`, `lyrics.*`, and `resources[]` retain their 4.1 structures and meanings.
- Ordinary MIDI performance continues to be represented by `notes[]` and `midiEvents[]`. CC, 14-bit Pitch Bend, channel/poly aftertouch and MPE semantics are not redefined.
- `song.melodyTrackIds`, `primaryMelodyTrackId`, `track.role`, and `trackType="melodic"` **do not** imply a vocal track. Vocal parts can exist in non-melody roles; instrumental melodies remain valid.
- `lyrics.documents`, `phrases` and `units` retain lyric ownership; `lyrics.voices` and `lyrics.alignments` retain vocal assignment and lyric-to-note relationships.
- An otherwise valid OSTF 4.1 document can ordinarily be migrated by changing only `version` to `4.2.0`. New vocal fields MUST NOT be fabricated to satisfy a migration.

## 3. Optional 4.2 fields

```text
lyrics.units[].phonetics[]                   optional
lyrics.voices[].vocalProfile                 optional
tracks[].clips[].vocalPerformances[]         optional
  id, voiceId                                required within each performance
  noteIds[]                                  optional explicit ownership
  phonemeEvents[]                            optional phoneme timing
    order                                    optional same-tick tie breaker
  pitchCurves[]                              optional note-relative cents
  expressionCurves[]                         optional voice/clip or note curves
  techniques[]                               optional vocal intent
  breathEvents[]                             optional breath timing
```

These fields extend existing 4.1 objects and are never required for an instrumental track. Basic explicit voice + alignment can be exported without `vocalPerformances`. Field types, enums, numeric ranges and required properties are specified by the 4.2 Schema and `PARAMETER_REFERENCE.md`.

## 4. Identity, ownership and note authority

1. Each vocal performance references a `lyrics.voices[].id` using `voiceId`. That Voice's `trackId` MUST match the enclosing Track.
2. At most one VocalPerformance per Voice is permitted in the same Clip. A Clip MAY have several different Voices. Existing 4.1 pitch Notes are referenced, never recreated as separate authoritative vocal notes.
3. When `noteIds[]` is supplied, it explicitly identifies existing pitched Notes within the parent Clip. It MUST contain every Note assigned by the same Voice's scoped Alignments in that Clip. Missing Notes, fixed triggers and non-pitched sound slots MUST NOT be referenced.
4. Without `noteIds[]`, use Notes explicitly resolved through `lyrics.alignments[].voiceId`. A melody role MUST NOT be treated as a substitute for assignment.
5. A legacy Alignment without `voiceId` MUST NOT be silently attributed to a specific Voice. Require explicit resolution when necessary.
6. Alignments must reference existing Notes. Voice-scoped Alignments must use pitched Notes on the declared Voice Track. Multiple Voices MAY share a source Note ID, but exporting separate voices may require duplication/splitting with an explicit diagnostic.

## 5. Lyrics and pronunciation

`lyrics.units[].text` is display text; `pronunciation` is authored reading; `phonetics[]` supplies optional phoneme candidates. Neither field silently overwrites another. `phonetics[].alphabet` is one of `ipa`, `xsampa`, `arpabet`, `other`; `other` requires `namespace`, and `symbols[]` is ordered. `preferred:true` is permitted at most once for each alphabet and case-insensitively compared language grouping; different alphabets may each have a preferred entry.

The adapter's source priority is: explicitly timed `phonemeEvents` → target-mappable `phonetics` → `pronunciation` → a documented target dictionary estimate based on display `text`. Estimates MUST NOT silently modify the source. No interchange format guarantees pronunciation equivalence across languages, phoneme dictionaries or voicebanks.

### 5.1 Same-tick phoneme event order

`phonemeEvents[].order` is an optional signed integer that orders events of the same Voice, Clip and start Tick. If any event in such a same-start group supplies `order`, all events in that group MUST supply distinct values. If all omit it, structure remains valid, but their ordering is unresolved: an exporter MUST NOT claim a completely determined phoneme sequence without resolution. `order` does not govern MIDI or acoustic rendering priority.

### 5.2 Many-to-many lyric alignment

- One Unit to one Note: ordinary syllable-to-note association.
- One Unit to several Notes: melisma; do not invent repeated words or continuation symbols without a target-specific, disclosed loss/approximation policy.
- Several Units to one Note: requires explicit sequencing/timing to determine phoneme delivery; otherwise flag ambiguity.
- Several Units to several Notes: a valid representation but ambiguous for automated export until sufficiently disambiguated by alignment and phoneme timing.

`lyrics.alignments` is authoritative. A second, conflicting lyric mapping MUST NOT be invented in VocalPerformance. AI authors SHOULD prefer explicit, single-unit alignments when possible.

## 6. Vocal expression semantics

### 6.1 Vocal pitch

- Each `pitchCurves[].targetNoteId` references an existing pitched Note. `points[].value` is a **cents offset from that Note's base pitch**; `points[].at` is Clip-relative Tick. Interpolation is `step` or `linear`.
- At most one pitch curve exists per Voice/Clip/Note. Points are strictly ordered with no repeated Tick and MUST remain inside that Note's gate.
- A single-point curve defines a constant offset across the Note. With multiple points, values are **unspecified** outside the explicit point interval; do not extrapolate silently.
- For vocal export, an explicitly authored 4.2 pitch curve takes priority over overlapping 4.1 pitch-bend information for the corresponding Note. For ordinary MIDI playback, the **4.1 MIDI stream** remains authoritative. Do not sum curves and bend unconditionally.
- A legato or portamento contour across Note boundaries may exceed this note-scoped representation. Approximate or omit only with transparent loss reporting; do not create another authoritative melody.

### 6.2 Vocal expression curves

- Parameters are `dynamics`, `breathiness`, `tension`, `brightness`, and `voicing`, in abstract `[0, 1]` ranges. Missing is **unspecified**, not 0.5. These are not acoustically equivalent parameters across vendor engines.
- Without `targetNoteId`, the curve applies to the Voice/Clip; a note-scoped curve **replaces**, rather than adds to, the matching Clip-level parameter during its defined interval.
- A single point is a constant for the applicable scope. The interval outside a multi-point curve is unspecified; a note curve may fall back to a defined Clip curve outside its interval. Neither is silently extended.
- Vendor parameter mapping, audible fidelity and range conversions are adapter- and application-specific.

### 6.3 Techniques and breath events

Technique kinds (e.g., `scoop`, `fall`, `vibrato`, `legato`, `whisper`, `growl`, `falsetto`) are performance **intent**, not a replacement for explicit numeric curves. Optional intensity is abstract `[0,1]`. `breathEvents` represent timed `inhale` and `exhale`; rendering remains target-dependent. A technique MUST NOT be applied twice when the concrete curve already embodies it.

## 7. Shared timeline and tick conversion

- All time uses the existing song `ppq`. `clip.start` is song-absolute; Notes and vocal events/curves use Clip-relative Ticks.
- Negative local starts may represent preceding consonants or gestures, but the resulting song-absolute time MUST NOT be negative. Events MUST NOT extend beyond their parent Clip end.
- A target adapter SHOULD quantize absolute start/end positions using the exact rational PPQ ratio, then subtract the mapped end minus mapped start. Do not separately round an original duration and add it to the rounded start.
- The proposed deterministic reference rounding rule for target tick quantization is nearest integer, with exact halfway ties **away from zero**. It is an adapter reference rule and does not override a target format's specified interpretation.
- Positive events that collapse to zero duration, or distinct curve points that collide after quantization, MUST NOT be silently discarded or merged. Preflight must block or require an explicit approximation decision.
- `timeline.tempoChanges` remains authoritative. When converting Tick positions to milliseconds, integrate across every applicable tempo segment; never silently flatten tempo changes.

## 8. Rendering authority and compatibility

1. MIDI playback uses 4.1 `notes[]` and `midiEvents[]`; vocal metadata may be ignored.
2. Vocal export resolves Voice → Track/Clip/Note → Alignment → phonetic timing → pitch/expression → target-specific mapping.
3. Basic vocal data without VocalPerformance is a valid interchange input; a 4.1-to-4.2 version-only migration is valid when Schema and semantics pass.
4. Report exact mapping, approximations, omissions, ambiguity, and unverified features separately. Do not rewrite the source.
5. `unverified` or a successful local file write MUST NOT be described as an application-tested conversion. Application import, re-save and round-trip require independent evidence.
6. A 4.2 Reader MUST NOT silently drop future 4.3+ properties and save the result as if their meaning was preserved.

## 9. Conformance checks and limitations

Readers and writers must check structural validity and the applicable normative semantics: declared IDs, typed references, Voice/Track ownership, note membership, time bounds, curve order, value ranges and phoneme tie order. A reference containing an `id` is not a new ID definition. Export ambiguity is distinct from an invalid Core document. The bundled audit is a static package/field-coverage checker; it does not certify all semantic rules or execute a synthesizer.

## 10. Strict JSON intake

- OSTF 4.2 accepts UTF-8 JSON. Reject duplicate member names, NaN/Infinity, non-finite values, nonzero numeric underflow to zero, malformed UTF-8 and isolated Unicode surrogates before Schema validation. No implicit first-wins or last-wins interpretation.
- On rejection, do not silently repair or write source/converted documents. Reading a UTF-8 BOM MAY be supported solely for legacy input compatibility.
- Schema validity alone never proves complete semantic constraints (Voice/Note ownership, lyric mapping, same-tick order, PPQ conversion fidelity).

## 11. Adapter contracts (outside the Core Schema)

- **Export:** Explicitly resolve Voices from `lyrics.voices`/`lyrics.alignments`; do not infer them from a melodic Track. Disclose lost, approximated, ambiguous, and unsupported notes, phonemes, pitch, expression, voicebank, tempo or meter. Data loss is never implicitly approved.
- **Sidecar:** The opt-in `.vocal-sidecar.json` captures source vocal data and binds source/native/report hashes and original PPQ. It is neither a native synthesizer project nor a replacement for the source OSTF.
- **Edited-native review:** Independently verify source OSTF, baseline native, edited native, export report and sidecar. Display eligible lyric/pitch changes for read-only review; changed Notes, tempo, meter and Voice routing block safe mapping. Native pitch edits are not silently converted into OSTF cents.
- **Lyric-only approval/writeback:** New approval manifests default to `pending`/`false`. Only unambiguous one-Unit-to-one-Note edits with explicit approval may create a **new** OSTF containing changes limited to `lyrics.units[].text` and `lyrics.phrases[].text`. Preserving potentially stale pronunciation/phonetics/vocal performance requires additional explicit acknowledgement. Do not overwrite any existing file.
- SHA256 (SHA-256) is an identity/integrity check, not a signature or proof of authorship. Local adapter tests do not establish synth application interoperability.

Implementation-specific adapter contracts are outside this Core specification.

## 12. Versioning and compatibility

- Version-only migration from valid 4.1 changes `version: "4.1.0"` to `"4.2.0"` without inventing unspecified vocal data.
- Down-conversion to 4.1 when 4.2-only fields exist is lossy and MUST be disclosed. Unknown later-version fields MUST NOT be dropped through an apparently lossless save.
- Core conformance, locally tested adapter output, independently verified application import and acoustically equivalent rendering are **different claims with different evidence**.
- Post-release changes to an existing field's meaning, required status or timebase require a compatibility review. The 4.2.0 Core field definitions and normative semantics are frozen for this release.

For export and preservation boundaries, see [Conformance](CONFORMANCE.md) and [Migration](MIGRATION_4.2_TO_4.3.md).

## 13. Specification release scope

This is the OSTF 4.2.0 Core specification release. It defines portable data and semantics, not target-application compatibility. Native converters, voicebanks and synthesizer programs are not shipped in this package. No external application test is claimed. See [conformance and implementation boundaries](CONFORMANCE.md).

# Part XIII — Practical authoring, editing and publication

## A. Build a basic document

Start with the ten required root properties. Choose PPQ once, define global Sections and harmonic context, then create Track-owned Clips and Clip-local Notes. Use stable IDs and explicit references. Empty optional collections do not create fabricated musical content. The [Basic Vocal example](../examples/15-vocal-response-phrasing.ostf) shows the conventional Voice/Alignment path without requiring detailed vocal curves.

## B. Add an expressive vocal

Create a Lyric Document, Phrase and Units. Create a Voice referring to the actual Track and Document. Associate each Unit with existing Notes through voice-specific Alignments. Add a single VocalPerformance for each Voice/Clip only when authored expression is available. Add note IDs for wordless vocals rather than inventing display lyrics. Phoneme candidate data and timed phoneme events are separate.

For each pitch point use a Clip-local tick and a cents deviation from the targeted Note. A value of 100 means one semitone; it is neither an absolute MIDI note number nor a raw bend word. For expression use an explicit 0..1 value only when authored. A missing value is not a neutral preset.

## C. Editing operations

Moving a Clip updates global `clip.start` but normally preserves local Note and vocal timings. Recheck absolute time for pre-note negative offsets. Moving or deleting a Note must reconcile Voice membership, Alignments, curve targets, phoneme links and technique targets. Moving a vocal Track must preserve the Voice relationship. Splitting a Clip requires splitting or rehoming its vocal events without duplicating authoritative Notes. Update IDs and references together, never by display-name matching.

Changing displayed lyrics does not authorize rewriting pronunciation, phonetics or expression. A non-lossy editor either preserves these independent fields or explicitly requests a regeneration action. Deleting a Unit must not leave dangling phoneme references.

## D. Export decisions

Keep the OSTF source unchanged. Ask the adapter to select explicit Voices, resolve Notes and Alignments, map timing, and report omitted or approximated content. Reject an export that would silently collapse positive-duration events to zero or merge distinct curve points after rounding. Do not infer a commercial voicebank from `voiceDescription`. Shared voice Notes may require target-specific duplication, but that duplication belongs to the export result.

## E. Demo suite and parameter witnesses

See [Demo Guide](EXAMPLES_GUIDE.md) for the technical fixtures and complete mini-arrangements. [Parameter Coverage](COVERAGE_REPORT.md) identifies a real example and JSON Pointer for every reachable named field declaration. The count is declaration-location coverage, not exhaustive combinations of enum values, languages, numeric boundaries or external application outcomes.

## F. Read-only local audit

```bash
python -m pip install -r requirements.txt
python tools/verify_package.py --coverage
```

This current-package command checks manifest/checksum integrity, declared active schema structures and the example coverage counts. The exact coverage metric is described in COVERAGE_REPORT.md. It does not run a DAW, a singing application or an acoustic comparison. It is not a complete semantic validator.



## OSTF 4.3 musical-intent authoring

### Phrasing

Add a Track Direction with `type="phrasing"`, a unique `id`, a global `start`/`duration` and `parameters`. The parameter object requires `adherence` (`strict` or `preferred`) **and at least one musical property**. `phraseLengthTicks` and `onsetGroupsPerQuarter` are min/max ranges; compare their bounds semantically. Count coincident note attacks as one onset group. `development`, `contour` and `energyShape` describe musical intent, not a direct velocity or gain command. `motifRef` resolves to `phraseLibrary.templates[].id`.

The five development values, six contours and six energy shapes are listed with exact spelling in the reference. `strict` is not permission to rewrite concrete Notes on import. Detect contradictory or overlapping same-kind scopes according to the adopted rules. See examples 02, 03, 09, 20, 26 and 29.

### Vocal Freedom

A `vocalFreedom` Direction refers to an explicit Lyric Voice owned by the same Track. Text policy (`fixed`, `alternatives`, `open`) and melody policy (`fixed`, `ornamentable`, `open`) are independent. `vocalizationKind` distinguishes lexical singing, scat, humming and non-lexical vocalization. Adherence remains explicit.

Only `textPolicy="alternatives"` admits and requires `candidatePhraseSets`; it contains at least two distinct ordered candidate Phrase sequences. Every referenced Phrase belongs to the Voice's Lyric Document. Other text policies must not carry that property. A freedom policy does not invent lyric units, concrete notes, phoneme timing or a voicebank. Fixed text is not fixed melody and fixed melody is not fixed text. See examples 05–08, 15, 19, 26 and 29.

### Ensemble Interactions

`ensembleInteractions` gives a directed actor/partner relationship: `respondTo`, `followRhythm`, `alternateWith`, `leaveSpaceFor`, or `reinforce`. Choose a source range, a Plan/Visit scope, or both. When both are present they intersect rather than overwrite one another. `responseWindowTicks` is a musical bound, not network scheduling or motor-control latency.

Cross-track references resolve to existing Tracks. A same-Track relationship requires two explicit, distinct Lyric Voices owned by that Track; missing or identical voice IDs are not self-response shorthand. Relations do not emit notes or send messages. See examples 12, 21, 24, 26 and 29.

### Performance Requirements

Track `performanceRequirements` can declare required polyphony, a required pitch range, required articulations and peak onset-group density. The object must contain at least one requirement. These are requirements of authored music, **not a declaration that a human, AI or robot can satisfy them**. A capability mismatch is reported rather than silently narrowing the music or executing physical motion.

## Finite performance plans and boundaries

### Plan and Visit authoring

`performancePlans` are opt-in derived traversals of the source timeline. Each Plan has `mode="orderedFinite"`, an explicit `defaultRealization`, and at least one Visit. Visits have contiguous unique zero-based ordinals and choose exactly one of `sourceSectionIds` or `sourceRange`. Do not serialize both selectors. Section labels never substitute for IDs. All selected source spans must resolve.

Parts select existing Tracks once per Visit. `realization` is `fixed`, `open`, or `silent`. Unlisted Track behavior follows the Plan's `defaultRealization`: `fixed`, `silent`, or `unspecified`. The last cannot claim deterministic replay. An explicit Visit `role` can replace conflicting timed `playingRole` Directions only through the appropriate same-Track `replacesDirectionIds`; it cannot replace pitch, phrasing or vocal instructions indiscriminately.

### Mapping the three time domains

Maintain source global time, Clip-local time and derived performance time separately. A source tick appears at each selected occurrence; do not rewrite the source Note's ID or onset merely because the Plan repeats it. A derived occurrence can use a tuple of Plan, Visit, selected segment and source Note identity. Materializing new Core Notes is a separate explicit edit with new identities and provenance.

A source-contiguous fixed segment join is different from a hard cut, non-contiguous jump, repeated range or realization-mode transition. Use [performance time](PERFORMANCE_TIMELINE.md), [cut semantics](NOTE_AND_MIDI_CUT_SEMANTICS.md), and [source occurrence identity](SOURCE_OCCURRENCE_IDENTITIES.md) for the adopted details. Examples 17, 25 and their companion explanations illustrate cut/repetition cases.

### Notes, controller targets and vocal data

Source Notes and their enabled/probability/velocity state remain authoritative. A fixed Plan selects saved material; it does not standardize the random realization of probability or velocity variation. Track/Clip/Note disabled state must not be erased. Hard boundaries truncate surviving gates according to the adopted rules rather than inventing a fresh attack for every intersecting note.

A selected MIDI event is not automatically a selected target Note occurrence. Note-scoped pressure, bend and controller references must be associated with the surviving occurrence; retained descriptors are not evidence of sound. Continuous joins can preserve an eligible gate, whereas a repeated jump starts a different occurrence.

Resolve Voice membership, lyric alignment, phonemes, curves and technique scopes before mapping them into Visits. Partial many-Note alignment is not a complete delivered lyric unit. Note-targeted expression follows the eligible Note gate; Voice/Clip-wide data is not attached to an arbitrary nearby Note. Truncation, omission or approximation during materialized export must be disclosed. S22, S23 and S24 are distinct rule IDs; S13/S14 remain Session rules.

## Distributed Session 0.2

### Separate identity and source pin

A record is a Snapshot or an Event, not a modified Core Score. Both identify the session, source `documentId`, source `revisionId`, finite `performancePlanId` and `scoreSha256`. Hash the actual original Score bytes; do not reserialize, normalize Unicode, change line endings, remove a BOM or hash the ZIP instead. The included examples pin song 22.

A changed Score or revision requires deliberate source reassociation and a new Session; it must not mutate an already pinned Session's history. Production binding and Distributed binding are separately evaluated, even when they name the same Score.

### Participants, capabilities and state

Snapshots declare participants, assignments and the authority participant. Capabilities are descriptive and cannot authorize physical or network activity. Session lifecycle is `prepared`, `playing`, `stopped`. Playing state requires the appropriate position and musical clock information; stopped is terminal under the adopted state-machine rules. Follow the current Schema for the conditional fields.

State-changing accepted events use `baseStateRevision` and `resultStateRevision`, with the result advancing by one. Issuer/authority, revision order, idempotency, duplicate event identity and target allocation are distinct checks. A proposal is not a commitment, and a commitment is not a recording of audible performance.

### All typed events

| Kind | Payload responsibility |
|---|---|
| `phraseProposed` | Proposal ID, target Track, explicit relative MIDI-note phrase |
| `phraseCommitted` | Authority-accepted proposal/Track/phrase data |
| `turnRequested` | Requested Track role and optional Visit |
| `cueIssued` | Cue identity and optional Visit |
| `performanceObserved` | Observed participant, source Track, confidence and optional features |
| `participantStatus` | Participant availability and optional message |
| `sessionStateChanged` | Start, stop, Visit change or assignment change with kind-specific data |

`midi1Notes` phrases carry explicit duration and note timing/pitch/velocity. Notes must fit their phrase. Committed phrases and explicit commitment windows are necessary to make a limited late-join completeness claim; a window does not establish completeness of all history.

### Position and clock

Position ties performance time to a source Visit/tick plus `clockDomainId`, `epochUtc` and uncertainty. Source tempo remains musical authority; the companion does not install a new independent tempo map. Re-entry or Visit changes may require an explicit anchor. Distinguish musical scheduling time, observed wall-clock time and latency uncertainty. A correct timestamp is not proof of WAN synchronization.

See the [Session parameter reference](SESSION_PARAMETER_REFERENCE.md), [state-machine notes](SESSION_STATE_MACHINE.md) and the 18 example records. Do not replay those scenario files as one filename-ordered authoritative log.

## Production Session 0.2.0

### Score, channels and mixer authority

The profile binds the exact Score through `score.sha256`, optional document/revision fields and a descriptive source URI. Channels are `track` (bound to an existing Score Track), `audioTrack` (Production-only audio), `bus`, or `master`. Keep one master and validate acyclic output/send/sidechain routes. `trackId` must not be invented for Production-only channels.

`gainDb`, `pan`, `mute`, `solo` and `soloSafe` are production state, independent from MIDI CC 7/10/11 and Note enabled state. Gain is in dB, pan in -1…1, and mono/stereo is explicit. The portable Solo/source-eligibility rules are defined by the adopted Production specification; they do not guarantee the same proprietary pan law, insert implementation or acoustic result across hosts. Audition state must not delete Score Notes.

### Device chains and assets

`channel.deviceIds` preserves device order. Devices have instrument/effect/utility roles, plugin identity, enabled/bypass state and optional state assets. Supported format labels include VST2, VST3, AU, AAX, CLAP, builtin, host-native and other descriptors; a label is not a binary, installation or license. The `onUnavailable` policy distinguishes reporting/preservation, silence and bypass without pretending audio equivalence.

Asset descriptors carry purpose, URI, exact-byte hash and optional metadata. Audio-source sample rate, frame count and channel count refer to the decoded stream domain, not source ticks. Those fields are restricted by the asset-purpose conditional schema. An absent file is an unavailable asset, not an empty valid file. Synthetic BIN data in the examples is intentionally nonfunctional.

### Audio Regions

A Region identifies a Production audio channel and audio-source asset, placement in source ticks, selected source frames, playback mode, gain, mute and optional fades. `native` and `fit` are distinct; pitch policy is conditional and is not a promise of identical time-stretch algorithms. Frame bounds and tick bounds must be checked independently. Plan projection re-enters the source Region/Automation timeline without mutating the Core or flattening source tempo.

Core `realization="silent"` governs the associated Core material, not an automatic mute for every Production-only recorded audio track. Cross-profile behavior requires an explicit operation and disclosure, not a guessed host session.

### Automation and sidechains

| Target kind | Portable target fields |
|---|---|
| `channel` | `gainDb`, `pan`, `mute` |
| `device` | Explicit `parameterId`, normalized numeric points |
| `deviceControl` | `enabled`, `bypass` |
| `send` | `gainDb`, `enabled` |
| `audioRegion` | `gainDb`, `mute` |

Point ticks are source ticks and must be ordered. Boolean targets use step interpolation; numeric targets use the declared numeric interpolation. Never reinterpret a plugin parameter as MIDI CC. Sidechains name a source channel, target device and input port, tap point, mute-follow policy and gain. They are detector/key paths distinct from audible output routing, not permission to access hardware inputs.

### Host extensions and preservation

Host extensions carry namespaced opaque data. Preserve unsupported state and describe unsupported playback/edit/restore operations separately. A plugin-state byte round trip does not prove successful restoration, and retaining an asset URI does not prove retaining the asset bytes. See the [Production reference](PRODUCTION_PARAMETER_REFERENCE.md), [compatibility notes](PRODUCTION_COMPATIBILITY.md), and examples 01–04.

## Editing, interchange and implementation workflow

1. Identify exact family/version and parse strict JSON without automatic source mutation.
2. Validate structure, build typed ID indexes, resolve references and distinguish malformed data from unsupported interpretation.
3. Establish the explicit operation: read, preview, edit, save, materialize, export, accept a Session event, or rebind a companion. Permissions do not flow from the document text.
4. Preserve unknown data and source bytes when that is part of the claimed operation. Changes to Notes/Clips/Tracks reconcile their dependent lyric, expression, template and reference metadata.
5. Save a new revision deliberately. Score byte changes invalidate old hashes even when musical content is unchanged. Rebind a Production profile only after resolving Track/Region/Plan dependencies; create a new Distributed session when its immutable source changes.
6. Report exact preservation, approximation, omission, unsupported interpretation, unavailable assets and actual execution separately. Do not hide data loss behind a successful parse/save.

### Binding diagnostics

The active decision order is: malformed companion → `INVALID`; unsupported identity → `UNSUPPORTED`; incomplete authorized candidate enumeration/required retrieval → `NOT_EVALUATED`; complete scope with zero candidates → `MISSING`; candidates but no byte-hash match → `MISMATCH`; matched invalid Score → Score-format error; unresolved required referents → `AMBIGUOUS` with details; unique resolved required referents → `RESOLVED`.

These are **implementation diagnostics**, not added JSON properties. Report the evaluated authorization boundary. Identical byte copies are one identity; a filename, URL or cached digest is not retrieved bytes. Narrowing a failed candidate set is a new explicitly disclosed assessment. Source resolution never proves rights, execution, acoustic reproduction or physical safety.

## Publication, coverage and local tools

This repository contains 100 files. Manuals, all current references, all examples and required illustrative assets are included. The ZIP is a distribution envelope, not a standardized session/project archive format.

The [coverage report](COVERAGE_REPORT.md) links 842 reachable parameter declarations, 328 enum literals and 53 positive union branches to actual sample JSON pointers. It does not exhaust unbounded values or all combinations. No schema constraint has been relaxed to make a sample fit.

```bash
python tools/verify_package.py
python -m pip install -r requirements.txt
python tools/verify_package.py --coverage
python tools/validate.py examples/26-complete-authoring.ostf
python tools/validate.py --session --pinned-ostf examples/22-pinned-session-aaba.ostf examples/session/03-snapshot-02.json
python tools/validate_production_profile.py examples/production/04-complete-production-02.json --score examples/22-pinned-session-aaba.ostf
```

The package checker verifies file inventories and byte hashes; optional coverage mode reproduces the coverage counts. Authoring tools cover selected semantic constraints only. Their success is not a full independent implementation, legal audit, DAW/plugin/vocal/WAN test or robot certification.

Publication is publisher-approved as a **written format specification**, with the explicitly excluded runtime and independent checks left unperformed. Third-party rights and any actual product claims remain separate responsibilities.
