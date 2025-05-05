```bash
whatweb --color=never --no-errors -a 3 -v https://198.248.86.124:443 2>&1
```

[/home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_whatweb.txt](file:///home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_whatweb.txt):

```
WhatWeb report for https://198.248.86.124:443
Status    : 200 OK
Title     : Speedtest | Kansas State University
IP        : 198.248.86.124
Country   : UNITED STATES, US

Summary   : Frame, HTML5, HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], Meta-Author[Kansas State University], nginx[1.18.0], Open-Graph-Protocol[website], Script[text/javascript]

Detected Plugins:
[ Frame ]
	This plugin detects instances of frame and iframe HTML
	elements.


[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Ubuntu Linux
	String       : nginx/1.18.0 (Ubuntu) (from server string)

[ Meta-Author ]
	This plugin retrieves the author name from the meta name
	tag - info:
	http://www.webmarketingnow.com/tips/meta-tags-uncovered.html
	#author

	String       : Kansas State University

[ Open-Graph-Protocol ]
	The Open Graph protocol enables you to integrate your Web
	pages into the social graph. It is currently designed for
	Web pages representing profiles of real-world things .
	things like movies, sports teams, celebrities, and
	restaurants. Including Open Graph tags on your Web page,
	makes your page equivalent to a Facebook Page.

	Version      : website

[ Script ]
	This plugin detects instances of script HTML elements and
	returns the script language/type.

	String       : text/javascript

[ nginx ]
	Nginx (Engine-X) is a free, open-source, high-performance
	HTTP server and reverse proxy, as well as an IMAP/POP3
	proxy server.

	Version      : 1.18.0
	Website     : http://nginx.net/

HTTP Headers:
	HTTP/1.1 200 OK
	Server: nginx/1.18.0 (Ubuntu)
	Date: Sat, 03 May 2025 20:57:24 GMT
	Content-Type: text/html
	Last-Modified: Wed, 15 Nov 2017 17:43:48 GMT
	Transfer-Encoding: chunked
	Connection: close
	ETag: W/"5a0c7cd4-288e"
	Content-Encoding: gzip



```
