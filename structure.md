# Deck Structure — The Atmosphere

The map of the deck. Slide order, one line per slide, timings. No prose here.
The spoken words live in `chapter-1.md` to `chapter-5.md`.
What the audience reads on screen, in English and Spanish, lives in `slides.md`.

## Deck specs

- **Format:** one self-contained HTML file. Opens from the file, no internet, no install.
- **Languages:** English and Spanish. EN / ES buttons in the header, keys 1 and 2. Switchable mid talk.
- **Theme:** dark only. Black background `#0C0C0F`, off-white text, gold accent, teal for links. Wave band from the cover artwork, `atproto BARCELONA` badge on the first and last slide.
- **Palette (sampled from the artwork):** bg `#0C0C0F`, ink `#F5F5F3`, sand `#D8D8C8`, gold `#E0A83F`, amber `#F8B050`, orange `#C46A2C`, terracotta `#B8602A`, rust `#8C3A22`, teal `#3E7A84`.
- **Type:** system sans, no web fonts. Big statements, few bullets. Nothing below 24px on screen.
- **Screen:** one screen, mirrored. Your notes are a hold to peek strip (hold `N`), so they never sit on the audience screen. Press `S` for the full script of the slide.
- **Links:** every site named is a real link, opens in a new tab. The URL is also written out, so the deck still reads with no internet.
- **Navigation:** arrows or click to move, `Home` / `End`, `Esc` for the slide index, `F` for fullscreen.
- **Budget:** 28 minutes of speaking, 41 slides, roughly 41 seconds each.
- **Chapter colour:** each chapter carries its own wave colour and a corner badge, so the audience always knows where they are. No extra divider slides.
  C1 gold - C2 orange - C3 terracotta - C4 rust - C5 teal

## Front — 2 slides

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| F1 | Title | The Atmosphere, Building the Open Social Web. Your name, handle, Terrassa and Barcelona, the date. | 30s |
| F2 | The five parts | Agenda: my story, the protocol, the ecosystem, young people, what comes next. | 30s |

## Chapter 1 — Personal Story (5 min, 5 slides)

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| C1.1 | Who I am | Architecture studies, 11 years in Barcelona, support to sales to customer success, OpenProvider, between jobs. Not a developer, but technical: own home server, tries every new thing. | 60s |
| C1.2 | From domains to identity | Your handle on the AT Protocol is a domain you own. Not a username on someone else's platform. | 60s |
| C1.3 | With Meta, you are the product | Instagram ate my time with doom scrolling. Ads, noise, and a feed I never chose. | 60s |
| C1.4 | The line | Meta AI pushed into WhatsApp. Deleted WhatsApp, Instagram, Facebook. Not a trial. | 60s |
| C1.5 | What I use now | Signal daily, iMessage for the holdouts, Bluesky for social. How this talk happened. Bridge: so what is this protocol? | 60s |

## Chapter 2 — The Story So Far (8 min, 10 slides)

The chapter opens with the timeline. Two slides carry every dated milestone, 2019 to 2026, and the
protocol explanation follows underneath. The six year slides that used to sit through the chapter,
C2.1, C2.2, C2.9, C2.10, C2.12 and C2.14, are merged into the first two.

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| C2.1 | 2019 to 2022 | Timeline. Twitter starts Bluesky. Graber takes the lead from Zcash. Musk buys Twitter and Bluesky goes independent. Carries the Jay Graber photo. | 50s |
| C2.2 | 2023 to 2026 | Timeline. Invite only and one million users, the 2024 election surge, the Seattle developer wave, Graber to CINO. The front end gets a friendlier name, the Atmosphere, while AT Protocol stays the protocol underneath. | 50s |
| C2.3 | What is the AT Protocol | What is the AT Protocol? Think of email: Gmail and ProtonMail still talk to each other. Open, decentralized, owned by no one. | 45s |
| C2.4 | Piece one: identity | Your handle is your domain. Under it a DID that stays with you forever. Every record is signed. Link: the PLC organization. | 45s |
| C2.5 | Piece two: your data | Your posts live on a PDS you choose. Move provider, keep your posts and your followers. | 45s |
| C2.6 | Piece three: the network | Relays merge all public activity into a firehose. Anyone can subscribe. No API key, no permission. | 45s |
| C2.7 | Piece four: the format | Everything is JSON with a Lexicon schema. Apps speak the same language. | 40s |
| C2.8 | Today | Over 46 million accounts, more than 3.2 billion posts, 100% of public content reachable. | 40s |
| C2.9 | The philosophy | Dan Abramov on Open Social. Three lines: open source did it for code. A row in their table becomes: with traditional social media, you are the product. If you cannot leave without losing something, the platform has no reason to respect you. | 60s |
| C2.10 | Not the same as ActivityPub | Portability: on Mastodon a dead server takes your history. On the AT Protocol everything moves. Scale: relays instead of server to server flooding, which makes global search and feeds possible. | 60s |

## Chapter 3 — The Ecosystem Today (5 min, 9 slides)

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| C3.1 | Where we are | Vibrant and growing, and with real problems. Close to 300 curated apps in the AT Store. | 30s |
| C3.2 | EuroSky and mu.social | Dutch non-profit runs the infrastructure. They forked the Bluesky app because the code is open. That is the point for developers in this room. | 40s |
| C3.3 | The non-profit model | EuroSky runs on a Dutch non-profit. Signal and Proton. The PLC identity directory now belongs to an independent Swiss association, not Bluesky. Open code, portable data, no single owner. Link: plcred.org. | 35s |
| C3.4 | Data you keep | PopFeed for films, books and music. Sifa ID as a LinkedIn replacement with signed endorsements. Tangled for code. All on your PDS. | 40s |
| C3.5 | Everything else | Marque, Grain, npmx, pckt.blog, standard.site for publishing a site to the protocol. One login, one handle, everywhere. | 35s |
| C3.6 | Europe leads | EuroSky, mu.social, PDS MOOver, Sifa ID, Tangled, Margin. Not just an American project. | 30s |
| C3.7 | The hard part: it is all public | Public by design is a gift for developers and a limit for users. Spaces is in alpha. Pointer to chapter 5. | 35s |
| C3.8 | The hard part: moderation, money, discovery | Fragmented moderation, a DDoS story, no monetisation layer yet, and 300 apps with no quality control. This is the opportunity, not just the problem. | 55s |
| C3.9 | W Social | Launched at Davos, EU institutions moved their accounts there, then the source code disappeared. European is not a synonym for ethical. | 45s |

## Chapter 4 — Social Media and Young People (3 min, 3 slides)

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| C4.1 | The new rules | Australia bans under 16 (December 2025). France bans under 15 (July 2026). The EU KIDS Act proposes tiers: under 13 parent controlled, 13 to 15 restricted, full access after 15. | 45s |
| C4.2 | Right worry, wrong fix | Parents, schools and governments are right to worry, but the fix is more surveillance: age checks and more data. The platforms themselves do not change. | 55s |
| C4.3 | A different path | You choose your feeds, not the other way around. A school on its own PDS. Move app without losing your people. | 55s |

## Chapter 5 — The Future (5 min, 8 slides)

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| C5.1 | Private data | Spaces is the number one protocol priority. "Once we enable private data, it is like 10 or 100 times the number of use cases we can serve." | 45s |
| C5.2 | Bluesky is two things | The app, and the protocol underneath. Your account is on the network, not in the app. Bluesky is one app of over a thousand in weekly use. | 40s |
| C5.3 | The numbers | Apps in weekly use doubled since January, heading to a thousand. SDK downloads tripled, heading to a million a month. Ten year goal: a billion people. | 40s |
| C5.4 | How it gets paid for | No ads. Affiliate model: the network sends you traffic, takes a small share. The WordPress analogy. | 40s |
| C5.5 | Europe | AtmosphereConf number three, Spring 2027, in Europe. atproto.eu estimates around 2.8 million European-language accounts. | 35s |
| C5.6 | Barcelona | atproto.barcelona, our own meetups. Mozilla Festival, 28 to 30 October, sessions on decentralized social media. | 35s |
| C5.7 | Why communities first | People do not move because everyone is there, and it is easy, and it is free. Not Web 3.0, more like Web 2.5: attach a social identity to the site you already own. | 45s |
| C5.8 | Where to put your account | Bluesky for simple, EuroSky for European non-profit, BlackSky for community, your own server for full sovereignty. You have a choice. That is the whole point. | 50s |

## Close — 3 slides

| ID | Slide | What it says | Time |
|----|-------|--------------|------|
| Z1 | It starts with us | Talk to your local government, your school, your company. Town hall on its own PDS. Students take their data when they graduate. Your handle and a QR code. | 45s |
| Z2 | Sifa Party | Tonight's homework: get your professional profile off LinkedIn. Drop the LinkedIn export at sifa.id/import and it is written to your own PDS. QR on screen. | 90s |
| Z3 | Everything I mentioned | Clickable list of every site in the talk, for the people who want to go and look. | 20s |

---

## Totals

| Chapter | Slides | Speaking time |
|---------|--------|---------------|
| Front | 2 | 1 min |
| 1 Personal story | 5 | 5 min |
| 2 The story so far | 10 | 8 min |
| 3 The ecosystem | 9 | 5 min |
| 4 Young people | 3 | 3 min |
| 5 The future | 8 | 5 min |
| Close | 3 | 1 min |
| **Total** | **40** | **28 min** |

The timeline merge took four slides and about two minutes forty out of the deck, which is what
brings the run time onto the 28 minute budget. It also retires the old suggested cut of C2.10:
that slide is now the Mastodon comparison, not the 2023 milestone. If the slot turns out tighter
than 28, the cuts left are C3.6 (Europe leads, folds into C3.2) and Z3 (the link list becomes a
printed handout). The close is three slides, not two, because Z2, the Sifa party, was added after
the first version of this map. The slide counts here now match `slides.md`.

## Open points

1. **EuroSky address.** The sources and chapter 3 say `eurosky.social`. atproto.eu now sends new accounts to `eurosky.tech`. Confirm which one you tell the room.
2. **Catalan** is out. English and Spanish only.
3. **The Telegram line** in C1.5 is personal and it dates. Keep it as a human note or drop it. Your call, one line either way.
4. **Not in the sources folder:** the 2026 Atmosphere Report from AtmosphereConf (the about 1,000 weekly active apps, 5,600 atproto repos on GitHub). It supports C5.2 and C5.3. Worth adding as a source file.
