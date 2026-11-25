# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 was to explain fundamental computer-networking concepts with real-world examples, run privacy-safe connectivity and DNS lookup tests from Terminal on a public example domain (`example.com`), and describe step-by-step what happens when a user opens a website.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| LAN | A Local Area Network connects devices inside a small physical space so they can share internet access and local resources quickly. | Laptops, phones, and a printer connected to the same home Wi-Fi router or college computer lab switch. |
| MAN | A Metropolitan Area Network links multiple local networks across a single city or large university campus. | Fiber-optic links connecting different academic buildings and hostels across a university campus. |
| WAN | A Wide Area Network spans huge geographical distances—across cities, countries, or continents—by interconnecting smaller networks. | The global Internet or a bank's network linking branches across multiple countries. |
| DNS | The Domain Name System acts like the internet's phonebook, translating human-friendly domain names into numeric IP addresses. | Resolving `example.com` into `104.20.23.154` and `172.66.147.243`. |
| Router | A network device that inspects packet destination addresses and forwards traffic between separate networks along the best path. | A home Wi-Fi router forwarding requests from a laptop on the LAN out to an ISP on the WAN. |
| Protocol | A standardized set of rules and formats that both sender and receiver follow so data can be exchanged reliably. | `HTTPS` / `HTTP/2` for fetching web pages, `TCP` for reliable delivery, and `DNS` for name lookups. |
| Packet switching | Splitting messages into small numbered packets that travel independently across shared network links and are reassembled at the destination. | A webpage's HTML file broken into small TCP/IP packets routed across internet hops and reassembled by your browser. |
| Client-server | A communication model where a client program requests a resource or service and a server program processes and sends back the response. | Safari or `curl` (client) requesting `https://example.com` from the `example.com` web server. |

---

### Task 7.2 — Observe network information
Tested `example.com` from Terminal (local DNS server IP and personal network details redacted for privacy):
- **Connectivity test (`ping -c 3 example.com`):** Sent 3 ICMP echo requests to `104.20.23.154`, received 3 replies (`0.0% packet loss`, average round-trip time `182.390 ms`).
- **DNS lookup (`nslookup example.com`):** Reported `Server: [redacted]` and returned two IPv4 addresses for `example.com`: `172.66.147.243` and `104.20.23.154`.
- **HTTP header check (`curl -I https://example.com`):** Returned `HTTP/2 200` with `content-type: text/html; charset=utf-8`.

**Answers to Task 7.2 questions:**
- **What a connectivity test (`ping`) helps check:** It confirms whether your computer can reach a remote host across the network, measures how fast packets travel there and back (latency in milliseconds), and detects whether any packets were dropped.
- **What information a DNS lookup displays:** It displays which DNS resolver answered the query (redacted here for privacy) along with the domain name and the IP address(es) mapped to that domain.
- **Role of DNS when you enter a website name in a browser:** People remember names like `example.com`, while routers and servers route packets using IP addresses; DNS bridges that gap automatically by looking up the destination IP address before the browser connects.

---

### Task 7.3 — What happens when you open a website?
1. **User enters the URL in the client:** You type `https://example.com` into your web browser (the **client**).
2. **DNS resolution:** Because the network routes traffic using IP addresses rather than words, the client sends a **DNS** query to find the IP address for `example.com` (`104.20.23.154`).
3. **Establishing connection & sending request:** Using network **protocols** (TCP/TLS and HTTPS), the client splits its `GET /` request into small packets and sends them to your local router.
4. **Routing across the network:** Your router forwards those packets onto your ISP and across intermediate WAN routers until they reach the destination **server**.
5. **Server processing and response:** The `example.com` web **server** receives the request, applies the HTTP **protocol**, and sends back a `200 OK` status along with the webpage's HTML, CSS, and media packets.
6. **Reassembly and display:** The packets return through the routers to the **client**, which reassembles them in order, checks integrity, and renders the finished webpage on your screen.

## 3. Commands / tools used
- `ping -c 3 example.com` — Sent three test packets to verify reachability and measure round-trip time.
- `nslookup example.com` — Queried DNS to inspect the IP addresses associated with `example.com` (local resolver IP redacted).
- `curl -I https://example.com` — Fetched HTTP response headers to confirm an `HTTP/2 200` server response.

## 4. My understanding
Opening a single webpage relies on multiple layered systems working seamlessly together: **DNS** finds the destination IP, **routers** move **packets** across LANs and WANs, **protocols** ensure both sides speak the same rules, and the **client-server** model delivers the page content back to the browser.

## 5. Difficulties faced
Understanding how to present real `nslookup` and `curl` outputs without exposing local network details (such as the local DNS server IP) required careful review.

## 6. How I resolved them
I kept the public `example.com` responses intact and replaced the local DNS server IP address with `[redacted]` in both my notes and screenshots.

## 7. Evidence / files
- `mission-07-networking/README.md`
- [Privacy-safe network diagnostics screenshot](../evidence/mission-07/01-network-diagnostics.png)
- [Website client-DNS-server flow diagram](../evidence/mission-07/02-website-request-flow.png)

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Status:** Committed locally on `main` (ready to push to GitHub).
