```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/rp1/results/198.248.86.124/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/rp1/results/198.248.86.124/scans/tcp80/xml/tcp_80_http_nmap.xml" 198.248.86.124
```

[/home/kali/rp1/results/198.248.86.124/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/rp1/results/198.248.86.124/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.95 scan initiated Fri May  2 19:40:12 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/rp1/results/198.248.86.124/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/rp1/results/198.248.86.124/scans/tcp80/xml/tcp_80_http_nmap.xml 198.248.86.124
Nmap scan report for 198.248.86.124
Host is up, received user-set (0.038s latency).
Scanned at 2025-05-02 19:40:12 EDT for 55s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 128 nginx 1.18.0 (Ubuntu)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-malware-host: Host appears to be clean
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-mobileversion-checker: No mobile version detected.
|_http-comments-displayer: Couldn't find any comments.
| http-vhosts: 
|_128 names had status ERROR
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-traceroute: ERROR: Script execution failed (use -d to debug)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-errors: ERROR: Script execution failed (use -d to debug)
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Redirected To: https://198.248.86.124/
|   Allowed User Agents: 
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-feed: Couldn't find any feeds.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-chrono: Request times for /; avg: 387.96ms; min: 162.49ms; max: 1173.69ms
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri May  2 19:41:07 2025 -- 1 IP address (1 host up) scanned in 55.31 seconds

```
