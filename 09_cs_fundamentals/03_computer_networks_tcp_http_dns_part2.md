---
domain: cs
topic: computer_networks_tcp_http_dns
title: Computer networks: TCP/IP, HTTP, DNS
tags: [networks, tcp, http, dns, tls]
count: 115
part: 2/2
---
# Computer networks: TCP/IP, HTTP, DNS (part 2)

## HTTP methods, status codes and REST
- [CS03-127] What are the components of a URL?
- [CS03-128] What is the difference between a URI, a URL and a URN?
- [CS03-129] What are the main HTTP methods and what is each used for?
- [CS03-130] Explain the difference between stateful and stateless communication.
- [CS03-131] What do the status code classes 1xx, 2xx, 3xx, 4xx and 5xx mean, and what are the most common codes in each?
- [CS03-132] Which success status codes would you return for a create, an update with no body and a delete, and how do 200, 201 and 204 differ?
- [CS03-133] What is the difference between 401 and 403?
- [CS03-134] What is the difference between GET and POST regarding semantics, safety, idempotency, cacheability and parameter placement?
- [CS03-135] Which HTTP methods are safe and which are idempotent, and why does that matter for retries?
- [CS03-136] Why is DELETE idempotent even though it modifies state?
- [CS03-137] Why is PUT idempotent but PATCH might not be?
- [CS03-138] When would you use PUT versus PATCH versus POST for updating a resource?
- [CS03-139] What is the OPTIONS method used for, and how does it relate to CORS preflight?
- [CS03-140] What is the difference between 301, 302, 307 and 308 redirects, and what does the Location header do?
- [CS03-141] When should an API return 400, 404, 409, 422 or 429, and how does 422 differ from 400?
- [CS03-142] When should a service return 500, 502, 503 or 504, and how do they differ?
- [CS03-143] How should a client safely retry a failed POST request, and what role does an idempotency key play?
- [CS03-144] What does the Retry-After header communicate, and when would you pair it with 429 or 503?
- [CS03-145] What is CORS, why does the browser block some cross-origin requests, and when is a preflight request sent?
- [CS03-146] What is a RESTful API and what architectural constraints define REST?
- [CS03-147] How should resource URIs, HTTP verbs and status codes be designed in a REST API, and what makes an API truly RESTful?
- [CS03-148] How would you design pagination, filtering and versioning for a REST API so clients and caches keep working as it evolves?

## HTTP headers, caching and content negotiation
- [CS03-149] Name common HTTP request and response headers and explain what Content-Type, Cache-Control, Authorization and Accept-Encoding do.
- [CS03-150] What is the difference between the Content-Type and Accept headers?
- [CS03-151] What is content negotiation, why is it important, and which headers drive it?
- [CS03-152] How do quality values (q-values) work in content negotiation?
- [CS03-153] What is the purpose of the Vary header?
- [CS03-154] What is the difference between server-driven and agent-driven negotiation?
- [CS03-155] What should a server do when it cannot satisfy a content negotiation request?
- [CS03-156] What problem does the Host header solve, and why was it needed in HTTP/1.1?
- [CS03-157] How does HTTP caching work with Cache-Control, ETag, Last-Modified, Expires and If-None-Match?
- [CS03-158] How does HTTP caching differ between 1.0 (Expires, Pragma) and 1.1 (Cache-Control, ETag)?
- [CS03-159] Explain the difference between no-cache and no-store in Cache-Control.
- [CS03-160] What is the difference between ETag and Last-Modified headers?
- [CS03-161] How do conditional requests work, what does a 304 response mean, and how does it differ from a 200 served from cache?
- [CS03-162] How do ETag headers support both caching and concurrency control?
- [CS03-163] What are chunked transfer encoding, range requests and 100-continue, and what use cases do they serve?
- [CS03-164] How would you set cache headers for a fingerprinted static asset versus an HTML page that changes frequently?
- [CS03-165] What does stale-while-revalidate do, and what trade-off does it make?
- [CS03-166] A CDN serves users the wrong language version of a page. Which header is probably missing or misused, and how would you fix it?

## HTTP/1.1, HTTP/2 and HTTP/3
- [CS03-167] What did HTTP/1.1 add over HTTP/1.0?
- [CS03-168] What are persistent connections in HTTP/1.1, and how do connection reuse and pooling reduce latency?
- [CS03-169] What is HTTP pipelining, and why did it fail to solve head-of-line blocking in HTTP/1.1?
- [CS03-170] What are the problems of HTTP/1.x that HTTP/2 addresses?
- [CS03-171] What makes HTTP/2 faster than HTTP/1.1 for loading modern pages, and what does HTTP/3 change again?
- [CS03-172] Explain HTTP/2 binary framing, multiplexing, HPACK header compression and server push.
- [CS03-173] How does HTTP/3 over QUIC differ from HTTP/2 over TCP, and why does it use UDP?
- [CS03-174] Why do domain sharding and asset bundling help under HTTP/1.1 but become counterproductive under HTTP/2?
- [CS03-175] How does head-of-line blocking differ between HTTP/1.1, HTTP/2 over TCP and HTTP/3 over QUIC?
- [CS03-176] How does a browser learn that a server supports HTTP/3, and what happens if UDP is blocked on the path?

## Proxies, firewalls and load balancers
- [CS03-177] What is the difference between a forward proxy, a reverse proxy and a tunnel proxy?
- [CS03-178] How does an HTTPS request pass through a forward proxy that cannot read the encrypted traffic?
- [CS03-179] What headers (X-Forwarded-For, Via) are added when a request passes through proxies, and why can they be spoofed?
- [CS03-180] How can a backend service obtain the real client IP when requests pass through proxies and load balancers?
- [CS03-181] What is SSL offloading, and what are its security trade-offs?
- [CS03-182] How does a stateful firewall differ from a packet-filtering firewall?
- [CS03-183] Compare L4 and L7 load balancing. What can each see and decide on?
- [CS03-184] What is the PROXY protocol, and why would a TCP load balancer use it?

## Cookies, sessions and state
- [CS03-185] What is a cookie, and what is it used for?
- [CS03-186] What is the difference between a cookie and a session?
- [CS03-187] Why is HTTP stateless, and how do web applications maintain user state across requests?
- [CS03-188] What is the difference between a session cookie and a persistent cookie?
- [CS03-189] What do the Secure, HttpOnly, SameSite and Domain cookie attributes do, and what attacks do they protect against?
- [CS03-190] Can sessions still work without cookies?
- [CS03-191] Compare cookie-based session IDs with token-based approaches such as JWT for tracking authenticated users.
- [CS03-192] How would you share session state across several backend servers behind a load balancer?
- [CS03-193] How does SameSite=Lax differ from Strict, and how does it change behaviour for cross-site navigations and POST requests?
- [CS03-194] What is session fixation, and how do you prevent it?
- [CS03-195] Why is storing a JWT in localStorage riskier than keeping it in an HttpOnly cookie, and what new problem does the cookie option introduce?

## TLS and HTTPS
- [CS03-196] What are the differences between HTTP and HTTPS?
- [CS03-197] What problems does HTTPS solve that plain HTTP does not: confidentiality, integrity and authentication?
- [CS03-198] Walk through the TLS handshake, say what is negotiated, and explain how the shared symmetric key is established.
- [CS03-199] Why does HTTPS combine asymmetric and symmetric encryption instead of using only one?
- [CS03-200] How does a client validate a server certificate chain during the TLS handshake?
- [CS03-201] What is the difference between SSL and TLS, and which versions are considered obsolete?
- [CS03-202] What disadvantages does HTTPS have (latency, CPU cost, certificate management), and how are they reduced?
- [CS03-203] How many round trips do TCP plus TLS add before the first HTTP byte, and how do session resumption and keep-alive reduce that cost?
- [CS03-204] How do TLS session resumption and session tickets affect forward secrecy and handshake cost?
- [CS03-205] What is SNI and why was it added to TLS?
- [CS03-206] Is HTTPS actually safe? What attacks remain possible against a TLS connection?
- [CS03-207] What is mutual TLS, and when would you use it between services?
- [CS03-208] A site suddenly shows certificate errors to some clients only. What are the likely causes (expiry, missing intermediate, clock skew, SNI) and how would you diagnose them?
- [CS03-209] What is forward secrecy, and how does ephemeral Diffie-Hellman provide it?
- [CS03-210] What does HSTS do, and what risk does it remove that a plain redirect to HTTPS leaves open?
- [CS03-211] Compare RSA key exchange with ECDHE key exchange in a TLS handshake. Why does only ECDHE give forward secrecy?
- [CS03-212] In a cipher suite named ECDHE_RSA_AES128_GCM_SHA256, what does each component do, and is the data encrypted with both RSA and ECDHE?
- [CS03-213] What changed in TLS 1.3 compared with TLS 1.2 in terms of handshake round trips and supported key exchange modes?
- [CS03-214] What is certificate pinning, and what operational risks does it create?

## WebSockets and real-time communication
- [CS03-215] What is the WebSocket protocol, and how does it differ from HTTP?
- [CS03-216] What are some common use cases for WebSockets?
- [CS03-217] Can you describe the WebSocket API provided by HTML5?
- [CS03-218] Explain how the WebSocket handshake works on top of HTTP.
- [CS03-219] Compare short polling, long polling, WebSockets and server-sent events for pushing updates to browsers.
- [CS03-220] When would you pick server-sent events over WebSocket for a real-time feature such as streaming responses?
- [CS03-221] Compare polling and webhooks for learning about events in another system.
- [CS03-222] How do WebSockets handle communication through proxies and firewalls?
- [CS03-223] Explain the role of ping/pong frames in WebSockets.
- [CS03-224] How would you detect and handle WebSocket connection loss?
- [CS03-225] How does WebSocket ensure ordered delivery of messages?
- [CS03-226] Explain how a WebSocket connection is closed.
- [CS03-227] What are the limitations of WebSockets?
- [CS03-228] Why do WebSocket connections complicate load balancing and horizontal scaling, and how would you scale many persistent connections?
- [CS03-229] How should a client reconnect after a WebSocket drops, and why do you need backoff with jitter?
- [CS03-230] How would you authenticate a WebSocket connection, given that the browser API cannot set custom headers?
- [CS03-231] Explain the WebSocket frame format.
- [CS03-232] How many concurrent WebSocket connections can a single server handle, and what resources become the bottleneck?

## End-to-end flows and other protocols
- [CS03-233] What happens, step by step, when you type a URL into a browser and press Enter?
- [CS03-234] In the URL-to-page flow, which protocols are involved at each layer, and where can caching shortcut the process?
- [CS03-235] After the browser receives the HTML, how does it load CSS, JS and images and render the page, and which resources block rendering?
- [CS03-236] How is an email delivered from sender to recipient?
- [CS03-237] What is the difference between SMTP, POP3 and IMAP?
- [CS03-238] Active vs passive FTP mode: how do they differ, and why does passive mode work better behind firewalls?
- [CS03-239] What are SSH, FTP, Telnet and RTP used for, and which of them are insecure by design?
- [CS03-240] How does SSH authenticate a user and encrypt a session?
- [CS03-241] What happens at the network level when you click a link on a site you already have an open connection to, compared with a first visit?
