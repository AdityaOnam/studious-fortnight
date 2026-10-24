---
domain: cs
topic: computer_networks_tcp_http_dns
title: Computer networks: TCP/IP, HTTP, DNS
tags: [networks, tcp, http, dns, tls]
count: 126
part: 1/2
---
# Computer networks: TCP/IP, HTTP, DNS (part 1)

## Network models, layering and the link layer
- [CS03-001] What problem does layering solve in network protocols, and why does the OSI model still matter when debugging?
- [CS03-002] Describe the seven layers of the OSI model and what each layer is responsible for.
- [CS03-003] Compare the OSI seven-layer model with the TCP/IP model. How do their layers map to each other?
- [CS03-004] What are the differences between LAN, WAN, MAN and PAN?
- [CS03-005] What is the difference between circuit switching and packet switching, and why is the Internet packet-switched?
- [CS03-006] What is the difference between a hub, a switch and a router, and at which layer does each operate?
- [CS03-007] What is the difference between a MAC address and an IP address?
- [CS03-008] What is ARP, and how does a host find the MAC address of a destination on the same subnet?
- [CS03-009] What are the four components of packet delay: processing, queuing, transmission and propagation?
- [CS03-010] What is the difference between big-endian and little-endian byte order, and when does it matter in networking?
- [CS03-011] Two hosts communicate over a network. Walk through encapsulation and decapsulation, naming the data unit used at each layer.
- [CS03-012] At which layers do load balancers and firewalls operate, and what information does each layer's device use to make forwarding decisions?
- [CS03-013] Why did the Internet adopt TCP/IP rather than the OSI stack, and where does strict layering leak in practice?
- [CS03-014] Given a 1500-byte packet on a 100 Mbps link spanning 1000 km, compute transmission and propagation delay and say which dominates.
- [CS03-015] What problems must a link layer solve: framing, transparent transmission and error detection?
- [CS03-016] How does CSMA/CD work, and why does it not apply to switched full-duplex Ethernet?
- [CS03-017] What do CSMA/CD and CSMA/CA do, and why is collision detection impractical on wireless networks?
- [CS03-018] How does a learning switch build and use its forwarding table, and what happens to a frame whose destination is unknown?
- [CS03-019] What is a broadcast domain versus a collision domain, and how do hubs, switches, routers and VLANs affect each?
- [CS03-020] What is a VLAN and why would you deploy one?
- [CS03-021] What is ARP spoofing, how does it enable a man-in-the-middle attack on a local network, and how can it be mitigated?
- [CS03-022] What is a broadcast storm, and how does the Spanning Tree Protocol prevent switching loops?

## IP addressing, NAT, routing and ICMP
- [CS03-023] What is an IP address, and how does IP routing deliver a packet across networks?
- [CS03-024] What is the difference between public, private, static and dynamic IP addresses?
- [CS03-025] What is the difference between unicast, broadcast and multicast delivery?
- [CS03-026] What is the difference between TCP and IP?
- [CS03-027] Explain classful IP addressing, subnetting and CIDR.
- [CS03-028] What is NAT, why was it introduced, and what benefits does a NAT firewall provide?
- [CS03-029] What fields does an IPv4 header contain, and what are TTL, fragmentation offset and protocol used for?
- [CS03-030] How many usable hosts can a 192.168.1.0/26 subnet have?
- [CS03-031] Given the address 192.168.10.37/27, how do you compute the network address, broadcast address and number of usable hosts?
- [CS03-032] Why was CIDR introduced and how does route aggregation reduce routing table size?
- [CS03-033] What are the main differences between IPv4 and IPv6, and why has IPv6 adoption been slow?
- [CS03-034] What is MTU and path MTU discovery, and how can fragmentation cause connectivity problems?
- [CS03-035] How do ping and traceroute work, and which ICMP messages and TTL behaviour do they rely on?
- [CS03-036] How does a router forward a packet: longest prefix match, next hop and TTL decrement?
- [CS03-037] A host can reach machines on its own subnet but nothing beyond it. What configuration and network issues would you check?
- [CS03-038] Compare distance-vector routing (RIP) with link-state routing (OSPF). What is count-to-infinity?
- [CS03-039] Why is BGP used between autonomous systems while RIP and OSPF are used inside them?
- [CS03-040] How does NAT with port translation keep track of many internal hosts sharing one public IP?
- [CS03-041] What problems does NAT create for peer-to-peer applications, and how are they worked around?
- [CS03-042] How does DHCP work, and what happens in each step of the DORA exchange?
- [CS03-043] What is a VPN and how does tunneling protect traffic across the public Internet?
- [CS03-044] What is a VPN and how is it different from a proxy?

## UDP and TCP connection lifecycle
- [CS03-045] What are the key differences between TCP and UDP?
- [CS03-046] Which common application-layer protocols run over TCP and which over UDP?
- [CS03-047] When would you choose UDP over TCP for an application? Give concrete examples and justify each.
- [CS03-048] Why is TCP byte-stream oriented while UDP is message oriented, and what practical problems does this cause for application protocols?
- [CS03-049] How does an application deal with message boundaries (sticky packets) when reading from a TCP socket?
- [CS03-050] What fields does a UDP header contain, and why is UDP so lightweight?
- [CS03-051] How do TCP and UDP each handle transmission errors?
- [CS03-052] How would you build reliability on top of UDP, and which protocol takes this approach?
- [CS03-053] What fields does a TCP header contain, and what do sequence number, acknowledgment number and window size do?
- [CS03-054] Explain the TCP three-way handshake and what each segment contains.
- [CS03-055] Why does TCP need a handshake at all, and why three messages rather than two?
- [CS03-056] In the second handshake step, why does the server send a SYN in addition to the ACK?
- [CS03-057] Can data be carried in the segments of the three-way handshake? Which ones, and why?
- [CS03-058] What happens if the SYN or the final ACK of the TCP handshake is lost?
- [CS03-059] What is a SYN flood attack, and how do SYN cookies and other measures mitigate it?
- [CS03-060] What are the SYN (half-open) queue and the accept queue on a TCP server, what does the listen backlog control, and what happens when each overflows?
- [CS03-061] Explain the TCP four-way connection termination.
- [CS03-062] Why does connection teardown take four steps while setup takes three?
- [CS03-063] Under what circumstances can a TCP close appear to take only three segments?
- [CS03-064] What happens in TCP if the ACK of the first FIN is lost on its way back to the closing side?
- [CS03-065] What is TIME_WAIT, why does the active closer wait 2*MSL, and what two problems does the state solve?
- [CS03-066] A server shows tens of thousands of sockets in TIME_WAIT. Is that a problem, and how do you decide what to do about it?
- [CS03-067] A server shows thousands of connections stuck in CLOSE_WAIT. What does that indicate and how would you debug it?
- [CS03-068] Why is enabling tcp_tw_reuse or recycling TIME_WAIT sockets aggressively risky, and when is it safe?

## TCP reliability, flow and congestion control
- [CS03-069] How does TCP guarantee reliable delivery: sequence numbers, acknowledgments, retransmission and checksums? And how do you choose between TCP and UDP on that basis?
- [CS03-070] Compare stop-and-wait, Go-Back-N and Selective Repeat ARQ. Why is a sliding window more efficient than stop-and-wait?
- [CS03-071] How does the TCP sliding window work, and how does it differ from flow control and congestion control?
- [CS03-072] How does TCP flow control prevent a fast sender from overwhelming a slow receiver, and what happens with a zero window?
- [CS03-073] What is the difference between flow control and congestion control in TCP?
- [CS03-074] How does TCP compute the retransmission timeout, what is Karn's algorithm avoiding, and what goes wrong if the timeout is too short or too long?
- [CS03-075] Explain TCP fast retransmit. Why does it trigger on duplicate ACKs instead of waiting for a timeout?
- [CS03-076] Explain slow start, congestion avoidance, fast retransmit and fast recovery.
- [CS03-077] How does TCP congestion control react differently to a retransmission timeout versus three duplicate ACKs, and what happens to cwnd and ssthresh?
- [CS03-078] How do TCP Tahoe and Reno differ in their reaction to packet loss?
- [CS03-079] What are the Nagle algorithm and delayed ACK, and how can their interaction hurt latency for small writes?
- [CS03-080] What is head-of-line blocking in TCP, and how does QUIC address it?
- [CS03-081] How can an application maximize bandwidth utilization over TCP, given window sizes and round-trip time?
- [CS03-082] What is TCP window scaling, and why is it needed on high-bandwidth, high-latency paths?
- [CS03-083] What problem does selective acknowledgement (SACK) solve, and what extra information does D-SACK report to the sender?
- [CS03-084] On a 1 Gbps link with 50 ms round-trip time, what window size is needed to keep the link full, and what limits you if the window is only 64 KB?
- [CS03-085] Why does packet loss crush TCP throughput on long-fat networks, and how do algorithms such as BBR differ from loss-based control?
- [CS03-086] Why does TCP perform poorly over high-latency lossy links such as satellite or mobile, and what could you do about it?
- [CS03-087] What is ECN (explicit congestion notification), and how does it let routers signal congestion without dropping packets?

## Sockets, ports and connection troubleshooting
- [CS03-088] What is a socket, and what are some well-known ports for HTTP, HTTPS, SSH, FTP, DNS and SMTP?
- [CS03-089] Can TCP and UDP use the same port number simultaneously, and why does that not conflict?
- [CS03-090] What is the sequence of system calls for a TCP server and for a TCP client?
- [CS03-091] How does a non-blocking socket behave differently from a blocking one, and how does an I/O-multiplexed server loop fit in?
- [CS03-092] Why should a process serving many connections avoid one thread per connection, and how do event-driven servers address it?
- [CS03-093] What is TCP keepalive, and how does it differ from HTTP keep-alive?
- [CS03-094] What are the possible outcomes of a TCP keepalive probe, and what are its limitations for detecting dead peers?
- [CS03-095] How does a server learn about half-dead TCP connections after a client crash, and why do applications add their own heartbeats?
- [CS03-096] How are idle HTTP persistent connections closed and reclaimed on the server and client side?
- [CS03-097] What fields make up the four-tuple that identifies a TCP connection?
- [CS03-098] A host has only 65535 ports. Why can a server still hold far more concurrent TCP connections than that?
- [CS03-099] What is ephemeral port exhaustion on a client or proxy, how do you recognise it, and how do you fix it?
- [CS03-100] What does SO_REUSEADDR do, and why is it needed when restarting a server that has sockets in TIME_WAIT?
- [CS03-101] What do the states shown by netstat or ss (ESTABLISHED, SYN_RECV, FIN_WAIT_2, LISTEN) tell you about a misbehaving service?
- [CS03-102] If you can ping a host, does a TCP connection to it definitely succeed? Ping works but a TCP connection times out: what are the possible causes?
- [CS03-103] Why can an HTTPS request fail at the TLS stage even though TCP connects fine, for example with SNI-based filtering?
- [CS03-104] How would you debug intermittent connection resets between two services using tcpdump or Wireshark?
- [CS03-105] How do you troubleshoot if you cannot reach a particular website?
- [CS03-106] What actually limits the number of concurrent TCP connections on a Linux server, and why do clients or NAT gateways hit limits earlier?
- [CS03-107] A service sees many connection resets under load. What kernel, TCP and application-level causes would you investigate?
- [CS03-108] Users report a website is slow only from one region. How would you use DNS, traceroute, TCP and HTTP-level tools to localize the problem?
- [CS03-109] In a packet capture, how would you recognise retransmissions, zero-window stalls and a slow DNS lookup, and what does each imply?

## Domain Name System
- [CS03-110] How does DNS resolution work step by step, from the browser to the authoritative server?
- [CS03-111] What types of DNS servers exist (root, TLD, authoritative, local resolver) and what role does each play?
- [CS03-112] What are the common DNS record types (A, AAAA, CNAME, MX, NS, TXT, SRV) and what is each used for?
- [CS03-113] What is the difference between recursive and iterative DNS queries?
- [CS03-114] How do CNAME records differ from A records, and what restriction does a CNAME impose at the zone apex?
- [CS03-115] How does DNS caching work across browser, OS and resolver, and what are the trade-offs of long and short TTLs when changing a record or failing over?
- [CS03-116] In what order are caches checked before a DNS query leaves the machine?
- [CS03-117] Why does DNS mostly use UDP, and when does it switch to TCP?
- [CS03-118] How does DNS-based load balancing work, and what are its limitations?
- [CS03-119] What is DNS hijacking, and how can you detect and mitigate it?
- [CS03-120] What disadvantages does DNS have as an infrastructure component, such as propagation delay and DDoS exposure?
- [CS03-121] What is a glue record, and why is it needed when a domain's name servers live inside the domain itself?
- [CS03-122] A domain resolves to different IPs from different networks. How would you investigate with dig or nslookup?
- [CS03-123] What do DNS over HTTPS and DNS over TLS protect against, and what do they not protect?
- [CS03-124] What does DNSSEC add to DNS, and which attack does it address?
- [CS03-125] How does a DNS amplification attack work, and what makes open resolvers dangerous?
- [CS03-126] How do root DNS servers use anycast to serve queries from hundreds of locations under a small set of addresses?
