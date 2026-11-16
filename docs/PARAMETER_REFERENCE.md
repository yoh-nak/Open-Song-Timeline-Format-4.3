# OSTF 4.3 Core — Complete Parameter Reference / 全項目リファレンス

**Release edition: 4.3.0 · 2026-11-16.** No wire-format fields are added by this reference.

Authoritative structure: [`ostf-4.3.0.schema.json`](../schema/ostf-4.3.0.schema.json). SHA-256: `72bf44666b42a760c883fbfa87e1da891467768032ee8e96fbee9fb47f673fc7`.

全てのルート項目・`$defs`・入れ子の旧形式定義・条件付き制約を掲載します。型、必須条件、列挙値、数値範囲、既定値、参照先を原Schemaから転記し、収録サンプルのファイル名とJSON Pointerを対応付けています。条件分岐の必須性は、その分岐が適用される場合の条件です。省略可能な値を保存時に勝手に補完する意味ではありません。

The exact schema blocks preserve every validation keyword. Historical Draft labels inside the frozen schema annotations do not alter the adopted release version; see [edition and authority guide](RELEASE_READINESS.md). No execution, asset retrieval or synthesis permission follows from valid data.

**Coverage:** 646/646 reachable parameter declarations; 263/263 enum literals; 37/37 positive union branches. [Detailed coverage](COVERAGE_REPORT.md).

## Definition index / 定義索引

- [Root](#def-)
- [id](#def-defs-id)
- [nonnegative](#def-defs-nonnegative)
- [positive](#def-defs-positive)
- [signed](#def-defs-signed)
- [pitch](#def-defs-pitch)
- [ref](#def-defs-ref)
- [range](#def-defs-range)
- [spelledPitchClass](#def-defs-spelledpitchclass)
- [song](#def-defs-song)
- [section](#def-defs-section)
- [tempo](#def-defs-tempo)
- [meter](#def-defs-meter)
- [timeline](#def-defs-timeline)
- [chord](#def-defs-chord)
- [scale](#def-defs-scale)
- [harmony](#def-defs-harmony)
- [instrument](#def-defs-instrument)
- [note](#def-defs-note)
- [clip](#def-defs-clip)
- [track](#def-defs-track)
- [soundSlot](#def-defs-soundslot)
- [lyricDocument](#def-defs-lyricdocument)
- [lyricPhrase](#def-defs-lyricphrase)
- [lyricUnit](#def-defs-lyricunit)
- [lyricAlignment](#def-defs-lyricalignment)
- [lyrics](#def-defs-lyrics)
- [sha256](#def-defs-sha256)
- [resource](#def-defs-resource)
- [dependencies](#def-defs-dependencies)
- [relativeAssignment](#def-defs-relativeassignment)
- [generator](#def-defs-generator)
- [generationInput](#def-defs-generationinput)
- [generationProcess](#def-defs-generationprocess)
- [color](#def-defs-color)
- [roleDefinition](#def-defs-roledefinition)
- [roleColorMap](#def-defs-rolecolormap)
- [customRoleColorMap](#def-defs-customrolecolormap)
- [objectColor](#def-defs-objectcolor)
- [phraseTemplate](#def-defs-phrasetemplate)
- [phraseNoteMapping](#def-defs-phrasenotemapping)
- [phraseInstance](#def-defs-phraseinstance)
- [clipCandidate](#def-defs-clipcandidate)
- [clipChoiceGroup](#def-defs-clipchoicegroup)
- [midiMapping](#def-defs-midimapping)
- [soundSource](#def-defs-soundsource)
- [localizedNames](#def-defs-localizednames)
- [drumKit](#def-defs-drumkit)
- [voicing](#def-defs-voicing)
- [contributor](#def-defs-contributor)
- [credit](#def-defs-credit)
- [alternateTitle](#def-defs-alternatetitle)
- [languageMap32](#def-defs-languagemap32)
- [localizationTarget](#def-defs-localizationtarget)
- [localizationEntry](#def-defs-localizationentry)
- [genre](#def-defs-genre)
- [legacy33](#def-defs-legacy33) — definition container
- [legacy33.id](#def-defs-legacy33-defs-id)
- [legacy33.nonnegative](#def-defs-legacy33-defs-nonnegative)
- [legacy33.positive](#def-defs-legacy33-defs-positive)
- [legacy33.signed](#def-defs-legacy33-defs-signed)
- [legacy33.pitch](#def-defs-legacy33-defs-pitch)
- [legacy33.ref](#def-defs-legacy33-defs-ref)
- [legacy33.range](#def-defs-legacy33-defs-range)
- [legacy33.spelledPitchClass](#def-defs-legacy33-defs-spelledpitchclass)
- [legacy33.song](#def-defs-legacy33-defs-song)
- [legacy33.section](#def-defs-legacy33-defs-section)
- [legacy33.tempo](#def-defs-legacy33-defs-tempo)
- [legacy33.meter](#def-defs-legacy33-defs-meter)
- [legacy33.timeline](#def-defs-legacy33-defs-timeline)
- [legacy33.chord](#def-defs-legacy33-defs-chord)
- [legacy33.scale](#def-defs-legacy33-defs-scale)
- [legacy33.harmony](#def-defs-legacy33-defs-harmony)
- [legacy33.instrument](#def-defs-legacy33-defs-instrument)
- [legacy33.note](#def-defs-legacy33-defs-note)
- [legacy33.clip](#def-defs-legacy33-defs-clip)
- [legacy33.track](#def-defs-legacy33-defs-track)
- [legacy33.soundSlot](#def-defs-legacy33-defs-soundslot)
- [legacy33.lyricDocument](#def-defs-legacy33-defs-lyricdocument)
- [legacy33.lyricPhrase](#def-defs-legacy33-defs-lyricphrase)
- [legacy33.lyricUnit](#def-defs-legacy33-defs-lyricunit)
- [legacy33.lyricAlignment](#def-defs-legacy33-defs-lyricalignment)
- [legacy33.lyrics](#def-defs-legacy33-defs-lyrics)
- [legacy33.sha256](#def-defs-legacy33-defs-sha256)
- [legacy33.resource](#def-defs-legacy33-defs-resource)
- [legacy33.dependencies](#def-defs-legacy33-defs-dependencies)
- [legacy33.extension](#def-defs-legacy33-defs-extension)
- [legacy33.relativeAssignment](#def-defs-legacy33-defs-relativeassignment)
- [legacy33.relativeData](#def-defs-legacy33-defs-relativedata)
- [legacy33.generator](#def-defs-legacy33-defs-generator)
- [legacy33.generationInput](#def-defs-legacy33-defs-generationinput)
- [legacy33.generationProcess](#def-defs-legacy33-defs-generationprocess)
- [legacy33.generationData](#def-defs-legacy33-defs-generationdata)
- [legacy33.color](#def-defs-legacy33-defs-color)
- [legacy33.roleDefinition](#def-defs-legacy33-defs-roledefinition)
- [legacy33.roleColorMap](#def-defs-legacy33-defs-rolecolormap)
- [legacy33.customRoleColorMap](#def-defs-legacy33-defs-customrolecolormap)
- [legacy33.objectColor](#def-defs-legacy33-defs-objectcolor)
- [legacy33.appearanceData](#def-defs-legacy33-defs-appearancedata)
- [legacy33.legacyData](#def-defs-legacy33-defs-legacydata)
- [legacy33.extensions](#def-defs-legacy33-defs-extensions)
- [legacy33.phraseTemplate](#def-defs-legacy33-defs-phrasetemplate)
- [legacy33.phraseNoteMapping](#def-defs-legacy33-defs-phrasenotemapping)
- [legacy33.phraseInstance](#def-defs-legacy33-defs-phraseinstance)
- [legacy33.phraseLibraryData](#def-defs-legacy33-defs-phraselibrarydata)
- [legacy33.clipCandidate](#def-defs-legacy33-defs-clipcandidate)
- [legacy33.clipChoiceGroup](#def-defs-legacy33-defs-clipchoicegroup)
- [legacy33.clipChoicesData](#def-defs-legacy33-defs-clipchoicesdata)
- [legacy33.midiMapping](#def-defs-legacy33-defs-midimapping)
- [legacy33.soundSource](#def-defs-legacy33-defs-soundsource)
- [legacy33.localizedNames](#def-defs-legacy33-defs-localizednames)
- [legacy33.drumKit](#def-defs-legacy33-defs-drumkit)
- [legacy33.phraseSourceNote](#def-defs-legacy33-defs-phrasesourcenote)
- [legacy33.voicing](#def-defs-legacy33-defs-voicing)
- [legacy33.contributor](#def-defs-legacy33-defs-contributor)
- [legacy33.credit](#def-defs-legacy33-defs-credit)
- [legacy33.alternateTitle](#def-defs-legacy33-defs-alternatetitle)
- [legacy33.languageMap32](#def-defs-legacy33-defs-languagemap32)
- [legacy33.localizationTarget](#def-defs-legacy33-defs-localizationtarget)
- [legacy33.localizationEntry](#def-defs-legacy33-defs-localizationentry)
- [legacy33.localizationData](#def-defs-legacy33-defs-localizationdata)
- [legacy33.genre](#def-defs-legacy33-defs-genre)
- [opaqueDocumentId](#def-defs-opaquedocumentid)
- [revisionRef](#def-defs-revisionref)
- [software](#def-defs-software)
- [documentInfo](#def-defs-documentinfo)
- [key](#def-defs-key)
- [keyChange](#def-defs-keychange)
- [scaleDefinition](#def-defs-scaledefinition)
- [scaleTarget](#def-defs-scaletarget)
- [mood](#def-defs-mood)
- [rightsStatement](#def-defs-rightsstatement)
- [grooveIntent](#def-defs-grooveintent)
- [generationIntent](#def-defs-generationintent)
- [relativePhrases](#def-defs-relativephrases)
- [generation](#def-defs-generation)
- [presentation](#def-defs-presentation)
- [phraseLibrary](#def-defs-phraselibrary)
- [clipChoices](#def-defs-clipchoices)
- [localization](#def-defs-localization)
- [corePhraseSourceNote](#def-defs-corephrasesourcenote)
- [provenanceSource](#def-defs-provenancesource)
- [provenanceRecord](#def-defs-provenancerecord)
- [provenance](#def-defs-provenance)
- [midiChannel](#def-defs-midichannel)
- [midiBus](#def-defs-midibus)
- [midi](#def-defs-midi)
- [mpeSettings](#def-defs-mpesettings)
- [trackMidi](#def-defs-trackmidi)
- [controlChangeEvent](#def-defs-controlchangeevent)
- [channelModeEvent](#def-defs-channelmodeevent)
- [programChangeEvent](#def-defs-programchangeevent)
- [pitchBendEvent](#def-defs-pitchbendevent)
- [channelPressureEvent](#def-defs-channelpressureevent)
- [polyPressureEvent](#def-defs-polypressureevent)
- [midiEvent](#def-defs-midievent)
- [lyricVoice](#def-defs-lyricvoice)
- [playablePitchRange](#def-defs-playablepitchrange)
- [directionPitchCollection](#def-defs-directionpitchcollection)
- [directionPitchSource](#def-defs-directionpitchsource)
- [improvisationDirectionParameters](#def-defs-improvisationdirectionparameters)
- [playingRoleDirectionParameters](#def-defs-playingroledirectionparameters)
- [pitchRangeDirectionParameters](#def-defs-pitchrangedirectionparameters)
- [vendorDirectionParameters](#def-defs-vendordirectionparameters)
- [improvisationDirection](#def-defs-improvisationdirection)
- [playingRoleDirection](#def-defs-playingroledirection)
- [pitchRangeDirection](#def-defs-pitchrangedirection)
- [vendorRangeDirection](#def-defs-vendorrangedirection)
- [vendorPointDirection](#def-defs-vendorpointdirection)
- [trackDirection](#def-defs-trackdirection)
- [vocalPhonetics](#def-defs-vocalphonetics)
- [vocalProfile](#def-defs-vocalprofile)
- [vocalPerformance](#def-defs-vocalperformance)
- [vocalPhonemeEvent](#def-defs-vocalphonemeevent)
- [vocalCurvePointPitch](#def-defs-vocalcurvepointpitch)
- [vocalCurvePointNormalized](#def-defs-vocalcurvepointnormalized)
- [vocalPitchCurve](#def-defs-vocalpitchcurve)
- [vocalExpressionCurve](#def-defs-vocalexpressioncurve)
- [vocalTechnique](#def-defs-vocaltechnique)
- [vocalBreathEvent](#def-defs-vocalbreathevent)
- [positiveIntRange](#def-defs-positiveintrange)
- [nonnegativeNumberRange](#def-defs-nonnegativenumberrange)
- [phrasingDirectionParameters](#def-defs-phrasingdirectionparameters)
- [phrasingDirection](#def-defs-phrasingdirection)
- [lyricCandidateSet](#def-defs-lyriccandidateset)
- [vocalFreedomDirectionParameters](#def-defs-vocalfreedomdirectionparameters)
- [vocalFreedomDirection](#def-defs-vocalfreedomdirection)
- [performanceRequirements](#def-defs-performancerequirements)
- [performanceScope](#def-defs-performancescope)
- [ensembleInteraction](#def-defs-ensembleinteraction)
- [visitPart](#def-defs-visitpart)
- [performanceVisit](#def-defs-performancevisit)
- [performancePlan](#def-defs-performanceplan)

<a id="def-"></a>
## Root

**Schema pointer:** `#`. Reachable from release root / 公開ルートから到達可能。

Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.

### Root — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `format` | Yes / 必須 | `"OSTF"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/format` |
| `version` | Yes / 必須 | `"4.3.0"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/version` |
| `ppq` | Yes / 必須 | integer | minimum=1; maximum=960000 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/ppq` |
| `song` | Yes / 必須 | [song](#def-defs-song) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/song` |
| `timeline` | Yes / 必須 | [timeline](#def-defs-timeline) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline` |
| `harmony` | Yes / 必須 | [harmony](#def-defs-harmony) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/harmony` |
| `tracks` | Yes / 必須 | array | items: track | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/tracks` |
| `soundSlots` | Yes / 必須 | array | items: soundSlot | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/soundSlots` |
| `lyrics` | Yes / 必須 | [lyrics](#def-defs-lyrics) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/lyrics` |
| `resources` | Yes / 必須 | array | items: resource | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/resources` |
| `extensions` | Optional / 任意（条件付きの場合あり） | [extensions](#def-defs-legacy33-defs-extensions) | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here. | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions` |
| `drumKits` | Optional / 任意（条件付きの場合あり） | array | items: drumKit; Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/drumKits` |
| `contributors` | Optional / 任意（条件付きの場合あり） | array | items: contributor; Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/contributors` |
| `document` | Optional / 任意（条件付きの場合あり） | [documentInfo](#def-defs-documentinfo) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document` |
| `relativePhrases` | Optional / 任意（条件付きの場合あり） | [relativePhrases](#def-defs-relativephrases) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases` |
| `generation` | Optional / 任意（条件付きの場合あり） | [generation](#def-defs-generation) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation` |
| `presentation` | Optional / 任意（条件付きの場合あり） | [presentation](#def-defs-presentation) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation` |
| `phraseLibrary` | Optional / 任意（条件付きの場合あり） | [phraseLibrary](#def-defs-phraselibrary) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary` |
| `clipChoices` | Optional / 任意（条件付きの場合あり） | [clipChoices](#def-defs-clipchoices) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices` |
| `localization` | Optional / 任意（条件付きの場合あり） | [localization](#def-defs-localization) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization` |
| `provenance` | Optional / 任意（条件付きの場合あり） | [provenance](#def-defs-provenance) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance` |
| `midi` | Optional / 任意（条件付きの場合あり） | [midi](#def-defs-midi) | Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/midi` |
| `ensembleInteractions` | Optional / 任意（条件付きの場合あり） | array | items: ensembleInteraction; Optional directed music relationships; these neither materialize notes nor initiate network messages. | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions` |
| `performancePlans` | Optional / 任意（条件付きの場合あり） | array | items: performancePlan; Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes. | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-4.3.0.schema.json",
  "title": "Open Song Timeline Format (OSTF) 4.3.0 — Draft 0.4 editorial candidate",
  "description": "Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.",
  "$comment": "Draft 0.4. Full 4.2.0 Core inherited from published SHA-verified baseline. Added optional phrasing, vocalFreedom, ensembleInteractions, performancePlans and performanceRequirements only. Source-cut realization and session-event meanings are in docs/SPECIFICATION.md; independent remote Session Profile is not part of .ostf.",
  "type": "object",
  "properties": {
    "format": {
      "const": "OSTF"
    },
    "version": {
      "const": "4.3.0"
    },
    "ppq": {
      "type": "integer",
      "minimum": 1,
      "maximum": 960000
    },
    "song": {
      "$ref": "#/$defs/song"
    },
    "timeline": {
      "$ref": "#/$defs/timeline"
    },
    "harmony": {
      "$ref": "#/$defs/harmony"
    },
    "tracks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/track"
      }
    },
    "soundSlots": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/soundSlot"
      }
    },
    "lyrics": {
      "$ref": "#/$defs/lyrics"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "extensions": {
      "$ref": "#/$defs/legacy33/$defs/extensions",
      "description": "Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here."
    },
    "drumKits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/drumKit"
      },
      "description": "Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible)."
    },
    "contributors": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/contributor"
      },
      "description": "Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format."
    },
    "document": {
      "$ref": "#/$defs/documentInfo"
    },
    "relativePhrases": {
      "$ref": "#/$defs/relativePhrases"
    },
    "generation": {
      "$ref": "#/$defs/generation"
    },
    "presentation": {
      "$ref": "#/$defs/presentation"
    },
    "phraseLibrary": {
      "$ref": "#/$defs/phraseLibrary"
    },
    "clipChoices": {
      "$ref": "#/$defs/clipChoices"
    },
    "localization": {
      "$ref": "#/$defs/localization"
    },
    "provenance": {
      "$ref": "#/$defs/provenance"
    },
    "midi": {
      "$ref": "#/$defs/midi",
      "description": "Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded."
    },
    "ensembleInteractions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ensembleInteraction"
      },
      "description": "Optional directed music relationships; these neither materialize notes nor initiate network messages."
    },
    "performancePlans": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performancePlan"
      },
      "description": "Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes."
    }
  },
  "required": [
    "format",
    "version",
    "ppq",
    "song",
    "timeline",
    "harmony",
    "tracks",
    "soundSlots",
    "lyrics",
    "resources"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-id"></a>
## id

**Schema pointer:** `#/$defs/id`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-nonnegative"></a>
## nonnegative

**Schema pointer:** `#/$defs/nonnegative`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```


<a id="def-defs-positive"></a>
## positive

**Schema pointer:** `#/$defs/positive`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```


<a id="def-defs-signed"></a>
## signed

**Schema pointer:** `#/$defs/signed`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```


<a id="def-defs-pitch"></a>
## pitch

**Schema pointer:** `#/$defs/pitch`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```


<a id="def-defs-ref"></a>
## ref

**Schema pointer:** `#/$defs/ref`. Reachable from release root / 公開ルートから到達可能。

### ref — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | enum | enum=["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre","contributor","credit","alternateTitle","mood","keyChange","phraseTemplate","phraseInstance","clipChoiceGroup","clipCandidate","roleDefinition","generationProcess","provenanceRecord","midiBus","midiEvent","lyricVoice","trackDirection","ensembleInteraction","performancePlan","performanceVisit"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/dependencies/refs/0/type` |
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/dependencies/refs/0/id` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre",
        "contributor",
        "credit",
        "alternateTitle",
        "mood",
        "keyChange",
        "phraseTemplate",
        "phraseInstance",
        "clipChoiceGroup",
        "clipCandidate",
        "roleDefinition",
        "generationProcess",
        "provenanceRecord",
        "midiBus",
        "midiEvent",
        "lyricVoice",
        "trackDirection",
        "ensembleInteraction",
        "performancePlan",
        "performanceVisit"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-range"></a>
## range

**Schema pointer:** `#/$defs/range`. Reachable from release root / 公開ルートから到達可能。

### range — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/targetRange/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/targetRange/duration` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-spelledpitchclass"></a>
## spelledPitchClass

**Schema pointer:** `#/$defs/spelledPitchClass`. Reachable from release root / 公開ルートから到達可能。

### spelledPitchClass — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `step` | Yes / 必須 | enum | enum=["A","B","C","D","E","F","G"] | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key/tonic/step` |
| `alter` | Yes / 必須 | integer | minimum=-2; maximum=2 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key/tonic/alter` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-song"></a>
## song

**Schema pointer:** `#/$defs/song`. Reachable from release root / 公開ルートから到達可能。

### song — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `title` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/song/title` |
| `primaryMelodyTrackId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/primaryMelodyTrackId` |
| `localizedTitles` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized song-title alternatives. song.title is the stable fallback. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/localizedTitles` |
| `subtitle` | Optional / 任意（条件付きの場合あり） | string | Optional original-language subtitle. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/subtitle` |
| `description` | Optional / 任意（条件付きの場合あり） | string | Optional original-language description, including Unicode and line breaks. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/description` |
| `alternateTitles` | Optional / 任意（条件付きの場合あり） | array | items: alternateTitle; Additional stable-ID source-language titles. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/alternateTitles` |
| `credits` | Optional / 任意（条件付きの場合あり） | array | items: credit; Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/credits` |
| `genres` | Optional / 任意（条件付きの場合あり） | array | items: genre; Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/genres` |
| `key` | Optional / 任意（条件付きの場合あり） | [key](#def-defs-key) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key` |
| `scale` | Optional / 任意（条件付きの場合あり） | [scaleDefinition](#def-defs-scaledefinition) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/scale` |
| `languages` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: string | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/languages` |
| `primaryLyricDocumentId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/primaryLyricDocumentId` |
| `moods` | Optional / 任意（条件付きの場合あり） | array | items: mood | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/moods` |
| `rights` | Optional / 任意（条件付きの場合あり） | [rightsStatement](#def-defs-rightsstatement) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/rights` |
| `melodyTrackIds` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: id; Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/melodyTrackIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "scale": {
      "$ref": "#/$defs/scaleDefinition"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
      },
      "uniqueItems": true
    },
    "primaryLyricDocumentId": {
      "$ref": "#/$defs/id"
    },
    "moods": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/mood"
      }
    },
    "rights": {
      "$ref": "#/$defs/rightsStatement"
    },
    "melodyTrackIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-section"></a>
## section

**Schema pointer:** `#/$defs/section`. Reachable from release root / 公開ルートから到達可能。

### section — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/sections/0/id` |
| `name` | Yes / 必須 | string | minLength=1 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/sections/0/name` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/sections/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/sections/0/duration` |
| `role` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/timeline/sections/0/role` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/sections/0/localizedNames` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-tempo"></a>
## tempo

**Schema pointer:** `#/$defs/tempo`. Reachable from release root / 公開ルートから到達可能。

### tempo — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/tempoChanges/0/at` |
| `bpm` | Yes / 必須 | number | maximum=1000; exclusiveMinimum=0 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/tempoChanges/0/bpm` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-meter"></a>
## meter

**Schema pointer:** `#/$defs/meter`. Reachable from release root / 公開ルートから到達可能。

### meter — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/meterChanges/0/at` |
| `numerator` | Yes / 必須 | integer | minimum=1; maximum=64 | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/meterChanges/0/numerator` |
| `denominator` | Yes / 必須 | enum | enum=[1,2,4,8,16,32,64] | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/meterChanges/0/denominator` |
| `beatGroups` | Optional / 任意（条件付きの場合あり） | array | minItems=1; maxItems=64; items: integer; Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/meterChanges/0/beatGroups` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    },
    "beatGroups": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 64
      },
      "minItems": 1,
      "maxItems": 64,
      "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-timeline"></a>
## timeline

**Schema pointer:** `#/$defs/timeline`. Reachable from release root / 公開ルートから到達可能。

### timeline — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `sections` | Yes / 必須 | array | items: section | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/sections` |
| `tempoChanges` | Yes / 必須 | array | minItems=1; items: tempo | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/tempoChanges` |
| `meterChanges` | Yes / 必須 | array | minItems=1; items: meter | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/timeline/meterChanges` |
| `keyChanges` | Optional / 任意（条件付きの場合あり） | array | items: keyChange | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/keyChanges` |
| `duration` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/timeline/duration` |
| `barOrigin` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/barOrigin` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/meter"
      },
      "minItems": 1
    },
    "keyChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/keyChange"
      }
    },
    "duration": {
      "$ref": "#/$defs/nonnegative"
    },
    "barOrigin": {
      "$ref": "#/$defs/nonnegative"
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-chord"></a>
## chord

**Schema pointer:** `#/$defs/chord`. Reachable from release root / 公開ルートから到達可能。

### chord — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/duration` |
| `label` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/label` |
| `root` | Optional / 任意（条件付きの場合あり） | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/root` |
| `intervals` | Optional / 任意（条件付きの場合あり） | array | minItems=1; maxItems=36; uniqueItems=true; items: integer | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/harmony/chords/0/intervals` |
| `bass` | Optional / 任意（条件付きの場合あり） | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/chords/0/bass` |
| `voicing` | Optional / 任意（条件付きの場合あり） | [voicing](#def-defs-voicing) | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/chords/0/voicing` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```


<a id="def-defs-scale"></a>
## scale

**Schema pointer:** `#/$defs/scale`. Reachable from release root / 公開ルートから到達可能。

### scale — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/label` |
| `tonic` | Yes / 必須 | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/tonic` |
| `intervals` | Yes / 必須 | array | minItems=1; maxItems=12; uniqueItems=true; items: integer | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/intervals` |
| `targets` | Optional / 任意（条件付きの場合あり） | array | minItems=1; uniqueItems=true; items: scaleTarget; Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/targets` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scaleTarget"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-harmony"></a>
## harmony

**Schema pointer:** `#/$defs/harmony`. Reachable from release root / 公開ルートから到達可能。

### harmony — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `chords` | Yes / 必須 | array | items: chord | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/harmony/chords` |
| `scales` | Yes / 必須 | array | items: scale | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/harmony/scales` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-instrument"></a>
## instrument

**Schema pointer:** `#/$defs/instrument`. Reachable from release root / 公開ルートから到達可能。

### instrument — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/instrument/name` |
| `family` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/instrument/family` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/instrument/localizedNames` |
| `playablePitchRange` | Optional / 任意（条件付きの場合あり） | [playablePitchRange](#def-defs-playablepitchrange) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/instrument/playablePitchRange` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "playablePitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-note"></a>
## note

**Schema pointer:** `#/$defs/note`. Reachable from release root / 公開ルートから到達可能。

Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.

### note — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes/0/duration` |
| `pitch` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes/0/pitch` |
| `soundSlotId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/2/clips/0/notes/0/soundSlotId` |
| `velocity` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes/0/velocity` |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true; Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/notes/0/enabled` |
| `releaseVelocity` | Optional / 任意（条件付きの場合あり） | integer | minimum=0; maximum=127; Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/notes/0/releaseVelocity` |
| `probability` | Optional / 任意（条件付きの場合あり） | number | minimum=0; maximum=1; default=1; Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. | [25-source-note-repeated-visits.ostf](../examples/25-source-note-repeated-visits.ostf)<br>`/tracks/0/clips/0/notes/0/probability` |
| `velocityDeviation` | Optional / 任意（条件付きの場合あり） | integer | minimum=-126; maximum=126; default=0; Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. | [25-source-note-repeated-visits.ostf](../examples/25-source-note-repeated-visits.ostf)<br>`/tracks/0/clips/0/notes/0/velocityDeviation` |
| `pitchRole` | Optional / 任意（条件付きの場合あり） | enum | enum=["musical","fixedTrigger"]; default="musical"; Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/notes/0/pitchRole` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/notes/0/channel` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel",
      "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-clip"></a>
## clip

**Schema pointer:** `#/$defs/clip`. Reachable from release root / 公開ルートから到達可能。

### clip — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/id` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/name` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/duration` |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/enabled` |
| `notes` | Yes / 必須 | array | items: note | [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf)<br>`/tracks/0/clips/0/notes` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/localizedNames` |
| `midiEvents` | Optional / 任意（条件付きの場合あり） | array | items: midiEvent; Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]. | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents` |
| `vocalPerformances` | Optional / 任意（条件付きの場合あり） | array | minItems=1; items: vocalPerformance; Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback. | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "midiEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiEvent"
      },
      "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
    },
    "vocalPerformances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPerformance"
      },
      "minItems": 1,
      "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-track"></a>
## track

**Schema pointer:** `#/$defs/track`. Reachable from release root / 公開ルートから到達可能。

### track — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/id` |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/name` |
| `role` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/role` |
| `instrument` | Optional / 任意（条件付きの場合あり） | [instrument](#def-defs-instrument) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/instrument` |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/enabled` |
| `clips` | Yes / 必須 | array | items: clip | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/clips` |
| `trackType` | Optional / 任意（条件付きの場合あり） | enum | enum=["melodic","drum","mixed"]; Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/trackType` |
| `preferredView` | Optional / 任意（条件付きの場合あり） | enum | enum=["auto","pianoRoll","drumGrid"]; default="auto"; Non-binding presentation preference. Does not change note meaning. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/2/preferredView` |
| `soundSource` | Optional / 任意（条件付きの場合あり） | [soundSource](#def-defs-soundsource) | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/soundSource` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/localizedNames` |
| `drumKitId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/2/drumKitId` |
| `midi` | Optional / 任意（条件付きの場合あり） | [trackMidi](#def-defs-trackmidi) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/midi` |
| `directions` | Optional / 任意（条件付きの場合あり） | array | items: trackDirection; Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline. | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions` |
| `performanceRequirements` | Optional / 任意（条件付きの場合あり） | [performanceRequirements](#def-defs-performancerequirements) | Portable requirements for realizing this track, not a robot/device capability report. | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    },
    "midi": {
      "$ref": "#/$defs/trackMidi"
    },
    "directions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/trackDirection"
      },
      "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
    },
    "performanceRequirements": {
      "$ref": "#/$defs/performanceRequirements",
      "description": "Portable requirements for realizing this track, not a robot/device capability report."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-soundslot"></a>
## soundSlot

**Schema pointer:** `#/$defs/soundSlot`. Reachable from release root / 公開ルートから到達可能。

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

### soundSlot — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/id` |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/name` |
| `role` | Optional / 任意（条件付きの場合あり） | string | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/soundSlots/0/role` |
| `midiNote` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-pitch) | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/soundSlots/0/midiNote` |
| `midiMapping` | Optional / 任意（条件付きの場合あり） | [midiMapping](#def-defs-midimapping) | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/midiMapping` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/soundSlots/0/localizedNames` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```


<a id="def-defs-lyricdocument"></a>
## lyricDocument

**Schema pointer:** `#/$defs/lyricDocument`. Reachable from release root / 公開ルートから到達可能。

### lyricDocument — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/documents/0/id` |
| `title` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/documents/0/title` |
| `language` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/lyrics/documents/0/language` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-lyricphrase"></a>
## lyricPhrase

**Schema pointer:** `#/$defs/lyricPhrase`. Reachable from release root / 公開ルートから到達可能。

### lyricPhrase — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf)<br>`/lyrics/phrases/0/id` |
| `documentId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf)<br>`/lyrics/phrases/0/documentId` |
| `text` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf)<br>`/lyrics/phrases/0/text` |
| `pronunciation` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/phrases/0/pronunciation` |
| `start` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/phrases/0/start` |
| `duration` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/phrases/0/duration` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```


<a id="def-defs-lyricunit"></a>
## lyricUnit

**Schema pointer:** `#/$defs/lyricUnit`. Reachable from release root / 公開ルートから到達可能。

### lyricUnit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/units/0/id` |
| `phraseId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/units/0/phraseId` |
| `text` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/units/0/text` |
| `pronunciation` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/pronunciation` |
| `start` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/start` |
| `duration` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/duration` |
| `phonetics` | Optional / 任意（条件付きの場合あり） | array | minItems=1; items: vocalPhonetics; Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "phonetics": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonetics"
      },
      "minItems": 1,
      "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```


<a id="def-defs-lyricalignment"></a>
## lyricAlignment

**Schema pointer:** `#/$defs/lyricAlignment`. Reachable from release root / 公開ルートから到達可能。

### lyricAlignment — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/alignments/0/id` |
| `unitIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/alignments/0/unitIds` |
| `noteIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/alignments/0/noteIds` |
| `voiceId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track. | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/lyrics/alignments/0/voiceId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "voiceId": {
      "$ref": "#/$defs/id",
      "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-lyrics"></a>
## lyrics

**Schema pointer:** `#/$defs/lyrics`. Reachable from release root / 公開ルートから到達可能。

### lyrics — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `documents` | Yes / 必須 | array | items: lyricDocument | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/lyrics/documents` |
| `phrases` | Yes / 必須 | array | items: lyricPhrase | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/lyrics/phrases` |
| `units` | Yes / 必須 | array | items: lyricUnit | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/lyrics/units` |
| `alignments` | Yes / 必須 | array | items: lyricAlignment | [01-minimal.ostf](../examples/01-minimal.ostf)<br>`/lyrics/alignments` |
| `voices` | Optional / 任意（条件付きの場合あり） | array | items: lyricVoice; Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics. | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/voices` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricAlignment"
      }
    },
    "voices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricVoice"
      },
      "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-sha256"></a>
## sha256

**Schema pointer:** `#/$defs/sha256`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-resource"></a>
## resource

**Schema pointer:** `#/$defs/resource`. Reachable from release root / 公開ルートから到達可能。

### resource — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/resources/0/id` |
| `kind` | Yes / 必須 | enum | enum=["audio","midi","text","other"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/resources/0/kind` |
| `uri` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/resources/0/uri` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/resources/0/name` |
| `sha256` | Optional / 任意（条件付きの場合あり） | [sha256](#def-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/resources/0/sha256` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-dependencies"></a>
## dependencies

**Schema pointer:** `#/$defs/dependencies`. Reachable from release root / 公開ルートから到達可能。

### dependencies/oneOf/0 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `scope` | Yes / 必須 | enum | enum=["document","none"] | [20-phrasing-with-motif-reference.ostf](../examples/20-phrasing-with-motif-reference.ostf)<br>`/phraseLibrary/dependencies/scope` |

### dependencies/oneOf/1 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `scope` | Yes / 必須 | `"objects"` (const) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/dependencies/scope` |
| `refs` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: ref | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/dependencies/refs` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```


<a id="def-defs-relativeassignment"></a>
## relativeAssignment

**Schema pointer:** `#/$defs/relativeAssignment`. Reachable from release root / 公開ルートから到達可能。

### relativeAssignment — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `noteId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/noteId` |
| `basis` | Yes / 必須 | enum | enum=["chordTone","scaleDegree"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/basis` |
| `contextId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/contextId` |
| `anchorPitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/anchorPitch` |
| `index` | Yes / 必須 | integer | minimum=1; maximum=36 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/index` |
| `chromaticOffset` | Yes / 必須 | integer | minimum=-24; maximum=24 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments/0/chromaticOffset` |

### relativeAssignment/allOf/0/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `index` | Optional / 任意（条件付きの場合あり） | unconstrained / 制限なし | maximum=12 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/relativePhrases/assignments/1/index` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```


<a id="def-defs-generator"></a>
## generator

**Schema pointer:** `#/$defs/generator`. Reachable from release root / 公開ルートから到達可能。

### generator — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/generator/id` |
| `version` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/generator/version` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-generationinput"></a>
## generationInput

**Schema pointer:** `#/$defs/generationInput`. Reachable from release root / 公開ルートから到達可能。

### generationInput — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `role` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/inputs/0/role` |
| `ref` | Yes / 必須 | [ref](#def-defs-ref) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/inputs/0/ref` |
| `readRange` | Optional / 任意（条件付きの場合あり） | [range](#def-defs-range) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/inputs/0/readRange` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-generationprocess"></a>
## generationProcess

**Schema pointer:** `#/$defs/generationProcess`. Reachable from release root / 公開ルートから到達可能。

### generationProcess — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/id` |
| `generator` | Yes / 必須 | [generator](#def-defs-generator) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/generator` |
| `inputs` | Yes / 必須 | array | items: generationInput | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/inputs` |
| `outputs` | Yes / 必須 | array | minItems=1; items: ref | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/outputs` |
| `targetRange` | Optional / 任意（条件付きの場合あり） | [range](#def-defs-range) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/targetRange` |
| `protectedNoteIds` | Yes / 必須 | array | uniqueItems=true; items: id | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/protectedNoteIds` |
| `intent` | Optional / 任意（条件付きの場合あり） | [generationIntent](#def-defs-generationintent) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/intent` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "intent": {
      "$ref": "#/$defs/generationIntent"
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-color"></a>
## color

**Schema pointer:** `#/$defs/color`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-roledefinition"></a>
## roleDefinition

**Schema pointer:** `#/$defs/roleDefinition`. Reachable from release root / 公開ルートから到達可能。

### roleDefinition — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/roleDefinitions/0/id` |
| `name` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/roleDefinitions/0/name` |
| `baseRole` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/roleDefinitions/0/baseRole` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-rolecolormap"></a>
## roleColorMap

**Schema pointer:** `#/$defs/roleColorMap`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```


<a id="def-defs-customrolecolormap"></a>
## customRoleColorMap

**Schema pointer:** `#/$defs/customRoleColorMap`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```


<a id="def-defs-objectcolor"></a>
## objectColor

**Schema pointer:** `#/$defs/objectColor`. Reachable from release root / 公開ルートから到達可能。

### objectColor — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `target` | Yes / 必須 | [ref](#def-defs-ref) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/appearance/objectColors/0/target` |
| `color` | Yes / 必須 | [color](#def-defs-color) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/appearance/objectColors/0/color` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-phrasetemplate"></a>
## phraseTemplate

**Schema pointer:** `#/$defs/phraseTemplate`. Reachable from release root / 公開ルートから到達可能。

### phraseTemplate — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/id` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/duration` |
| `notes` | Yes / 必須 | array | items: corePhraseSourceNote | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/corePhraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-phrasenotemapping"></a>
## phraseNoteMapping

**Schema pointer:** `#/$defs/phraseNoteMapping`. Reachable from release root / 公開ルートから到達可能。

### phraseNoteMapping — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `templateNoteId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/repeatIndex` |
| `noteId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/noteMap/0/noteId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-phraseinstance"></a>
## phraseInstance

**Schema pointer:** `#/$defs/phraseInstance`. Reachable from release root / 公開ルートから到達可能。

### phraseInstance — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/id` |
| `templateId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/templateId` |
| `clipId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/clipId` |
| `repeatCount` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/repeatCount` |
| `transpose` | Yes / 必須 | integer | minimum=-127; maximum=127 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/transpose` |
| `noteMap` | Yes / 必須 | array | items: phraseNoteMapping | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/noteMap` |
| `velocityMode` | Optional / 任意（条件付きの場合あり） | enum | enum=["independent","linked"]; default="independent"; independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/velocityMode` |
| `noteStateMode` | Optional / 任意（条件付きの場合あり） | enum | enum=["independent","linked"]; default="independent"; Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances/0/noteStateMode` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseNoteMapping"
      }
    },
    "velocityMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
    },
    "noteStateMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-clipcandidate"></a>
## clipCandidate

**Schema pointer:** `#/$defs/clipCandidate`. Reachable from release root / 公開ルートから到達可能。

### clipCandidate — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/candidates/0/id` |
| `clipIds` | Yes / 必須 | array | uniqueItems=true; items: id | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/candidates/0/clipIds` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/candidates/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-clipchoicegroup"></a>
## clipChoiceGroup

**Schema pointer:** `#/$defs/clipChoiceGroup`. Reachable from release root / 公開ルートから到達可能。

### clipChoiceGroup — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/id` |
| `candidates` | Yes / 必須 | array | minItems=1; items: clipCandidate | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/candidates` |
| `selectedCandidateId` | Yes / 必須 | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/selectedCandidateId` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-midimapping"></a>
## midiMapping

**Schema pointer:** `#/$defs/midiMapping`. Reachable from release root / 公開ルートから到達可能。

### midiMapping — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `standard` | Yes / 必須 | enum | enum=["gm1","custom"]; gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/midiMapping/standard` |
| `note` | Yes / 必須 | [pitch](#def-defs-pitch) | MIDI1 note number in 0..127; for gm1 restrict to 35..81. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/midiMapping/note` |

### midiMapping/allOf/0/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `note` | Optional / 任意（条件付きの場合あり） | integer | minimum=35; maximum=81 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/soundSlots/0/midiMapping/note` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```


<a id="def-defs-soundsource"></a>
## soundSource

**Schema pointer:** `#/$defs/soundSource`. Reachable from release root / 公開ルートから到達可能。

Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.

### soundSource — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | enum | enum=["unassigned","gm1","externalMidi","plugin","hostManaged"] | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/soundSource/kind` |
| `identifier` | Optional / 任意（条件付きの場合あり） | string | minLength=1; Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/soundSource/identifier` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-localizednames"></a>
## localizedNames

**Schema pointer:** `#/$defs/localizedNames`. Reachable from release root / 公開ルートから到達可能。

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```


<a id="def-defs-drumkit"></a>
## drumKit

**Schema pointer:** `#/$defs/drumKit`. Reachable from release root / 公開ルートから到達可能。

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

### drumKit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/drumKits/0/id` |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/drumKits/0/name` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/drumKits/0/localizedNames` |
| `soundSlotIds` | Yes / 必須 | array | uniqueItems=true; items: id; Ordered, unique references to global soundSlots; may be empty. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/drumKits/0/soundSlotIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-voicing"></a>
## voicing

**Schema pointer:** `#/$defs/voicing`. Reachable from release root / 公開ルートから到達可能。

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

### voicing — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `pitches` | Yes / 必須 | array | minItems=1; items: pitch; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/chords/0/voicing/pitches` |
| `velocities` | Optional / 任意（条件付きの場合あり） | array | minItems=1; items: see schema; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/chords/0/voicing/velocities` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```


<a id="def-defs-contributor"></a>
## contributor

**Schema pointer:** `#/$defs/contributor`. Reachable from release root / 公開ルートから到達可能。

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

### contributor — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/contributors/0/id` |
| `name` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/contributors/0/name` |
| `kind` | Optional / 任意（条件付きの場合あり） | enum | enum=["person","organization","other"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/contributors/0/kind` |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-localizednames) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/contributors/0/localizedNames` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```


<a id="def-defs-credit"></a>
## credit

**Schema pointer:** `#/$defs/credit`. Reachable from release root / 公開ルートから到達可能。

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

### credit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/credits/0/id` |
| `contributorId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/credits/0/contributorId` |
| `role` | Yes / 必須 | string | pattern="^[a-z][a-z0-9.-]*$" | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/credits/0/role` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/credits/0/label` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```


<a id="def-defs-alternatetitle"></a>
## alternateTitle

**Schema pointer:** `#/$defs/alternateTitle`. Reachable from release root / 公開ルートから到達可能。

Stable-ID song title alternative; array position and title text do not identify it.

### alternateTitle — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/alternateTitles/0/id` |
| `title` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/alternateTitles/0/title` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```


<a id="def-defs-languagemap32"></a>
## languageMap32

**Schema pointer:** `#/$defs/languageMap32`. Reachable from release root / 公開ルートから到達可能。

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```


<a id="def-defs-localizationtarget"></a>
## localizationTarget

**Schema pointer:** `#/$defs/localizationTarget`. Reachable from release root / 公開ルートから到達可能。

Core target; song is ID-less, all others use global Core ID. No namespace/profile selector.

### localizationTarget — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | enum | enum=["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre","mood","keyChange","scale","midiBus","lyricVoice"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries/0/target/kind` |
| `id` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries/1/target/id` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre",
        "mood",
        "keyChange",
        "scale",
        "midiBus",
        "lyricVoice"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "id"
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    }
  ],
  "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
}
```


<a id="def-defs-localizationentry"></a>
## localizationEntry

**Schema pointer:** `#/$defs/localizationEntry`. Reachable from release root / 公開ルートから到達可能。

Independent translations for one stable source field. Original source text remains authoritative as fallback.

### localizationEntry — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `target` | Yes / 必須 | [localizationTarget](#def-defs-localizationtarget) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries/0/target` |
| `field` | Yes / 必須 | string | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries/0/field` |
| `values` | Yes / 必須 | [languageMap32](#def-defs-languagemap32) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries/0/values` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```


<a id="def-defs-genre"></a>
## genre

**Schema pointer:** `#/$defs/genre`. Reachable from release root / 公開ルートから到達可能。

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

### genre — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | Stable song-local ID unique among all Core objects. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/genres/0/id` |
| `name` | Yes / 必須 | string | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/genres/0/name` |
| `externalUri` | Optional / 任意（条件付きの場合あり） | string | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/genres/0/externalUri` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33"></a>
## legacy33

**Schema pointer:** `#/$defs/legacy33`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### Exact JSON Schema / 厳密なSchema定義

```json
{}
```


<a id="def-defs-legacy33-defs-id"></a>
## legacy33.id

**Schema pointer:** `#/$defs/legacy33/$defs/id`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-legacy33-defs-nonnegative"></a>
## legacy33.nonnegative

**Schema pointer:** `#/$defs/legacy33/$defs/nonnegative`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```


<a id="def-defs-legacy33-defs-positive"></a>
## legacy33.positive

**Schema pointer:** `#/$defs/legacy33/$defs/positive`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```


<a id="def-defs-legacy33-defs-signed"></a>
## legacy33.signed

**Schema pointer:** `#/$defs/legacy33/$defs/signed`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```


<a id="def-defs-legacy33-defs-pitch"></a>
## legacy33.pitch

**Schema pointer:** `#/$defs/legacy33/$defs/pitch`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```


<a id="def-defs-legacy33-defs-ref"></a>
## legacy33.ref

**Schema pointer:** `#/$defs/legacy33/$defs/ref`. Reachable from release root / 公開ルートから到達可能。

### legacy33.ref — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | enum | enum=["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/refs/0/type` |
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/refs/0/id` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-range"></a>
## legacy33.range

**Schema pointer:** `#/$defs/legacy33/$defs/range`. Reachable from release root / 公開ルートから到達可能。

### legacy33.range — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `start` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange/duration` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-spelledpitchclass"></a>
## legacy33.spelledPitchClass

**Schema pointer:** `#/$defs/legacy33/$defs/spelledPitchClass`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.spelledPitchClass — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `step` | Yes / 必須 | enum | enum=["A","B","C","D","E","F","G"] |  —  |
| `alter` | Yes / 必須 | integer | minimum=-2; maximum=2 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-song"></a>
## legacy33.song

**Schema pointer:** `#/$defs/legacy33/$defs/song`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.song — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `title` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `primaryMelodyTrackId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `localizedTitles` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized song-title alternatives. song.title is the stable fallback. |  —  |
| `subtitle` | Optional / 任意（条件付きの場合あり） | string | Optional original-language subtitle. |  —  |
| `description` | Optional / 任意（条件付きの場合あり） | string | Optional original-language description, including Unicode and line breaks. |  —  |
| `alternateTitles` | Optional / 任意（条件付きの場合あり） | array | items: alternateTitle; Additional stable-ID source-language titles. |  —  |
| `credits` | Optional / 任意（条件付きの場合あり） | array | items: credit; Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. |  —  |
| `genres` | Optional / 任意（条件付きの場合あり） | array | items: genre; Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-section"></a>
## legacy33.section

**Schema pointer:** `#/$defs/legacy33/$defs/section`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.section — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Yes / 必須 | string | minLength=1 |  —  |
| `start` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `role` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-tempo"></a>
## legacy33.tempo

**Schema pointer:** `#/$defs/legacy33/$defs/tempo`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.tempo — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `bpm` | Yes / 必須 | number | maximum=1000; exclusiveMinimum=0 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-meter"></a>
## legacy33.meter

**Schema pointer:** `#/$defs/legacy33/$defs/meter`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.meter — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `numerator` | Yes / 必須 | integer | minimum=1; maximum=64 |  —  |
| `denominator` | Yes / 必須 | enum | enum=[1,2,4,8,16,32,64] |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-timeline"></a>
## legacy33.timeline

**Schema pointer:** `#/$defs/legacy33/$defs/timeline`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.timeline — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `sections` | Yes / 必須 | array | items: section |  —  |
| `tempoChanges` | Yes / 必須 | array | minItems=1; items: tempo |  —  |
| `meterChanges` | Yes / 必須 | array | minItems=1; items: meter |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/meter"
      },
      "minItems": 1
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-chord"></a>
## legacy33.chord

**Schema pointer:** `#/$defs/legacy33/$defs/chord`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.chord — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `label` | Yes / 必須 | string | minLength=1 |  —  |
| `root` | Optional / 任意（条件付きの場合あり） | [spelledPitchClass](#def-defs-legacy33-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `intervals` | Optional / 任意（条件付きの場合あり） | array | minItems=1; maxItems=36; uniqueItems=true; items: integer |  —  |
| `bass` | Optional / 任意（条件付きの場合あり） | [spelledPitchClass](#def-defs-legacy33-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `voicing` | Optional / 任意（条件付きの場合あり） | [voicing](#def-defs-legacy33-defs-voicing) | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/legacy33/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```


<a id="def-defs-legacy33-defs-scale"></a>
## legacy33.scale

**Schema pointer:** `#/$defs/legacy33/$defs/scale`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.scale — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `tonic` | Yes / 必須 | [spelledPitchClass](#def-defs-legacy33-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `intervals` | Yes / 必須 | array | minItems=1; maxItems=12; uniqueItems=true; items: integer |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-harmony"></a>
## legacy33.harmony

**Schema pointer:** `#/$defs/legacy33/$defs/harmony`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.harmony — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `chords` | Yes / 必須 | array | items: chord |  —  |
| `scales` | Yes / 必須 | array | items: scale |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-instrument"></a>
## legacy33.instrument

**Schema pointer:** `#/$defs/legacy33/$defs/instrument`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.instrument — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `family` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-note"></a>
## legacy33.note

**Schema pointer:** `#/$defs/legacy33/$defs/note`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape.

### legacy33.note — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Yes / 必須 | [signed](#def-defs-legacy33-defs-signed) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |  —  |
| `pitch` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-legacy33-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `soundSlotId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-legacy33-defs-id) | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. |  —  |
| `velocity` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=127; Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
}
```


<a id="def-defs-legacy33-defs-clip"></a>
## legacy33.clip

**Schema pointer:** `#/$defs/legacy33/$defs/clip`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.clip — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true |  —  |
| `notes` | Yes / 必須 | array | items: note |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-track"></a>
## legacy33.track

**Schema pointer:** `#/$defs/legacy33/$defs/track`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.track — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `role` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `instrument` | Optional / 任意（条件付きの場合あり） | [instrument](#def-defs-legacy33-defs-instrument) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true |  —  |
| `clips` | Yes / 必須 | array | items: clip |  —  |
| `trackType` | Optional / 任意（条件付きの場合あり） | enum | enum=["melodic","drum","mixed"]; Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. |  —  |
| `preferredView` | Optional / 任意（条件付きの場合あり） | enum | enum=["auto","pianoRoll","drumGrid"]; default="auto"; Non-binding presentation preference. Does not change note meaning. |  —  |
| `soundSource` | Optional / 任意（条件付きの場合あり） | [soundSource](#def-defs-legacy33-defs-soundsource) | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |  —  |
| `drumKitId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-legacy33-defs-id) | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/legacy33/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/legacy33/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-legacy33-defs-soundslot"></a>
## legacy33.soundSlot

**Schema pointer:** `#/$defs/legacy33/$defs/soundSlot`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

### legacy33.soundSlot — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `role` | Optional / 任意（条件付きの場合あり） | string | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. |  —  |
| `midiNote` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-legacy33-defs-pitch) | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. |  —  |
| `midiMapping` | Optional / 任意（条件付きの場合あり） | [midiMapping](#def-defs-legacy33-defs-midimapping) | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/legacy33/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```


<a id="def-defs-legacy33-defs-lyricdocument"></a>
## legacy33.lyricDocument

**Schema pointer:** `#/$defs/legacy33/$defs/lyricDocument`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.lyricDocument — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `title` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `language` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-lyricphrase"></a>
## legacy33.lyricPhrase

**Schema pointer:** `#/$defs/legacy33/$defs/lyricPhrase`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.lyricPhrase — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `documentId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `text` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `pronunciation` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```


<a id="def-defs-legacy33-defs-lyricunit"></a>
## legacy33.lyricUnit

**Schema pointer:** `#/$defs/legacy33/$defs/lyricUnit`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.lyricUnit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `phraseId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `text` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `pronunciation` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `start` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `duration` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```


<a id="def-defs-legacy33-defs-lyricalignment"></a>
## legacy33.lyricAlignment

**Schema pointer:** `#/$defs/legacy33/$defs/lyricAlignment`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.lyricAlignment — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `unitIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id |  —  |
| `noteIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-lyrics"></a>
## legacy33.lyrics

**Schema pointer:** `#/$defs/legacy33/$defs/lyrics`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.lyrics — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `documents` | Yes / 必須 | array | items: lyricDocument |  —  |
| `phrases` | Yes / 必須 | array | items: lyricPhrase |  —  |
| `units` | Yes / 必須 | array | items: lyricUnit |  —  |
| `alignments` | Yes / 必須 | array | items: lyricAlignment |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
      }
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-sha256"></a>
## legacy33.sha256

**Schema pointer:** `#/$defs/legacy33/$defs/sha256`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-legacy33-defs-resource"></a>
## legacy33.resource

**Schema pointer:** `#/$defs/legacy33/$defs/resource`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.resource — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `kind` | Yes / 必須 | enum | enum=["audio","midi","text","other"] |  —  |
| `uri` | Yes / 必須 | string | minLength=1 |  —  |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `sha256` | Optional / 任意（条件付きの場合あり） | [sha256](#def-defs-legacy33-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-dependencies"></a>
## legacy33.dependencies

**Schema pointer:** `#/$defs/legacy33/$defs/dependencies`. Reachable from release root / 公開ルートから到達可能。

### legacy33.dependencies/oneOf/0 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `scope` | Yes / 必須 | enum | enum=["document","none"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1/dependencies/scope` |

### legacy33.dependencies/oneOf/1 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `scope` | Yes / 必須 | `"objects"` (const) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/scope` |
| `refs` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: ref | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies/refs` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```


<a id="def-defs-legacy33-defs-extension"></a>
## legacy33.extension

**Schema pointer:** `#/$defs/legacy33/$defs/extension`. Reachable from release root / 公開ルートから到達可能。

### legacy33.extension — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `version` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/version` |
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-legacy33-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/dependencies` |
| `data` | Yes / 必須 | unconstrained / 制限なし | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string",
      "minLength": 1
    },
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/legacy33/$defs/dependencies"
    },
    "data": {}
  },
  "required": [
    "version",
    "status",
    "dependencies",
    "data"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-relativeassignment"></a>
## legacy33.relativeAssignment

**Schema pointer:** `#/$defs/legacy33/$defs/relativeAssignment`. Reachable from release root / 公開ルートから到達可能。

### legacy33.relativeAssignment — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `noteId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/noteId` |
| `basis` | Yes / 必須 | enum | enum=["chordTone","scaleDegree"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/basis` |
| `contextId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/contextId` |
| `anchorPitch` | Yes / 必須 | [pitch](#def-defs-legacy33-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/anchorPitch` |
| `index` | Yes / 必須 | integer | minimum=1; maximum=36 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/index` |
| `chromaticOffset` | Yes / 必須 | integer | minimum=-24; maximum=24 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/0/chromaticOffset` |

### legacy33.relativeAssignment/allOf/0/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `index` | Optional / 任意（条件付きの場合あり） | unconstrained / 制限なし | maximum=12 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments/1/index` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```


<a id="def-defs-legacy33-defs-relativedata"></a>
## legacy33.relativeData

**Schema pointer:** `#/$defs/legacy33/$defs/relativeData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.relativeData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `assignments` | Yes / 必須 | array | items: relativeAssignment | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1/data/assignments` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "assignments"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-generator"></a>
## legacy33.generator

**Schema pointer:** `#/$defs/legacy33/$defs/generator`. Reachable from release root / 公開ルートから到達可能。

### legacy33.generator — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator/id` |
| `version` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator/version` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-generationinput"></a>
## legacy33.generationInput

**Schema pointer:** `#/$defs/legacy33/$defs/generationInput`. Reachable from release root / 公開ルートから到達可能。

### legacy33.generationInput — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `role` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/role` |
| `ref` | Yes / 必須 | [ref](#def-defs-legacy33-defs-ref) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/ref` |
| `readRange` | Optional / 任意（条件付きの場合あり） | [range](#def-defs-legacy33-defs-range) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs/0/readRange` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-generationprocess"></a>
## legacy33.generationProcess

**Schema pointer:** `#/$defs/legacy33/$defs/generationProcess`. Reachable from release root / 公開ルートから到達可能。

### legacy33.generationProcess — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/id` |
| `generator` | Yes / 必須 | [generator](#def-defs-legacy33-defs-generator) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/generator` |
| `inputs` | Yes / 必須 | array | items: generationInput | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/inputs` |
| `outputs` | Yes / 必須 | array | minItems=1; items: ref | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/outputs` |
| `targetRange` | Optional / 任意（条件付きの場合あり） | [range](#def-defs-legacy33-defs-range) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/targetRange` |
| `protectedNoteIds` | Yes / 必須 | array | uniqueItems=true; items: id | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/protectedNoteIds` |
| `vendorExtension` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes/0/vendorExtension` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/legacy33/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/legacy33/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "vendorExtension": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-generationdata"></a>
## legacy33.generationData

**Schema pointer:** `#/$defs/legacy33/$defs/generationData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.generationData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `processes` | Yes / 必須 | array | items: generationProcess | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1/data/processes` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/generationProcess"
      }
    }
  },
  "required": [
    "processes"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-color"></a>
## legacy33.color

**Schema pointer:** `#/$defs/legacy33/$defs/color`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```


<a id="def-defs-legacy33-defs-roledefinition"></a>
## legacy33.roleDefinition

**Schema pointer:** `#/$defs/legacy33/$defs/roleDefinition`. Reachable from release root / 公開ルートから到達可能。

### legacy33.roleDefinition — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/id` |
| `name` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/name` |
| `baseRole` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions/0/baseRole` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-rolecolormap"></a>
## legacy33.roleColorMap

**Schema pointer:** `#/$defs/legacy33/$defs/roleColorMap`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```


<a id="def-defs-legacy33-defs-customrolecolormap"></a>
## legacy33.customRoleColorMap

**Schema pointer:** `#/$defs/legacy33/$defs/customRoleColorMap`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/legacy33/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/color"
  }
}
```


<a id="def-defs-legacy33-defs-objectcolor"></a>
## legacy33.objectColor

**Schema pointer:** `#/$defs/legacy33/$defs/objectColor`. Reachable from release root / 公開ルートから到達可能。

### legacy33.objectColor — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `target` | Yes / 必須 | [ref](#def-defs-legacy33-defs-ref) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance/objectColors/0/target` |
| `color` | Yes / 必須 | [color](#def-defs-legacy33-defs-color) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance/objectColors/0/color` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/legacy33/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-appearancedata"></a>
## legacy33.appearanceData

**Schema pointer:** `#/$defs/legacy33/$defs/appearanceData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.appearanceData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `roleDefinitions` | Yes / 必須 | array | items: roleDefinition | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/roleDefinitions` |
| `sectionRoleAssignments` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/sectionRoleAssignments` |
| `appearance` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1/data/appearance` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/legacy33/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-legacydata"></a>
## legacy33.legacyData

**Schema pointer:** `#/$defs/legacy33/$defs/legacyData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.legacyData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `sourceVersion` | Yes / 必須 | `"2.3.0"` (const) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceVersion` |
| `sourceSha256` | Yes / 必須 | [sha256](#def-defs-legacy33-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceSha256` |
| `sourceText` | Yes / 必須 | string | minLength=1 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/sourceText` |
| `conversionReport` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1/data/conversionReport` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "sourceVersion": {
      "const": "2.3.0"
    },
    "sourceSha256": {
      "$ref": "#/$defs/legacy33/$defs/sha256"
    },
    "sourceText": {
      "type": "string",
      "minLength": 1
    },
    "conversionReport": {
      "type": "object"
    }
  },
  "required": [
    "sourceVersion",
    "sourceSha256",
    "sourceText",
    "conversionReport"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-extensions"></a>
## legacy33.extensions

**Schema pointer:** `#/$defs/legacy33/$defs/extensions`. Reachable from release root / 公開ルートから到達可能。

### legacy33.extensions — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `org.ostf.relative-phrase.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.relative-phrase.v1` |
| `org.ostf.generation-context.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.generation-context.v1` |
| `org.ostf.appearance.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.appearance.v1` |
| `org.ostf.legacy-import.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.legacy-import.v1` |
| `org.ostf.phrase-library.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1` |
| `org.ostf.clip-choices.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1` |
| `org.ostf.localization.v1` | Optional / 任意（条件付きの場合あり） | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "propertyNames": {
    "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
    "not": {
      "pattern": "[\\r\\n\\u2028\\u2029]"
    }
  },
  "properties": {
    "org.ostf.relative-phrase.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/relativeData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.generation-context.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/generationData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.appearance.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/appearanceData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.legacy-import.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/legacyData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.phrase-library.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.clip-choices.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0-draft.1"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
              }
            }
          }
        }
      ]
    },
    "org.ostf.localization.v1": {
      "allOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/extension"
        },
        {
          "if": {
            "properties": {
              "version": {
                "const": "1.0.0"
              }
            },
            "required": [
              "version"
            ]
          },
          "then": {
            "properties": {
              "data": {
                "$ref": "#/$defs/legacy33/$defs/localizationData"
              }
            }
          }
        }
      ]
    }
  },
  "additionalProperties": {
    "$ref": "#/$defs/legacy33/$defs/extension"
  }
}
```


<a id="def-defs-legacy33-defs-phrasetemplate"></a>
## legacy33.phraseTemplate

**Schema pointer:** `#/$defs/legacy33/$defs/phraseTemplate`. Reachable from release root / 公開ルートから到達可能。

### legacy33.phraseTemplate — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/id` |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/duration` |
| `notes` | Yes / 必須 | array | items: phraseSourceNote | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-phrasenotemapping"></a>
## legacy33.phraseNoteMapping

**Schema pointer:** `#/$defs/legacy33/$defs/phraseNoteMapping`. Reachable from release root / 公開ルートから到達可能。

### legacy33.phraseNoteMapping — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `templateNoteId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/templateNoteId` |
| `repeatIndex` | Yes / 必須 | [nonnegative](#def-defs-legacy33-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/repeatIndex` |
| `noteId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap/0/noteId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/legacy33/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-phraseinstance"></a>
## legacy33.phraseInstance

**Schema pointer:** `#/$defs/legacy33/$defs/phraseInstance`. Reachable from release root / 公開ルートから到達可能。

### legacy33.phraseInstance — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/id` |
| `templateId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/templateId` |
| `clipId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/clipId` |
| `repeatCount` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/repeatCount` |
| `transpose` | Yes / 必須 | integer | minimum=-127; maximum=127 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/transpose` |
| `noteMap` | Yes / 必須 | array | items: phraseNoteMapping | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances/0/noteMap` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
      }
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-phraselibrarydata"></a>
## legacy33.phraseLibraryData

**Schema pointer:** `#/$defs/legacy33/$defs/phraseLibraryData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.phraseLibraryData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `templates` | Yes / 必須 | array | items: phraseTemplate | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates` |
| `instances` | Yes / 必須 | array | items: phraseInstance | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/instances` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "templates",
    "instances"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-clipcandidate"></a>
## legacy33.clipCandidate

**Schema pointer:** `#/$defs/legacy33/$defs/clipCandidate`. Reachable from release root / 公開ルートから到達可能。

### legacy33.clipCandidate — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/id` |
| `clipIds` | Yes / 必須 | array | uniqueItems=true; items: id | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/clipIds` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-clipchoicegroup"></a>
## legacy33.clipChoiceGroup

**Schema pointer:** `#/$defs/legacy33/$defs/clipChoiceGroup`. Reachable from release root / 公開ルートから到達可能。

### legacy33.clipChoiceGroup — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/id` |
| `candidates` | Yes / 必須 | array | minItems=1; items: clipCandidate | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/candidates` |
| `selectedCandidateId` | Yes / 必須 | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/selectedCandidateId` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-clipchoicesdata"></a>
## legacy33.clipChoicesData

**Schema pointer:** `#/$defs/legacy33/$defs/clipChoicesData`. Reachable from release root / 公開ルートから到達可能。

### legacy33.clipChoicesData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `groups` | Yes / 必須 | array | items: clipChoiceGroup | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.clip-choices.v1/data/groups` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "groups"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-midimapping"></a>
## legacy33.midiMapping

**Schema pointer:** `#/$defs/legacy33/$defs/midiMapping`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

### legacy33.midiMapping — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `standard` | Yes / 必須 | enum | enum=["gm1","custom"]; gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. |  —  |
| `note` | Yes / 必須 | [pitch](#def-defs-legacy33-defs-pitch) | MIDI1 note number in 0..127; for gm1 restrict to 35..81. |  —  |

### legacy33.midiMapping/allOf/0/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `note` | Optional / 任意（条件付きの場合あり） | integer | minimum=35; maximum=81 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/legacy33/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```


<a id="def-defs-legacy33-defs-soundsource"></a>
## legacy33.soundSource

**Schema pointer:** `#/$defs/legacy33/$defs/soundSource`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.

### legacy33.soundSource — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | enum | enum=["unassigned","gm1","externalMidi","plugin","hostManaged"] |  —  |
| `identifier` | Optional / 任意（条件付きの場合あり） | string | minLength=1; Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-legacy33-defs-localizednames"></a>
## legacy33.localizedNames

**Schema pointer:** `#/$defs/legacy33/$defs/localizedNames`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```


<a id="def-defs-legacy33-defs-drumkit"></a>
## legacy33.drumKit

**Schema pointer:** `#/$defs/legacy33/$defs/drumKit`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

### legacy33.drumKit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `soundSlotIds` | Yes / 必須 | array | uniqueItems=true; items: id; Ordered, unique references to global soundSlots; may be empty. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-legacy33-defs-phrasesourcenote"></a>
## legacy33.phraseSourceNote

**Schema pointer:** `#/$defs/legacy33/$defs/phraseSourceNote`. Reachable from release root / 公開ルートから到達可能。

Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity.

### legacy33.phraseSourceNote — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-legacy33-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-legacy33-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/duration` |
| `pitch` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-legacy33-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/0/notes/0/pitch` |
| `soundSlotId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.phrase-library.v1/data/templates/1/notes/0/soundSlotId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/legacy33/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/legacy33/$defs/positive"
    },
    "pitch": {
      "$ref": "#/$defs/legacy33/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
}
```


<a id="def-defs-legacy33-defs-voicing"></a>
## legacy33.voicing

**Schema pointer:** `#/$defs/legacy33/$defs/voicing`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

### legacy33.voicing — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `pitches` | Yes / 必須 | array | minItems=1; items: pitch; Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. |  —  |
| `velocities` | Optional / 任意（条件付きの場合あり） | array | minItems=1; items: see schema; Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/legacy33/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```


<a id="def-defs-legacy33-defs-contributor"></a>
## legacy33.contributor

**Schema pointer:** `#/$defs/legacy33/$defs/contributor`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

### legacy33.contributor — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `name` | Yes / 必須 | string | minLength=1 |  —  |
| `kind` | Optional / 任意（条件付きの場合あり） | enum | enum=["person","organization","other"] |  —  |
| `localizedNames` | Optional / 任意（条件付きの場合あり） | [localizedNames](#def-defs-legacy33-defs-localizednames) | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/legacy33/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```


<a id="def-defs-legacy33-defs-credit"></a>
## legacy33.credit

**Schema pointer:** `#/$defs/legacy33/$defs/credit`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

### legacy33.credit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `contributorId` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `role` | Yes / 必須 | string | pattern="^[a-z][a-z0-9.-]*$" |  —  |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```


<a id="def-defs-legacy33-defs-alternatetitle"></a>
## legacy33.alternateTitle

**Schema pointer:** `#/$defs/legacy33/$defs/alternateTitle`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

Stable-ID song title alternative; array position and title text do not identify it.

### legacy33.alternateTitle — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 |  —  |
| `title` | Yes / 必須 | string | minLength=1 |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```


<a id="def-defs-legacy33-defs-languagemap32"></a>
## legacy33.languageMap32

**Schema pointer:** `#/$defs/legacy33/$defs/languageMap32`. Reachable from release root / 公開ルートから到達可能。

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```


<a id="def-defs-legacy33-defs-localizationtarget"></a>
## legacy33.localizationTarget

**Schema pointer:** `#/$defs/legacy33/$defs/localizationTarget`. Reachable from release root / 公開ルートから到達可能。

Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators.

### legacy33.localizationTarget — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | enum | enum=["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target/kind` |
| `id` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-legacy33-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/1/target/id` |
| `profile` | Optional / 任意（条件付きの場合あり） | enum | enum=["org.ostf.phrase-library.v1","org.ostf.clip-choices.v1","org.ostf.appearance.v1"] | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/2/target/profile` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre"
      ]
    },
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id"
    },
    "profile": {
      "type": "string",
      "enum": [
        "org.ostf.phrase-library.v1",
        "org.ostf.clip-choices.v1",
        "org.ostf.appearance.v1"
      ]
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "id"
              ]
            },
            {
              "required": [
                "profile"
              ]
            }
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    },
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "phraseTemplate",
              "clipCandidate",
              "clipChoiceGroup",
              "roleDefinition"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "required": [
          "profile"
        ]
      },
      "else": {
        "not": {
          "required": [
            "profile"
          ]
        }
      }
    }
  ],
  "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
}
```


<a id="def-defs-legacy33-defs-localizationentry"></a>
## legacy33.localizationEntry

**Schema pointer:** `#/$defs/legacy33/$defs/localizationEntry`. Reachable from release root / 公開ルートから到達可能。

Independent translations for one stable source field. Original source text remains authoritative as fallback.

### legacy33.localizationEntry — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `target` | Yes / 必須 | [localizationTarget](#def-defs-legacy33-defs-localizationtarget) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/target` |
| `field` | Yes / 必須 | string | minLength=1; Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/field` |
| `values` | Yes / 必須 | [languageMap32](#def-defs-legacy33-defs-languagemap32) | See exact schema / 厳密な定義は下記Schema。 | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries/0/values` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/legacy33/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/legacy33/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```


<a id="def-defs-legacy33-defs-localizationdata"></a>
## legacy33.localizationData

**Schema pointer:** `#/$defs/legacy33/$defs/localizationData`. Reachable from release root / 公開ルートから到達可能。

Language-map translations indexed by stable kind/id/field, never by names or array positions.

### legacy33.localizationData — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `entries` | Yes / 必須 | array | items: localizationEntry | [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf)<br>`/extensions/org.ostf.localization.v1/data/entries` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/legacy33/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "entries"
  ],
  "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
}
```


<a id="def-defs-legacy33-defs-genre"></a>
## legacy33.genre

**Schema pointer:** `#/$defs/legacy33/$defs/genre`. Retained schema definition / 継承された定義。Rootから直接使用されない定義も省略しません。

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

### legacy33.genre — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-legacy33-defs-id) | Stable song-local ID unique among all Core objects. |  —  |
| `name` | Yes / 必須 | string | minLength=1; Original Unicode genre label, never normalized or rewritten during import. |  —  |
| `externalUri` | Optional / 任意（条件付きの場合あり） | string | minLength=1; format="uri"; Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. |  —  |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/legacy33/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-opaquedocumentid"></a>
## opaqueDocumentId

**Schema pointer:** `#/$defs/opaqueDocumentId`. Reachable from release root / 公開ルートから到達可能。

Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "minLength": 1,
  "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
}
```


<a id="def-defs-revisionref"></a>
## revisionRef

**Schema pointer:** `#/$defs/revisionRef`. Reachable from release root / 公開ルートから到達可能。

### revisionRef — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `documentId` | Yes / 必須 | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/document/parents/0/documentId` |
| `revisionId` | Yes / 必須 | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/document/parents/0/revisionId` |
| `sha256` | Optional / 任意（条件付きの場合あり） | [sha256](#def-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/document/parents/0/sha256` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "documentId",
    "revisionId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-software"></a>
## software

**Schema pointer:** `#/$defs/software`. Reachable from release root / 公開ルートから到達可能。

### software — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `name` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document/createdBy/name` |
| `version` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document/createdBy/version` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-documentinfo"></a>
## documentInfo

**Schema pointer:** `#/$defs/documentInfo`. Reachable from release root / 公開ルートから到達可能。

### documentInfo — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document/id` |
| `revisionId` | Yes / 必須 | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document/revisionId` |
| `parents` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: revisionRef | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/document/parents` |
| `createdBy` | Optional / 任意（条件付きの場合あり） | [software](#def-defs-software) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/document/createdBy` |
| `modifiedBy` | Optional / 任意（条件付きの場合あり） | [software](#def-defs-software) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/document/modifiedBy` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "parents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/revisionRef"
      },
      "uniqueItems": true
    },
    "createdBy": {
      "$ref": "#/$defs/software"
    },
    "modifiedBy": {
      "$ref": "#/$defs/software"
    }
  },
  "required": [
    "id",
    "revisionId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-key"></a>
## key

**Schema pointer:** `#/$defs/key`. Reachable from release root / 公開ルートから到達可能。

### key — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `state` | Yes / 必須 | enum | enum=["tonal","atonal","unspecified"] | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key/state` |
| `tonic` | Optional / 任意（条件付きの場合あり） | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key/tonic` |
| `mode` | Optional / 任意（条件付きの場合あり） | string | minLength=1; Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor. | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/song/key/mode` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/key/label` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "state": {
      "enum": [
        "tonal",
        "atonal",
        "unspecified"
      ]
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "mode": {
      "type": "string",
      "minLength": 1,
      "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "state": {
            "const": "tonal"
          }
        },
        "required": [
          "state"
        ]
      },
      "then": {
        "required": [
          "tonic",
          "mode"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "tonic"
              ]
            },
            {
              "required": [
                "mode"
              ]
            }
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-keychange"></a>
## keyChange

**Schema pointer:** `#/$defs/keyChange`. Reachable from release root / 公開ルートから到達可能。

A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority.

### keyChange — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/keyChanges/0/id` |
| `at` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/keyChanges/0/at` |
| `key` | Yes / 必須 | [key](#def-defs-key) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/keyChanges/0/key` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/timeline/keyChanges/0/label` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/positive"
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "at",
    "key"
  ],
  "additionalProperties": false,
  "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
}
```


<a id="def-defs-scaledefinition"></a>
## scaleDefinition

**Schema pointer:** `#/$defs/scaleDefinition`. Reachable from release root / 公開ルートから到達可能。

### scaleDefinition — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/scale/id` |
| `tonic` | Yes / 必須 | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/scale/tonic` |
| `intervals` | Yes / 必須 | array | minItems=1; maxItems=12; uniqueItems=true; items: integer | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/scale/intervals` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/scale/label` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-scaletarget"></a>
## scaleTarget

**Schema pointer:** `#/$defs/scaleTarget`. Reachable from release root / 公開ルートから到達可能。

### scaleTarget — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | enum | enum=["section","track","clip","chord","note"] | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/targets/0/type` |
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/harmony/scales/0/targets/0/id` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "chord",
        "note"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-mood"></a>
## mood

**Schema pointer:** `#/$defs/mood`. Reachable from release root / 公開ルートから到達可能。

Authored descriptive mood tag; not a generator preset or a probability.

### mood — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | Stable song-local ID unique among all Core objects. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/moods/0/id` |
| `name` | Yes / 必須 | string | minLength=1; Original Unicode genre label, never normalized or rewritten during import. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/moods/0/name` |
| `externalUri` | Optional / 任意（条件付きの場合あり） | string | minLength=1; format="uri"; Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/moods/0/externalUri` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Authored descriptive mood tag; not a generator preset or a probability.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-rightsstatement"></a>
## rightsStatement

**Schema pointer:** `#/$defs/rightsStatement`. Reachable from release root / 公開ルートから到達可能。

Authored rights statement only; no rights or permissions are inferred or granted by the format.

### rightsStatement — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `notice` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/rights/notice` |
| `licenseUri` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/song/rights/licenseUri` |
| `rightsHolderIds` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: id | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/song/rights/rightsHolderIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "notice": {
      "type": "string"
    },
    "licenseUri": {
      "type": "string",
      "minLength": 1
    },
    "rightsHolderIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
  "minProperties": 1
}
```


<a id="def-defs-grooveintent"></a>
## grooveIntent

**Schema pointer:** `#/$defs/grooveIntent`. Reachable from release root / 公開ルートから到達可能。

Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.

### grooveIntent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/groove/name` |
| `unitTicks` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/groove/unitTicks` |
| `longWeight` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=1000000 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/groove/longWeight` |
| `shortWeight` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=1000000 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/groove/shortWeight` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "unitTicks": {
      "$ref": "#/$defs/positive"
    },
    "longWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    },
    "shortWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
  "minProperties": 1,
  "dependentRequired": {
    "unitTicks": [
      "longWeight",
      "shortWeight"
    ],
    "longWeight": [
      "unitTicks",
      "shortWeight"
    ],
    "shortWeight": [
      "unitTicks",
      "longWeight"
    ]
  }
}
```


<a id="def-defs-generationintent"></a>
## generationIntent

**Schema pointer:** `#/$defs/generationIntent`. Reachable from release root / 公開ルートから到達可能。

Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods.

### generationIntent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `genreNames` | Optional / 任意（条件付きの場合あり） | array | items: string | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/intent/genreNames` |
| `moodNames` | Optional / 任意（条件付きの場合あり） | array | items: string | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/intent/moodNames` |
| `groove` | Optional / 任意（条件付きの場合あり） | [grooveIntent](#def-defs-grooveintent) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/groove` |
| `prompt` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes/0/intent/prompt` |
| `seed` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/generation/processes/0/intent/seed` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "genreNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "moodNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "groove": {
      "$ref": "#/$defs/grooveIntent"
    },
    "prompt": {
      "type": "string"
    },
    "seed": {
      "type": "string"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
}
```


<a id="def-defs-relativephrases"></a>
## relativePhrases

**Schema pointer:** `#/$defs/relativePhrases`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### relativePhrases — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/dependencies` |
| `assignments` | Yes / 必須 | array | items: relativeAssignment | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/relativePhrases/assignments` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "assignments"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-generation"></a>
## generation

**Schema pointer:** `#/$defs/generation`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### generation — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/dependencies` |
| `processes` | Yes / 必須 | array | items: generationProcess | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/generation/processes` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationProcess"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "processes"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-presentation"></a>
## presentation

**Schema pointer:** `#/$defs/presentation`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### presentation — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/dependencies` |
| `roleDefinitions` | Yes / 必須 | array | items: roleDefinition | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/roleDefinitions` |
| `sectionRoleAssignments` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/sectionRoleAssignments` |
| `appearance` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/presentation/appearance` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "status",
    "dependencies",
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-phraselibrary"></a>
## phraseLibrary

**Schema pointer:** `#/$defs/phraseLibrary`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### phraseLibrary — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/dependencies` |
| `templates` | Yes / 必須 | array | items: phraseTemplate | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates` |
| `instances` | Yes / 必須 | array | items: phraseInstance | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/instances` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "templates",
    "instances"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-clipchoices"></a>
## clipChoices

**Schema pointer:** `#/$defs/clipChoices`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### clipChoices — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/dependencies` |
| `groups` | Yes / 必須 | array | items: clipChoiceGroup | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/clipChoices/groups` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "groups"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-localization"></a>
## localization

**Schema pointer:** `#/$defs/localization`. Reachable from release root / 公開ルートから到達可能。

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

### localization — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `status` | Yes / 必須 | enum | enum=["current","stale","unverified"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/status` |
| `dependencies` | Yes / 必須 | [dependencies](#def-defs-dependencies) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/dependencies` |
| `entries` | Yes / 必須 | array | items: localizationEntry | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/localization/entries` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "entries"
  ],
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```


<a id="def-defs-corephrasesourcenote"></a>
## corePhraseSourceNote

**Schema pointer:** `#/$defs/corePhraseSourceNote`. Reachable from release root / 公開ルートから到達可能。

Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.

### corePhraseSourceNote — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/duration` |
| `pitch` | Optional / 任意（条件付きの場合あり） | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/pitch` |
| `soundSlotId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/1/notes/0/soundSlotId` |
| `velocity` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=127; Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/phraseLibrary/templates/0/notes/0/velocity` |
| `enabled` | Optional / 任意（条件付きの場合あり） | boolean | default=true; Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/0/notes/0/enabled` |
| `releaseVelocity` | Optional / 任意（条件付きの場合あり） | integer | minimum=0; maximum=127; Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/0/notes/0/releaseVelocity` |
| `probability` | Optional / 任意（条件付きの場合あり） | number | minimum=0; maximum=1; default=1; Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/0/notes/0/probability` |
| `velocityDeviation` | Optional / 任意（条件付きの場合あり） | integer | minimum=-126; maximum=126; default=0; Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/0/notes/0/velocityDeviation` |
| `pitchRole` | Optional / 任意（条件付きの場合あり） | enum | enum=["musical","fixedTrigger"]; default="musical"; Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/phraseLibrary/templates/0/notes/0/pitchRole` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-provenancesource"></a>
## provenanceSource

**Schema pointer:** `#/$defs/provenanceSource`. Reachable from release root / 公開ルートから到達可能。

Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.

### provenanceSource — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `format` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/format` |
| `version` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/version` |
| `sha256` | Optional / 任意（条件付きの場合あり） | [sha256](#def-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/sha256` |
| `uri` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/uri` |
| `documentId` | Optional / 任意（条件付きの場合あり） | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/documentId` |
| `revisionId` | Optional / 任意（条件付きの場合あり） | [opaqueDocumentId](#def-defs-opaquedocumentid) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/revisionId` |
| `resourceId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources/0/resourceId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "format": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "resourceId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
  "minProperties": 1,
  "dependentRequired": {
    "revisionId": [
      "documentId"
    ]
  }
}
```


<a id="def-defs-provenancerecord"></a>
## provenanceRecord

**Schema pointer:** `#/$defs/provenanceRecord`. Reachable from release root / 公開ルートから到達可能。

### provenanceRecord — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance/records/0/id` |
| `action` | Yes / 必須 | enum | enum=["create","import","conversion","edit","transpose","merge","generation","other"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance/records/0/action` |
| `description` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance/records/0/description` |
| `tool` | Optional / 任意（条件付きの場合あり） | [software](#def-defs-software) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance/records/0/tool` |
| `sources` | Optional / 任意（条件付きの場合あり） | array | items: provenanceSource | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/sources` |
| `semitones` | Optional / 任意（条件付きの場合あり） | integer | minimum=-127; maximum=127 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/semitones` |
| `beforeKey` | Optional / 任意（条件付きの場合あり） | [key](#def-defs-key) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/beforeKey` |
| `afterKey` | Optional / 任意（条件付きの場合あり） | [key](#def-defs-key) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/provenance/records/1/afterKey` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "action": {
      "enum": [
        "create",
        "import",
        "conversion",
        "edit",
        "transpose",
        "merge",
        "generation",
        "other"
      ]
    },
    "description": {
      "type": "string"
    },
    "tool": {
      "$ref": "#/$defs/software"
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceSource"
      }
    },
    "semitones": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "beforeKey": {
      "$ref": "#/$defs/key"
    },
    "afterKey": {
      "$ref": "#/$defs/key"
    }
  },
  "required": [
    "id",
    "action"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "not": {
          "properties": {
            "action": {
              "const": "transpose"
            }
          },
          "required": [
            "action"
          ]
        }
      },
      "then": {
        "not": {
          "required": [
            "semitones"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-provenance"></a>
## provenance

**Schema pointer:** `#/$defs/provenance`. Reachable from release root / 公開ルートから到達可能。

Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness.

### provenance — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `records` | Yes / 必須 | array | items: provenanceRecord | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/provenance/records` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "records": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceRecord"
      }
    }
  },
  "required": [
    "records"
  ],
  "additionalProperties": false,
  "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
}
```


<a id="def-defs-midichannel"></a>
## midiChannel

**Schema pointer:** `#/$defs/midiChannel`. Reachable from release root / 公開ルートから到達可能。

Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 16,
  "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
}
```


<a id="def-defs-midibus"></a>
## midiBus

**Schema pointer:** `#/$defs/midiBus`. Reachable from release root / 公開ルートから到達可能。

Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.

### midiBus — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/midi/buses/0/id` |
| `name` | Yes / 必須 | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/midi/buses/0/name` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-midi"></a>
## midi

**Schema pointer:** `#/$defs/midi`. Reachable from release root / 公開ルートから到達可能。

### midi — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `buses` | Yes / 必須 | array | items: midiBus | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/midi/buses` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "buses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiBus"
      }
    }
  },
  "required": [
    "buses"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-mpesettings"></a>
## mpeSettings

**Schema pointer:** `#/$defs/mpeSettings`. Reachable from release root / 公開ルートから到達可能。

Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.

### mpeSettings — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `zone` | Yes / 必須 | enum | enum=["lower","upper"] | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/midi/mpe/zone` |
| `memberChannelCount` | Yes / 必須 | integer | minimum=1; maximum=15 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/midi/mpe/memberChannelCount` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
  "properties": {
    "zone": {
      "enum": [
        "lower",
        "upper"
      ]
    },
    "memberChannelCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 15
    }
  },
  "required": [
    "zone",
    "memberChannelCount"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-trackmidi"></a>
## trackMidi

**Schema pointer:** `#/$defs/trackMidi`. Reachable from release root / 公開ルートから到達可能。

Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.

### trackMidi — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `busId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/midi/busId` |
| `mode` | Yes / 必須 | enum | enum=["singleChannel","multiChannel","mpe"] | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/midi/mode` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/midi/channel` |
| `mpe` | Optional / 任意（条件付きの場合あり） | [mpeSettings](#def-defs-mpesettings) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/midi/mpe` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
  "properties": {
    "busId": {
      "$ref": "#/$defs/id"
    },
    "mode": {
      "enum": [
        "singleChannel",
        "multiChannel",
        "mpe"
      ]
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "mpe": {
      "$ref": "#/$defs/mpeSettings"
    }
  },
  "required": [
    "mode"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "mode": {
            "const": "singleChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "channel"
        ],
        "not": {
          "required": [
            "mpe"
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "multiChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "channel"
              ]
            },
            {
              "required": [
                "mpe"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "mpe"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "mpe"
        ],
        "not": {
          "required": [
            "channel"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-controlchangeevent"></a>
## controlChangeEvent

**Schema pointer:** `#/$defs/controlChangeEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.

### controlChangeEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/0/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/0/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/0/channel` |
| `type` | Yes / 必須 | `"controlChange"` (const) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/0/type` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/0/targetNoteId` |
| `controller` | Yes / 必須 | integer | minimum=0; maximum=119 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/0/controller` |
| `value` | Yes / 必須 | integer | minimum=0; maximum=127 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/0/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "controlChange"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "controller": {
      "type": "integer",
      "minimum": 0,
      "maximum": 119
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-channelmodeevent"></a>
## channelModeEvent

**Schema pointer:** `#/$defs/channelModeEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.

### channelModeEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/channel` |
| `type` | Yes / 必須 | `"channelMode"` (const) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/type` |
| `controller` | Yes / 必須 | integer | minimum=120; maximum=127 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/controller` |
| `value` | Yes / 必須 | integer | minimum=0; maximum=127 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/5/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelMode"
    },
    "controller": {
      "type": "integer",
      "minimum": 120,
      "maximum": 127
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-programchangeevent"></a>
## programChangeEvent

**Schema pointer:** `#/$defs/programChangeEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.

### programChangeEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/4/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/4/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/1/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/1/channel` |
| `type` | Yes / 必須 | `"programChange"` (const) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/4/type` |
| `program` | Yes / 必須 | integer | minimum=0; maximum=127 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/4/program` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "programChange"
    },
    "program": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "program"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-pitchbendevent"></a>
## pitchBendEvent

**Schema pointer:** `#/$defs/pitchBendEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.

### pitchBendEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/channel` |
| `type` | Yes / 必須 | `"pitchBend"` (const) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/type` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/targetNoteId` |
| `value14` | Yes / 必須 | integer | minimum=0; maximum=16383; Raw MIDI 1.0 14-bit pitch-bend value; center is 8192. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/2/value14` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "pitchBend"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value14": {
      "type": "integer",
      "minimum": 0,
      "maximum": 16383,
      "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value14"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-channelpressureevent"></a>
## channelPressureEvent

**Schema pointer:** `#/$defs/channelPressureEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 Channel Pressure (channel aftertouch).

### channelPressureEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/channel` |
| `type` | Yes / 必須 | `"channelPressure"` (const) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/type` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/targetNoteId` |
| `value` | Yes / 必須 | integer | minimum=0; maximum=127 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/3/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-polypressureevent"></a>
## polyPressureEvent

**Schema pointer:** `#/$defs/polyPressureEvent`. Reachable from release root / 公開ルートから到達可能。

MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).

### polyPressureEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/start` |
| `order` | Optional / 任意（条件付きの場合あり） | [signed](#def-defs-signed) | default=1; Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/4/order` |
| `channel` | Optional / 任意（条件付きの場合あり） | [midiChannel](#def-defs-midichannel) | See exact schema / 厳密な定義は下記Schema。 | [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)<br>`/tracks/0/clips/0/midiEvents/4/channel` |
| `type` | Yes / 必須 | `"polyPressure"` (const) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/type` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/targetNoteId` |
| `pitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/pitch` |
| `value` | Yes / 必須 | integer | minimum=0; maximum=127 | [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf)<br>`/tracks/0/clips/0/midiEvents/2/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "polyPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "pitch",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-midievent"></a>
## midiEvent

**Schema pointer:** `#/$defs/midiEvent`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/controlChangeEvent"
    },
    {
      "$ref": "#/$defs/channelModeEvent"
    },
    {
      "$ref": "#/$defs/programChangeEvent"
    },
    {
      "$ref": "#/$defs/pitchBendEvent"
    },
    {
      "$ref": "#/$defs/channelPressureEvent"
    },
    {
      "$ref": "#/$defs/polyPressureEvent"
    }
  ]
}
```


<a id="def-defs-lyricvoice"></a>
## lyricVoice

**Schema pointer:** `#/$defs/lyricVoice`. Reachable from release root / 公開ルートから到達可能。

Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.

### lyricVoice — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/voices/0/id` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/lyrics/voices/0/name` |
| `role` | Optional / 任意（条件付きの場合あり） | string | minLength=1; Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response. | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/voices/0/role` |
| `trackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/voices/0/trackId` |
| `documentId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/lyrics/voices/0/documentId` |
| `vocalProfile` | Optional / 任意（条件付きの場合あり） | [vocalProfile](#def-defs-vocalprofile) | Optional engine-neutral vocal defaults; absence does not mean an instrument voice. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/voices/0/vocalProfile` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "vocalProfile": {
      "$ref": "#/$defs/vocalProfile",
      "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
    }
  },
  "required": [
    "id",
    "trackId",
    "documentId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-playablepitchrange"></a>
## playablePitchRange

**Schema pointer:** `#/$defs/playablePitchRange`. Reachable from release root / 公開ルートから到達可能。

Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch.

### playablePitchRange — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `lowPitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/requiredPitchRange/lowPitch` |
| `highPitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/requiredPitchRange/highPitch` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    }
  },
  "required": [
    "lowPitch",
    "highPitch"
  ],
  "additionalProperties": false,
  "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
}
```


<a id="def-defs-directionpitchcollection"></a>
## directionPitchCollection

**Schema pointer:** `#/$defs/directionPitchCollection`. Reachable from release root / 公開ルートから到達可能。

Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity.

### directionPitchCollection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `tonic` | Yes / 必須 | [spelledPitchClass](#def-defs-spelledpitchclass) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/tonic` |
| `intervals` | Yes / 必須 | array | minItems=1; maxItems=12; uniqueItems=true; items: integer | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/intervals` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale/label` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "tonic",
    "intervals"
  ],
  "additionalProperties": false,
  "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
}
```


<a id="def-defs-directionpitchsource"></a>
## directionPitchSource

**Schema pointer:** `#/$defs/directionPitchSource`. Reachable from release root / 公開ルートから到達可能。

Source of pitch vocabulary for an improvisation Direction.

### directionPitchSource/oneOf/0 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | `"effectiveKeyScale"` (const) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/parameters/pitchSource/type` |

### directionPitchSource/oneOf/1 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | `"songScale"` (const) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/3/parameters/pitchSource/type` |

### directionPitchSource/oneOf/2 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | `"harmonyScales"` (const) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/4/parameters/pitchSource/type` |
| `scaleIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/4/parameters/pitchSource/scaleIds` |

### directionPitchSource/oneOf/3 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `type` | Yes / 必須 | `"explicitScale"` (const) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/type` |
| `scale` | Yes / 必須 | [directionPitchCollection](#def-defs-directionpitchcollection) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/1/parameters/pitchSource/scale` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "effectiveKeyScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "songScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "harmonyScales"
        },
        "scaleIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "type",
        "scaleIds"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "explicitScale"
        },
        "scale": {
          "$ref": "#/$defs/directionPitchCollection"
        }
      },
      "required": [
        "type",
        "scale"
      ],
      "additionalProperties": false
    }
  ],
  "description": "Source of pitch vocabulary for an improvisation Direction."
}
```


<a id="def-defs-improvisationdirectionparameters"></a>
## improvisationDirectionParameters

**Schema pointer:** `#/$defs/improvisationDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

### improvisationDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `pitchSource` | Yes / 必須 | [directionPitchSource](#def-defs-directionpitchsource) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/parameters/pitchSource` |
| `adherence` | Yes / 必須 | enum | enum=["strict","preferred"] | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/parameters/adherence` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "pitchSource": {
      "$ref": "#/$defs/directionPitchSource"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "pitchSource",
    "adherence"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-playingroledirectionparameters"></a>
## playingRoleDirectionParameters

**Schema pointer:** `#/$defs/playingRoleDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

### playingRoleDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `role` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/parameters/role` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "role"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-pitchrangedirectionparameters"></a>
## pitchRangeDirectionParameters

**Schema pointer:** `#/$defs/pitchRangeDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

### pitchRangeDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `lowPitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/parameters/lowPitch` |
| `highPitch` | Yes / 必須 | [pitch](#def-defs-pitch) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/parameters/highPitch` |
| `constraint` | Yes / 必須 | enum | enum=["strict","preferred"] | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/parameters/constraint` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    },
    "constraint": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "lowPitch",
    "highPitch",
    "constraint"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vendordirectionparameters"></a>
## vendorDirectionParameters

**Schema pointer:** `#/$defs/vendorDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

### vendorDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `namespace` | Yes / 必須 | string | minLength=3; pattern="^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$" | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/parameters/namespace` |
| `name` | Yes / 必須 | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/parameters/name` |
| `version` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/parameters/version` |
| `data` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/parameters/data` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "minLength": 3,
      "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
      "not": {
        "pattern": "^org\\.ostf(?:\\.|$)"
      }
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": "object"
    }
  },
  "required": [
    "namespace",
    "name",
    "data"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-improvisationdirection"></a>
## improvisationDirection

**Schema pointer:** `#/$defs/improvisationDirection`. Reachable from release root / 公開ルートから到達可能。

### improvisationDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/1/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/1/instruction` |
| `type` | Yes / 必須 | `"improvisation"` (const) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/type` |
| `parameters` | Yes / 必須 | [improvisationDirectionParameters](#def-defs-improvisationdirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "improvisation"
    },
    "parameters": {
      "$ref": "#/$defs/improvisationDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-playingroledirection"></a>
## playingRoleDirection

**Schema pointer:** `#/$defs/playingRoleDirection`. Reachable from release root / 公開ルートから到達可能。

### playingRoleDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/0/instruction` |
| `type` | Yes / 必須 | `"playingRole"` (const) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/type` |
| `parameters` | Yes / 必須 | [playingRoleDirectionParameters](#def-defs-playingroledirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "playingRole"
    },
    "parameters": {
      "$ref": "#/$defs/playingRoleDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-pitchrangedirection"></a>
## pitchRangeDirection

**Schema pointer:** `#/$defs/pitchRangeDirection`. Reachable from release root / 公開ルートから到達可能。

### pitchRangeDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/instruction` |
| `type` | Yes / 必須 | `"pitchRange"` (const) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/type` |
| `parameters` | Yes / 必須 | [pitchRangeDirectionParameters](#def-defs-pitchrangedirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/5/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "pitchRange"
    },
    "parameters": {
      "$ref": "#/$defs/pitchRangeDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vendorrangedirection"></a>
## vendorRangeDirection

**Schema pointer:** `#/$defs/vendorRangeDirection`. Reachable from release root / 公開ルートから到達可能。

### vendorRangeDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/id` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/instruction` |
| `type` | Yes / 必須 | `"vendor"` (const) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/type` |
| `parameters` | Yes / 必須 | [vendorDirectionParameters](#def-defs-vendordirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/6/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vendorpointdirection"></a>
## vendorPointDirection

**Schema pointer:** `#/$defs/vendorPointDirection`. Reachable from release root / 公開ルートから到達可能。

### vendorPointDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/id` |
| `at` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/at` |
| `type` | Yes / 必須 | `"vendor"` (const) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/type` |
| `parameters` | Yes / 必須 | [vendorDirectionParameters](#def-defs-vendordirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/parameters` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/directions/2/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative. | [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf)<br>`/tracks/0/directions/2/instruction` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
    }
  },
  "required": [
    "id",
    "at",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-trackdirection"></a>
## trackDirection

**Schema pointer:** `#/$defs/trackDirection`. Reachable from release root / 公開ルートから到達可能。

Typed semantic instruction owned by a track and positioned on the OSTF global timebase.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/improvisationDirection"
    },
    {
      "$ref": "#/$defs/playingRoleDirection"
    },
    {
      "$ref": "#/$defs/pitchRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorPointDirection"
    },
    {
      "$ref": "#/$defs/phrasingDirection"
    },
    {
      "$ref": "#/$defs/vocalFreedomDirection"
    }
  ],
  "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
}
```


<a id="def-defs-vocalphonetics"></a>
## vocalPhonetics

**Schema pointer:** `#/$defs/vocalPhonetics`. Reachable from release root / 公開ルートから到達可能。

Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.

### vocalPhonetics — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `alphabet` | Yes / 必須 | enum | enum=["ipa","xsampa","arpabet","other"] | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics/0/alphabet` |
| `language` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics/0/language` |
| `symbols` | Yes / 必須 | array | minItems=1; items: string | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics/0/symbols` |
| `namespace` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics/1/namespace` |
| `preferred` | Optional / 任意（条件付きの場合あり） | boolean | Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/units/0/phonetics/0/preferred` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
  "properties": {
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "language": {
      "type": "string",
      "minLength": 1
    },
    "symbols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "preferred": {
      "type": "boolean",
      "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
    }
  },
  "required": [
    "alphabet",
    "symbols"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```


<a id="def-defs-vocalprofile"></a>
## vocalProfile

**Schema pointer:** `#/$defs/vocalProfile`. Reachable from release root / 公開ルートから到達可能。

Voice default independent of commercial singer preset or license.

### vocalProfile — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `language` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/voices/0/vocalProfile/language` |
| `deliveryMode` | Optional / 任意（条件付きの場合あり） | enum | enum=["sing","rap","speak","hum"] | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/voices/0/vocalProfile/deliveryMode` |
| `voiceDescription` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/lyrics/voices/0/vocalProfile/voiceDescription` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Voice default independent of commercial singer preset or license.",
  "properties": {
    "language": {
      "type": "string",
      "minLength": 1
    },
    "deliveryMode": {
      "enum": [
        "sing",
        "rap",
        "speak",
        "hum"
      ]
    },
    "voiceDescription": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": false
}
```


<a id="def-defs-vocalperformance"></a>
## vocalPerformance

**Schema pointer:** `#/$defs/vocalPerformance`. Reachable from release root / 公開ルートから到達可能。

Performance belonging to exactly one lyric voice within a containing clip.

### vocalPerformance — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/id` |
| `voiceId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/voiceId` |
| `phonemeEvents` | Optional / 任意（条件付きの場合あり） | array | items: vocalPhonemeEvent | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents` |
| `pitchCurves` | Optional / 任意（条件付きの場合あり） | array | items: vocalPitchCurve | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves` |
| `expressionCurves` | Optional / 任意（条件付きの場合あり） | array | items: vocalExpressionCurve | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves` |
| `techniques` | Optional / 任意（条件付きの場合あり） | array | items: vocalTechnique | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques` |
| `breathEvents` | Optional / 任意（条件付きの場合あり） | array | items: vocalBreathEvent | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents` |
| `noteIds` | Optional / 任意（条件付きの場合あり） | array | minItems=1; uniqueItems=true; items: id; Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds. | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/noteIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Performance belonging to exactly one lyric voice within a containing clip.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "phonemeEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonemeEvent"
      }
    },
    "pitchCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPitchCurve"
      }
    },
    "expressionCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalExpressionCurve"
      }
    },
    "techniques": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalTechnique"
      }
    },
    "breathEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalBreathEvent"
      }
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
    }
  },
  "required": [
    "id",
    "voiceId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocalphonemeevent"></a>
## vocalPhonemeEvent

**Schema pointer:** `#/$defs/vocalPhonemeEvent`. Reachable from release root / 公開ルートから到達可能。

Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.

### vocalPhonemeEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/id` |
| `unitId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/unitId` |
| `noteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/noteId` |
| `alphabet` | Yes / 必須 | enum | enum=["ipa","xsampa","arpabet","other"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/alphabet` |
| `namespace` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/namespace` |
| `symbol` | Yes / 必須 | string | minLength=1 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/symbol` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/duration` |
| `order` | Optional / 任意（条件付きの場合あり） | integer | Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority. | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/phonemeEvents/0/order` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitId": {
      "$ref": "#/$defs/id"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "symbol": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "order": {
      "type": "integer",
      "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
    }
  },
  "required": [
    "id",
    "unitId",
    "alphabet",
    "symbol",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```


<a id="def-defs-vocalcurvepointpitch"></a>
## vocalCurvePointPitch

**Schema pointer:** `#/$defs/vocalCurvePointPitch`. Reachable from release root / 公開ルートから到達可能。

### vocalCurvePointPitch — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points/0/at` |
| `value` | Yes / 必須 | number | Semitone offset from the targeted MIDI note, in cents (signed). | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points/0/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocalcurvepointnormalized"></a>
## vocalCurvePointNormalized

**Schema pointer:** `#/$defs/vocalCurvePointNormalized`. Reachable from release root / 公開ルートから到達可能。

### vocalCurvePointNormalized — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `at` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points/0/at` |
| `value` | Yes / 必須 | number | minimum=0; maximum=1 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points/0/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocalpitchcurve"></a>
## vocalPitchCurve

**Schema pointer:** `#/$defs/vocalPitchCurve`. Reachable from release root / 公開ルートから到達可能。

Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.

### vocalPitchCurve — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/id` |
| `targetNoteId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/targetNoteId` |
| `unit` | Yes / 必須 | `"cents"` (const) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/unit` |
| `interpolation` | Yes / 必須 | enum | enum=["step","linear"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/interpolation` |
| `points` | Yes / 必須 | array | minItems=1; items: vocalCurvePointPitch | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/pitchCurves/0/points` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    },
    "unit": {
      "const": "cents"
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointPitch"
      }
    }
  },
  "required": [
    "id",
    "targetNoteId",
    "unit",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocalexpressioncurve"></a>
## vocalExpressionCurve

**Schema pointer:** `#/$defs/vocalExpressionCurve`. Reachable from release root / 公開ルートから到達可能。

Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.

### vocalExpressionCurve — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/id` |
| `parameter` | Yes / 必須 | enum | enum=["dynamics","breathiness","tension","brightness","voicing"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/parameter` |
| `interpolation` | Yes / 必須 | enum | enum=["step","linear"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/interpolation` |
| `points` | Yes / 必須 | array | minItems=1; items: vocalCurvePointNormalized | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/points` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves. | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/expressionCurves/0/targetNoteId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "parameter": {
      "enum": [
        "dynamics",
        "breathiness",
        "tension",
        "brightness",
        "voicing"
      ]
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointNormalized"
      }
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
    }
  },
  "required": [
    "id",
    "parameter",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocaltechnique"></a>
## vocalTechnique

**Schema pointer:** `#/$defs/vocalTechnique`. Reachable from release root / 公開ルートから到達可能。

Semantic artistic intention, not deterministic rendering or an extra pitch source.

### vocalTechnique — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/duration` |
| `kind` | Yes / 必須 | enum | enum=["scoop","fall","vibrato","portamento","legato","staccato","accent","whisper","growl","falsetto","humming","rap","melisma"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/kind` |
| `intensity` | Optional / 任意（条件付きの場合あり） | number | minimum=0; maximum=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/intensity` |
| `targetNoteId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/techniques/0/targetNoteId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "scoop",
        "fall",
        "vibrato",
        "portamento",
        "legato",
        "staccato",
        "accent",
        "whisper",
        "growl",
        "falsetto",
        "humming",
        "rap",
        "melisma"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-vocalbreathevent"></a>
## vocalBreathEvent

**Schema pointer:** `#/$defs/vocalBreathEvent`. Reachable from release root / 公開ルートから到達可能。

Optional breath marker. The renderer decides whether to synthesize audible breath.

### vocalBreathEvent — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/id` |
| `start` | Yes / 必須 | [signed](#def-defs-signed) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/duration` |
| `kind` | Yes / 必須 | enum | enum=["inhale","exhale"] | [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/kind` |
| `intensity` | Optional / 任意（条件付きの場合あり） | number | minimum=0; maximum=1 | [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf)<br>`/tracks/0/clips/0/vocalPerformances/0/breathEvents/0/intensity` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "inhale",
        "exhale"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-positiveintrange"></a>
## positiveIntRange

**Schema pointer:** `#/$defs/positiveIntRange`. Reachable from release root / 公開ルートから到達可能。

Inclusive tick bounds; semantic check min <= max.

### positiveIntRange — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `min` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/phraseLengthTicks/min` |
| `max` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/phraseLengthTicks/max` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "min": {
      "$ref": "#/$defs/positive"
    },
    "max": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive tick bounds; semantic check min <= max."
}
```


<a id="def-defs-nonnegativenumberrange"></a>
## nonnegativeNumberRange

**Schema pointer:** `#/$defs/nonnegativeNumberRange`. Reachable from release root / 公開ルートから到達可能。

Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset.

### nonnegativeNumberRange — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `min` | Yes / 必須 | number | minimum=0; maximum=128 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/onsetGroupsPerQuarter/min` |
| `max` | Yes / 必須 | number | minimum=0; maximum=128 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/onsetGroupsPerQuarter/max` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "min": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    },
    "max": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset."
}
```


<a id="def-defs-phrasingdirectionparameters"></a>
## phrasingDirectionParameters

**Schema pointer:** `#/$defs/phrasingDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.

### phrasingDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `phraseLengthTicks` | Optional / 任意（条件付きの場合あり） | [positiveIntRange](#def-defs-positiveintrange) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/phraseLengthTicks` |
| `onsetGroupsPerQuarter` | Optional / 任意（条件付きの場合あり） | [nonnegativeNumberRange](#def-defs-nonnegativenumberrange) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/onsetGroupsPerQuarter` |
| `development` | Optional / 任意（条件付きの場合あり） | enum | enum=["repetition","motivicVariation","sequence","contrast","free"] | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/development` |
| `contour` | Optional / 任意（条件付きの場合あり） | enum | enum=["ascending","descending","arch","valley","stable","free"] | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/contour` |
| `energyShape` | Optional / 任意（条件付きの場合あり） | enum | enum=["rising","falling","arch","valley","stable","free"]; Abstract musical-energy direction; not equivalent to output velocity or volume. | [09-techno-variation.ostf](../examples/09-techno-variation.ostf)<br>`/tracks/0/directions/0/parameters/energyShape` |
| `motifRef` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [20-phrasing-with-motif-reference.ostf](../examples/20-phrasing-with-motif-reference.ostf)<br>`/tracks/0/directions/0/parameters/motifRef` |
| `adherence` | Yes / 必須 | enum | enum=["strict","preferred"] | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters/adherence` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "phraseLengthTicks": {
      "$ref": "#/$defs/positiveIntRange"
    },
    "onsetGroupsPerQuarter": {
      "$ref": "#/$defs/nonnegativeNumberRange"
    },
    "development": {
      "enum": [
        "repetition",
        "motivicVariation",
        "sequence",
        "contrast",
        "free"
      ]
    },
    "contour": {
      "enum": [
        "ascending",
        "descending",
        "arch",
        "valley",
        "stable",
        "free"
      ]
    },
    "energyShape": {
      "enum": [
        "rising",
        "falling",
        "arch",
        "valley",
        "stable",
        "free"
      ],
      "description": "Abstract musical-energy direction; not equivalent to output velocity or volume."
    },
    "motifRef": {
      "$ref": "#/$defs/id"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "adherence"
  ],
  "additionalProperties": false,
  "description": "At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.",
  "minProperties": 2
}
```


<a id="def-defs-phrasingdirection"></a>
## phrasingDirection

**Schema pointer:** `#/$defs/phrasingDirection`. Reachable from release root / 公開ルートから到達可能。

4.3 optional phrasing Track Direction, using global source-timeline ticks.

### phrasingDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/id` |
| `type` | Yes / 必須 | `"phrasing"` (const) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/type` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [20-phrasing-with-motif-reference.ostf](../examples/20-phrasing-with-motif-reference.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Non-executable music-text context, subordinate to structured fields. | [20-phrasing-with-motif-reference.ostf](../examples/20-phrasing-with-motif-reference.ostf)<br>`/tracks/0/directions/0/instruction` |
| `parameters` | Yes / 必須 | [phrasingDirectionParameters](#def-defs-phrasingdirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "phrasing"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/phrasingDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional phrasing Track Direction, using global source-timeline ticks."
}
```


<a id="def-defs-lyriccandidateset"></a>
## lyricCandidateSet

**Schema pointer:** `#/$defs/lyricCandidateSet`. Reachable from release root / 公開ルートから到達可能。

One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment.

### lyricCandidateSet — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `phraseIds` | Yes / 必須 | array | minItems=1; uniqueItems=true; items: id | [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf)<br>`/tracks/0/directions/0/parameters/candidatePhraseSets/0/phraseIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "phraseIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true
    }
  },
  "required": [
    "phraseIds"
  ],
  "additionalProperties": false,
  "description": "One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment."
}
```


<a id="def-defs-vocalfreedomdirectionparameters"></a>
## vocalFreedomDirectionParameters

**Schema pointer:** `#/$defs/vocalFreedomDirectionParameters`. Reachable from release root / 公開ルートから到達可能。

Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.

### vocalFreedomDirectionParameters — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `voiceId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters/voiceId` |
| `textPolicy` | Yes / 必須 | enum | enum=["fixed","alternatives","open"] | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters/textPolicy` |
| `melodyPolicy` | Yes / 必須 | enum | enum=["fixed","ornamentable","open"] | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters/melodyPolicy` |
| `vocalizationKind` | Optional / 任意（条件付きの場合あり） | enum | enum=["lexical","scat","humming","nonLexical"] | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters/vocalizationKind` |
| `candidatePhraseSets` | Optional / 任意（条件付きの場合あり） | array | minItems=2; items: lyricCandidateSet | [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf)<br>`/tracks/0/directions/0/parameters/candidatePhraseSets` |
| `adherence` | Yes / 必須 | enum | enum=["strict","preferred"] | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters/adherence` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "textPolicy": {
      "enum": [
        "fixed",
        "alternatives",
        "open"
      ]
    },
    "melodyPolicy": {
      "enum": [
        "fixed",
        "ornamentable",
        "open"
      ]
    },
    "vocalizationKind": {
      "enum": [
        "lexical",
        "scat",
        "humming",
        "nonLexical"
      ]
    },
    "candidatePhraseSets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricCandidateSet"
      },
      "minItems": 2
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "voiceId",
    "textPolicy",
    "melodyPolicy",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.",
  "if": {
    "properties": {
      "textPolicy": {
        "const": "alternatives"
      }
    },
    "required": [
      "textPolicy"
    ]
  },
  "then": {
    "required": [
      "candidatePhraseSets"
    ]
  },
  "else": {
    "not": {
      "required": [
        "candidatePhraseSets"
      ]
    }
  }
}
```


<a id="def-defs-vocalfreedomdirection"></a>
## vocalFreedomDirection

**Schema pointer:** `#/$defs/vocalFreedomDirection`. Reachable from release root / 公開ルートから到達可能。

4.3 optional vocalFreedom Track Direction, using global source-timeline ticks.

### vocalFreedomDirection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/id` |
| `type` | Yes / 必須 | `"vocalFreedom"` (const) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/type` |
| `start` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/start` |
| `duration` | Yes / 必須 | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/duration` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [19-concurrent-voice-directions.ostf](../examples/19-concurrent-voice-directions.ostf)<br>`/tracks/0/directions/0/label` |
| `instruction` | Optional / 任意（条件付きの場合あり） | string | Non-executable music-text context, subordinate to structured fields. | [19-concurrent-voice-directions.ostf](../examples/19-concurrent-voice-directions.ostf)<br>`/tracks/0/directions/0/instruction` |
| `parameters` | Yes / 必須 | [vocalFreedomDirectionParameters](#def-defs-vocalfreedomdirectionparameters) | See exact schema / 厳密な定義は下記Schema。 | [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf)<br>`/tracks/0/directions/0/parameters` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "vocalFreedom"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/vocalFreedomDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional vocalFreedom Track Direction, using global source-timeline ticks."
}
```


<a id="def-defs-performancerequirements"></a>
## performanceRequirements

**Schema pointer:** `#/$defs/performanceRequirements`. Reachable from release root / 公開ルートから到達可能。

Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.

### performanceRequirements — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `requiredPolyphony` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=128 | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/requiredPolyphony` |
| `requiredPitchRange` | Optional / 任意（条件付きの場合あり） | [playablePitchRange](#def-defs-playablepitchrange) | See exact schema / 厳密な定義は下記Schema。 | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/requiredPitchRange` |
| `requiredArticulations` | Optional / 任意（条件付きの場合あり） | array | minItems=1; uniqueItems=true; items: string | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/requiredArticulations` |
| `peakOnsetGroupsPerQuarter` | Optional / 任意（条件付きの場合あり） | number | maximum=128; exclusiveMinimum=0 | [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf)<br>`/tracks/0/performanceRequirements/peakOnsetGroupsPerQuarter` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "requiredPolyphony": {
      "type": "integer",
      "minimum": 1,
      "maximum": 128
    },
    "requiredPitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    },
    "requiredArticulations": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "peakOnsetGroupsPerQuarter": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 128
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.",
  "minProperties": 1
}
```


<a id="def-defs-performancescope"></a>
## performanceScope

**Schema pointer:** `#/$defs/performanceScope`. Reachable from release root / 公開ルートから到達可能。

Bind to exactly one finite visit within a specific plan.

### performanceScope — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `performancePlanId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [12-visit-scoped-response.ostf](../examples/12-visit-scoped-response.ostf)<br>`/ensembleInteractions/0/scope/performancePlanId` |
| `visitId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [12-visit-scoped-response.ostf](../examples/12-visit-scoped-response.ostf)<br>`/ensembleInteractions/0/scope/visitId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "performancePlanId": {
      "$ref": "#/$defs/id"
    },
    "visitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "performancePlanId",
    "visitId"
  ],
  "additionalProperties": false,
  "description": "Bind to exactly one finite visit within a specific plan."
}
```


<a id="def-defs-ensembleinteraction"></a>
## ensembleInteraction

**Schema pointer:** `#/$defs/ensembleInteraction`. Reachable from release root / 公開ルートから到達可能。

Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).

### ensembleInteraction — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/id` |
| `actorTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/actorTrackId` |
| `partnerTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/partnerTrackId` |
| `actorVoiceId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [08-gospel-response.ostf](../examples/08-gospel-response.ostf)<br>`/ensembleInteractions/0/actorVoiceId` |
| `partnerVoiceId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [08-gospel-response.ostf](../examples/08-gospel-response.ostf)<br>`/ensembleInteractions/0/partnerVoiceId` |
| `relation` | Yes / 必須 | enum | enum=["respondTo","followRhythm","alternateWith","leaveSpaceFor","reinforce"] | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/relation` |
| `start` | Optional / 任意（条件付きの場合あり） | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/start` |
| `duration` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/duration` |
| `scope` | Optional / 任意（条件付きの場合あり） | [performanceScope](#def-defs-performancescope) | See exact schema / 厳密な定義は下記Schema。 | [12-visit-scoped-response.ostf](../examples/12-visit-scoped-response.ostf)<br>`/ensembleInteractions/0/scope` |
| `responseWindowTicks` | Optional / 任意（条件付きの場合あり） | [positive](#def-defs-positive) | See exact schema / 厳密な定義は下記Schema。 | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/responseWindowTicks` |
| `adherence` | Yes / 必須 | enum | enum=["strict","preferred"] | [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf)<br>`/ensembleInteractions/0/adherence` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "actorTrackId": {
      "$ref": "#/$defs/id"
    },
    "partnerTrackId": {
      "$ref": "#/$defs/id"
    },
    "actorVoiceId": {
      "$ref": "#/$defs/id"
    },
    "partnerVoiceId": {
      "$ref": "#/$defs/id"
    },
    "relation": {
      "enum": [
        "respondTo",
        "followRhythm",
        "alternateWith",
        "leaveSpaceFor",
        "reinforce"
      ]
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "scope": {
      "$ref": "#/$defs/performanceScope"
    },
    "responseWindowTicks": {
      "$ref": "#/$defs/positive"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "id",
    "actorTrackId",
    "partnerTrackId",
    "relation",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).",
  "anyOf": [
    {
      "required": [
        "start",
        "duration"
      ]
    },
    {
      "required": [
        "scope"
      ]
    }
  ],
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```


<a id="def-defs-visitpart"></a>
## visitPart

**Schema pointer:** `#/$defs/visitPart`. Reachable from release root / 公開ルートから到達可能。

A part rule within one performance visit, not a mutation of the source Track.

### visitPart — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `trackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/parts/0/trackId` |
| `role` | Optional / 任意（条件付きの場合あり） | string | minLength=1; Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement. | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/parts/0/role` |
| `realization` | Yes / 必須 | enum | enum=["fixed","open","silent"] | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/parts/0/realization` |
| `replacesDirectionIds` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: id; Only explicit source-track playingRole Direction IDs may be replaced by the visit role. | [18-visit-role-override.ostf](../examples/18-visit-role-override.ostf)<br>`/performancePlans/0/visits/1/parts/0/replacesDirectionIds` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement."
    },
    "realization": {
      "enum": [
        "fixed",
        "open",
        "silent"
      ]
    },
    "replacesDirectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "description": "Only explicit source-track playingRole Direction IDs may be replaced by the visit role."
    }
  },
  "required": [
    "trackId",
    "realization"
  ],
  "additionalProperties": false,
  "description": "A part rule within one performance visit, not a mutation of the source Track."
}
```


<a id="def-defs-performancevisit"></a>
## performanceVisit

**Schema pointer:** `#/$defs/performanceVisit`. Reachable from release root / 公開ルートから到達可能。

Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.

### performanceVisit — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/id` |
| `ordinal` | Yes / 必須 | [nonnegative](#def-defs-nonnegative) | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/ordinal` |
| `label` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [23-range-visit-and-label.ostf](../examples/23-range-visit-and-label.ostf)<br>`/performancePlans/0/visits/0/label` |
| `sourceSectionIds` | Optional / 任意（条件付きの場合あり） | array | minItems=1; items: id | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/sourceSectionIds` |
| `sourceRange` | Optional / 任意（条件付きの場合あり） | [range](#def-defs-range) | See exact schema / 厳密な定義は下記Schema。 | [23-range-visit-and-label.ostf](../examples/23-range-visit-and-label.ostf)<br>`/performancePlans/0/visits/0/sourceRange` |
| `parts` | Yes / 必須 | array | items: visitPart | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits/0/parts` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "ordinal": {
      "$ref": "#/$defs/nonnegative"
    },
    "label": {
      "type": "string"
    },
    "sourceSectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1
    },
    "sourceRange": {
      "$ref": "#/$defs/range"
    },
    "parts": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/visitPart"
      }
    }
  },
  "required": [
    "id",
    "ordinal",
    "parts"
  ],
  "additionalProperties": false,
  "description": "Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.",
  "oneOf": [
    {
      "required": [
        "sourceSectionIds"
      ]
    },
    {
      "required": [
        "sourceRange"
      ]
    }
  ],
  "not": {
    "required": [
      "sourceSectionIds",
      "sourceRange"
    ]
  }
}
```


<a id="def-defs-performanceplan"></a>
## performancePlan

**Schema pointer:** `#/$defs/performancePlan`. Reachable from release root / 公開ルートから到達可能。

Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state.

### performancePlan — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/id` |
| `name` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/name` |
| `mode` | Yes / 必須 | `"orderedFinite"` (const) | See exact schema / 厳密な定義は下記Schema。 | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/mode` |
| `defaultRealization` | Yes / 必須 | enum | enum=["fixed","silent","unspecified"]; Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay. | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/defaultRealization` |
| `visits` | Yes / 必須 | array | minItems=1; items: performanceVisit | [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf)<br>`/performancePlans/0/visits` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "mode": {
      "const": "orderedFinite"
    },
    "defaultRealization": {
      "enum": [
        "fixed",
        "silent",
        "unspecified"
      ],
      "description": "Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay."
    },
    "visits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performanceVisit"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "mode",
    "defaultRealization",
    "visits"
  ],
  "additionalProperties": false,
  "description": "Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state."
}
```
