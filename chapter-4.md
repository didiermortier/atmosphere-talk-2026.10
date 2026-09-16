# Chapter 4 — Chat Control & EU Regulation

**Target:** ~5 minutes

---

Let us talk about the storm that is coming from the European Union. Because while the Atmosphere is growing, there is a law being debated that could change how every messaging and social platform works — including the ones we rely on today.

**What is Chat Control?**

There is not one Chat Control law. There are two, and they are moving through the EU institutions in parallel. This is why the news can seem contradictory.

Chat Control 1.0 is already in force. It is a temporary law originally adopted in 2021 that allows — but does not require — platforms to scan all private messages for known child sexual abuse material. It expired in April 2026 when Parliament voted against extending it. But in July 2026, the Council pushed it through a fast-track procedure. Only 314 MEPs voted to stop it, short of the 361 needed. So suspicionless mass scanning is now permitted until 2028 — even though a majority of the MEPs who voted wanted it stopped.

Chat Control 2.0 is the permanent version. It was proposed in 2022 and has been deadlocked ever since. It would make detection and reporting of abuse material a legal requirement for digital platforms. After five rounds of negotiations, there is still no agreement. The red line is encryption.

**How it works and why it matters**

If Chat Control 2.0 passes in its current form, platforms that use end-to-end encryption — like WhatsApp, Signal, and iMessage — would be required to insert a pre-encryption scanning layer. Before your message is encrypted, it gets scanned. The encryption itself may remain mathematically intact, but the privacy guarantee is gone. Someone else can read your messages before you send them.

The Council's own lawyers said this still constitutes generalised scanning of communications, which is incompatible with Article 7 of the EU Charter — the right to private life — without reasonable suspicion and prior judicial authorisation.

**Does it actually work?**

This is the most important question. The European Commission itself admits there is no evidence that suspicionless scanning of private messages has increased convictions or rescued more children.

Patrick Breyer, a former MEP who led the fight against Chat Control, shared striking statistics. 99% of Meta's reports under Chat Control involve previously known material — doing nothing to address active abuse. 48% of alerts are not criminally relevant. 40% of resulting investigations target minors themselves. Mass scanning of private chats made up just 36% of abuse reports in 2024 — most reports came from public posts and cloud storage, which were never at risk.

In other words: the most effective tools — court-ordered wiretaps, user reports, scanning of public platforms — remain fully intact. What Chat Control does is add suspicionless surveillance of everyone, while doing almost nothing to actually protect children.

**Why this connects to the AT Protocol**

This is where the AT Protocol becomes relevant beyond just being a nice piece of technology.

The traditional social media model is a walled garden. You are on a platform, the platform controls everything, and the platform can be forced to comply with laws like Chat Control. WhatsApp, Instagram, Facebook Messenger — they all have a single point of control. If the EU tells them to scan, they scan.

The AT Protocol offers a fundamentally different architecture. Your data lives on a PDS that you choose. Your identity is tied to a domain you control. The apps you use are just windows into your data, not the owners of it.

This matters for several reasons.

**Choice and exit**

On the AT Protocol, you can choose your PDS provider. Some are in Europe, some are in the US, some you can run yourself. If one jurisdiction forces harmful surveillance on its providers, you can move your account to a provider in a different jurisdiction. You take your data, your followers, your identity — everything — with you. You are not locked in.

This is the opposite of the closed social model, where leaving means losing your audience and your history. As Dan Abramov said, if you cannot leave without losing something important, the platform has no incentives to respect you. The AT Protocol gives you the ability to leave, which forces every provider to compete on trust.

**Verification without central authority**

One of the challenges with Chat Control is deciding who is real and who is not. Traditional platforms like Twitter and Instagram verify users from a central office. They decide who is legitimate and who is not. This is a single point of failure and a single point of control.

On the AT Protocol, verification works differently. Bluesky has its own verification program. But EuroSky and mu are doing something more interesting: they are exploring a model where each community verifies its own people. A Spanish community verifies Spanish users. A developer community verifies developers. A university verifies its students. The verification is distributed, just like the protocol itself.

This means no single authority can decide who is valid and who is not. And it means verified identity can work even in a world where central platforms are forced to surveil their users.

**Redundancy through multiple app views**

Today, most people access the AT Protocol through Bluesky's app view. But EuroSky is building their own alternative app view. If Bluesky goes down — whether due to a legal order, a technical failure, or political pressure — EuroSky stays up. Users on EuroSky can still access the network, still post, still connect.

This is redundancy by design. No single app is the network. The network is the protocol, and the apps are interchangeable.

**AT Protocol vs Mastodon**

People often compare the AT Protocol to Mastodon and ActivityPub. Both are decentralised alternatives. But there is a key difference that matters for this conversation.

Mastodon runs on small servers, each with tight control over their own community. A Mastodon server is like a small town — friendly, predictable, but isolated. If you leave that server, you lose your followers and your posts. There is no global view of the network. Global search, algorithmic feeds, and cross-server discovery are difficult.

The AT Protocol is the other way around. Your identity is portable across the entire network. You can move between providers without losing anything. The firehose is open, so anyone can build global search, custom feeds, or discovery tools. The network is connected, not fragmented into small islands.

This matters for the fight against Chat Control because a fragmented network is harder to defend. When every server has to make its own stand against legislation, some will comply and some will resist, but users have no way to take their data with them. On the AT Protocol, users can vote with their feet — and their data follows.

**The bottom line**

Chat Control is not a hypothetical threat. Chat Control 1.0 is already law. Chat Control 2.0 is still being negotiated, and the outcome is uncertain. But even if 2.0 is softened, the fact that the EU has passed mass surveillance legislation sets a dangerous precedent.

The AT Protocol is not immune to this. If you run a PDS in the EU, you are subject to EU law. But the protocol gives users a choice that no closed platform can offer: the ability to move, to choose, to leave. And it gives communities the ability to verify their own members, build their own moderation, and run their own infrastructure.

In a world where governments are increasingly demanding access to our private communications, the ability to choose who hosts your data is not just a convenience. It is a fundamental protection.

**There is more: the EU wants to control who can use social media too**

While Chat Control targets encryption and privacy, there is another EU initiative moving in parallel. The European Commission has proposed the EU KIDS Act, a set of rules that would restrict social media access based on age.

The proposal creates a tiered system. Under 13, parents can open fully controlled accounts. Between 13 and 15, introductory accounts with limits on screen time and contact with strangers. Only after 15 can teenagers set up their own accounts. The rules would apply to social media, video platforms, online games, and even AI companions.

France has already become the first EU country to ban social media for under 15s. Poland, Italy, Germany, and Spain are all pushing their own laws. 23 out of 27 EU Member States are now considering some form of age restriction.

On the surface, this is about protecting children. But the mechanism being proposed is significant: platforms would be required to verify the age of every user before letting them access the service. That means ID checks, biometric data, or government-issued verification — for everyone, not just minors. The same infrastructure used for age verification could easily be repurposed for other forms of surveillance.

This matters for the AT Protocol because the protocol's model offers a different path. On the AT Protocol, verification can be distributed. Communities verify their own members. Parents can choose which apps their children use, and which PDS hosts their data. A teenager on the AT Protocol could have an account that is controlled by their parents until a certain age, and then graduate to full control — not because a platform decided so, but because the architecture makes it possible.

The protocol does not have a built-in age verification system. It does not need one. The choice of PDS provider and app determines the rules. And that choice belongs to the user — or, for minors, to their parents.

**Bridge to the next chapter**

So that is the threat. But there is also reason for hope. The AT Protocol is still early. It is still being built. And there is a future where it becomes the default way we communicate online. Let us talk about what that future could look like.