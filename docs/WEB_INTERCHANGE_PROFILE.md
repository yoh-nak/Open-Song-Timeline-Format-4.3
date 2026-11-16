> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **OSTF 4.3.0 formal-release supporting material.** The adopted specification is publisher-approved. Older Draft labels and pending-approval statements below are historical editorial records, not the current release decision. See [release status and authority](RELEASE_READINESS.md). These notes and local examples do not certify runtime interoperability.
> **正式公開版の補助資料です。** 以下に残るDraft表記や承認待ちの記録は編集履歴です。現在の承認状態と優先関係はリンク先を参照してください。

# OSTF 4.3 — Optional Web Interchange Guidance (Draft 0.53)

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

## Draft 0.33 — Read versus write or remote execution (unratified)

HTTP(S) GET returning valid OSTF JSON is a data retrieval operation, not an authorization to call remote AI generation, persist a revision, accept a distributed event, download referenced third-party Assets, run a plug-in or actuate a robot. Each action requires its own application protocol and permissions outside Score Core. A transport failure must not be represented as committed Session state. This clarifies scope only; no REST endpoint or authentication protocol is newly standardized.

---

## Draft 0.32 — Resource delivery and reserialization (proposal)

A client calculating a companion Score SHA-256 must hash the **decompressed original response entity bytes** of the UTF-8 `.ostf` resource, before JSON reparsing or rewriting. Transport headers, compressed wire bytes, ETag and URL are not the Score body. Semantically equivalent JSON obtained by rewriting whitespace, escape sequences, or property order may produce a *different binding identity*. Never silently reuse old distributed/production digests after serialization; follow the versioned explicit rebind rules. This is not a new REST API, canonical-JSON rule or permission to fetch untrusted resources.

---

## OSTF Web JSON Interchange — Optional guidance (not Core)

OSTF 4.3 remains a JSON **song data format**. QR codes may contain HTTPS URLs that resolve to a Web app or API. This is a pattern for using OSTF, not a required HTTP service or a new `.ostf` field.

## Current Draft 0.23 — exact-byte identity and historical guidance

**Current interpretation (unratified):** OSTF Core 4.3 itself has **no mandatory content digest or canonical JSON serialization**. However, the *separately versioned* **Distributed Session Profile 0.2** requires root `scoreSha256`, and **Production Session Profiles 0.1/0.2** require `score.sha256`. When any of these companion records is present, its digest is calculated over the **exact UTF-8 bytes of the supplied Score `.ostf` resource** (after HTTP content-encoding decompression, before JSON reserialization), not an ETag, ZIP hash, pretty-printed JSON, URL, semantic equality check or guessed SHA from a name. Digest equality across two companion declarations without the original Score bytes proves **declaration consistency only**; it does not verify the pinned source.

The older Draft 0.7 discussion below saying there was no *canonical content digest* referred to the absence of a generalized **JSON canonicalization** algorithm in Core; it MUST NOT be interpreted as cancelling the exact-byte SHA-256 requirements introduced in the unpublished 0.9 companion amendment and retained in 0.23. The explicit document/revision IDs, finite Plan resolution and permissions remain independent conditions. New Score bytes require explicit Production re-binding and, for remote performance, a new Session. No fetching, authentication, cache/ETag or real-time transport protocol is mandated by OSTF Core.

| Supplied data | Verified claim possible | Claim not justified |
| --- | --- | --- |
| Score bytes + compatible Profile digest | Byte identity of that referenced Score | Musical fidelity, publisher identity or robot permission |
| Production and Distributed digests, Score bytes missing | Declarations agree or disagree | Actual Score identity or Track/Plan reference validity |
| Score-only GET with no companions | Validated Score JSON / Core semantics as supported | Any Production/Distributed Session exists or is synchronized |

This section is a **clarifying proposal**, not a new JSON field, HTTP endpoint, API authentication service or claim of tested cross-host interoperability.


## Illustrative sequence

1. Scan a QR code containing `https://example.org/songs/song-001`.
2. A Web app resolves its song ID and requested revision, then retrieves an OSTF JSON document through a documented HTTPS GET endpoint (for example `GET /api/songs/song-001/revisions/rev-001`).
3. The client checks `format:"OSTF"`, `version:"4.3.0"`, the full JSON Schema, and semantic references. A client that supports only 4.2 MUST NOT silently treat the document as 4.2.
4. The client may render source score, chords, concrete Notes or the optional Performance Plan; **open** material does not promise deterministic playback.
5. An authorized editing operation may create a new revision. Retrieval alone must never generate notes, send third-party prompts or start a physical device.

Example request/response shape, **not** a standardized endpoint:

```http
GET /api/songs/song-001/revisions/rev-001 HTTP/1.1
Host: example.org
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
ETag: "sha256-content-versioned-token"
```

Actual response body is one complete OSTF 4.3 JSON document. Content-Type is indicative; no IANA-registered OSTF-specific MIME type is claimed. SHA256 may be used for integrity. Versioned URLs and conditional GET/ETag are recommended implementation choices, not mandatory Core semantics. Read-only public songs and private session data must have different access policies and authentication.

## Session state

For remote sessions, keep mutable participant/clock/event records in the separate **Distributed Session Profile** and avoid rewriting the immutable OSTF song JSON every beat. A host must choose network transport, clock synchronization and permission model. A participant must pin its song document/revision and check that all collaborators refer to equivalent content before trusting shared source ticks.

## Safety boundary

HTTP/JSON is not a robot command protocol. A retrieved `instruction`, Voice Role, Interaction or Event is never permission to control physical equipment, record media, execute scripts or transmit private content. These decisions remain with the host/robot operator.

## Draft 0.7 — Immutable resource revision guidance

When a remote Session references `(documentId, revisionId)`, each participant should obtain an equivalent OSTF JSON content version for that exact revision. A mutable `latest` URL is a discovery convenience, not a valid implicit source replacement during a running Session. If an API returns semantically different OSTF data under the *same* pinned revision, the Session must report an integrity conflict; no `stateRevision` increment can repair a hidden score rebase. Using versioned immutable URLs and independent content hashes/ETags can help hosts establish equivalence, but OSTF does not standardize an HTTP endpoint, authentication scheme or canonical content digest. A QR-code URL does not itself authorize remote actuation or automatic AI generation.

## Draft 0.9 — Immutable score artifact in remote sessions

A remote Session using separate Profile 0.2 MUST bind a finite `performancePlanId` and the score's exact original-byte `scoreSha256` together with document/revision identifiers. A QR code / HTTPS URL may fetch a `.ostf`, but the service must compute/verify the digest of the decoded UTF-8 resource bytes **before** rewriting/reformatting the document. A semantically identical reserialized JSON has a different digest and requires explicit rebinding as a new revision/session. ETag, cache metadata, document labels and SHA-256 do not authenticate a publisher or give robot execution privileges. Transport negotiation is not a Core OSTF requirement.

## Draft 0.13 — Separate studio-profile retrieval

A Web app MAY retrieve an OSTF score JSON and its separately versioned Production Session Profile JSON from independent authenticated HTTPS resources. The Studio Profile pins the exact source score via `score.sha256`, but the server endpoints, cross-origin permission policy, integrity transport, plug-in binary acquisition and execution authorization are *not* defined by OSTF. Accessing a URL or scanning a QR code must never automatically execute or install a plug-in. This is unrelated to the live remote Distributed Session Profile. See `PRODUCTION_SESSION_PROFILE.md`.

## Draft 0.19 — Web retrieval is not cross-profile authorization

A QR code or HTTPS endpoint may supply separately versioned OSTF Score, Production Profile and Distributed Session Profile JSON. A client binding the three records uses the **actual original Score bytes** rather than guessed names or equivalent reserialized JSON; Production `score.sha256` and Distributed `scoreSha256` must match those bytes. Neither an informational `score.sourceUri` nor a hash authorizes fetching a plugin-state blob, audio media, starting a session or robot actuation. Reformatting `.ostf` content creates a new original-byte SHA-256 and requires intentional re-binding, even when the music looks equivalent. Production-only edits do not change the pinned Score hash. See `PRODUCTION_SESSION_PROFILE.md` §25.

## Draft 0.20 — Revision-bound API retrieval and explicit re-binding

When a Web API supplies a new OSTF source resource, the client MUST compare original-byte score SHA-256 before treating any existing Production Profile as still pinned. An unchanged song title, Track ID, `latest` URL or `ETag` alone does not authorize a new pin. A client MAY expose an explicit author-reviewed Production Profile re-binding to the new Score document/revision/digest, preserving the original source/profile and disclosing changes to source-Tick Automation, audio Region mappings and selected Performance Plans. A new Distributed Session Profile 0.2 Session is required for a new score pin; active Session ID, accepted events and performance clock never follow `latest` automatically. Updating a Production Profile must not create, edit or authorize a remote Session. JSON endpoints and conditional requests are implementation choices, not mandated OSTF Core fields. These are candidate editorial semantics, not network tests or runtime authorization.

## Draft 0.21 — HTTP retrieval and byte-pinned companion preservation

An HTTP endpoint or QR-code link may locate a Score or a bundle; it is **not itself** the authoritative content identity. Validate the exact retrieved Score bytes against explicit hashes in separate Production/Distributed Profiles before treating them as one related work. JSON pretty-printing or any save changes byte pins; HTTP `ETag`, filename, `latest` route, mutable web path or equal display title is insufficient for an automatic live Session or Studio rebind. A client MAY retain and display independently versioned companion JSON without implementing its Production DSP or real-time Session semantics. It MUST NOT imply a complete bundle/asset round-trip unless referenced opaque bytes are actually retained. Fetch policy, CORS, authentication, authorization, HTTP cache management and robot safety remain external to OSTF.

## Draft 0.22 — Web retrieval and non-standard archive boundaries

A URI retrieved via an application-specific HTTP API can supply a Score, a Profile or an Asset, provided the caller has appropriate access and verifies applicable original-byte identities. The OSTF 4.3 format does not define a multipart API, archive extraction algorithm, authorization grant, session signaling service or portable production `.zip` container. Do not reinterpret the **specification's own release ZIP** or publisher manifest as a user-project container standard. A URL and SHA-256 do not authorize fetching proprietary assets, executing plug-ins or controlling a physical device. For data preservation claims, inventory the bytes actually received rather than assuming every referenced Asset was downloaded. See `PRODUCTION_SESSION_PROFILE.md` §28.
