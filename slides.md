# Slides — The Atmosphere

Every slide in the deck, English and Spanish. This file is the source the deck is built from.
Edit here, run `python3 build_deck.py`, and `deck.html` is rebuilt.

Format, one block per slide:

    ### ID — Working title
    - type: statement | points | quote | stats | apps | links | title | agenda | cta
    - chapter: front | 1 | 2 | 3 | 4 | 5 | close
    - time: target seconds
    - en_title / es_title: the headline on screen
    - en_sub / es_sub: the line under it, optional
    - en_item / es_item: repeatable. Points and agenda take plain text.
      Stats take "number | label". Apps take "logo | name | one line".
      Links take "label | url".
    - en_quote / es_quote: for quote slides, plus en_attrib / es_attrib
    - note_en / note_es: what you say. Shown on hold N, never on the audience screen.

The chips at the bottom of a slide come from en_item lines with a url in them, or from a
links line. Keep on-screen text short. Long sentences belong in the note.

---

### F1 — Title
- type: title
- chapter: front
- time: 30s
- en_title: The Atmosphere
- es_title: The Atmosphere
- en_sub: Building the open social web
- es_sub: Building the open social web
- en_item: Didier Mortier | @didiermortier.eu | Terrassa, Barcelona
- es_item: Didier Mortier | @didiermortier.eu | Terrassa, Barcelona
- note_en: Good evening. Short version of who I am: I work in SaaS and domains, I live in Barcelona, and a year and a half ago I left Big Tech social media. Today I want to show you what replaced it, and why it is worth your time as developers.
- note_es: Buenas tardes. La versión corta de quién soy: trabajo en SaaS y dominios, vivo en Barcelona, y hace año y medio dejé las redes sociales de las grandes tecnológicas. Hoy quiero enseñaros que las sustituyo, y por qué vale la pena vuestro tiempo como developers.

### F2 — The five parts
- type: agenda
- chapter: front
- time: 30s
- en_title: Five parts
- es_title: Cinco partes
- en_item: My story: from Meta to the open social web
- es_item: Mi historia: de Meta a la web social abierta
- en_item: The protocol: how it actually works
- es_item: El protocolo: cómo funciona de verdad
- en_item: The ecosystem today: the good and the bad
- es_item: El ecosistema hoy: lo bueno y lo malo
- en_item: Young people and the new rules
- es_item: Los jóvenes y las nuevas normas
- en_item: What comes next, and what you can do
- es_item: Lo que viene, y lo que puedes hacer
- note_en: Five parts, about half an hour. I will keep the tech honest, and I will show you the problems too, not just the pitch.
- note_es: Cinco partes, unos treinta minutos. Sere honesto con la parte técnica, y os enseñaré también los problemas, no solo el discurso.

### C1.1 — Who I am
- type: statement
- chapter: 1
- time: 60s
- en_title: I am not a developer
- es_title: No soy developer
- en_sub: Architecture studies, eleven years in Barcelona, support to sales to customer success
- es_sub: Estudié arquitectura, once años en Barcelona, de soporte a ventas y a customer success
- en_item: Last role: Senior Account Manager at OpenProvider, a domain registrar
- es_item: Último puesto: Senior Account Manager en OpenProvider, un registrador de dominios
- en_item: On the other hand I am quite technical: I run my own home server, and I try every new thing that comes out
- es_item: Por otro lado sí soy bastante técnico: tengo mi propio servidor en casa, y pruebo todo lo nuevo que sale
- note_en: I studied architecture and never practised it. I moved to Barcelona eleven years ago, started in a call centre, went into sales, then customer success. My last job was at a domain registrar, and that job turned out to be the reason I am standing here. So I am not a developer, but I am not a stranger to this either: I run my own home server, I break things and fix them, and I try almost every new thing that comes out. That is the honest version of my profile.
- note_es: Estudié arquitectura y nunca la ejercí. Llegué a Barcelona hace once años, empecé en un call center, pasé a ventas y luego a customer success. Mi último trabajo fue en un registrador de dominios, y ese trabajo resulto ser la razón por la que estoy aquí. No soy developer, pero tampoco soy un desconocido en esto: tengo mi propio servidor en casa, rompo cosas y las arreglo, y pruebo casi todo lo nuevo que sale. Esa es la versión honesta de mi perfil.

### C1.2 — Domains are identity
- type: points
- chapter: 1
- time: 60s
- en_title: Domains are identity
- es_title: Los dominios son identidad
- en_item: At OpenProvider I went deep into domains, DNS, SSL, email security
- es_item: En OpenProvider me metí de lleno en dominios, DNS, SSL, seguridad de email
- en_item: On the AT Protocol, your handle is a domain you own
- es_item: En el AT Protocol, tu handle es un dominio que te pertenece
- en_item: Not "username on platform X". You control it.
- es_item: No es "usuario en la plataforma X". Lo controlas tú.
- note_en: Here is the connection that matters for this talk. The AT Protocol uses domain names as identity. Your handle is literally a domain you own. That is a fundamental shift, and my years in the domain industry gave me a front row seat to why it matters.
- note_es: Aquí está la conexión que importa para esta charla. El AT Protocol usa los nombres de dominio como identidad. Tu handle es literalmente un dominio que te pertenece. Es un cambio de fondo, y mis años en la industria de dominios me hicieron ver por qué importa.

### C1.3 — With Meta, you are the product
- type: points
- chapter: 1
- time: 60s
- en_title: With Meta, you are the product
- es_title: Con Meta, tú eres el producto
- en_item: Instagram was eating my time with doom scrolling
- es_item: Instagram me comía el tiempo con doom scrolling (deslizar sin parar)
- en_item: Ads, noise, and a feed I never chose
- es_item: Anuncios, ruido, y un feed que nunca elegí
- en_item: I noticed it, and I did not like what I saw
- es_item: Me di cuenta, y no me gustó lo que vi
- note_en: Leaving Meta was not sudden. It built up. I was spending too much time on Instagram, letting the algorithm feed me endless content. The ads, the noise, the feeling of being the product instead of the person.
- note_es: Dejar Meta no fue de un dia para otro. Fue acumulandose. Pasaba demasiado tiempo en Instagram, dejando que el algoritmo me diera contenido sin fin. Los anuncios, el ruido, la sensación de ser el producto en vez de la persona.

### C1.4 — The line
- type: statement
- chapter: 1
- time: 60s
- en_title: The line was Meta AI in WhatsApp
- es_title: La linea roja fue Meta AI en WhatsApp
- en_sub: I did not want my private conversations used to train a model
- es_sub: No quería mis conversaciones privadas entrenando un modelo
- en_item: Deleted WhatsApp, Instagram, Facebook
- es_item: Borre WhatsApp, Instagram y Facebook
- en_item: Not a trial, not a detox
- es_item: No fue una prueba, ni un detox
- en_item: That was a year and a half ago
- es_item: Hace ya año y medio
- link_en: Instagram is dropping encrypted chats | https://www.euronews.com/2026/05/08/instagram-is-dropping-end-to-end-encrypted-chats-this-is-what-is-changing
- link_es: Instagram quita los chats cifrados | https://www.euronews.com/2026/05/08/instagram-is-dropping-end-to-end-encrypted-chats-this-is-what-is-changing
- link_en: And the WhatsApp encryption lawsuit | https://proton.me/blog/whatsapp-encryption-lawsuit
- link_es: Y la demanda por el cifrado de WhatsApp | https://proton.me/blog/whatsapp-encryption-lawsuit
- note_en: The final straw was Meta AI being pushed into WhatsApp. I did not want Meta training its AI on my private conversations. So I deleted WhatsApp, Instagram and Facebook. Not as an experiment. I was done. A year and a half later I have not looked back.
- note_es: La gota que colmo el vaso fue ver Meta AI metido en WhatsApp. No quería que Meta entrenara su IA con mis conversaciones privadas. Así que borré WhatsApp, Instagram y Facebook. No como experimento. Había terminado. Ano y medio después no he vuelto atrás.

### C1.5 — What I use now
- type: points
- chapter: 1
- time: 60s
- en_title: What I use now
- es_title: Lo que uso ahora
- en_item: Signal for messaging. iMessage for the holdouts
- es_item: Signal para mensajes. iMessage para los que no se mueven
- en_item: Telegram for AI and for my girlfriend. It is a grey area.
- es_item: Telegram para la IA y para mi novia. Es un terreno gris.
- en_item: Bluesky for social, EuroSky for my account
- es_item: Bluesky para lo social, EuroSky para mi cuenta
- en_item: That is where I found the AT Protocol, and this community
- es_item: Ahí encontré el AT Protocol, y esta comunidad
- link_en: Signal | https://signal.org
- link_es: Signal | https://signal.org
- link_en: Telegram pulled from the App Store | https://www.forbes.com/sites/siladityaray/2026/08/04/telegram-briefly-removed-from-apples-app-store-over-alleged-child-sexual-abuse-content/
- link_es: Telegram fuera de la App Store | https://www.forbes.com/sites/siladityaray/2026/08/04/telegram-briefly-removed-from-apples-app-store-over-alleged-child-sexual-abuse-content/
- link_en: Telegram's CEO charged in France | https://www.cnbc.com/2024/09/06/telegram-ceo-pavel-durov-says-france-charges-are-misguided.html
- link_es: El CEO de Telegram, acusado en Francia | https://www.cnbc.com/2024/09/06/telegram-ceo-pavel-durov-says-france-charges-are-misguided.html
- note_en: For messaging, Signal is the best and most secure option, that is my daily driver. For the people who will not leave iMessage, I use that too. And yes, I still use Telegram, as you may have noticed. It is a grey area: a for-profit company, a Russian founder now living in Dubai, and enough controversies that I would not recommend it. I use it for AI tools and because my girlfriend has not moved yet. One caveat I do believe in: business and private are not the same. If you run a business and your customers are on WhatsApp or Instagram, use it, that is making you money. For myself, I try not to use it at all. For social, Bluesky, and EuroSky for the account underneath. That is how I ended up in the AT Protocol, and how this talk ended up in Terrassa, after Dario from atproto.barcelona asked me to give it.
- note_es: Para mensajes, Signal es la mejor opción y la más segura, es mi herramienta diaria. Para los que no sueltan iMessage, también lo uso. Y sí, sigo usando Telegram, como habréis notado. Es un terreno gris: una empresa con ánimo de lucro, un fundador ruso que vive en Dubái, y suficientes polémicas como para no recomendarla. Yo la uso para herramientas de IA y porque mi novia todavía no se ha movido. Un matiz en el que sí creo: negocio y privado no son lo mismo. Si tienes un negocio y tus clientes están en WhatsApp o Instagram, úsalos, eso te da dinero. Para mí, intento no usarlos nada. Para lo social, Bluesky, y EuroSky para la cuenta por debajo. Así acabé en el AT Protocol, y así acabó esta charla en Terrassa, después de que Dario, de atproto.barcelona, me propusiera darla.

### C2.1 — 2019 to 2022
- type: points
- chapter: 2
- time: 50s
- en_title: 2019 to 2022 - from an idea to independence
- es_title: 2019 a 2022 - de una idea a la independencia
- img: assets/jay-graber.jpg
- img_credit: Photo: Wikimedia Commons, CC BY-SA 4.0
- en_item: 2019 - Twitter starts Bluesky: an open protocol, funded by Twitter, controlled by nobody
- es_item: 2019 - Twitter arranca Bluesky: un protocolo abierto, financiado por Twitter, controlado por nadie
- en_item: 2021 - Jay Graber takes the lead, from Zcash
- es_item: 2021 - Jay Graber toma el mando, venía de Zcash
- en_item: 2022 - Musk buys Twitter, Bluesky is cut loose and becomes a public benefit company
- es_item: 2022 - Musk compra Twitter, Bluesky se independiza y se convierte en public benefit company
- note_en: Quick timeline before the how. It starts in 2019, when Jack Dorsey announced Bluesky: an open protocol that Twitter would fund but not control. Jay Graber came in to lead it in 2021, from Zcash. Then in 2022 Musk bought Twitter, the new leadership wanted nothing to do with open source, and Bluesky was cut loose as an independent public benefit company. That turned out to be a blessing: it had to become a real product.
- note_es: Una cronología rápida antes del cómo. Empieza en 2019, cuando Jack Dorsey anunció Bluesky: un protocolo abierto que Twitter financiaría pero no controlaría. Jay Graber llegó a liderarlo en 2021, desde Zcash. Y en 2022 Musk compró Twitter, la nueva dirección no quería saber nada del open source, y Bluesky se independizó como public benefit company. Al final fue una bendición: tuvo que convertirse en un producto real.

### C2.2 — 2023 to 2026
- type: points
- chapter: 2
- time: 50s
- en_title: 2023 to 2026 - a million users, then the developer wave
- es_title: 2023 a 2026 - un millón de usuarios, luego la ola developer
- en_item: 2023 - invite only, one million users, and the builders arrive before the crowd
- es_item: 2023 - solo por invitación, un millón de usuarios, y los builders llegan antes que el público
- en_item: 2024 - public launch, then the US election: a million users in a week, 25 million by December
- es_item: 2024 - apertura pública, luego las elecciones de EEUU: un millón de usuarios en una semana, 25 millones en diciembre
- en_item: 2025 and 2026 - the Seattle conference, independent PDS providers, Graber moves to CINO
- es_item: 2025 y 2026 - la conferencia de Seattle, proveedores de PDS independientes, Graber pasa a CINO
- en_item: 2026 - the front gets a friendlier name, the Atmosphere, while AT Protocol stays the protocol underneath
- es_item: 2026 - el frente estrena un nombre más amable, the Atmosphere, mientras el AT Protocol sigue siendo el protocolo por debajo
- link_en: AtmosphereConf | https://atmosphereconf.org
- link_es: AtmosphereConf | https://atmosphereconf.org
- note_en: Then the growth. Invite only in 2023, one million users, and interestingly the builders arrived before the crowd. February 2024 it opened to everyone, and after the US election it gained a million users in a week and passed 25 million by December. Since the Seattle conference in March 2025 it has been a developer wave: independent PDS providers, European hosting, apps by the dozen. In March 2026 Jay Graber moved to Chief Innovation Officer and Toni Schneider took over. And that same year the name in use changed. Nothing underneath changed: the AT Protocol is still the protocol, the layer the developers build on. What changed is the front end, where the ecosystem now puts one friendlier name over the whole group of things: the Atmosphere.
- note_es: Luego el crecimiento. Solo por invitación en 2023, un millón de usuarios, y lo interesante: los builders llegaron antes que el público. En febrero de 2024 se abrió a todos, y tras las elecciones de EEUU ganó un millón de usuarios en una semana y pasó de 25 millones en diciembre. Desde la conferencia de Seattle, en marzo de 2025, ha sido una ola developer: proveedores de PDS independientes, hosting europeo, apps por docenas. En marzo de 2026 Jay Graber pasó a Chief Innovation Officer y Toni Schneider asumió como CEO. Y ese mismo año cambió el nombre de uso. Por debajo no cambió nada: el AT Protocol sigue siendo el protocolo, la capa sobre la que construyen los developers. Lo que cambió es el frente, donde el ecosistema ahora pone un nombre más amable sobre todo el conjunto: the Atmosphere.

### C2.3 — What is the AT Protocol
- type: statement
- chapter: 2
- time: 45s
- en_title: What is the AT Protocol?
- es_title: ¿Qué es el AT Protocol?
- en_sub: Think of email. You use Gmail, I use ProtonMail, and we still reach each other. Same idea, for social media.
- es_sub: Piensa en el email. Tú usas Gmail, yo uso ProtonMail, y seguimos hablando. La misma idea, para redes sociales.
- en_item: The Authenticated Transfer Protocol
- es_item: El Authenticated Transfer Protocol
- en_item: Open, decentralized, owned by no one
- es_item: Abierto, descentralizado, sin dueño
- en_item: Email is a protocol, not a company. This is the same move.
- es_item: El email es un protocolo, no una empresa. Este es el mismo movimiento.
- en_item: Four pieces coming up: your identity, your data, the network, the format
- es_item: Cuatro piezas a continuación: tu identidad, tus datos, la red, el formato
- note_en: So what did they build? The AT Protocol. Think of it like email. You can use Gmail, I can use ProtonMail, and we still email each other, because email is a protocol that works across providers. This does the same thing for social media. Four pieces make it work, and they are what comes next: your identity, your data, the network, and the format.
- note_es: ¿Y qué construyeron? El AT Protocol. Piénsalo como el email. Tú puedes usar Gmail, yo ProtonMail, y seguimos escribiendonos, porque el email es un protocolo que funciona entre proveedores. Esto hace lo mismo para las redes sociales. Cuatro piezas lo hacen funcionar, y son las que vienen ahora: tu identidad, tus datos, la red y el formato.

### C2.4 — Piece one: identity
- type: points
- chapter: 2
- time: 45s
- en_title: One: your identity
- es_title: Uno: tu identidad
- en_item: Your handle is a domain you own, like @didiermortier.eu
- es_item: Tu handle es un dominio que puedes comprar, como @didiermortier.eu
- en_item: Under it, a DID: a permanent ID that stays with you
- es_item: Debajo, un DID: un identificador permanente que va contigo
- en_item: Every record is signed by its owner, so the network can verify it
- es_item: Cada registro va firmado por su dueño, y la red puede verificarlo
- link_en: The PLC directory gets its own organization | https://blog.plcred.org/3mwlphq42d227
- link_es: El directorio PLC ya tiene su propia organización | https://blog.plcred.org/3mwlphq42d227
- note_en: First, identity. Your username is your domain name. Under the hood every user has a permanent ID called a DID that stays with you forever, even if you change domain or move provider. Every piece of data is signed, so the network can always verify who created it.
- note_es: Primero, la identidad. Tu nombre de usuario es tu dominio. Por debajo, cada usuario tiene un identificador permanente llamado DID que te acompana siempre, aunque cambies de dominio o de proveedor. Cada dato va firmado, así la red siempre puede verificar quién lo creó.

### C2.5 — Piece two: your data
- type: points
- chapter: 2
- time: 45s
- en_title: Two: your data
- es_title: Dos: tus datos
- en_item: Your posts live on a Personal Data Server, a PDS
- es_item: Tus posts viven en un Personal Data Server, un PDS
- en_item: You choose who runs it: Bluesky, EuroSky, or your own server
- es_item: Tú eliges quién lo lleva: Bluesky, EuroSky, o tu propio servidor
- en_item: Change provider and take everything with you, followers included
- es_item: Cambia de proveedor y llévate todo, incluidos tus seguidores
- link_en: My own account, opened in the browser | https://pdsls.dev/at://did:plc:dhckga4os5p3owgewd4hevca
- link_es: Mi propia cuenta, abierta en el navegador | https://pdsls.dev/at://did:plc:dhckga4os5p3owgewd4hevca
- note_en: Second, your data. Your posts, likes and profile live on a Personal Data Server. You choose who runs it. You can switch providers at any time and take everything with you: your followers, your posts, your history. Neither Twitter nor Instagram will ever give you that.
- note_es: Segundo, tus datos. Tus posts, likes y perfil viven en un Personal Data Server. Tú eliges quién lo lleva. Puedes cambiar de proveedor cuando quieras y llevarte todo: seguidores, posts, historial. Ni Twitter ni Instagram te darán eso jamás.

### C2.6 — Piece three: the network
- type: points
- chapter: 2
- time: 45s
- en_title: Three: the network
- es_title: Tres: la red
- en_item: Relays collect all public activity into a firehose
- es_item: Los relays recogen toda la actividad pública en un firehose
- en_item: Anyone can subscribe and build on it
- es_item: Cualquiera puede suscribirse y construir encima
- en_item: No API keys. No permission. No gatekeeper.
- es_item: Sin API keys. Sin permisos. Sin portero.
- link_en: The live firehose | https://pdsls.dev/streams?type=firehose
- link_es: El firehose en vivo | https://pdsls.dev/streams?type=firehose
- note_en: Third, the network. Relays collect all public activity and make it available as a firehose. Anyone can subscribe and build applications on top of it: search engines, custom feeds, bots, analytics. This is the part I would underline for the developers in this room. No permission needed.
- note_es: Tercero, la red. Los relays recogen toda la actividad pública y la ofrecen como un firehose. Cualquiera puede suscribirse y construir aplicaciones encima: buscadores, feeds, bots, analitica. Esta es la parte que subrayaría para los developers de esta sala. No hace falta permiso.

### C2.7 — Piece four: the format
- type: points
- chapter: 2
- time: 40s
- en_title: Four: the format
- es_title: Cuatro: el formato
- en_item: Everything is JSON with a shared schema, a Lexicon
- es_item: Todo es JSON con un formato compartido, un Lexicon
- en_item: A post, a like, a follow: structured data with a known shape
- es_item: Un post, un like, un follow: datos estructurados con una forma conocida
- en_item: Apps understand each other. They speak one language.
- es_item: Las apps se entienden entre ellas. Hablan un mismo idioma.
- link_en: The lexicons, in a browser | https://atproto.at/lexicons
- link_es: Los lexicons, en el navegador | https://atproto.at/lexicons
- link_en: Lexicon Community | https://mu.social/profile/lexicon.community
- link_es: Lexicon Community | https://mu.social/profile/lexicon.community
- note_en: Fourth, the format. Everything is JSON with a defined schema called a Lexicon. This means apps can understand each other. An app that shows photos can read the same data as an app that shows text posts.
- note_es: Cuarto, el formato. Todo es JSON con un esquema definido llamado Lexicon. Esto significa que las apps se entienden entre ellas. Una app de fotos puede leer los mismos datos que una app de texto.

### C2.8 — Where it stands today
- type: stats
- chapter: 2
- time: 40s
- en_title: Where it stands today
- es_title: Dónde está hoy
- en_item: 46M+ | accounts on the network
- es_item: 46M+ | cuentas en la red
- en_item: 3.2B+ | posts
- es_item: 3.200M+ | posts
- en_item: 100% | of public content, open to anyone
- es_item: 100% | del contenido público, abierto a cualquiera
- link_en: bskycheck, live counters | https://bskycheck.com/stats.php
- link_es: bskycheck, contadores en vivo | https://bskycheck.com/stats.php
- link_en: Bluesky stats | https://theblue.social/tools/bluesky-stats
- link_es: Bluesky stats | https://theblue.social/tools/bluesky-stats
- note_en: Numbers from the public trackers this month. Over 46 million accounts, more than 3.2 billion posts, and one hundred percent of public content reachable through the protocol. No API keys, no permission, anyone can build.
- note_es: Datos públicos de este mes. Mas de 46 millones de cuentas, más de 3.200 millones de posts, y el cien por cien del contenido público accesible a través del protocolo. Sin API keys, sin permisos, cualquiera puede construir.

### C2.9 — Open social
- type: quote
- chapter: 2
- time: 60s
- en_title: The philosophy
- es_title: La filosofía
- en_quote: What open source did for code, open social does for data.
- es_quote: What open source did for code, open social does for data.
- en_attrib: Dan Abramov, creator of Redux, worked on the Bluesky client
- es_attrib: Dan Abramov, creador de Redux, trabajó en el cliente de Bluesky
- en_item: With traditional social media, you are the product
- es_item: Con las redes sociales tradicionales, eres el producto
- en_item: If you cannot leave without losing something important, the platform has no incentives to respect you
- es_item: Si no puedes irte sin perder algo importante, la plataforma no tiene ningún incentivo para respetarte
- en_item: Apps are windows into your data. They do not own it.
- es_item: Las apps son ventanas a tus datos. No son sus dueños.
- link_en: Open Social, by Dan Abramov | https://overreacted.io/open-social/
- link_es: Open Social, de Dan Abramov | https://overreacted.io/open-social/
- note_en: Dan Abramov, who created Redux and worked on the Bluesky client, wrote a series of articles about the philosophy behind this. He calls it open social and compares it to the open source movement. Before social media you owned your own website. If you did not like your hosting, you moved your files and pointed your domain at the new server. Closed social media changed that. Your posts, follows and likes live in someone else's database. You are a row in their table.
- note_es: Dan Abramov, creador de Redux y colaborador del cliente de Bluesky, escribio una serie de artículos sobre la filosofía que hay detrás. Lo llama open social y lo compara con el movimiento del open source. Antes de las redes sociales tenias tu propia web. Si no te gustaba tu hosting, movias los archivos y apuntabas el dominio al nuevo servidor. Las redes sociales cerradas cambiaron eso. Tus posts, follows y likes viven en la base de datos de otro. Eres una fila en su tabla.

### C2.10 — Why not Mastodon
- type: points
- chapter: 2
- time: 60s
- en_title: Why not Mastodon?
- es_title: ¿Por qué no Mastodon?
- en_item: Portability: on ActivityPub, a dead server takes your posts and followers with it
- es_item: Portabilidad: en ActivityPub, un servidor caído se lleva tus posts y seguidores
- en_item: On the AT Protocol you move everything, and the links keep working
- es_item: En el AT Protocol te llevas todo, y los enlaces siguen funcionando
- en_item: Scale: relays instead of server to server flooding, which is what makes global search and real feeds possible
- es_item: Escala: relays en vez de tráfico entre servidores, que es lo que hace posible la búsqueda global y feeds de verdad
- note_en: By this point people were comparing Bluesky to Mastodon. Both are decentralized, the protocols are different. On ActivityPub, if your server shuts down, moving is hard, your posts and followers stay behind. Here you take everything. And scale: ActivityPub delivers messages between individual servers, which causes flooding when a popular account posts. Relays aggregate activity, and that is what makes global search and algorithmic feeds possible.
- note_es: A estas alturas la gente comparaba Bluesky con Mastodon. Los dos son descentralizados, los protocolos son distintos. En ActivityPub, si tu servidor cierra, mudarse es difícil: tus posts y tus seguidores se quedan atrás. Aquí te lo llevas todo. Y la escala: ActivityPub entrega mensajes entre servidores individuales, lo que crea demasiado tráfico cuando una cuenta popular publica. Los relays agregan la actividad, y eso es lo que hace posible la búsqueda global y los feeds con algoritmo.

### C3.1 — The ecosystem today
- type: points
- chapter: 3
- time: 30s
- en_title: The ecosystem today
- es_title: El ecosistema hoy
- en_item: 445 listings in the AT Store, and more every week
- es_item: 445 listings en la AT Store, y más cada semana
- en_item: Real infrastructure, real users, real projects
- es_item: Infraestructura real, usuarios reales, proyectos reales
- en_item: And real problems. I will show you both.
- es_item: Y problemas reales. Os enseñaré los dos lados.
- en_item: The AT Store | https://atstore.fyi
- es_item: The AT Store | https://atstore.fyi
- note_en: So where are we right now? The ecosystem in 2026 is vibrant, growing and genuinely exciting. 445 listings in the store, and new ones every week. But it also has real problems. Let us look at both sides.
- note_es: ¿Dónde estamos ahora? El ecosistema en 2026 es vibrante, crece y es genuinamente interesante. 445 listings en la tienda, y nuevas cada semana. Pero también tiene problemas reales. Vamos a ver los dos lados.

### C3.2 — EuroSky and mu.social
- type: apps
- chapter: 3
- time: 40s
- en_title: EuroSky and mu.social
- es_title: EuroSky y mu.social
- en_item: eurosky.social | EuroSky | The biggest European PDS. Run by Stichting Modal, a Dutch non-profit | https://eurosky.social
- es_item: eurosky.social | EuroSky | El mayor PDS europeo. Lo lleva Stichting Modal, una fundación holandesa sin ánimo de lucro | https://eurosky.social
- en_item: mu.social | mu.social | They forked the Bluesky app and shipped their own. That is the point. | https://mu.social
- es_item: mu.social | mu.social | Hicieron un fork de la app de Bluesky y sacaron la suya. Esa es la cuestión. | https://mu.social
- note_en: EuroSky is the biggest European PDS provider, run by a non-profit foundation in the Netherlands. On top of that they built mu.social, a fork of the Bluesky app. Because Bluesky is fully open source, they took the code, adapted it for a European audience, and shipped it. That is the part I want the developers in this room to notice: the protocol and the apps are open, so anyone can fork and build their own version.
- note_es: EuroSky es el mayor proveedor de PDS europeo, lo lleva una fundación sin ánimo de lucro en Países Bajos. Encima de eso construyeron mu.social, un fork de la app de Bluesky. Como Bluesky es totalmente open source, cogieron el código, lo adaptaron para el público europeo, y lo sacaron. Esa es la parte que quiero que vean los developers de esta sala: el protocolo y las apps son abiertos, cualquiera puede hacer un fork y construir su versión.

### C3.3 — The non-profit model
- type: points
- chapter: 3
- time: 35s
- en_title: The non-profit model matters
- es_title: El modelo sin ánimo de lucro importa
- en_item: EuroSky, our biggest European PDS, is run by a non-profit
- es_item: EuroSky, nuestro mayor PDS europeo, lo lleva una fundación sin ánimo de lucro
- en_item: Signal and Proton, for example
- es_item: Signal y Proton, por ejemplo
- en_item: What matters is not the passport: open code, portable data, no single owner
- es_item: Lo que importa no es de dónde venga: código abierto, datos portables, ningún dueño único
- en_item: The identity directory (PLC) now belongs to an independent Swiss association
- es_item: El directorio de identidades (PLC) ahora pertenece a una asociación suiza independiente
- link_en: The PLC directory gets its own organization | https://blog.plcred.org/3mwlphq42d227
- link_es: El directorio PLC ya tiene su propia organización | https://blog.plcred.org/3mwlphq42d227
- note_en: The protocol itself is not a company, it is an open standard being handed to the IETF. Bluesky is a public benefit company, separate from the protocol. And there are good examples of this model: Signal, Proton, and our own EuroSky, the biggest European PDS, run by a non-profit foundation in the Netherlands. It is happening on the protocol itself too. The PLC directory, which holds every account's identity and which server hosts it, now has its own independent Swiss association, with a board drawn from Let's Encrypt, Google and the W3C. That is the identity layer leaving one company's hands. The point is that a project is not better because it is European or worse because it is American. What matters is that the code is open, the data is portable, and no single entity controls the network.
- note_es: El protocolo en si no es una empresa, es un estándar abierto que se está pasando al IETF. Bluesky es una public benefit company, separada del protocolo. Y hay buenos ejemplos de este modelo: Signal, Proton, y EuroSky, el mayor PDS europeo, que lo lleva una fundación sin ánimo de lucro en Países Bajos. Y en el propio protocolo también está pasando. El directorio PLC, que guarda la identidad de cada cuenta y en qué servidor vive, ahora tiene su propia asociación suiza independiente, con un consejo que viene de Let's Encrypt, Google y la W3C. Es la capa de identidad saliendo de las manos de una sola empresa. La cuestión es que un proyecto no es mejor por ser europeo ni peor por ser americano. Lo que importa es que el código sea abierto, los datos portables, y que ninguna entidad controle la red.

### C3.4 — Data you actually keep
- type: apps
- chapter: 3
- time: 40s
- en_title: Data you actually keep
- es_title: Datos que de verdad te llevas
- en_item: popfeed.social | PopFeed | Your films, books, games and music. Reviews you can take with you. | https://popfeed.social
- es_item: popfeed.social | PopFeed | Tus películas, libros, juegos y música. Reseñas que te puedes llevar. | https://popfeed.social
- en_item: sifa.id | Sifa ID | The professional profile. Endorsements signed by real accounts. | https://sifa.id
- es_item: sifa.id | Sifa ID | El perfil profesional. Recomendaciones firmadas por cuentas reales. | https://sifa.id
- en_item: tangled.org | Tangled | Social coding. Your repos and activity on your own PDS. | https://tangled.org
- es_item: tangled.org | Tangled | Código social. Tus repos y tu actividad en tu propio PDS. | https://tangled.org
- en_item: atmo.rsvp | atmo.rsvp | Events for the open social web. Sign in with your account, your RSVPs stay yours. | https://atmo.rsvp
- es_item: atmo.rsvp | atmo.rsvp | Eventos para la web social abierta. Entra con tu cuenta y tus RSVP son tuyos. | https://atmo.rsvp
- note_en: Examples of the same idea. PopFeed for logging films, books, games and music, connected to TMDB, with your reviews stored on the protocol. Sifa ID as a LinkedIn replacement that pulls your activity from across the network, with endorsements signed by real accounts. Tangled for social coding, GitHub but your repos and activity live on your own PDS. Dan Abramov uses it. And atmo.rsvp for events: sign in with the account you already have, and your RSVPs travel with you.
- note_es: Ejemplos de la misma idea. PopFeed para registrar películas, libros, juegos y música, conectado a TMDB, con tus reseñas guardadas en el protocolo. Sifa ID como alternativa a LinkedIn, que recoge tu actividad de toda la red, con recomendaciones firmadas por cuentas reales. Tangled para código social: como GitHub, pero tus repos y tu actividad viven en tu propio PDS. Dan Abramov lo usa. Y atmo.rsvp para eventos: entras con la cuenta que ya tienes, y tus RSVP viajan contigo.

### C3.5 — And everything else
- type: apps
- chapter: 3
- time: 35s
- en_title: And everything else
- es_title: Y todo lo demás
- en_item: marque.at | Marque | A registrar built for the open web. Your domain becomes your handle. | https://marque.at
- es_item: marque.at | Marque | Un registrador hecho para la web abierta. Tu dominio se convierte en tu handle. | https://marque.at
- en_item: grain.social | Grain | Photo galleries on the protocol. | https://grain.social
- es_item: grain.social | Grain | Galerías de fotos sobre el protocolo. | https://grain.social
- en_item: npmx.dev | npmx | A modern browser for the npm registry on the protocol | https://npmx.dev
- es_item: npmx.dev | npmx | Un navegador moderno para el registro de npm sobre el protocolo | https://npmx.dev
- en_item: pckt.blog | pckt.blog | Distraction free blogging, 4.44 dollars a month for the paid tier | https://pckt.blog
- es_item: pckt.blog | pckt.blog | Blogging sin distracciones, 4,44 dólares al mes la versión de pago | https://pckt.blog
- en_item: standard.site | standard.site | One schema for long-form publishing. Add the plugin to a site, or one link tag, and every post also becomes an AT Protocol record | https://standard.site
- es_item: standard.site | standard.site | Un esquema para la publicación de formato largo. Pones el plugin en una web, o una etiqueta link, y cada post pasa a ser también un registro en el AT Protocol | https://standard.site
- note_en: There are apps for almost everything now. Marque is a registrar built for the open web: you buy a domain and it becomes your handle, which is very close to my own job. Grain for photo galleries. npmx is a modern browser for the npm registry. pckt.blog for distraction free blogging. Flashes for photos and video, Germ for encrypted messaging, games like Chaos Soccer and Witchsky. And standard.site, which is the one to remember if you build websites for clients: one schema for long-form publishing, so a blog, a newsroom, a documentation site and a reader all agree on the same format. Put the plugin on a WordPress site, or add a single link tag, and every post is also an AT Protocol record. You hand a client a website, and it plugs straight into the protocol. What ties everything together is one login. The same handle everywhere, and your data flows between apps.
- note_es: Ya hay apps para casi todo. Marque es un registrador hecho para la web abierta: compras un dominio y se convierte en tu handle, muy cerca de mi propio trabajo. Grain para galerías de fotos. npmx es un navegador moderno para el registro de npm. pckt.blog para escribir sin distracciones. Flashes para fotos y vídeo, Germ para mensajería cifrada, juegos como Chaos Soccer y Witchsky. Y standard.site, que es el que hay que recordar si haces webs para clientes: un esquema para la publicación de formato largo, para que un blog, una redacción, una documentación y un lector hablen el mismo formato. Pones el plugin en un WordPress, o añades una sola etiqueta link, y cada post es también un registro en el AT Protocol. Entregas una web a un cliente, y queda conectada al protocolo. Lo que lo une todo es un solo login. El mismo handle en todas partes, y tus datos circulan entre apps.

### C3.6 — Europe is not a side note
- type: points
- chapter: 3
- time: 30s
- en_title: Europe is not a side note
- es_title: Europa no es un detalle menor
- en_item: EuroSky, mu.social, atmo.rsvp, Flashes, Sifa ID, npmx, Tangled, Currents
- es_item: EuroSky, mu.social, atmo.rsvp, Flashes, Sifa ID, npmx, Tangled, Currents
- en_item: Built and hosted in Europe, with European privacy standards
- es_item: Construidas y alojadas en Europa, con estándares europeos de privacidad
- en_item: This is not an American project. It is genuinely global.
- es_item: No es un proyecto americano. Es genuinamente global.
- note_en: Europe is playing a major role. EuroSky, mu.social, atmo.rsvp, Flashes, Sifa ID, npmx, Tangled, Currents and many more are built and hosted in Europe. It shows the protocol is not just an American project, and European developers are leading on privacy, portability and user rights.
- note_es: Europa juega un papel importante. EuroSky, mu.social, atmo.rsvp, Flashes, Sifa ID, npmx, Tangled, Currents y muchas más se construyen y alojan en Europa. Demuestra que el protocolo no es solo un proyecto americano, y que los developers europeos lideran en privacidad, portabilidad y derechos de usuario.

### C3.7 — The hard part: it is all public
- type: points
- chapter: 3
- time: 35s
- en_title: The hard part: it is all public
- es_title: La parte dura: todo es público
- en_item: Public by design is a gift if you build on the firehose
- es_item: Público por diseño es un regalo si construyes sobre el firehose
- en_item: It is a limit if you want to share something privately
- es_item: Es un límite si quieres compartir algo en privado
- en_item: Spaces is in alpha: private posts, groups, communities. Back to this at the end.
- es_item: Spaces está en alpha: posts privados, grupos, comunidades. Volvemos a esto al final.
- link_en: AT Protocol Spaces, the alpha | https://atproto.com/blog/atproto-spaces-alpha
- link_es: AT Protocol Spaces, la alpha | https://atproto.com/blog/atproto-spaces-alpha
- note_en: One thing the protocol cannot do yet is private posts. Everything is public by design. That is a feature for developers building on the firehose, and a limitation for users. Spaces is in alpha now, which will add private posts, group conversations and membership communities. I will come back to that in the last chapter.
- note_es: Algo que el protocolo aún no sabe hacer son los posts privados. Todo es público por diseño. Es una ventaja si construyes sobre el firehose, y una limitación para los usuarios. Spaces está en alpha, anadira posts privados, conversaciones de grupo y comunidades de miembros. Vuelvo a esto en el último capitulo.

### C3.8 — The three hard problems
- type: points
- chapter: 3
- time: 55s
- en_title: The hard parts
- es_title: Las partes difíciles
- en_item: Moderation is fragmented. Anyone can run a labeler, and that is also the problem.
- es_item: La moderación está fragmentada. Cualquiera puede correr un labeler, y eso es también el problema.
- en_item: Community verification is the answer, and it is starting: mu.social verification, and my own labeler for Spain
- es_item: La verificación de la comunidad es la respuesta, y ya empieza: la verificación de mu.social, y mi propio labeler para España
- en_item: No monetisation layer yet. No ads, no platform tax, but no obvious revenue either.
- es_item: Todavía no hay forma de ganar dinero. Sin anuncios, sin comisión de plataforma, pero tampoco ingresos claros.
- en_item: Discovery: 445 listings, no review process, no quality control
- es_item: Encontrar apps: 445 listings, sin revisión, sin control de calidad
- en_item: And a reminder that this is real: Tangled was knocked offline by a DDoS attack this month
- es_item: Y un recordatorio de que esto es real: este mes un ataque DDoS tumbó Tangled
- link_en: mu.social verification | https://mu.social/verification/
- link_es: Verificación de mu.social | https://mu.social/verification/
- link_en: Spain Atmosphe.re, the labeler I run | https://mu.social/profile/spain-atmosphe.re
- link_es: Spain Atmosphe.re, el labeler que llevo | https://mu.social/profile/spain-atmosphe.re
- link_en: Tangled, hit by a DDoS attack | https://status.tangled.org/
- link_es: Tangled, atacada con un DDoS | https://status.tangled.org/
- link_en: Bluesky's own outage | https://bsky.social/about/blog/04-20-2026-bluesky-service-interruption-update3
- link_es: La caída de Bluesky | https://bsky.social/about/blog/04-20-2026-bluesky-service-interruption-update3
- note_en: Three hard problems. Moderation is powerful in theory and fragmented in practice: you can subscribe to the moderation you trust, but someone has to run it, and for many apps that is still unsolved. Monetisation does not exist yet: Bluesky runs no ads, there is no ad inventory, no way for creators to earn from the network. And discovery: with three hundred apps there is no quality control, users have to work out which ones are good. Plus a DDoS attack took Tangled offline this month, and Bluesky had its own outage in April. As the ecosystem grows, it attracts attention. The answer to the moderation problem is community verification: mu.social runs a verification service, and I run a small labeler called Spain Atmosphe.re, where people in the Barcelona community can vouch for accounts. That is what a labeler is: a group you trust, doing the moderation for you.
- note_es: Tres problemas serios. La moderación es potente en teoría y fragmentada en la práctica: puedes suscribirte a la moderación en la que confias, pero alguien tiene que llevarla, y en muchas apps sigue sin resolverse. Ganar dinero todavía no está resuelto: Bluesky no pone anuncios, no hay espacio para anuncios, y no hay forma de que creadores y developers ganen dinero con la red. Y encontrar apps: con trescientas apps no hay control de calidad, los usuarios tienen que averiguar cuáles son buenas. Además, un ataque DDoS tumbó Tangled este mes, y Bluesky tuvo su propia caída en abril. Cuando el ecosistema crece, atrae atención. La respuesta al problema de la moderación es la verificación de la comunidad: mu.social tiene un servicio de verificación, y yo llevo un labeler pequeño que se llama Spain Atmosphe.re, donde la gente de la comunidad de Barcelona puede avalar cuentas. Eso es un labeler: un grupo en el que confías, que hace la moderación por ti.

### C3.9 — W Social
- type: points
- chapter: 3
- time: 45s
- en_title: W Social: a cautionary tale
- es_title: W Social: un cuento con moraleja
- en_item: Launched at Davos in January 2026, backed by Swedish investors and former ministers
- es_item: Se lanzó en Davos en enero de 2026, con inversores suecos y ex ministros detrás
- en_item: The European Commission, von der Leyen and the ECB moved their accounts there
- es_item: La Comisión Europea, von der Leyen y el BCE movieron allí sus cuentas
- en_item: Then the public source code repository disappeared
- es_item: Y después desapareció su repositorio público de código
- en_item: European is not a synonym for ethical
- es_item: Europeo no es sinónimo de ético
- link_en: W Social, TruthSocial with a European accent | https://wecanjustdothings.leaflet.pub/3mokohkfb4224
- link_es: W Social, TruthSocial con acento europeo | https://wecanjustdothings.leaflet.pub/3mokohkfb4224
- note_en: One project deserves special mention. W Social launched at Davos, backed by Swedish investors and former ministers, positioned as the trustworthy European alternative to Twitter. Built on the AT Protocol. Then it deleted its public source code repository. No explanation. And EU institutions had already moved their official accounts there. Official EU data on a private, for profit company's servers. Compare that with EuroSky: a non-profit, transparent, open development project building the same infrastructure the right way.
- note_es: Hay un caso que merece atención especial. W Social se lanzó en Davos, con inversores suecos y ex ministros detrás, presentándose como la alternativa europea fiable a Twitter. Construida sobre el AT Protocol. Y después borro su repositorio público de código. Sin explicación. Y las instituciones europeas ya habian movido allí sus cuentas oficiales. Datos oficiales de la UE en servidores de una empresa privada con ánimo de lucro. Comparadlo con EuroSky: sin ánimo de lucro, transparente, desarrollo abierto, construyendo la misma infraestructura bien.

### C4.1 — The rules are changing
- type: points
- chapter: 4
- time: 45s
- en_title: The rules are changing
- es_title: Las normas están cambiando
- en_item: Australia banned social media for under 16s in December 2025
- es_item: Australia prohibió las redes sociales a menores de 16 en diciembre de 2025
- en_item: France banned under 15s in July 2026
- es_item: Francia prohibió el acceso a menores de 15 en julio de 2026
- en_item: The EU KIDS Act proposes tiers: under 13 parent controlled, 13 to 15 restricted, full access after 15
- es_item: La EU KIDS Act propone niveles: menores de 13 controlados por los padres, de 13 a 15 restringidos, acceso completo a partir de 15
- note_en: There is one more thing happening right now that makes this relevant beyond the tech. Countries are starting to restrict social media for young people. Australia banned under 16s in December 2025. France banned under 15s in July 2026. The European Commission is proposing the EU KIDS Act, with a tiered system.
- note_es: Hay algo más que está pasando ahora mismo y que hace esto relevante más alla de la tecnologia. Los países empiezan a restringir las redes sociales para los jóvenes. Australia prohibió el acceso a menores de 16 en diciembre de 2025. Francia a menores de 15 en julio de 2026. La Comisión Europea propone la EU KIDS Act, con un sistema por niveles.

### C4.2 — Right worry, wrong fix
- type: points
- chapter: 4
- time: 55s
- en_title: The right worry, the wrong fix
- es_title: La preocupación correcta, la solución no
- en_item: Traditional social media is built to keep you scrolling, and parents, schools and governments are right to worry
- es_item: Las redes sociales tradicionales están hechas para que sigas haciendo scroll, y los padres, los colegios y los gobiernos tienen razón en preocuparse
- en_item: But the fix is more surveillance: verify everyone's age, collect more data
- es_item: Pero la solución es más vigilancia: verificar la edad de todos, recoger más datos
- en_item: The platforms themselves do not change
- es_item: Las plataformas en sí no cambian
- note_en: The intention is good. Traditional social media is designed to keep people scrolling, and the algorithms optimise for engagement, not wellbeing. Parents, schools and governments are right to worry. But the fix being proposed is the same old approach: force the platforms to verify everyone's age, collect more data, build more surveillance. The platforms themselves do not change, they just add an age gate.
- note_es: La intención es buena. Las redes sociales tradicionales están diseñadas para mantener a la gente haciendo scroll, y los algoritmos optimizan el engagement, no el bienestar. Los padres, los colegios y los gobiernos tienen razón en preocuparse. Pero la solución que se propone es la de siempre: obligar a las plataformas a verificar la edad de todos, recoger más datos, construir más vigilancia. Las plataformas en sí no cambian, solo añaden una barrera de edad.

### C4.3 — A different path
- type: points
- chapter: 4
- time: 55s
- en_title: A different path
- es_title: Un camino diferente
- en_item: No algorithm pushing content at you. You choose your feeds.
- es_item: Ningún algoritmo te mete contenido. Tú eliges tus feeds.
- en_item: A school on its own PDS: no ads, chronological, rules set by the community, and students take their data when they graduate
- es_item: Un colegio con su propio PDS: sin anuncios, cronológico, normas de la comunidad, y los alumnos se llevan sus datos cuando terminan
- en_item: Do not like the app? Move. Your posts and your followers come with you.
- es_item: ¿No te gusta la app? Múdate. Tus posts y tus seguidores vienen contigo.
- note_en: The Atmosphere offers a different path. Bluesky has no algorithm pushing content at you. You choose your feeds. For parents and schools this matters. Imagine a school social network where students own their data, the feed is chronological, there are no ads, and the community sets the rules. The school runs its own PDS, and when students graduate, they take their data with them. And if one app introduces an algorithm you do not like, you move to another one, and your people come with you. No other platform offers that.
- note_es: El Atmosphere ofrece un camino diferente. Bluesky no te mete contenido con un algoritmo. Tú eliges tus feeds. Para padres y colegios esto importa. Imagina una red social de colegio donde los alumnos son dueños de sus datos, el feed es cronológico, no hay anuncios, y las normas las pone la comunidad. El colegio lleva su propio PDS, y cuando terminan el colegio, se llevan sus datos. Y si una app introduce un algoritmo que no te gusta, te mudas a otra, y tu gente viene contigo. Ninguna otra plataforma ofrece eso.

### C5.1 — Private data is coming
- type: quote
- chapter: 5
- time: 45s
- en_title: Private data is coming
- es_title: Los datos privados llegan
- en_quote: Once we enable private data, it is like 10 or 100 times the number of use cases we can serve.
- es_quote: Once we enable private data, it is like 10 or 100 times the number of use cases we can serve.
- en_attrib: Toni Schneider, CEO of Bluesky
- es_attrib: Toni Schneider, CEO de Bluesky
- en_item: Spaces is in alpha: private posts, group conversations, membership communities
- es_item: Spaces está en alpha: posts privados, conversaciones de grupo, comunidades de miembros
- en_item: Built into the protocol, not owned by one company
- es_item: Integrado en el protocolo, no propiedad de una empresa
- en_item: Closer to Reddit than to a folder: smaller communities, still connected to the network
- es_item: Más cerca de Reddit que de una carpeta: comunidades más pequeñas, conectadas a la red
- en_item: AT Protocol Spaces | https://atproto.com/blog/atproto-spaces-alpha
- es_item: AT Protocol Spaces | https://atproto.com/blog/atproto-spaces-alpha
- note_en: The biggest thing the protocol team is working on right now is private data, called AT Protocol Spaces. Everything today is public by design, which is great for developers and limiting for users. When you build a private space on the protocol, you own it completely, it is not owned by Bluesky or any company. And because it is on a shared protocol, these communities can plug together. Schneider compared it to Reddit: smaller, closed communities that are still connected to the broader network. But unlike Reddit, your community is truly yours.
- note_es: Lo más grande en lo que trabaja ahora el equipo del protocolo son los datos privados, lo que llaman AT Protocol Spaces. Hoy todo es público por diseño, lo cual es bueno para los developers y limitante para los usuarios. Cuando construyes un espacio privado sobre el protocolo, es tuyo por completo, no es de Bluesky ni de ninguna empresa. Y como está sobre un protocolo compartido, esas comunidades pueden conectarse entre si. Schneider lo comparo con Reddit: comunidades más pequeñas y cerradas, pero conectadas a la red. A diferencia de Reddit, tu comunidad es de verdad tuya.

### C5.2 — Bluesky is two things
- type: points
- chapter: 5
- time: 40s
- en_title: Bluesky is two things
- es_title: Bluesky son dos cosas
- en_item: Bluesky is the app. The frontend most people use.
- es_item: Bluesky es la app. El frontend que usa casi todo el mundo.
- en_item: The Atmosphere is the network: every app, every service, every PDS
- es_item: El Atmosphere es la red: todas las apps, todos los servicios, todos los PDS
- en_item: Your account is on the network, not in the app
- es_item: Tu cuenta está en la red, no en la app
- en_item: Bluesky is moving to that naming. The network is bigger than the app.
- es_item: Bluesky se está moviendo a ese nombre. La red es más grande que la app.
- link_en: Toni Schneider on the naming | https://atproto.com/off-protocol/2026-08-26-toni-schneider-ama
- link_es: Toni Schneider sobre el nombre | https://atproto.com/off-protocol/2026-08-26-toni-schneider-ama
- note_en: Schneider made a point worth repeating. Bluesky is two things, and the words matter. Bluesky is the app, the frontend most people use. The Atmosphere is the network: every app, every service, every PDS. Bluesky itself is moving to that naming, because the network is bigger than one app. An Atmosphere account is not the same as a Bluesky account. The account is on the network. The apps are just windows into your data.
- note_es: Schneider hizo un apunte que merece repetirse. Bluesky son dos cosas, y las palabras importan. Bluesky es la app, el frontend que usa la mayoría. El Atmosphere es la red: todas las apps, todos los servicios, todos los PDS. El propio Bluesky se está moviendo a ese nombre, porque la red es más grande que una app. Una cuenta Atmosphere no es lo mismo que una cuenta de Bluesky. La cuenta está en la red. Las apps son solo ventanas a tus datos.

### C5.3 — The numbers are moving
- type: stats
- chapter: 5
- time: 40s
- en_title: The numbers are moving
- es_title: Los números se mueven
- en_item: 1,000+ | apps in weekly use, doubled since January
- es_item: 1.000+ | apps en uso semanal, el doble que en enero
- en_item: 3x | SDK downloads, heading to a million a month
- es_item: 3x | descargas de SDK, camino del millón al mes
- en_item: 1B | people, the ten year goal
- es_item: 1.000M | personas, el objetivo a diez años
- en_item: Network stats, updated daily | https://blue.mackuba.eu/stats/
- es_item: Network stats, actualizadas cada día | https://blue.mackuba.eu/stats/
- note_en: The numbers already show this is working. Over a thousand apps in weekly use now, doubled since the start of 2026. SDK downloads for developer tools have tripled, heading to a million a month. And Schneider's ten year goal is a billion people on the protocol. You can watch these numbers yourself on the public stats pages, they update every day.
- note_es: Los números ya muestran que esto funciona. Más de mil apps en uso semanal, el doble que a principios de 2026. Las descargas de SDK para herramientas de desarrollo se han triplicado, camino del millón al mes. Y el objetivo a diez años de Schneider es mil millones de personas en el protocolo. Podéis seguir estos números vosotros mismos en las páginas públicas de stats, se actualizan cada día.

### C5.4 — How it gets paid for
- type: points
- chapter: 5
- time: 40s
- en_title: How it gets paid for
- es_title: Cómo se paga esto
- en_item: Not ads
- es_item: No con anuncios
- en_item: No monetisation layer yet, but the first tools are appearing, like atmopay
- es_item: Todavía no hay forma de ganar dinero, pero aparecen las primeras herramientas, como atmopay
- en_item: Affiliate model: the network sends you traffic, and takes a small share when it converts
- es_item: Modelo de afiliación: la red te manda tráfico, y se lleva una parte pequeña cuando convierte
- en_item: The WordPress comparison: a platform that grew an ecosystem of businesses around it
- es_item: La comparación con WordPress: una plataforma que hizo crecer un ecosistema de negocios a su alrededor
- en_item: For developers: no platform tax. Also no playbook yet.
- es_item: Para developers: sin comisión de plataforma. Y sin manual todavía.
- link_en: atmopay, one of the first payment tools | https://atmopay.birdsongapps.com/
- link_es: atmopay, una de las primeras herramientas de pago | https://atmopay.birdsongapps.com/
- note_en: One of the biggest open questions is how the ecosystem makes money. Schneider addressed it directly: no ads. Instead an affiliate style model, where the network helps creators and publishers make money and takes a small piece when that traffic converts into subscribers or sales. The same model that made WordPress into an ecosystem with thousands of businesses around it. For developers that means no platform tax, nobody takes thirty percent of your revenue, but also that there is no playbook yet.
- note_es: Una de las grandes preguntas abiertas es cómo gana dinero el ecosistema. Schneider lo dijo claro: sin anuncios. En su lugar un modelo de afiliación, donde la red ayuda a creadores y editores a ganar dinero y se lleva una parte pequeña cuando ese tráfico convierte en suscriptores o ventas. El mismo modelo que convirtió WordPress en un ecosistema con miles de negocios alrededor. Para los developers significa que no hay comisión de plataforma, nadie se lleva el treinta por ciento de tus ingresos, pero también que todavía no hay manual.

### C5.5 — Europe is where the energy is
- type: points
- chapter: 5
- time: 35s
- en_title: Europe is where the energy is
- es_title: Europa es donde está la energía
- en_item: AtmosphereConf #3: April 29 to May 2, 2027, in Amsterdam
- es_item: AtmosphereConf nº 3: del 29 de abril al 2 de mayo de 2027, en Ámsterdam
- en_item: atproto.eu estimates around 2.8 million European-language accounts
- es_item: atproto.eu estima unos 2,8 millones de cuentas en lenguas europeas
- en_item: Connections in France, Belgium, the Netherlands, Italy, Germany
- es_item: Conexiones en Francia, Bélgica, Países Bajos, Italia, Alemania
- en_item: atproto.eu | https://atproto.eu
- es_item: atproto.eu | https://atproto.eu
- note_en: Europe is where the energy is. AtmosphereConf, the unofficial gathering of the community, will hold its third edition in Amsterdam, from the 29th of April to the 2nd of May 2027. The first two were smaller community events. And through atproto.eu, the European hub, we have connections in France, Belgium, the Netherlands, Italy and Germany. They estimate around 2.8 million European language accounts.
- note_es: Europa es donde está la energía. AtmosphereConf, el encuentro no oficial de la comunidad, celebrará su tercera edición en Ámsterdam, del 29 de abril al 2 de mayo de 2027. Las dos primeras fueron eventos de comunidad más pequeños. Y a través de atproto.eu, el hub europeo, tenemos conexiones en Francia, Bélgica, Países Bajos, Italia y Alemania. Estiman unos 2,8 millones de cuentas en lenguas europeas.

### C5.6 — Barcelona
- type: points
- chapter: 5
- time: 35s
- en_title: Barcelona
- es_title: Barcelona
- en_item: atproto.barcelona: the meetups start now
- es_item: atproto.barcelona: los meetups empiezan ahora
- en_item: Mozilla Festival, 28 to 30 October, sessions on decentralized social media
- es_item: Mozilla Festival, del 28 al 30 de octubre, sesiones sobre redes sociales descentralizadas
- en_item: "One session: Hints of a new open platform"
- es_item: "Una sesión: Hints of a new open platform"
- en_item: atproto.barcelona | https://atproto.barcelona
- es_item: atproto.barcelona | https://atproto.barcelona
- note_en: In Barcelona we are building our own community. atproto.barcelona is starting its meetups now, and there will be more. And the Mozilla Festival lands in Barcelona at the end of October, with sessions on decentralized social media and open platforms. Exactly the conversation we want the people in this room to be part of.
- note_es: En Barcelona estamos construyendo nuestra propia comunidad. atproto.barcelona empieza ahora con los meetups, y habrá más. Y el Mozilla Festival llega a Barcelona a finales de octubre, con sesiones sobre redes sociales descentralizadas y plataformas abiertas. Exactamente la conversación en la que queremos que esté en esta sala.

### C5.7 — Why it has to start with communities
- type: points
- chapter: 5
- time: 45s
- en_title: Why it has to start with communities
- es_title: Por qué tiene que empezar por las comunidades
- en_item: People do not move because everyone is there, and it is easy, and it is free
- es_item: La gente no se mueve porque todo el mundo está allí, y es fácil, y es gratis
- en_item: Not Web 3.0. More like Web 2.5: you already have a website, now attach a social identity you own.
- es_item: No es Web 3.0. Es más bien Web 2.5: ya tienes una web, ahora ponle una identidad social que es tuya.
- en_item: Developers, IT, designers: you can push this in your company, your school, your city
- es_item: Developers, IT, diseñadores: podéis llevar esto a vuestra empresa, vuestro colegio, vuestra ciudad
- note_en: The real opportunity is not just technical, it is social. People are tired of traditional social media, but they do not move, because everyone is there, and it is easy, and it is free. So we have to make an effort. The best way is to start with communities. This is not Web 3.0 or blockchain hype. It is more like Web 2.5, an extension of what the web already is. You have a website, you have a blog, now you can attach a social identity that is yours, portable and open. It is the web finally doing what it was supposed to do.
- note_es: La oportunidad real no es solo técnica, es social. La gente está cansada de las redes sociales tradicionales, pero no se mueve, porque todo el mundo está allí, y es fácil, y es gratis. Así que hay que hacer un esfuerzo. La mejor forma es empezar por comunidades. Esto no es Web 3.0 ni la moda del blockchain. Es más bien Web 2.5, una extension de lo que la web ya es. Tienes una web, tienes un blog, ahora puedes engancharle una identidad social que es tuya, portable y abierta. Es la web haciendo por fin lo que debia hacer.

### C5.8 — Where to put your account
- type: points
- chapter: 5
- time: 50s
- en_title: Where to put your account
- es_title: Dónde poner tu cuenta
- en_item: Bluesky: simplest, sign up and go
- es_item: Bluesky: lo más simple, te registras y listo
- en_item: EuroSky: European non-profit, GDPR, transparent
- es_item: EuroSky: europea, sin ánimo de lucro, GDPR, transparente
- en_item: BlackSky: community run, built for Black users and their communities
- es_item: BlackSky: gestionada por la comunidad, pensada para usuarios negros y sus comunidades
- en_item: Your own server: full sovereignty if you are technical
- es_item: Tu propio servidor: control total si eres técnico
- en_item: eurosky.social | https://eurosky.social
- es_item: eurosky.social | https://eurosky.social
- en_item: blacksky.app | https://blacksky.app
- es_item: blacksky.app | https://blacksky.app
- note_en: You can choose where to host your account. Bluesky is the simplest, sign up and you are on their PDS. EuroSky is the European non-profit option, GDPR compliant, transparent. BlackSky is a community focused PDS, showing that you can build for a specific audience on the same open network. And if you are technical, you can host your own PDS at home, under your own control. The point is that you have a choice. That is what makes this different from every social platform that came before.
- note_es: Puedes elegir dónde alojar tu cuenta. Bluesky es lo más simple, te registras y estas en su PDS. EuroSky es la opción europea sin ánimo de lucro, conforme al GDPR, transparente. BlackSky es un PDS centrado en comunidad, y demuestra que se puede construir para un público concreto sobre la misma red abierta. Y si eres técnico, puedes alojar tu propio PDS en casa, bajo tu control. La cuestión es que tienes elección. Eso es lo que lo hace distinto de todas las plataformas sociales anteriores.

### Z1 — It starts with us
- type: cta
- chapter: close
- time: 45s
- en_title: It starts with us
- es_title: Empieza con nosotros
- en_item: Talk to your local government: a town hall on its own PDS
- es_item: Habla con tu ayuntamiento: un ayuntamiento con su propio PDS
- en_item: Talk to your school: students own their data and take it with them
- es_item: Habla con tu colegio: los alumnos son dueños de sus datos y se los llevan
- en_item: Talk to your company: a professional network that is not LinkedIn
- es_item: Habla con tu empresa: una red profesional que no es LinkedIn
- en_item: The Atmosphere belongs to all of us. I am building it here in Barcelona, and I would like you in.
- es_item: El Atmosphere es de todos. Yo lo estoy construyendo aquí en Barcelona, y me gustaría que estuvieras dentro.
- en_item: @didiermortier.eu
- es_item: @didiermortier.eu
- note_en: This presentation is just the beginning. The protocol works, the apps are growing, the community is forming. What we need now is people who take this into their own circles. Talk to your local government. Talk to your school. Talk to your company. It starts with communities, and it starts with people like you. Come and find me afterwards, my handle is on the screen.
- note_es: Esta charla es solo el principio. El protocolo funciona, las apps crecen, la comunidad se está formando. Lo que hace falta ahora es gente que se lo lleve a sus circulos. Habla con tu ayuntamiento. Habla con tu colegio. Habla con tu empresa. Empieza por las comunidades, y empieza por gente como vosotros. Venid a buscarme al terminar, mi handle está en pantalla.

### Z2 — Sifa Party
- type: party
- chapter: close
- time: 90s
- en_title: Sifa Party
- es_title: Sifa Party
- en_sub: Tonight's homework: get your professional profile off LinkedIn
- es_sub: Los deberes de hoy: saca tu perfil profesional de LinkedIn
- en_item: Download your LinkedIn data export and drop the ZIP at sifa.id/import
- es_item: Descarga tus datos de LinkedIn y suelta el ZIP en sifa.id/import
- en_item: It is unpacked in your browser. Nothing goes to their servers.
- es_item: Se descomprime en tu navegador. Nada va a sus servidores.
- en_item: Sign in with your Atmosphere account, or create one on EuroSky in a minute
- es_item: Entra con tu cuenta Atmosphere, o crea una en EuroSky en un minuto
- en_item: Your profile is written to your own PDS, and it is public, that is the deal
- es_item: Tu perfil se escribe en tu propio PDS, y es público, ese es el trato
- en_item: Then LinkedIn becomes optional
- es_item: Y después LinkedIn es opcional
- img: assets/sifa-import.png
- qr: https://sifa.id/import
- link_en: sifa.id/import | https://sifa.id/import
- link_es: sifa.id/import | https://sifa.id/import
- note_en: Now the practical part. This is a small party I would like to start tonight. Sifa is the professional profile app I showed you, and this is how you get off LinkedIn. Go to sifa.id/import, ask LinkedIn for your data export, and drop the ZIP file in that page. Everything is unpacked in your browser, nothing is uploaded to a server, and the result is written straight to your own PDS. If you do not have an Atmosphere account yet, the login screen lets you create one on EuroSky in about a minute. One warning: your profile will be public, that is how the network works, and Sifa tells you so before you import. And once your professional history is here, LinkedIn becomes optional. The QR code is on the screen. Scan it now, do it while I finish the last slides, and show me afterwards.
- note_es: Ahora la parte práctica. Esta es una pequeña fiesta que quiero empezar esta noche. Sifa es la app de perfil profesional que os he enseñado, y esto es cómo salir de LinkedIn. Entra en sifa.id/import, pide a LinkedIn tu export de datos, y suelta el archivo ZIP en esa página. Todo se descomprime en tu navegador, no se sube nada a un servidor, y el resultado se escribe directo en tu propio PDS. Si todavía no tienes cuenta Atmosphere, la pantalla de login te deja crear una en EuroSky en un minuto. Un aviso: tu perfil será público, así funciona la red, y Sifa te lo dice antes de importar. Y cuando tu historial profesional está aquí, LinkedIn es opcional. El QR está en pantalla. Escanéalo ahora, hazlo mientras termino las últimas diapositivas, y me lo enseñas después.

### Z3 — Everything I mentioned
- type: links
- chapter: close
- time: 20s
- en_title: Everything I mentioned
- es_title: Todo lo que he mencionado
- en_item: The AT Store | https://atstore.fyi
- es_item: La AT Store | https://atstore.fyi
- en_item: EuroSky | https://eurosky.social
- es_item: EuroSky | https://eurosky.social
- en_item: mu.social | https://mu.social
- es_item: mu.social | https://mu.social
- en_item: Sifa ID | https://sifa.id
- es_item: Sifa ID | https://sifa.id
- en_item: sifa.id/import | https://sifa.id/import
- es_item: sifa.id/import | https://sifa.id/import
- en_item: PopFeed | https://popfeed.social
- es_item: PopFeed | https://popfeed.social
- en_item: Tangled | https://tangled.org
- es_item: Tangled | https://tangled.org
- en_item: Marque | https://marque.at
- es_item: Marque | https://marque.at
- en_item: Grain | https://grain.social
- es_item: Grain | https://grain.social
- en_item: atmo.rsvp | https://atmo.rsvp
- es_item: atmo.rsvp | https://atmo.rsvp
- en_item: Currents | https://currents.is
- es_item: Currents | https://currents.is
- en_item: Flashes | https://www.flashes.blue/
- es_item: Flashes | https://www.flashes.blue/
- en_item: npmx | https://npmx.dev
- es_item: npmx | https://npmx.dev
- en_item: pckt.blog | https://pckt.blog
- es_item: pckt.blog | https://pckt.blog
- en_item: BlackSky | https://blacksky.app
- es_item: BlackSky | https://blacksky.app
- en_item: PDS MOOver | https://pdsmoover.com
- es_item: PDS MOOver | https://pdsmoover.com
- en_item: AT Protocol | https://atproto.com
- es_item: AT Protocol | https://atproto.com
- en_item: Spaces alpha | https://atproto.com/blog/atproto-spaces-alpha
- es_item: Spaces alpha | https://atproto.com/blog/atproto-spaces-alpha
- en_item: Network stats | https://blue.mackuba.eu/stats/
- es_item: Network stats | https://blue.mackuba.eu/stats/
- en_item: AtmosphereConf | https://atmosphereconf.org
- es_item: AtmosphereConf | https://atmosphereconf.org
- en_item: atproto.eu | https://atproto.eu
- es_item: atproto.eu | https://atproto.eu
- en_item: atproto.barcelona | https://atproto.barcelona
- es_item: atproto.barcelona | https://atproto.barcelona
- en_item: Mozilla Festival | https://www.mozillafoundation.org/festival/
- es_item: Mozilla Festival | https://www.mozillafoundation.org/festival/
- note_en: Everything I mentioned, in one place. Take a photo of this slide.
- note_es: Todo lo que he mencionado, en un solo sitio. Haced una foto de esta diapositiva.