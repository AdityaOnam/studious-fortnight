---
domain: cs
topic: security_crypto_web_basics
title: Security, cryptography and web basics
tags: [security, cryptography, owasp, auth]
count: 91
part: 1/2
---
# Security, cryptography and web basics (part 1)

## Security fundamentals and common vulnerabilities
- [CS08-001] What is the CIA triad, and what is an example of an attack against each property?
- [CS08-002] What is web security, and why is it important?
- [CS08-003] What is the difference between encryption, hashing and encoding, and when should each be used?
- [CS08-004] What are some of the most common web security vulnerabilities?
- [CS08-005] What is the OWASP Top 10? Name several entries and explain why the list matters.
- [CS08-006] What are CVE and CVSS, and how would you use them to prioritise patching?
- [CS08-007] What is the principle of least privilege, and where do you apply it in a web application?
- [CS08-008] Why do both the front end and the back end need to perform data validation?
- [CS08-009] What does secure coding mean, and what common vulnerabilities (injection, broken authentication, sensitive data exposure) should developers guard against?
- [CS08-010] What strategies help prevent error information disclosure vulnerabilities?
- [CS08-011] What is defense in depth, and how would you apply it to a typical web application?
- [CS08-012] What is an insecure direct object reference (IDOR/BOLA), and how do you prevent it?
- [CS08-013] What is SSRF, why is it dangerous in cloud environments, and how do you mitigate it?
- [CS08-014] What is path traversal, and how do you protect file-serving endpoints against it?
- [CS08-015] What risks come with accepting file uploads, and how do you handle them safely?
- [CS08-016] How do vulnerable third-party dependencies and supply-chain attacks threaten an application, and how do you reduce that risk?
- [CS08-017] What is threat modeling, and how would you use STRIDE on a new feature?
- [CS08-018] What is the difference between horizontal and vertical privilege escalation?
- [CS08-019] What is an open redirect, and how can it be chained into a phishing or OAuth attack?

## Symmetric cryptography and hash functions
- [CS08-020] What is cryptography, and what are its main goals?
- [CS08-021] What is the difference between symmetric and asymmetric encryption, and what are the strengths and weaknesses of each?
- [CS08-022] Why is it said you should never roll your own cryptography?
- [CS08-023] State Kerckhoffs's principle. Why does a cipher's security not depend on keeping the algorithm secret?
- [CS08-024] What does it mean for a cryptographic algorithm to be "computationally secure"?
- [CS08-025] What is perfect secrecy, and which encryption system achieves it? Why is it impractical?
- [CS08-026] What is a nonce, and how is it used in cryptography?
- [CS08-027] How does a stream cipher differ from a block cipher?
- [CS08-028] What are substitution and permutation in the context of encryption algorithms?
- [CS08-029] Can you describe the Feistel cipher structure?
- [CS08-030] What is DES, and why is it considered insecure today?
- [CS08-031] What are the key differences between DES and 3DES?
- [CS08-032] Explain the basic principle behind the AES encryption algorithm.
- [CS08-033] Why is AES in ECB mode insecure, and how do CBC, CTR and GCM differ?
- [CS08-034] What goes wrong if you reuse a nonce with AES-GCM?
- [CS08-035] What is authenticated encryption (AEAD), and why is encryption without integrity dangerous?
- [CS08-036] Why must a security-sensitive application use a cryptographically secure random number generator instead of a regular PRNG?
- [CS08-037] Roughly how long would an exhaustive search of a 128-bit key take, and why does key length matter so much?
- [CS08-038] What is a cryptographic hash function, and what properties must it have?
- [CS08-039] Why are MD5 and SHA-1 considered broken? What should be used instead?
- [CS08-040] What is the difference between collision resistance, preimage resistance and second-preimage resistance?
- [CS08-041] What is an HMAC, and why is it better than hashing a key concatenated with a message?
- [CS08-042] What is a length-extension attack, and which hash constructions are vulnerable?

## Public-key cryptography, signatures and PKI
- [CS08-043] Describe the differences between RSA and ECC (elliptic curve cryptography).
- [CS08-044] At a high level, how does RSA encryption work, and why is it not used to encrypt bulk data directly?
- [CS08-045] How does a hybrid scheme combine public-key and symmetric encryption to exchange a key?
- [CS08-046] How does the Diffie-Hellman key exchange let two parties agree on a secret over an insecure channel?
- [CS08-047] Why is plain Diffie-Hellman vulnerable to a man-in-the-middle attack, and how is that fixed in practice?
- [CS08-048] What is a digital signature, and how is it different from encryption and from a MAC?
- [CS08-049] Describe the concept of public key infrastructure (PKI).
- [CS08-050] What is a digital certificate, and why do we trust it?
- [CS08-051] What is a certificate authority, and how does the chain of trust work from a server certificate to a root?
- [CS08-052] How do certificate revocation mechanisms (CRL, OCSP, OCSP stapling) work, and what are their weaknesses?
- [CS08-053] Why is it still called an SSL certificate if SSL is deprecated?
- [CS08-054] Why does quantum computing threaten RSA and ECC but not AES to the same degree?

## TLS and HTTPS
- [CS08-055] What is HTTPS, how does it differ from HTTP, and why does it matter?
- [CS08-056] What are SSL and TLS, and what role do they play in web security?
- [CS08-057] Walk through the TLS handshake.
- [CS08-058] Define a secure session and explain how it is established.
- [CS08-059] What does HTTPS provide in terms of confidentiality, authentication and integrity, and how is integrity protected?
- [CS08-060] How does HTTPS authenticate a server using certificates and certificate authorities?
- [CS08-061] Why does HTTPS switch to symmetric encryption for transmitting data?
- [CS08-062] How is the session key material derived in an RSA handshake versus an ECDHE handshake?
- [CS08-063] Why did TLS 1.3 remove static RSA key exchange?
- [CS08-064] What is forward secrecy, and which TLS configurations provide it?
- [CS08-065] What changed between TLS 1.2 and TLS 1.3 in terms of handshake round trips and supported cipher suites?
- [CS08-066] What is TLS 0-RTT, and what replay risk does it introduce?
- [CS08-067] What is a man-in-the-middle attack, and how do HTTPS, certificate validation and pinning defend against it?
- [CS08-068] If HTTPS is safe, how can tools like Fiddler or Charles capture and read HTTPS traffic?
- [CS08-069] What is HSTS, and how does it defend against SSL stripping?
- [CS08-070] What is mutual TLS, and when would you use it?
- [CS08-071] Users report "certificate not trusted" errors for your site. What are the likely causes and how would you debug them?

## Injection, XSS and CSRF
- [CS08-072] What is SQL injection, and how does an attacker exploit it?
- [CS08-073] How do prepared statements and parameterized queries prevent SQL injection?
- [CS08-074] Why is escaping input a weaker defense than parameterized queries against SQL injection?
- [CS08-075] What is blind SQL injection, and how can attackers extract data without seeing query results?
- [CS08-076] What defense-in-depth measures besides parameterization reduce SQL injection risk (least privilege, input validation, ORM usage)?
- [CS08-077] Are stored procedures immune to SQL injection? When can they still be vulnerable?
- [CS08-078] Table names and ORDER BY columns cannot be bound as parameters. How do you handle them safely?
- [CS08-079] What other injection attacks exist besides SQL injection (NoSQL, OS command, LDAP), and how do you defend against them?
- [CS08-080] What is cross-site scripting (XSS), and how do stored, reflected and DOM-based XSS differ?
- [CS08-081] How do you prevent XSS using output encoding, CSP, HttpOnly cookies and input validation?
- [CS08-082] Why is output encoding context-dependent (HTML body, attribute, JavaScript, URL)?
- [CS08-083] How does a Content Security Policy mitigate XSS, and what makes a policy weak?
- [CS08-084] Does an HttpOnly cookie stop XSS? What can an attacker still do with an XSS foothold?
- [CS08-085] Modern frameworks like React escape output by default. How can XSS still occur in them?
- [CS08-086] What is cross-site request forgery (CSRF), and why does it work even though the attacker cannot read the response?
- [CS08-087] How do CSRF tokens, SameSite cookies and Origin/Referer checks each prevent CSRF?
- [CS08-088] Why does cookie-based authentication need more attention to CSRF than header-based token authentication?
- [CS08-089] What is the difference between CSRF and XSS in terms of which trust each one exploits?
- [CS08-090] What do SameSite=Strict, Lax and None mean, and which default do browsers apply?
- [CS08-091] Can an XSS vulnerability defeat CSRF protection? Explain.
