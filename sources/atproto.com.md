# atproto.com — Official AT Protocol Site

**URL:** https://atproto.com/

**Date accessed:** 2026-09-16

## What It Covers

The official site for the Authenticated Transfer Protocol (AT Protocol). Landing page, documentation, guides, tutorials, and specifications.

## Key Information Extracted

- Tagline: "Building the Social Internet"
- **40M+ users**, **2.4B+ posts**, **100% open data**
- Everything is JSON — posts, likes, follows, profiles are JSON records
- Strongly typed via Lexicon schemas (shared data formats)
- Hyperlinked — every piece of data has a URL
- Strong links using content-IDs (CIDs) — content-addressed references
- Public firehose available via WebSocket — no API key required
- Usernames are domains (DNS-based handles)

### Core Architecture
- **PDS** (Personal Data Server): hosts user accounts and data
- **Relays**: collect and rebroadcast user write events across network
- **Applications**: aggregate user data to produce app experiences
- **Labelers**: publish moderation decisions as metadata

### Key Differences from ActivityPub
1. Account portability — signed data repos + DIDs
2. Scalability — relays aggregate instead of point-to-point delivery
3. Domain-based usernames instead of double-@ email style
4. Lexicon schemas instead of JSON-LD/RDF
5. Better support for algorithmic feeds and global search

### Developer Offerings
- XRPC: HTTP with conventions for typed API calls
- OAuth for authentication
- SDKs for multiple languages
- Custom feed generators
- Bot tutorials
- Self-hosting guides