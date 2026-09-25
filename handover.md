# Handover: Didier Mortier

## Who I am

Customer Success & Sales Leader. From support to retention in SaaS and domains. Building an Atmosphere community in Barcelona. Originally from Belgium, based in Barcelona for 11 years. Currently between jobs after leaving OpenProvider (domain registrar) in July 2026.

## My story

Studied architecture but never practiced it. Moved to Barcelona 11 years ago. Started in a call center doing customer support, moved into sales, then customer success. Latest role: Senior Account Manager at OpenProvider (domain industry). Got deep into domains, DNS, SSL, email security -- connected directly to AT Protocol (DIDs use domain-based identity).

Quit Meta (Instagram, WhatsApp, Facebook) about 1.5 years ago. Final straw was Meta AI training on WhatsApp data. Switched to Signal (messaging) and Bluesky (social). Use iMessage for stubborn friends. Telegram because my girlfriend won't switch.

Discovered AT Protocol through Bluesky. Now use EuroSky (European PDS, non-profit in Netherlands, Stichting Modal). Advocate for open social web. Met Dario online, he suggested I give a talk in Sabadell.

## Communication preferences

- Plain English. Short sentences. No drama, no hype, no marketing tone.
- No em dashes (--) or en dashes (-). Use simple hyphens.
- No AI-sounding text, narrative flourishes, or storytelling fragments.
- Discuss first, action second. Present drafts or options, wait for explicit "go ahead."
- Stop signals: "don't change yet", "just feedback".
- Honest and direct. If something is wrong, say so plainly.
- Voice-to-text causes typos sometimes -- double-check odd commands.

## Projects worked on with Hermes Agent

### Atmosphere Presentation (Sabadell talk)
- Repo: didiermortier/atmosphere-talk-2026.10
- Title: "The Atmosphere: Building the Open Social Web"
- 5 chapters, 28 source files
- All content in English, to be translated to Spanish
- Topics: personal story, timeline + protocol, ecosystem good & bad, social media for young people, the future
- Focus on Atmosphere as the brand, not AT Protocol (protocol is backend)
- mu.social (not just "mu"), EuroSky in Netherlands, BlackSky as alternatives

### Jellyfin2PopFeed Plugin
- Jellyfin plugin that logs watch history to PopFeed (AT Protocol media tracking)
- Newest version first in manifest, name one word (Jellyfin2PopFeed), keep all revision history
- Single "Authenticate & Save" button only
- TMDB CDN URLs for permanence
- PopFeed Activity feed driven by private Popsphere API (popsphere-api.onrender.com), not PDS records
- Website calls POST /lists/mark-tv-series-watched-v2 with auth token from Bluesky OAuth

### Second Brain (Obsidian Vault)
- Vault at ~/hermes-vault/ (iPad -> GitHub sync)
- git pull --ff-only first
- Structure: 00-INBOX/, 01-NOTES/, 04-HERMES-OUTPUTS/
- Two entry formats: <Start Note> markers (iPad Shortcuts, primary) and `- ` bullets (fallback)
- Midnight cron for archive, hourly inbox processing
- vault-auto-sync (5min) can undo archive -- agent verifies mv, force-removes if race

### Job Search
- Using RemoteRocketship API
- Always filter jobs older than 3 months client-side using created_at field
- Tiers: T1 Spain, 50K+, senior, FT/contract, ops roles, instant notify
- T2 Europe-wide, 40K+, senior/mid, daily
- T3 Europe, any salary, weekly
- Spanish contract/tax preferred

## Git identity
- Name: Didier Mortier
- Email: 157531888+didiermortier@users.noreply.github.com
- Token at ~/.hermes/secrets/github_token

## Community
- atproto.barcelona -- local Atmosphere community
- atproto.eu -- European network (connections in France, Belgium, Netherlands, Italy, Germany)
- atproto.barcelona Bluesky profile for meetups

## Writing rules (critical)
- Never use em dashes (--) or en dashes (-) for sentence separation
- Write plain, direct, human
- No AI-sounding text, dramatic fragments, storytelling structure
- No filler like "Great question" or "I'd be happy to"
- No restating the request back
- When unsure, say so plainly
- Plain claims over adjectives