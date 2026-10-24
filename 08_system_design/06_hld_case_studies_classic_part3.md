---
domain: sd
topic: hld_case_studies_classic
title: HLD case studies (classic)
tags: [hld, case-study, design-x]
count: 120
part: 3/3
---
# HLD case studies (classic) (part 3)

## Proximity search and maps
- [SD06-207] Why do we need quadtrees for location data?
- [SD06-208] How does geohashing work, and what are its limitations?
- [SD06-209] Explain geohashing and quadtrees and their trade-offs for geospatial indexing, especially with uneven density.
- [SD06-210] Design a proximity service such as Yelp that returns nearby businesses for a given location and radius.
- [SD06-211] How do you find nearby businesses with a quadtree?
- [SD06-212] Design a who's-near-me service that finds all users within k kilometres of a location for 1 million users.
- [SD06-213] Design a system for fast lookup of cars on the market according to the user's geo-position.
- [SD06-214] For a proximity service, how do you handle dense urban areas with many points of interest versus sparse regions?
- [SD06-215] How do you update the location index in a proximity or ride-sharing service when objects move frequently?
- [SD06-216] Design a simplified Google Maps with location, map rendering and navigation services.
- [SD06-217] How are map tiles produced, stored and served efficiently at multiple zoom levels?
- [SD06-218] How would a navigation service compute top-K routes and estimate travel time with live traffic, and how would it send route alerts?
- [SD06-219] For a maps service, how do you refresh map tiles and traffic data without a full rebuild?

## Ride-hailing
- [SD06-220] Design a ride-sharing service such as Uber that matches riders to nearby drivers.
- [SD06-221] How would you track driver locations in real time and find nearby drivers efficiently? Compare geohash and quadtree approaches.
- [SD06-222] Estimate location update traffic for 5 million drivers sending a location every 4 seconds, and decide how to store it.
- [SD06-223] How does ride matching work, and how do you avoid assigning one driver to two riders?
- [SD06-224] How would a ride-sharing backend split into microservices for dispatch, payment, trip, user profile and notifications?
- [SD06-225] What happens when the dispatch service times out or a driver rejects a request in a ride-hailing system?
- [SD06-226] Design a surge pricing system. How do you compute demand and supply per area in near real time?
- [SD06-227] How would you design a payment system for a ride-hailing service that handles tens of millions of transactions per day?
- [SD06-228] If the location service is partially down in a ride-sharing service, how does matching degrade?
- [SD06-229] At peak demand a city has 100,000 concurrent ride requests. How do you scale matching and avoid hot geographic cells?
- [SD06-230] How do you keep trip state consistent across the rider app, driver app and backend when connectivity is flaky?
- [SD06-231] Design a food delivery service like DoorDash or Zomato that matches orders to restaurants and couriers and tracks deliveries.

## Web crawler and search
- [SD06-232] Design a web crawler that discovers and fetches billions of pages.
- [SD06-233] How do you avoid crawling duplicate URLs at Google scale, and how do you detect pages with duplicate content?
- [SD06-234] How would you build a crawler's URL frontier that respects per-host politeness while prioritizing important pages?
- [SD06-235] How does a crawler decide when to recrawl a page, and how does it handle crawler traps?
- [SD06-236] How do you handle robots.txt and per-domain rate limits in a crawler?
- [SD06-237] How does a crawler recover from a crash without refetching everything, and how do you keep the frontier consistent across workers?
- [SD06-238] How do you scale a crawler's duplicate detection when the number of seen URLs reaches tens of billions?
- [SD06-239] How do search engines work, from crawling to serving a query?
- [SD06-240] Design a basic search engine from crawling to indexing to ranked retrieval, as in Google Search.
- [SD06-241] How would you build the index and the query service on top of crawled pages to return titles and snippets?
- [SD06-242] Design a distributed search system for 1 billion documents at 1 million QPS.
- [SD06-243] How do you shard and replicate an inverted index, and how do you merge results across shards?
- [SD06-244] Design a text search engine from scratch without Elasticsearch, with TF-IDF ranking, boolean queries, typo tolerance and phonetic matching.
- [SD06-245] Build a search engine over 100 MB of text data. How does the design change if the data grows to 100 TB?
- [SD06-246] Design a podcast search engine with transcript indexing.
- [SD06-247] Design a plagiarism-detection style service that finds near-duplicate documents at scale.

## Typeahead and autocomplete
- [SD06-248] Design a typeahead or autocomplete service that returns suggestions as the user types.
- [SD06-249] How would you build a typeahead index with tries or inverted indexes, rank suggestions, and refresh them with newly trending queries?
- [SD06-250] How can a layered architecture of browser cache, web tier and result aggregator achieve very low-latency typeahead?
- [SD06-251] How would you personalize typeahead suggestions by social-network distance while keeping new accounts immediately searchable?
- [SD06-252] For a typeahead service, how fresh must suggestions be, and what is the cost of serving slightly stale results?
- [SD06-253] How would you scale a typeahead service to hundreds of thousands of queries per second without a cache stampede on rare prefixes?

## Booking, e-commerce and flash sales
- [SD06-254] Design a hotel booking system such as Airbnb with search by location and dates and reservations.
- [SD06-255] In a hotel reservation system, how do you find available rooms for a date range?
- [SD06-256] How do you prevent double booking of the same room for the same dates when many users book concurrently?
- [SD06-257] Design a flight booking system.
- [SD06-258] Design an airline web check-in system where passengers log in with a PNR, pick seats and get a boarding pass, and 100 passengers may pick seats simultaneously.
- [SD06-259] Design a ticket booking system such as BookMyShow or Ticketmaster, including flash-sale traffic for popular events.
- [SD06-260] How do you handle holds on inventory that expire if the user does not complete payment?
- [SD06-261] In a flash-sale ticketing system, how do you manage a queue of millions of waiting users while preventing overselling and bot abuse?
- [SD06-262] Design a flash sale selling 1,000 units in seconds, where winners get 5 minutes to pay and unpaid units are released to others.
- [SD06-263] How would you implement a cart reservation with a payment timeout, and what happens when a payment succeeds after the hold expired?
- [SD06-264] How would you use a virtual waiting room and an atomic counter such as Redis DECR to admit exactly N buyers?
- [SD06-265] Design a flash-sale (seckill) system that handles a sudden burst of traffic without overselling.
- [SD06-266] Design an e-commerce platform like Amazon covering catalog, inventory, cart, orders, payment and delivery.
- [SD06-267] Design an inventory management system.
- [SD06-268] Design an event-driven order processing pipeline in which inventory, payment and shipping are separate services.
- [SD06-269] Design Amazon's sales ranking by category, showing the most popular products of the past week.
- [SD06-270] How would you compute category rankings with a map-reduce job and serve them from a read store?
- [SD06-271] Design a live auction platform for a high-profile sports league.

## Payments and wallets
- [SD06-272] Design a payment system for an e-commerce site that handles payment events, orders, wallet and ledger.
- [SD06-273] Design a payment gateway like Razorpay or Stripe.
- [SD06-274] How do you ensure a customer is never charged twice in a payment system when requests time out or are retried?
- [SD06-275] How do you deduplicate non-idempotent payment operations under at-least-once delivery?
- [SD06-276] The payment provider times out after the charge actually succeeded. How does your system recover?
- [SD06-277] How would you design a payment system to survive crashes between updating the payment record, the wallet and the ledger?
- [SD06-278] How do you synchronize the transaction table with external banks and vendors in a payment system?
- [SD06-279] How would a payment system scale on peak days like Black Friday without sacrificing correctness?
- [SD06-280] How do you design payment systems for multi-currency settlement and reporting?
- [SD06-281] Design a PayPal or Cash App style money transfer system with deposits, payouts and transfers between accounts.
- [SD06-282] How do you keep a money transfer system strongly consistent across a ledger, wallet and external banks while tolerating failures?
- [SD06-283] Design a digital wallet, and compare a wallet at a traditional bank with one on a blockchain.
- [SD06-284] Describe the flow of a credit card swipe at a merchant, from card network to issuing bank, and how the card network earns revenue.
- [SD06-285] How do Apple Pay and Google Pay protect card details, and how do the different QR code payment approaches work?
- [SD06-286] How does an ACH payment work?
- [SD06-287] Design the Unified Payments Interface (UPI), and explain what makes a real-time payments scheme interoperable.
- [SD06-288] How does an international bank-to-bank messaging system such as SWIFT route payments and settle them?

## Stock exchange and order matching
- [SD06-289] Design a stock exchange order matching system supporting market, limit and stop-loss orders.
- [SD06-290] How do you implement price-time FIFO matching in an order matching system?
- [SD06-291] How do you support different kinds of orders in an order matching system?
- [SD06-292] How would you achieve low latency and strict ordering in an order matching engine while staying highly available?
- [SD06-293] How do you transmit order book data to clients in real time, and how do you publish market data to millions of clients?
- [SD06-294] How do you recover the order book state after the matching engine crashes?

## Analytics, metrics and leaderboards
- [SD06-295] Design a real-time analytics pipeline that ingests clickstream events and shows near-real-time dashboards.
- [SD06-296] Design a metrics and monitoring system that collects counters, timers and conversion rates and supports dashboards and alerts.
- [SD06-297] How would you store and downsample metrics in a time-series database to keep long-term data cheap?
- [SD06-298] How do you handle high-cardinality labels and bursty ingestion in a metrics system without overwhelming storage?
- [SD06-299] What happens to alerting if the metrics ingestion pipeline is delayed, and how do you detect that your own monitoring is failing?
- [SD06-300] Design a log aggregation and search system for thousands of servers, supporting queries over the last minute, hour, day and week.
- [SD06-301] Design a web analytics service that counts page views per URL at very high write volume.
- [SD06-302] Design a system that counts unique visitors or ad impressions over an arbitrary time range given at query time, with approximate answers and efficient storage.
- [SD06-303] Design a text-based live cricket commentary service written ball by ball and read by 5 million concurrent readers.
- [SD06-304] How would you push new commentary to millions of readers: polling, long polling, SSE or WebSockets, and with what caching strategy?
- [SD06-305] Design a stream processing system that computes rolling aggregates with exactly-once semantics.
- [SD06-306] Design a leaderboard for millions of players with real-time rank lookups.
- [SD06-307] For a leaderboard with millions of players, how do you handle ties, shard by score range and query a user's rank?
- [SD06-308] Design an ad click aggregator that reports the top K most-clicked ads per minute.

## Other classic prompts
- [SD06-309] Design an ads system for a website, including recommendation-driven delivery with budget pacing and bidding.
- [SD06-310] Design an A/B testing and experiment platform covering setup, variant assignment, instrumentation and analysis.
- [SD06-311] For an experiment platform, how do you keep variant assignment consistent for a user across sessions and devices?
- [SD06-312] Design an online code judge that safely runs untrusted submissions.
- [SD06-313] Design a scalable weather service that pulls data from a third-party API.
- [SD06-314] Design a personal finance aggregator like Mint that connects to users' financial accounts, extracts transactions and recommends budgets.
- [SD06-315] How does a personal finance aggregator categorize transactions and pull from thousands of banks reliably?
- [SD06-316] How do you design budget notifications and daily transaction extraction for millions of accounts, prioritizing active users?
- [SD06-317] How do you handle a bank API that is slow, rate limited or returns inconsistent data in a transaction aggregator?
- [SD06-318] Design a permission and access control service that answers authorization checks for many products.
- [SD06-319] Design a single sign-on system for an enterprise with multiple applications.
- [SD06-320] Design a ChatGPT-like conversational service. What are the main components for serving requests at scale?
- [SD06-321] Design a feature flag service used by thousands of services. How do you deliver flag changes quickly and safely?
- [SD06-322] Design a distributed tracing system for a microservice platform.
- [SD06-323] How would you create an asynchronous multiplayer game?
- [SD06-324] In a shooter game, characters fire in sequence during a big fight. How does the game server transmit state to the game clients?
- [SD06-325] Design a multi-region deployment of a user-facing service. How do you route traffic, replicate data and handle region failure?
- [SD06-326] For a real-time service such as chat or ride sharing, how would you handle the loss of an entire data center?
