---
domain: cs
topic: security_crypto_web_basics
title: Security, cryptography and web basics
tags: [security, cryptography, owasp, auth]
count: 88
part: 2/2
---
# Security, cryptography and web basics (part 2)

## Same-origin policy, CORS, cookies and headers
- [CS08-092] What is the same-origin policy, what counts as the same origin, and why does the browser enforce it?
- [CS08-093] What is CORS, and how does it relax the same-origin policy? Is it a security feature?
- [CS08-094] How does the CORS preflight work, and when is it triggered?
- [CS08-095] What CORS headers are needed for a cross-origin API request, and which headers must a preflight response echo back?
- [CS08-096] Why should you avoid Access-Control-Allow-Origin: * together with cookies or credentials?
- [CS08-097] What are the security implications of CORS, and how do you configure it safely?
- [CS08-098] How do you configure CORS dynamically per tenant without reflecting arbitrary origins?
- [CS08-099] How do you debug CORS issues in the browser?
- [CS08-100] Does CORS protect your server from a malicious client such as curl or an attacker's backend?
- [CS08-101] What is clickjacking, and what measures can prevent it?
- [CS08-102] How can web cookies compromise security, and how do you safeguard against these risks?
- [CS08-103] What do the Secure, HttpOnly, SameSite and Domain/Path cookie attributes control?
- [CS08-104] Which security headers would you set on a web application and why?
- [CS08-105] What security headers should be included in API responses, and what is the purpose of each?
- [CS08-106] What is Subresource Integrity, and what attack does it prevent?

## Passwords, MFA and sessions
- [CS08-107] How should a web application store user passwords, and why use salted slow hashes instead of encryption?
- [CS08-108] What is salting in password hashing, and why do it?
- [CS08-109] Compare bcrypt, scrypt and Argon2 with a fast hash like SHA-256 for password storage.
- [CS08-110] What is a pepper, and how does it differ from a salt?
- [CS08-111] How should a server validate a submitted password?
- [CS08-112] Why can a forgotten password only be reset and not retrieved in its original form?
- [CS08-113] How would you design a secure password reset flow?
- [CS08-114] Why is a constant-time comparison important when checking secrets, tokens or hashes?
- [CS08-115] How would you secure a login endpoint against brute force, credential stuffing and enumeration of valid accounts?
- [CS08-116] What is MFA, and why can SMS-based MFA be weak?
- [CS08-117] How does Google Authenticator (TOTP) work?
- [CS08-118] What are passkeys (WebAuthn), and why are they considered phishing-resistant?
- [CS08-119] What is the difference between a cookie, a session and a token (JWT)?
- [CS08-120] Describe the concept of session management in web security.
- [CS08-121] How do session fixation and session hijacking happen, and how do you prevent them?
- [CS08-122] What are the trade-offs between server-side sessions and stateless tokens for authentication?
- [CS08-123] Why is Bearer token authentication preferred over Basic authentication?
- [CS08-124] What is the Authorization HTTP header, and how do Basic and Bearer schemes use it?

## JWT and token handling
- [CS08-125] What is a JWT, what are its three parts, and what are its advantages?
- [CS08-126] How does the signature of a JWT prevent tampering, and why should sensitive data not be placed in the payload?
- [CS08-127] How do you validate a JWT on the server?
- [CS08-128] What is the difference between parsing a JWT and validating it?
- [CS08-129] What is the risk of alg=none in JWTs, and how do you prevent it?
- [CS08-130] What is an algorithm-confusion attack (RS256 vs HS256) on JWT verification?
- [CS08-131] Which registered claims (exp, iss, aud, nbf) must a verifier check, and why?
- [CS08-132] When would you use symmetric (HS256) versus asymmetric (RS256) JWT signing, and how does a JWKS endpoint help?
- [CS08-133] What is the difference between access tokens and refresh tokens?
- [CS08-134] How do access and refresh tokens work together, and why is the access token short-lived?
- [CS08-135] What lifetimes and storage approaches suit access tokens versus refresh tokens?
- [CS08-136] How should client applications handle token expiration?
- [CS08-137] How do you rotate and revoke tokens safely?
- [CS08-138] How do you secure tokens in browsers and mobile apps?
- [CS08-139] Is it safer to store a token in localStorage or an HttpOnly cookie? What attacks apply to each?
- [CS08-140] How do you implement logout with stateless JWTs?
- [CS08-141] What are the drawbacks of stateless JWT authentication, such as revocation and token theft, and how can they be mitigated?
- [CS08-142] How would you revoke tokens across microservices?
- [CS08-143] When should you choose opaque tokens over JWTs?
- [CS08-144] How do you implement token introspection for opaque tokens, and how does it compare with local JWT validation?
- [CS08-145] Compare session cookies, JWT and OAuth 2.0. When would you choose each?

## OAuth, OpenID Connect and access control
- [CS08-146] What is OAuth 2.0, and what problem does it solve?
- [CS08-147] Walk through the OAuth 2.0 authorization code flow and the roles of resource owner, client, authorization server and resource server.
- [CS08-148] What can an OAuth access token actually do, and what limits it?
- [CS08-149] What is the difference between OAuth and OpenID Connect, and between an ID token and an access token?
- [CS08-150] What are OAuth 2.0 scopes, and how are they used?
- [CS08-151] How do you design granular OAuth scopes?
- [CS08-152] Which OAuth flows suit native or mobile apps versus single-page apps, and why?
- [CS08-153] How do PKCE and the state parameter improve OAuth security?
- [CS08-154] Why was the implicit flow deprecated?
- [CS08-155] When is the client credentials grant appropriate?
- [CS08-156] Why must redirect URIs be matched exactly by the authorization server?
- [CS08-157] What is SSO (single sign-on), and how does it work at a high level?
- [CS08-158] How would you implement social login with a third-party identity provider, and what are the security considerations?
- [CS08-159] How do SAML and OpenID Connect differ?
- [CS08-160] How do you implement role-based access control in APIs?
- [CS08-161] Compare role-based and permission-based access control, and explain where attribute-based access control fits.
- [CS08-162] What is the best way to handle authorization for hierarchical resources?

## API security and denial-of-service attacks
- [CS08-163] What is the OWASP API Security Top 10, and how do you address these risks?
- [CS08-164] What security considerations apply to API keys, and what are their weaknesses?
- [CS08-165] API keys vs JWTs: when and why would you use each?
- [CS08-166] What are the pros and cons of mTLS compared to OAuth for service-to-service authentication?
- [CS08-167] How do you secure webhooks?
- [CS08-168] What are the security considerations for WebSockets, and how do you authenticate real-time connections?
- [CS08-169] How do you secure REST versus GraphQL (or SOAP) endpoints differently?
- [CS08-170] How would you design rate limiting to protect an API from abuse?
- [CS08-171] What is mass assignment, and how do you prevent it in API handlers?
- [CS08-172] What is a DoS attack, how does DDoS differ, and what layers of defense can mitigate volumetric and application-layer attacks?
- [CS08-173] Explain the SYN flood attack. How do SYN cookies and backlog tuning mitigate it?
- [CS08-174] How do UDP flood, HTTP flood and DNS flood attacks work, and how do you defend against each?
- [CS08-175] What is IP spoofing, and why does it enable reflection and amplification attacks?
- [CS08-176] What is a TCP reset attack, and how can an attacker forge a RST packet?
- [CS08-177] What is a Slowloris attack, and why can a single machine take down a naive web server with it?
- [CS08-178] Why do DNS and NTP amplification attacks have such a high amplification factor?
- [CS08-179] How would you design a layered defence against a large DDoS attack on a public web service?
