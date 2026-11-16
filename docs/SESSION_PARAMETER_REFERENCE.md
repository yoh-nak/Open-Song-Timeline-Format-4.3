# Distributed Session 0.2 — Complete Parameter Reference / 全項目リファレンス

**Release edition: 4.3.0 · 2026-11-16.** No wire-format fields are added by this reference.

Authoritative structure: [`ostf-distributed-session-0.2.schema.json`](../schema/ostf-distributed-session-0.2.schema.json). SHA-256: `f79832adea0e48d6042c820a7d7a51e7a7288944bde833e255ce96c22b5ed0e7`.

全てのルート項目・`$defs`・入れ子の旧形式定義・条件付き制約を掲載します。型、必須条件、列挙値、数値範囲、既定値、参照先を原Schemaから転記し、収録サンプルのファイル名とJSON Pointerを対応付けています。条件分岐の必須性は、その分岐が適用される場合の条件です。省略可能な値を保存時に勝手に補完する意味ではありません。

The exact schema blocks preserve every validation keyword. Historical Draft labels inside the frozen schema annotations do not alter the adopted release version; see [edition and authority guide](RELEASE_READINESS.md). No execution, asset retrieval or synthesis permission follows from valid data.

**Coverage:** 93/93 reachable parameter declarations; 20/20 enum literals; 9/9 positive union branches. [Detailed coverage](COVERAGE_REPORT.md).

## Definition index / 定義索引

- [Root](#def-)
- [id](#def-defs-id)
- [participant](#def-defs-participant)
- [position](#def-defs-position)
- [note](#def-defs-note)
- [phrase](#def-defs-phrase)
- [committedPhrase](#def-defs-committedphrase)
- [snapshot](#def-defs-snapshot)
- [phraseProposedPayload](#def-defs-phraseproposedpayload)
- [phraseCommittedPayload](#def-defs-phrasecommittedpayload)
- [turnRequestedPayload](#def-defs-turnrequestedpayload)
- [cueIssuedPayload](#def-defs-cueissuedpayload)
- [performanceObservedPayload](#def-defs-performanceobservedpayload)
- [participantStatusPayload](#def-defs-participantstatuspayload)
- [sessionStateChangedPayload](#def-defs-sessionstatechangedpayload)
- [event](#def-defs-event)
- [commitmentWindow](#def-defs-commitmentwindow)

<a id="def-"></a>
## Root

**Schema pointer:** `#`. Reachable from release root / 公開ルートから到達可能。

Separate transport-neutral collaboration data. Draft 0.9 requires an explicit finite performancePlanId and SHA-256 score-byte pin in every Snapshot/Event; changed source bytes/revisions require a new Session. No robot actuation authority is created.

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-distributed-session-0.2.schema.json",
  "title": "OSTF Distributed Session Profile 0.2 — Draft 0.9 (source-pin amendment)",
  "description": "Separate transport-neutral collaboration data. Draft 0.9 requires an explicit finite performancePlanId and SHA-256 score-byte pin in every Snapshot/Event; changed source bytes/revisions require a new Session. No robot actuation authority is created.",
  "oneOf": [
    {
      "$ref": "#/$defs/snapshot"
    },
    {
      "$ref": "#/$defs/event"
    }
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
  "minLength": 1
}
```


<a id="def-defs-participant"></a>
## participant

**Schema pointer:** `#/$defs/participant`. Reachable from release root / 公開ルートから到達可能。

### participant — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `participantId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants/0/participantId` |
| `kind` | Yes / 必須 | enum | enum=["human","softwareAgent","physicalRobot"] | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants/0/kind` |
| `assignedTrackIds` | Yes / 必須 | array | uniqueItems=true; items: id | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants/0/assignedTrackIds` |
| `supportedFeatures` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: string | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants/0/supportedFeatures` |
| `capabilities` | Optional / 任意（条件付きの場合あり） | object | Untrusted advisory data, not robot actuator authorization | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants/1/capabilities` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "human",
        "softwareAgent",
        "physicalRobot"
      ]
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "supportedFeatures": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "uniqueItems": true
    },
    "capabilities": {
      "type": "object",
      "description": "Untrusted advisory data, not robot actuator authorization",
      "additionalProperties": true
    }
  },
  "required": [
    "participantId",
    "kind",
    "assignedTrackIds"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-position"></a>
## position

**Schema pointer:** `#/$defs/position`. Reachable from release root / 公開ルートから到達可能。

epochUtc denotes the clock-domain estimate for the explicitly stated performanceTick (at the sourceTick). Clock synchronization algorithm is out of scope.

### position — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `performancePlanId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/performancePlanId` |
| `visitId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/visitId` |
| `sourceTick` | Yes / 必須 | integer | minimum=0 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/sourceTick` |
| `performanceTick` | Yes / 必須 | integer | minimum=0 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/performanceTick` |
| `clockDomainId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/clockDomainId` |
| `epochUtc` | Yes / 必須 | string | format="date-time" | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/epochUtc` |
| `uncertaintyMs` | Yes / 必須 | number | minimum=0 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/uncertaintyMs` |
| `tempoBpm` | Optional / 任意（条件付きの場合あり） | number | exclusiveMinimum=0 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position/tempoBpm` |

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
    },
    "sourceTick": {
      "type": "integer",
      "minimum": 0
    },
    "performanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "clockDomainId": {
      "$ref": "#/$defs/id"
    },
    "epochUtc": {
      "type": "string",
      "format": "date-time"
    },
    "uncertaintyMs": {
      "type": "number",
      "minimum": 0
    },
    "tempoBpm": {
      "type": "number",
      "exclusiveMinimum": 0
    }
  },
  "required": [
    "performancePlanId",
    "visitId",
    "sourceTick",
    "performanceTick",
    "clockDomainId",
    "epochUtc",
    "uncertaintyMs"
  ],
  "additionalProperties": false,
  "description": "epochUtc denotes the clock-domain estimate for the explicitly stated performanceTick (at the sourceTick). Clock synchronization algorithm is out of scope."
}
```


<a id="def-defs-note"></a>
## note

**Schema pointer:** `#/$defs/note`. Reachable from release root / 公開ルートから到達可能。

MIDI-like note within a proposed session phrase, not a new authoritative OSTF Core Note.

### note — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `startTick` | Yes / 必須 | integer | minimum=0 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/notes/0/startTick` |
| `durationTicks` | Yes / 必須 | integer | minimum=1 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/notes/0/durationTicks` |
| `pitch` | Yes / 必須 | integer | minimum=0; maximum=127 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/notes/0/pitch` |
| `velocity` | Yes / 必須 | integer | minimum=1; maximum=127 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/notes/0/velocity` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127
    }
  },
  "required": [
    "startTick",
    "durationTicks",
    "pitch",
    "velocity"
  ],
  "additionalProperties": false,
  "description": "MIDI-like note within a proposed session phrase, not a new authoritative OSTF Core Note."
}
```


<a id="def-defs-phrase"></a>
## phrase

**Schema pointer:** `#/$defs/phrase`. Reachable from release root / 公開ルートから到達可能。

A portable minimal pitched-note session phrase. No lyrics, MPE, instrument actuation or audio realization is implied. Notes are relative to phrase start/effectivePerformanceTick.

### phrase — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `representation` | Yes / 必須 | `"midi1Notes"` (const) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/representation` |
| `durationTicks` | Yes / 必須 | integer | minimum=1 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/durationTicks` |
| `notes` | Yes / 必須 | array | minItems=1; items: note | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase/notes` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "representation": {
      "const": "midi1Notes"
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      },
      "minItems": 1
    }
  },
  "required": [
    "representation",
    "durationTicks",
    "notes"
  ],
  "additionalProperties": false,
  "description": "A portable minimal pitched-note session phrase. No lyrics, MPE, instrument actuation or audio realization is implied. Notes are relative to phrase start/effectivePerformanceTick."
}
```


<a id="def-defs-committedphrase"></a>
## committedPhrase

**Schema pointer:** `#/$defs/committedPhrase`. Reachable from release root / 公開ルートから到達可能。

### committedPhrase — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `commitEventId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json)<br>`/committedPhrases/0/commitEventId` |
| `proposalId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json)<br>`/committedPhrases/0/proposalId` |
| `targetTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json)<br>`/committedPhrases/0/targetTrackId` |
| `effectivePerformanceTick` | Yes / 必須 | integer | minimum=0 | [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json)<br>`/committedPhrases/0/effectivePerformanceTick` |
| `phrase` | Yes / 必須 | [phrase](#def-defs-phrase) | See exact schema / 厳密な定義は下記Schema。 | [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json)<br>`/committedPhrases/0/phrase` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "commitEventId": {
      "$ref": "#/$defs/id"
    },
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "commitEventId",
    "proposalId",
    "targetTrackId",
    "effectivePerformanceTick",
    "phrase"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-snapshot"></a>
## snapshot

**Schema pointer:** `#/$defs/snapshot`. Reachable from release root / 公開ルートから到達可能。

A playing Session Snapshot must have a pinned Plan/Visit clock position. Prepared/stopped may omit position. Only the current authority can certify an authoritative Snapshot. Draft 0.5: commitmentWindow asserts complete accepted phrase coverage as of stateRevision; absence makes no completeness guarantee. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots. Draft 0.12: a Snapshot has at least one Participant so the required authority identity can resolve.

### snapshot — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `profile` | Yes / 必須 | `"OSTF-Distributed-Session-0.2"` (const) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/profile` |
| `recordType` | Yes / 必須 | `"snapshot"` (const) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/recordType` |
| `sessionId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/sessionId` |
| `documentId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/documentId` |
| `revisionId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/revisionId` |
| `performancePlanId` | Yes / 必須 | [id](#def-defs-id) | Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID. | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/performancePlanId` |
| `scoreSha256` | Yes / 必須 | string | pattern="^[0-9a-f]{64}$"; SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization. | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/scoreSha256` |
| `sessionStatus` | Yes / 必須 | enum | enum=["prepared","playing","stopped"]; Authoritative session lifecycle state; not participant availability or network connection status. | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/sessionStatus` |
| `stateRevision` | Yes / 必須 | integer | minimum=0 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/stateRevision` |
| `authorityParticipantId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/authorityParticipantId` |
| `participants` | Yes / 必須 | array | minItems=1; items: participant | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/participants` |
| `position` | Optional / 任意（条件付きの場合あり） | [position](#def-defs-position) | See exact schema / 厳密な定義は下記Schema。 | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/position` |
| `committedPhrases` | Optional / 任意（条件付きの場合あり） | array | items: committedPhrase; Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims. | [03-snapshot-02.json](../examples/session/03-snapshot-02.json)<br>`/committedPhrases` |
| `commitmentWindow` | Optional / 任意（条件付きの場合あり） | [commitmentWindow](#def-defs-commitmentwindow) | Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session. | [16-playing-after-start-02.json](../examples/session/16-playing-after-start-02.json)<br>`/commitmentWindow` |

### snapshot/allOf/1/then — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `sessionStatus` | Optional / 任意（条件付きの場合あり） | `"playing"` (const) | See exact schema / 厳密な定義は下記Schema。 | [16-playing-after-start-02.json](../examples/session/16-playing-after-start-02.json)<br>`/sessionStatus` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "snapshot"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "sessionStatus": {
      "enum": [
        "prepared",
        "playing",
        "stopped"
      ],
      "description": "Authoritative session lifecycle state; not participant availability or network connection status."
    },
    "stateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "authorityParticipantId": {
      "$ref": "#/$defs/id"
    },
    "participants": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/participant"
      },
      "minItems": 1
    },
    "position": {
      "$ref": "#/$defs/position"
    },
    "committedPhrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/committedPhrase"
      },
      "description": "Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims."
    },
    "commitmentWindow": {
      "$ref": "#/$defs/commitmentWindow",
      "description": "Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session."
    }
  },
  "required": [
    "profile",
    "recordType",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "sessionStatus",
    "stateRevision",
    "authorityParticipantId",
    "participants"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        },
        "required": [
          "sessionStatus"
        ]
      },
      "then": {
        "required": [
          "position"
        ]
      }
    },
    {
      "if": {
        "required": [
          "commitmentWindow"
        ]
      },
      "then": {
        "required": [
          "position",
          "committedPhrases"
        ],
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        }
      }
    }
  ],
  "description": "A playing Session Snapshot must have a pinned Plan/Visit clock position. Prepared/stopped may omit position. Only the current authority can certify an authoritative Snapshot. Draft 0.5: commitmentWindow asserts complete accepted phrase coverage as of stateRevision; absence makes no completeness guarantee. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots. Draft 0.12: a Snapshot has at least one Participant so the required authority identity can resolve."
}
```


<a id="def-defs-phraseproposedpayload"></a>
## phraseProposedPayload

**Schema pointer:** `#/$defs/phraseProposedPayload`. Reachable from release root / 公開ルートから到達可能。

### phraseProposedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `proposalId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/proposalId` |
| `targetTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/targetTrackId` |
| `phrase` | Yes / 必須 | [phrase](#def-defs-phrase) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload/phrase` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-phrasecommittedpayload"></a>
## phraseCommittedPayload

**Schema pointer:** `#/$defs/phraseCommittedPayload`. Reachable from release root / 公開ルートから到達可能。

### phraseCommittedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `proposalId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/payload/proposalId` |
| `targetTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/payload/targetTrackId` |
| `phrase` | Yes / 必須 | [phrase](#def-defs-phrase) | See exact schema / 厳密な定義は下記Schema。 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/payload/phrase` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-turnrequestedpayload"></a>
## turnRequestedPayload

**Schema pointer:** `#/$defs/turnRequestedPayload`. Reachable from release root / 公開ルートから到達可能。

### turnRequestedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `targetTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [08-turn-request-02.json](../examples/session/08-turn-request-02.json)<br>`/payload/targetTrackId` |
| `requestedRole` | Yes / 必須 | string | minLength=1 | [08-turn-request-02.json](../examples/session/08-turn-request-02.json)<br>`/payload/requestedRole` |
| `requestedVisitId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [08-turn-request-02.json](../examples/session/08-turn-request-02.json)<br>`/payload/requestedVisitId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "requestedRole": {
      "type": "string",
      "minLength": 1
    },
    "requestedVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "targetTrackId",
    "requestedRole"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-cueissuedpayload"></a>
## cueIssuedPayload

**Schema pointer:** `#/$defs/cueIssuedPayload`. Reachable from release root / 公開ルートから到達可能。

### cueIssuedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `cueId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [09-cue-issued-02.json](../examples/session/09-cue-issued-02.json)<br>`/payload/cueId` |
| `targetVisitId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [09-cue-issued-02.json](../examples/session/09-cue-issued-02.json)<br>`/payload/targetVisitId` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "cueId": {
      "$ref": "#/$defs/id"
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "cueId"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-performanceobservedpayload"></a>
## performanceObservedPayload

**Schema pointer:** `#/$defs/performanceObservedPayload`. Reachable from release root / 公開ルートから到達可能。

### performanceObservedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `observedParticipantId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/payload/observedParticipantId` |
| `sourceTrackId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/payload/sourceTrackId` |
| `confidence` | Yes / 必須 | number | minimum=0; maximum=1 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/payload/confidence` |
| `features` | Optional / 任意（条件付きの場合あり） | object | See exact schema / 厳密な定義は下記Schema。 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/payload/features` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "observedParticipantId": {
      "$ref": "#/$defs/id"
    },
    "sourceTrackId": {
      "$ref": "#/$defs/id"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "features": {
      "type": "object",
      "additionalProperties": true
    }
  },
  "required": [
    "observedParticipantId",
    "sourceTrackId",
    "confidence"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-participantstatuspayload"></a>
## participantStatusPayload

**Schema pointer:** `#/$defs/participantStatusPayload`. Reachable from release root / 公開ルートから到達可能。

### participantStatusPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `participantId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [11-participant-status-02.json](../examples/session/11-participant-status-02.json)<br>`/payload/participantId` |
| `availability` | Yes / 必須 | enum | enum=["ready","busy","disconnected"] | [11-participant-status-02.json](../examples/session/11-participant-status-02.json)<br>`/payload/availability` |
| `message` | Optional / 任意（条件付きの場合あり） | string | See exact schema / 厳密な定義は下記Schema。 | [18-participant-busy-02.json](../examples/session/18-participant-busy-02.json)<br>`/payload/message` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "availability": {
      "enum": [
        "ready",
        "busy",
        "disconnected"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "participantId",
    "availability"
  ],
  "additionalProperties": false
}
```


<a id="def-defs-sessionstatechangedpayload"></a>
## sessionStateChangedPayload

**Schema pointer:** `#/$defs/sessionStateChangedPayload`. Reachable from release root / 公開ルートから到達可能。

Authoritative sessionStarted and visitChanged both supply an explicit musical/UTC Position anchor. assignmentChanged changes assignments only and MUST NOT carry position or targetVisitId; sessionStopped is immediate.

### sessionStateChangedPayload — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `changeKind` | Yes / 必須 | enum | enum=["sessionStarted","visitChanged","assignmentChanged","sessionStopped"] | [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json)<br>`/payload/changeKind` |
| `targetVisitId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json)<br>`/payload/targetVisitId` |
| `participantId` | Optional / 任意（条件付きの場合あり） | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [20-assignment-changed-02.json](../examples/session/20-assignment-changed-02.json)<br>`/payload/participantId` |
| `assignedTrackIds` | Optional / 任意（条件付きの場合あり） | array | uniqueItems=true; items: id | [20-assignment-changed-02.json](../examples/session/20-assignment-changed-02.json)<br>`/payload/assignedTrackIds` |
| `position` | Optional / 任意（条件付きの場合あり） | [position](#def-defs-position) | Authoritative Plan/Visit/source/performance Tick and clock-domain/UTC anchor. Required for sessionStarted and visitChanged; position.performanceTick MUST equal event effectivePerformanceTick. For visitChanged, position.visitId MUST equal targetVisitId at that Visit start. | [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json)<br>`/payload/position` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "changeKind": {
      "enum": [
        "sessionStarted",
        "visitChanged",
        "assignmentChanged",
        "sessionStopped"
      ]
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    },
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "position": {
      "$ref": "#/$defs/position",
      "description": "Authoritative Plan/Visit/source/performance Tick and clock-domain/UTC anchor. Required for sessionStarted and visitChanged; position.performanceTick MUST equal event effectivePerformanceTick. For visitChanged, position.visitId MUST equal targetVisitId at that Visit start."
    }
  },
  "required": [
    "changeKind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStarted"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "visitChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "targetVisitId",
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "assignmentChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "participantId",
          "assignedTrackIds"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStopped"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Authoritative sessionStarted and visitChanged both supply an explicit musical/UTC Position anchor. assignmentChanged changes assignments only and MUST NOT carry position or targetVisitId; sessionStopped is immediate."
}
```


<a id="def-defs-event"></a>
## event

**Schema pointer:** `#/$defs/event`. Reachable from release root / 公開ルートから到達可能。

Authorized state changes increment base revision exactly once. Proposed Draft 0.10: sessionStarted and visitChanged carry clock-anchored Position; event effectivePerformanceTick equals Position performanceTick for each. See SESSION_STATE_MACHINE.md; semantic cross-checks require the pinned score.

### event — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `profile` | Yes / 必須 | `"OSTF-Distributed-Session-0.2"` (const) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/profile` |
| `recordType` | Yes / 必須 | `"event"` (const) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/recordType` |
| `eventId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/eventId` |
| `sessionId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/sessionId` |
| `documentId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/documentId` |
| `revisionId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/revisionId` |
| `performancePlanId` | Yes / 必須 | [id](#def-defs-id) | Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID. | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/performancePlanId` |
| `scoreSha256` | Yes / 必須 | string | pattern="^[0-9a-f]{64}$"; SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization. | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/scoreSha256` |
| `baseStateRevision` | Yes / 必須 | integer | minimum=0 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/baseStateRevision` |
| `resultStateRevision` | Optional / 任意（条件付きの場合あり） | integer | minimum=0 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/resultStateRevision` |
| `issuerParticipantId` | Yes / 必須 | [id](#def-defs-id) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/issuerParticipantId` |
| `kind` | Yes / 必須 | enum | enum=["phraseProposed","phraseCommitted","turnRequested","cueIssued","performanceObserved","participantStatus","sessionStateChanged"] | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/kind` |
| `effectivePerformanceTick` | Yes / 必須 | integer | minimum=0 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/effectivePerformanceTick` |
| `payload` | Yes / 必須 | object | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload` |

### event/oneOf/0 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"phraseProposed"` (const) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [phraseProposedPayload](#def-defs-phraseproposedpayload) | See exact schema / 厳密な定義は下記Schema。 | [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json)<br>`/payload` |

### event/oneOf/1 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"phraseCommitted"` (const) | See exact schema / 厳密な定義は下記Schema。 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [phraseCommittedPayload](#def-defs-phrasecommittedpayload) | See exact schema / 厳密な定義は下記Schema。 | [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json)<br>`/payload` |

### event/oneOf/2 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"turnRequested"` (const) | See exact schema / 厳密な定義は下記Schema。 | [08-turn-request-02.json](../examples/session/08-turn-request-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [turnRequestedPayload](#def-defs-turnrequestedpayload) | See exact schema / 厳密な定義は下記Schema。 | [08-turn-request-02.json](../examples/session/08-turn-request-02.json)<br>`/payload` |

### event/oneOf/3 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"cueIssued"` (const) | See exact schema / 厳密な定義は下記Schema。 | [09-cue-issued-02.json](../examples/session/09-cue-issued-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [cueIssuedPayload](#def-defs-cueissuedpayload) | See exact schema / 厳密な定義は下記Schema。 | [09-cue-issued-02.json](../examples/session/09-cue-issued-02.json)<br>`/payload` |

### event/oneOf/4 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"performanceObserved"` (const) | See exact schema / 厳密な定義は下記Schema。 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [performanceObservedPayload](#def-defs-performanceobservedpayload) | See exact schema / 厳密な定義は下記Schema。 | [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json)<br>`/payload` |

### event/oneOf/5 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"participantStatus"` (const) | See exact schema / 厳密な定義は下記Schema。 | [11-participant-status-02.json](../examples/session/11-participant-status-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [participantStatusPayload](#def-defs-participantstatuspayload) | See exact schema / 厳密な定義は下記Schema。 | [11-participant-status-02.json](../examples/session/11-participant-status-02.json)<br>`/payload` |

### event/oneOf/6 — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `kind` | Yes / 必須 | `"sessionStateChanged"` (const) | See exact schema / 厳密な定義は下記Schema。 | [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json)<br>`/kind` |
| `payload` | Yes / 必須 | [sessionStateChangedPayload](#def-defs-sessionstatechangedpayload) | See exact schema / 厳密な定義は下記Schema。 | [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json)<br>`/payload` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "event"
    },
    "eventId": {
      "$ref": "#/$defs/id"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "baseStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "resultStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "issuerParticipantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "phraseProposed",
        "phraseCommitted",
        "turnRequested",
        "cueIssued",
        "performanceObserved",
        "participantStatus",
        "sessionStateChanged"
      ]
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "payload": {
      "type": "object"
    }
  },
  "required": [
    "profile",
    "recordType",
    "eventId",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "baseStateRevision",
    "issuerParticipantId",
    "kind",
    "effectivePerformanceTick",
    "payload"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "properties": {
        "kind": {
          "const": "phraseProposed"
        },
        "payload": {
          "$ref": "#/$defs/phraseProposedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "phraseCommitted"
        },
        "payload": {
          "$ref": "#/$defs/phraseCommittedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    },
    {
      "properties": {
        "kind": {
          "const": "turnRequested"
        },
        "payload": {
          "$ref": "#/$defs/turnRequestedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "cueIssued"
        },
        "payload": {
          "$ref": "#/$defs/cueIssuedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "performanceObserved"
        },
        "payload": {
          "$ref": "#/$defs/performanceObservedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "participantStatus"
        },
        "payload": {
          "$ref": "#/$defs/participantStatusPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "sessionStateChanged"
        },
        "payload": {
          "$ref": "#/$defs/sessionStateChangedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    }
  ],
  "description": "Authorized state changes increment base revision exactly once. Proposed Draft 0.10: sessionStarted and visitChanged carry clock-anchored Position; event effectivePerformanceTick equals Position performanceTick for each. See SESSION_STATE_MACHINE.md; semantic cross-checks require the pinned score."
}
```


<a id="def-defs-commitmentwindow"></a>
## commitmentWindow

**Schema pointer:** `#/$defs/commitmentWindow`. Reachable from release root / 公開ルートから到達可能。

Optional assertion that all accepted committed phrases intersecting half-open [startPerformanceTick, endPerformanceTick) are listed in committedPhrases for the Snapshot stateRevision. Semantic validator MUST check start < end and intersection/completeness against authority log.

### commitmentWindow — properties / 項目

| Property / 項目 | Required / 必須 | Type / 型 | Constraints & meaning / 制約・意味 | Sample witness / 使用例 |
|---|---|---|---|---|
| `startPerformanceTick` | Yes / 必須 | integer | minimum=0 | [16-playing-after-start-02.json](../examples/session/16-playing-after-start-02.json)<br>`/commitmentWindow/startPerformanceTick` |
| `endPerformanceTick` | Yes / 必須 | integer | minimum=1 | [16-playing-after-start-02.json](../examples/session/16-playing-after-start-02.json)<br>`/commitmentWindow/endPerformanceTick` |

### Exact JSON Schema / 厳密なSchema定義

```json
{
  "type": "object",
  "properties": {
    "startPerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "endPerformanceTick": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": [
    "startPerformanceTick",
    "endPerformanceTick"
  ],
  "additionalProperties": false,
  "description": "Optional assertion that all accepted committed phrases intersecting half-open [startPerformanceTick, endPerformanceTick) are listed in committedPhrases for the Snapshot stateRevision. Semantic validator MUST check start < end and intersection/completeness against authority log."
}
```
