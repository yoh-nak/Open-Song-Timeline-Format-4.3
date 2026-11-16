# Production Session 0.2.0 — Complete Parameter Reference / 全項目リファレンス

**Release edition: 4.3.0 · 2026-11-16.** No wire-format fields are added by this reference.

Authoritative structure: [`ostf-production-session-0.2.schema.json`](../schema/ostf-production-session-0.2.schema.json). SHA-256: `1ac57129bfc1def9d5e1529b32d3905495c86e0d0b1f7530199a4dce72037e29`.

全てのルート項目・`$defs`・入れ子の旧形式定義・条件付き制約を掲載します。型、必須条件、列挙値、数値範囲、既定値、参照先を原Schemaから転記し、収録サンプルのファイル名とJSON Pointerを対応付けています。条件分岐の必須性は、その分岐が適用される場合の条件です。省略可能な値を保存時に勝手に補完する意味ではありません。

The exact schema blocks preserve every validation keyword. Historical Draft labels inside the frozen schema annotations do not alter the adopted release version; see [edition and authority guide](RELEASE_READINESS.md). No execution, asset retrieval or synthesis permission follows from valid data.

**Coverage:** 103/103 reachable parameter declarations; 45/45 enum literals; 7/7 positive union branches. [Detailed coverage](COVERAGE_REPORT.md).

## Definition index / 定義索引

- [Root](#def-)
- [id](#def-defs-id)
- [sha256](#def-defs-sha256)
- [score](#def-defs-score)
- [channel](#def-defs-channel)
- [send](#def-defs-send)
- [device](#def-defs-device)
- [plugin](#def-defs-plugin)
- [asset](#def-defs-asset)
- [automation](#def-defs-automation)
- [automationTarget](#def-defs-automationtarget)
- [point](#def-defs-point)
- [hostExtension](#def-defs-hostextension)
- [audioRegion](#def-defs-audioregion)
- [sidechainConnection](#def-defs-sidechainconnection)

<a id="def-"></a>
## Root

**Schema pointer:** `#`. Reachable from release root / 公開ルートから到達可能。

Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.

### Root — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `profile` | Yes / 必須 | `"OSTF-Production-Session"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/profile` |
| `profileVersion` | Yes / 必須 | `"0.2.0"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/profileVersion` |
| `score` | Yes / 必須 | [score](#def-defs-score) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score` |
| `channels` | Yes / 必須 | array | minItems=1; items: channel | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels` |
| `devices` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: device | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices` |
| `assets` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: asset | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets` |
| `automation` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: automation | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation` |
| `notes` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/notes` |
| `hostExtensions` | Optional / 任意（条件付きの場合あり） | array | items: hostExtension | [04-complete-production-02.json](../examples/production/04-complete-production-02.json)<br>`/hostExtensions` |
| `audioRegions` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: audioRegion; Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions` |
| `sidechainConnections` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: sidechainConnection; Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-production-session-0.2.schema.json",
  "title": "OSTF Production Session Profile 0.2.0 (Draft 0.15; not ratified)",
  "description": "Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "profile": {
      "const": "OSTF-Production-Session"
    },
    "profileVersion": {
      "const": "0.2.0"
    },
    "score": {
      "$ref": "#/$defs/score"
    },
    "channels": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/channel"
      },
      "minItems": 1
    },
    "devices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/device"
      },
      "minItems": 0
    },
    "assets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/asset"
      },
      "minItems": 0
    },
    "automation": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/automation"
      },
      "minItems": 0
    },
    "notes": {
      "type": "string"
    },
    "hostExtensions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/hostExtension"
      }
    },
    "audioRegions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/audioRegion"
      },
      "minItems": 0,
      "description": "Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes."
    },
    "sidechainConnections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sidechainConnection"
      },
      "minItems": 0,
      "description": "Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing."
    }
  },
  "required": [
    "profile",
    "profileVersion",
    "score",
    "channels"
  ]
}
```


<a id="def-defs-id"></a>
## id

**Schema pointer:** `#/$defs/id`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "minLength": 1,
  "pattern": "^\\S+$"
}
```


<a id="def-defs-sha256"></a>
## sha256

**Schema pointer:** `#/$defs/sha256`. Reachable from release root / 公開ルートから到達可能。

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$"
}
```


<a id="def-defs-score"></a>
## score

**Schema pointer:** `#/$defs/score`. Reachable from release root / 公開ルートから到達可能。

### score — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `formatVersion` | Yes / 必須 | `"4.3.0"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score/formatVersion` |
| `sha256` | Yes / 必須 | [sha256](#def-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score/sha256` |
| `documentId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score/documentId` |
| `revisionId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score/revisionId` |
| `sourceUri` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/score/sourceUri` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "formatVersion": {
      "const": "4.3.0"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "sourceUri": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "formatVersion",
    "sha256"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-channel"></a>
## channel

**Schema pointer:** `#/$defs/channel`. Reachable from release root / 公開ルートから到達可能。

### channel — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/id` |
| `kind` | Yes / 必須 | enum | enum=["track","audioTrack","bus","master"]; audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1. | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/kind` |
| `name` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/name` |
| `trackId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/trackId` |
| `audioChannels` | Yes / 必須 | enum | enum=[1,2] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/audioChannels` |
| `gainDb` | Yes / 必須 | number | minimum=-120; maximum=24 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/gainDb` |
| `pan` | Yes / 必須 | number | minimum=-1; maximum=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/pan` |
| `mute` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/mute` |
| `solo` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/solo` |
| `soloSafe` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/soloSafe` |
| `outputChannelId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/outputChannelId` |
| `deviceIds` | Yes / 必須 | array | minItems=0; uniqueItems=true; items: id | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/deviceIds` |
| `sends` | Optional / 任意（条件付きの場合あり） | array | minItems=0; items: send | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends` |

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
        "track",
        "audioTrack",
        "bus",
        "master"
      ],
      "description": "audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1."
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "audioChannels": {
      "enum": [
        1,
        2
      ]
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "pan": {
      "type": "number",
      "minimum": -1,
      "maximum": 1
    },
    "mute": {
      "type": "boolean"
    },
    "solo": {
      "type": "boolean"
    },
    "soloSafe": {
      "type": "boolean"
    },
    "outputChannelId": {
      "$ref": "#/$defs/id"
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 0,
      "uniqueItems": true
    },
    "sends": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/send"
      },
      "minItems": 0
    }
  },
  "required": [
    "id",
    "kind",
    "audioChannels",
    "gainDb",
    "pan",
    "mute",
    "solo",
    "soloSafe",
    "deviceIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-send"></a>
## send

**Schema pointer:** `#/$defs/send`. Reachable from release root / 公開ルートから到達可能。

### send — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends/0/id` |
| `targetChannelId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends/0/targetChannelId` |
| `gainDb` | Yes / 必須 | number | minimum=-120; maximum=24 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends/0/gainDb` |
| `preFader` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends/0/preFader` |
| `enabled` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/channels/0/sends/0/enabled` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetChannelId": {
      "$ref": "#/$defs/id"
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "preFader": {
      "type": "boolean"
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "targetChannelId",
    "gainDb",
    "preFader",
    "enabled"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-device"></a>
## device

**Schema pointer:** `#/$defs/device`. Reachable from release root / 公開ルートから到達可能。

### device — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/id` |
| `role` | Yes / 必須 | enum | enum=["instrument","effect","utility"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/role` |
| `plugin` | Yes / 必須 | [plugin](#def-defs-plugin) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/plugin` |
| `enabled` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/enabled` |
| `bypass` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/bypass` |
| `stateAssetId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/stateAssetId` |
| `onUnavailable` | Optional / 任意（条件付きの場合あり） | enum | enum=["reportAndPreserve","preserveAndBypass","preserveAndSilence"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/onUnavailable` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "enum": [
        "instrument",
        "effect",
        "utility"
      ]
    },
    "plugin": {
      "$ref": "#/$defs/plugin"
    },
    "enabled": {
      "type": "boolean"
    },
    "bypass": {
      "type": "boolean"
    },
    "stateAssetId": {
      "$ref": "#/$defs/id"
    },
    "onUnavailable": {
      "enum": [
        "reportAndPreserve",
        "preserveAndBypass",
        "preserveAndSilence"
      ]
    }
  },
  "required": [
    "id",
    "role",
    "plugin",
    "enabled",
    "bypass"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-plugin"></a>
## plugin

**Schema pointer:** `#/$defs/plugin`. Reachable from release root / 公開ルートから到達可能。

### plugin — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `format` | Yes / 必須 | enum | enum=["vst2","vst3","clap","au","aax","builtin","hostNative","other"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/plugin/format` |
| `pluginId` | Yes / 必須 | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/plugin/pluginId` |
| `vendor` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/plugin/vendor` |
| `name` | Yes / 必須 | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/devices/0/plugin/name` |
| `version` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [04-complete-production-02.json](../examples/production/04-complete-production-02.json)<br>`/devices/0/plugin/version` |
| `namespace` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/devices/4/plugin/namespace` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "format": {
      "enum": [
        "vst2",
        "vst3",
        "clap",
        "au",
        "aax",
        "builtin",
        "hostNative",
        "other"
      ]
    },
    "pluginId": {
      "type": "string",
      "minLength": 1
    },
    "vendor": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "format",
    "pluginId",
    "name"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-asset"></a>
## asset

**Schema pointer:** `#/$defs/asset`. Reachable from release root / 公開ルートから到達可能。

Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON.

### asset — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/id` |
| `purpose` | Yes / 必須 | enum | enum=["pluginState","renderedAudio","other","audioSource"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/purpose` |
| `uri` | Yes / 必須 | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/uri` |
| `sha256` | Yes / 必須 | [sha256](#def-defs-sha256) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/sha256` |
| `mediaType` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/mediaType` |
| `byteLength` | Optional / 任意（条件付きの場合あり） | integer | minimum=0 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/assets/0/byteLength` |
| `sampleRateHz` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; maximum=768000; Audio-source decoded sample frames per second; required only for purpose audioSource. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/assets/1/sampleRateHz` |
| `frameCount` | Optional / 任意（条件付きの場合あり） | integer | minimum=1; Number of decoded sample frames in the complete audio source asset; required for audioSource. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/assets/1/frameCount` |
| `audioChannels` | Optional / 任意（条件付きの場合あり） | enum | enum=[1,2]; Mono/stereo decoded source-channel count; required only for audioSource in 0.2. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/assets/1/audioChannels` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "purpose": {
      "enum": [
        "pluginState",
        "renderedAudio",
        "other",
        "audioSource"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "mediaType": {
      "type": "string",
      "minLength": 1
    },
    "byteLength": {
      "type": "integer",
      "minimum": 0
    },
    "sampleRateHz": {
      "type": "integer",
      "minimum": 1,
      "maximum": 768000,
      "description": "Audio-source decoded sample frames per second; required only for purpose audioSource."
    },
    "frameCount": {
      "type": "integer",
      "minimum": 1,
      "description": "Number of decoded sample frames in the complete audio source asset; required for audioSource."
    },
    "audioChannels": {
      "type": "integer",
      "enum": [
        1,
        2
      ],
      "description": "Mono/stereo decoded source-channel count; required only for audioSource in 0.2."
    }
  },
  "required": [
    "id",
    "purpose",
    "uri",
    "sha256"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "purpose": {
            "const": "audioSource"
          }
        },
        "required": [
          "purpose"
        ]
      },
      "then": {
        "required": [
          "sampleRateHz",
          "frameCount",
          "audioChannels",
          "mediaType"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "sampleRateHz"
              ]
            },
            {
              "required": [
                "frameCount"
              ]
            },
            {
              "required": [
                "audioChannels"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON."
}
```


<a id="def-defs-automation"></a>
## automation

**Schema pointer:** `#/$defs/automation`. Reachable from release root / 公開ルートから到達可能。

Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.

### automation — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/id` |
| `target` | Yes / 必須 | [automationTarget](#def-defs-automationtarget) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/target` |
| `valueType` | Yes / 必須 | enum | enum=["number","boolean"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/valueType` |
| `interpolation` | Yes / 必須 | enum | enum=["step","linear"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/interpolation` |
| `points` | Yes / 必須 | array | minItems=1; items: point | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/points` |

### automation/allOf/0/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `interpolation` | Optional / 任意（条件付きの場合あり） | `"step"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/1/interpolation` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "target": {
      "$ref": "#/$defs/automationTarget"
    },
    "valueType": {
      "enum": [
        "number",
        "boolean"
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
      "items": {
        "$ref": "#/$defs/point"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "target",
    "valueType",
    "interpolation",
    "points"
  ],
  "additionalProperties": false,
  "description": "Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.",
  "allOf": [
    {
      "if": {
        "properties": {
          "valueType": {
            "const": "boolean"
          }
        },
        "required": [
          "valueType"
        ]
      },
      "then": {
        "properties": {
          "interpolation": {
            "const": "step"
          }
        }
      }
    }
  ]
}
```


<a id="def-defs-automationtarget"></a>
## automationTarget

**Schema pointer:** `#/$defs/automationTarget`. Reachable from release root / 公開ルートから到達可能。

Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs.

### automationTarget/oneOf/0 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"channel"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/target/kind` |
| `channelId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/target/channelId` |
| `parameter` | Yes / 必須 | enum | enum=["gainDb","pan","mute"] | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/target/parameter` |

### automationTarget/oneOf/1 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"device"` (const) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/2/target/kind` |
| `deviceId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/2/target/deviceId` |
| `parameterId` | Yes / 必須 | string | minLength=1 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/2/target/parameterId` |

### automationTarget/oneOf/2 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"send"` (const) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/3/target/kind` |
| `sendId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/3/target/sendId` |
| `parameter` | Yes / 必須 | enum | enum=["gainDb","enabled"] | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/3/target/parameter` |

### automationTarget/oneOf/3 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"audioRegion"` (const) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/5/target/kind` |
| `audioRegionId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/5/target/audioRegionId` |
| `parameter` | Yes / 必須 | enum | enum=["gainDb","mute"] | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/5/target/parameter` |

### automationTarget/oneOf/4 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"deviceControl"` (const) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/7/target/kind` |
| `deviceId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/7/target/deviceId` |
| `parameter` | Yes / 必須 | enum | enum=["enabled","bypass"] | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/automation/7/target/parameter` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "channel"
        },
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "pan",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "channelId",
        "parameter"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "device"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameterId": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameterId"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "send"
        },
        "sendId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "enabled"
          ]
        }
      },
      "required": [
        "kind",
        "sendId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "audioRegion"
        },
        "audioRegionId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "audioRegionId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "deviceControl"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "enabled",
            "bypass"
          ]
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameter"
      ]
    }
  ],
  "description": "Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs."
}
```


<a id="def-defs-point"></a>
## point

**Schema pointer:** `#/$defs/point`. Reachable from release root / 公開ルートから到達可能。

### point — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `atTick` | Yes / 必須 | integer | minimum=0 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/points/0/atTick` |
| `value` | Yes / 必須 | composition / 分岐 | See exact schema / 厳密な定義は下記Schema。 | [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json)<br>`/automation/0/points/0/value` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "atTick": {
      "type": "integer",
      "minimum": 0
    },
    "value": {
      "oneOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean"
        }
      ]
    }
  },
  "required": [
    "atTick",
    "value"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-hostextension"></a>
## hostExtension

**Schema pointer:** `#/$defs/hostExtension`. Reachable from release root / 公開ルートから到達可能。

### hostExtension — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `namespace` | Yes / 必須 | string | pattern="^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$" | [04-complete-production-02.json](../examples/production/04-complete-production-02.json)<br>`/hostExtensions/0/namespace` |
| `version` | Optional / 任意（条件付きの場合あり） | string | minLength=1 | [04-complete-production-02.json](../examples/production/04-complete-production-02.json)<br>`/hostExtensions/0/version` |
| `data` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [04-complete-production-02.json](../examples/production/04-complete-production-02.json)<br>`/hostExtensions/0/data` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "pattern": "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$"
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
    "data"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-audioregion"></a>
## audioRegion

**Schema pointer:** `#/$defs/audioRegion`. Reachable from release root / 公開ルートから到達可能。

Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.

### audioRegion — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/id` |
| `channelId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/channelId` |
| `sourceAssetId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/sourceAssetId` |
| `startTick` | Yes / 必須 | integer | minimum=0 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/startTick` |
| `durationTicks` | Yes / 必須 | integer | minimum=1 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/durationTicks` |
| `sourceStartFrame` | Yes / 必須 | integer | minimum=0 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/sourceStartFrame` |
| `sourceFrameCount` | Yes / 必須 | integer | minimum=1 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/sourceFrameCount` |
| `playbackMode` | Yes / 必須 | enum | enum=["native","fit"]; native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/playbackMode` |
| `pitchPolicy` | Optional / 任意（条件付きの場合あり） | enum | enum=["preserve","followRate"]; Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/1/pitchPolicy` |
| `gainDb` | Yes / 必須 | number | minimum=-120; maximum=24 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/gainDb` |
| `mute` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/mute` |
| `fadeInTicks` | Optional / 任意（条件付きの場合あり） | integer | minimum=0 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/fadeInTicks` |
| `fadeOutTicks` | Optional / 任意（条件付きの場合あり） | integer | minimum=0 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/audioRegions/0/fadeOutTicks` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "channelId": {
      "$ref": "#/$defs/id"
    },
    "sourceAssetId": {
      "$ref": "#/$defs/id"
    },
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "sourceStartFrame": {
      "type": "integer",
      "minimum": 0
    },
    "sourceFrameCount": {
      "type": "integer",
      "minimum": 1
    },
    "playbackMode": {
      "enum": [
        "native",
        "fit"
      ],
      "description": "native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval."
    },
    "pitchPolicy": {
      "enum": [
        "preserve",
        "followRate"
      ],
      "description": "Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "mute": {
      "type": "boolean"
    },
    "fadeInTicks": {
      "type": "integer",
      "minimum": 0
    },
    "fadeOutTicks": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "id",
    "channelId",
    "sourceAssetId",
    "startTick",
    "durationTicks",
    "sourceStartFrame",
    "sourceFrameCount",
    "playbackMode",
    "gainDb",
    "mute"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "playbackMode": {
            "const": "fit"
          }
        },
        "required": [
          "playbackMode"
        ]
      },
      "then": {
        "required": [
          "pitchPolicy"
        ]
      },
      "else": {
        "not": {
          "required": [
            "pitchPolicy"
          ]
        }
      }
    }
  ]
}
```


<a id="def-defs-sidechainconnection"></a>
## sidechainConnection

**Schema pointer:** `#/$defs/sidechainConnection`. Reachable from release root / 公開ルートから到達可能。

Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.

### sidechainConnection — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `id` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/id` |
| `sourceChannelId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/sourceChannelId` |
| `targetDeviceId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/targetDeviceId` |
| `targetPortId` | Yes / 必須 | [id](#def-defs-id) | Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/targetPortId` |
| `tapPoint` | Yes / 必須 | enum | enum=["preFader","postFader"] | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/tapPoint` |
| `followMute` | Yes / 必須 | boolean | If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly. | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/followMute` |
| `gainDb` | Yes / 必須 | number | minimum=-120; maximum=24 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/gainDb` |
| `enabled` | Yes / 必須 | boolean | See exact schema / 厳密な定義は下記Schema。 | [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json)<br>`/sidechainConnections/0/enabled` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "sourceChannelId": {
      "$ref": "#/$defs/id"
    },
    "targetDeviceId": {
      "$ref": "#/$defs/id"
    },
    "targetPortId": {
      "$ref": "#/$defs/id",
      "description": "Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label."
    },
    "tapPoint": {
      "enum": [
        "preFader",
        "postFader"
      ]
    },
    "followMute": {
      "type": "boolean",
      "description": "If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "sourceChannelId",
    "targetDeviceId",
    "targetPortId",
    "tapPoint",
    "followMute",
    "gainDb",
    "enabled"
  ]
}
```
