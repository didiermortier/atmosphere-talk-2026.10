# Chapter 2 — The Story So Far: Timeline of the AT Protocol

**Target:** ~10 minutes (combined from original Ch2 + Ch3)

---

**2019 — The Beginning**

The story of the AT Protocol starts in 2019. Jack Dorsey, who was running Twitter at the time, announced an initiative called Bluesky. The idea was to create an open, decentralized protocol for social media. Twitter would fund it, but it would be independent — not controlled by Twitter.

Jay Graber was brought in to lead the project in 2021. She was a software engineer who had worked on Zcash, a privacy-focused cryptocurrency. Her name, Lantian, means "blue sky" in Mandarin — a coincidence, since Jack Dorsey chose the name Bluesky before she was involved.

The team started small. They spent the first two years researching and designing the protocol. The question was: if we could rebuild social media from scratch, what would it look like?

**What they built: the AT Protocol**

So what did they actually build? The Authenticated Transfer Protocol, or AT Protocol, is an open, decentralized protocol for social networking. Think of it like email — you can use Gmail, I can use ProtonMail, and we can still email each other because email is a protocol that works across providers. The AT Protocol does the same thing for social media.

There are four key pieces that make it work.

First, your identity. On the AT Protocol, your username is your domain name. My handle is @didiermortier.eu. That is not just branding — it is fundamental. Instead of being "username on someone else's platform", your identity is tied to something you control. Under the hood, every user has a permanent ID called a DID (Decentralized Identifier) that stays with you forever, even if you change your domain or move providers. Every piece of data is signed by its owner, so the network can always verify who created it.

Second, your data. Your posts, likes, and profile live on a Personal Data Server, or PDS. You choose who runs it — Blueshy's servers, a European provider like EuroSky, or your own server if you are technical. You can switch providers at any time and take all your data with you. Your followers, your posts, your history — it all moves. That is something neither Twitter nor Instagram will ever give you.

Third, the network. Relays are servers that collect all public activity across the network and make it available as a firehose. Anyone can subscribe to this firehose and build applications on top of it. Search engines, custom feeds, bots, analytics tools — all built on the same open stream of data. No permission needed.

Fourth, the data format. Everything is JSON with a defined schema called a Lexicon. A post, a like, a follow — they are all structured data with a known format. This means apps can understand each other. An app that shows photos can read the same data as an app that shows text posts. They speak the same language.

Today the network has over 46 million users and more than 3.2 billion posts. 100% of the public content is accessible through the protocol. No API keys, no permission. Anyone can build.

**2022 — The Break**

Everything changed in 2022 when Elon Musk bought Twitter. Twitter's new leadership had no interest in funding a decentralized competitor. Bluesky was cut loose and became an independent public benefit company.

This turned out to be a blessing in disguise. Bluesky was no longer a research project inside Twitter. It had to build an actual product. The team decided to build their own social app as a proof of concept for the protocol. That app became what we now know as Bluesky.

**2023 — Launch**

Bluesky launched as invite-only in early 2023. It was small, exclusive, and mostly used by early adopters and developers. But something interesting happened: people started building on the protocol before Bluesky even had mainstream attention. Custom feeds, moderation tools, alternative clients — the ecosystem began to grow.

One handle at a time, the network crossed one million users.

**The philosophy: open social**

Dan Abramov, who worked on the Bluesky client and is well known for creating Redux, wrote a series of articles that explain the philosophy behind the protocol. He calls it "Open Social" and compares it to the open source movement. His key line: "what open source did for code, open social does for data."

Before social media, you owned your own website. If you did not like your hosting provider, you moved your files to a new one and pointed your domain at the new server. All your links still worked. You were not a hostage.

Closed social media changed that. Your posts, your follows, your likes now live in someone else's database. You are a row in their table. If you leave, you start from zero. As Abramov says, "if you cannot leave without losing something important, the platform has no incentives to respect you."

The AT Protocol flips that. Your data lives on a server you choose. Apps are just windows into your data — they do not own it. Your connections, your posts, your history outlive any app. If an app shuts down or turns evil, someone else can build a new app that reads the same data. No one can take your audience away from you.

Abramov calls this "a social filesystem." Your posts, likes, follows are like files on your computer. Apps read and write those files, but the files belong to you. An app's database is just a cached view of everyone's files.

**2024 — Open to Everyone**

In February 2024, Bluesky opened to the public. The growth curve went vertical. People who had been waiting on the waitlist flooded in. The conversation shifted from "what is Bluesky" to "is this actually a Twitter replacement?"

Then something unexpected happened. In November 2024, Trump won the US presidential election. Millions of users fled X. Bluesky gained one million new users in a single week. Traffic surged by 500 percent. Overnight, Bluesky became the mainstream refuge for people who no longer felt welcome on X.

This election boom pushed Bluesky past 25 million users by the end of 2024. The network had real scale.

**Why it is different from ActivityPub**

By this point, people were comparing Bluesky to Mastodon. Both are decentralized, but the protocols are fundamentally different.

The AT Protocol prioritizes account portability. On ActivityPub, if your server shuts down, moving is difficult — your old posts and followers stay behind. On the AT Protocol, you move everything, including your followers and your data.

The AT Protocol also handles scale differently. ActivityPub delivers messages between individual servers, which causes flooding when a popular account posts. The AT Protocol uses relays to aggregate activity efficiently, making global search and algorithmic feeds possible without overloading anyone.

**2025 — The Developer Ecosystem Explodes**

The real turning point for developers was March 2025, when the first AT Protocol-focused conference was held in Seattle: AtmosphereConf. This was the moment the protocol stepped out of Bluesky's shadow. Developers from outside Bluesky started building in earnest — not just custom feeds and clients, but full applications on their own PDSs.

The firehose was open. Independent PDS providers like EuroSky launched, giving European users a GDPR-compliant hosting option. The ecosystem started to feel real.

Atmosphere apps appeared quickly after the conference. Flashes for photo sharing, like Instagram. Germ for private messaging — the first end-to-end encrypted messenger on the protocol. PopFeed for sharing books, movies, and music. mu, a European-hosted Twitter-like app from EuroSky. Leaflet for blogging. Tangled for collaborative coding. Semble for communities. Blento for link-in-bio pages. And many more — games, event platforms, algorithm feeds.

The common thread: one account works across all of them. You log in once and you are home everywhere. Your followers, your posts, your connections exist on the network, not inside any single app. If you do not like an app, you switch to another. Your data goes with you.

As Abramov says: "An everything app tries to do everything. An everything ecosystem lets everything get done." In the Atmosphere, third party is first party. Anyone can build a better algorithm, a better feed, a better moderation tool.

**2026 — Today**

In March 2026, Jay Graber stepped down as CEO of Bluesky and moved to Chief Innovation Officer. Interim CEO Toni Schneider took over. The message was clear: Bluesky was not a one-person project. The protocol was bigger than any single company.

The network crossed 46 million users. W Social, a controversial EU-backed platform, launched on the AT Protocol but closed its code — sparking debate about what "open" really means. The Atmosphere brand became the public face of the ecosystem. People stopped saying "AT Protocol" and started saying "the Atmosphere."

**Bridge to the next chapter**

So that is where we are today — 46 million people, dozens of apps, an open ecosystem growing faster every month. But it is not all good news. There are real problems in the current landscape: moderation struggles, scaling challenges, the tension between openness and safety. And there is a much bigger storm coming from the European Union that makes all of this even more urgent. Let us talk about that.