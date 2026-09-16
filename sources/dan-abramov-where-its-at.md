# Dan Abramov — Where It's at://

**URL:** https://overreacted.io/where-its-at/

**Date accessed:** 2026-09-16

## What It Covers

A technical deep dive into how at:// URIs work — the addressing system of the AT Protocol. Step-by-step resolution from handle to JSON data.

## Key Information Extracted

### The Key Design Decision
- In https:// URIs, the authority is the **host** (whoever serves the data)
- In at:// URIs, the authority is the **user** (whoever created the data)
- **"The user is the authority for their own data"**
- Hosting can change, identity stays the same

### Three-Step Resolution Process
1. **Handle to Identity (DID):** resolve @handle to a permanent DID via DNS TXT record or HTTPS .well-known endpoint
2. **Identity to Hosting:** fetch the DID Document to find the PDS URL
3. **Hosting to Data:** call getRecord on the PDS with the at:// URI

### Handle Resolution Methods
- DNS: `_atproto.<handle>` TXT record with `did=...`
- HTTPS: `https://<handle>/.well-known/atproto-did`

### DID Types
- **did:plc:** Bluesky-managed DID method (used by most Bluesky users)
- **did:web:** for users who host their identity on their own domain

### Permalinks
- at:// URIs with handles are human-readable but fragile
- at:// URIs with DIDs are permalinks — they won't break if user changes handle
- Apps should store the DID form

### Practical Takeaway
- SDKs handle resolution automatically
- Production apps use resolution caches (like QuickDID) instead of DNS lookups every time
- Many apps receive data via WebSocket firehose rather than pulling on demand