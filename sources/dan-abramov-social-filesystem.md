# Dan Abramov — A Social Filesystem

**URL:** https://overreacted.io/a-social-filesystem/

**Date accessed:** 2026-09-16

## What It Covers

An exploration of the AT Protocol through the metaphor of a filesystem. Your social data (posts, likes, follows) behaves like files on a computer — you own them, apps just read and write them.

## Key Information Extracted

### The Filesystem Analogy
- Personal computing: files live on YOUR computer, apps create/read them but don't own them
- Social computing: AT Protocol treats your data the same way — files in "your folder"
- **"What we make with a tool does not belong to the tool"**
- File formats let different apps work together without knowing about each other

### Records = Files
- Each post, like, follow is a JSON record (file)
- Records live in the user's repository (their folder)
- Records are named with timestamps + random clock IDs for uniqueness
- Records contain ONLY what the user actually created (no derived data like reply counts)

### The Collection View
- A user's repo is organized into collections (like folders): `app.bsky.feed.post/`, `app.bsky.feed.like/`, etc.
- Apps project from these collections into user interfaces
- Multiple apps can read the same collections without needing to talk to each other

### Key Concept: Social Filesystem
- Everyone's folders form a distributed social filesystem
- Apps are not the source of truth — the records are
- An app's database is "derived data — an app-specific cached materialized view"

### The Open Alternative Ecosystem
- AT Protocol apps that implement the filesystem paradigm:
  - Bluesky, Leaflet, Tangled, Semble, Wisp
- Third-party feeds: anyone can build a feed algorithm
  - Example: @spacecowboy17's "For You" feed, ran from a home computer
- Cross-app data: apps like Blento show data from apps that don't even exist yet

### Why The Algorithm Got Better
- "In the Atmosphere, third party is first party"
- Open feed algorithms mean users pick what works for them
- "An everything app tries to do everything. An everything ecosystem lets everything get done."

### Memorable Example
- A post record is just `{ text: 'no', createdAt: '2008-09-15T17:25:00.000Z' }` — no author metadata, no engagement counts. Those are derived from OTHER users' records.