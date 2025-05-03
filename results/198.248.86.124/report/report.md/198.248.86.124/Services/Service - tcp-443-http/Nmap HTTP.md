```bash
nmap -vv --reason -Pn -T4 -sV -p 443 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_nmap.txt" -oX "/home/kali/rp1/results/198.248.86.124/scans/tcp443/xml/tcp_443_https_nmap.xml" 198.248.86.124
```

[/home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_nmap.txt](file:///home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_nmap.txt):

```
# Nmap 7.95 scan initiated Fri May  2 19:40:12 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -p 443 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_nmap.txt -oX /home/kali/rp1/results/198.248.86.124/scans/tcp443/xml/tcp_443_https_nmap.xml 198.248.86.124
Nmap scan report for 198.248.86.124
Host is up, received user-set (0.034s latency).
Scanned at 2025-05-02 19:40:12 EDT for 73s

PORT    STATE SERVICE  REASON          VERSION
443/tcp open  ssl/http syn-ack ttl 128 nginx 1.18.0 (Ubuntu)
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=198.248.86.124
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: https://198.248.86.124:443/
|     Form id: ksu-search-box
|_    Form action: https://search.k-state.edu/
|_ssl-date: TLS randomness does not represent time
|_http-server-header: nginx/1.18.0 (Ubuntu)
| http-php-version: Logo query returned unknown hash b24d83ac7326865c463d043125d0bd55
|_Credits query returned unknown hash b24d83ac7326865c463d043125d0bd55
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-feed: Couldn't find any feeds.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-vuln-cve2011-3192: 
|   VULNERABLE:
|   Apache byterange filter DoS
|     State: VULNERABLE
|     IDs:  BID:49303  CVE:CVE-2011-3192
|       The Apache web server is vulnerable to a denial of service attack when numerous
|       overlapping byte ranges are requested.
|     Disclosure date: 2011-08-19
|     References:
|       https://seclists.org/fulldisclosure/2011/Aug/175
|       https://www.securityfocus.com/bid/49303
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-3192
|_      https://www.tenable.com/plugins/nessus/55976
|_http-date: Fri, 02 May 2025 23:40:28 GMT; -6s from local time.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1
|_http-chrono: Request times for /; avg: 300.52ms; min: 248.30ms; max: 322.36ms
| http-vhosts: 
| 75 names had status 200
|_53 names had status ERROR
| ssl-enum-ciphers: 
|   TLSv1.2: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (ecdh_x25519) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (rsa 4096) - A
|     compressors: 
|       NULL
|     cipher preference: server
|     warnings: 
|       Key exchange (ecdh_x25519) of lower strength than certificate key
|_  least strength: A
| http-enum: 
|   /admin/: Possible admin folder
|_  /admin/index.php: Possible admin folder
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=198.248.86.124
|     
|     Path: https://198.248.86.124:443/
|     Line number: 174
|     Comment: 
|         
|         //SPEEDTEST AND UI CODE
|     
|     Path: https://198.248.86.124:443/
|     Line number: 22
|     Comment: 
|         <!-- 57\xC3\x9757px -->
|     
|     Path: https://198.248.86.124:443/
|     Line number: 140
|     Comment: 
|         
|         //CODE FOR GAUGES
|     
|     Path: https://198.248.86.124:443/
|     Line number: 235
|     Comment: 
|          //start frame loop
|     
|     Path: https://198.248.86.124:443/
|     Line number: 225
|     Comment: 
|         
|         //poll the status from the worker (this will call updateUI)
|     
|     Path: https://198.248.86.124:443/
|     Line number: 229
|     Comment: 
|         
|         //update the UI every frame
|     
|     Path: https://198.248.86.124:443/
|     Line number: 189
|     Comment: 
|          //Add optional parameters (see doc.md)
|     
|     Path: https://198.248.86.124:443/
|     Line number: 188
|     Comment: 
|          //w.postMessage('start'); //Add optional parameters as a JSON object to this command
|     
|     Path: https://198.248.86.124:443/
|     Line number: 208
|     Comment: 
|         
|         //this function reads the data sent back by the worker and updates the UI
|     
|     Path: https://198.248.86.124:443/
|     Line number: 308
|     Comment: 
|         <!-- <a href="https://github.com/adolfintel/speedtest">Source code</a>   -->
|     
|     Path: https://198.248.86.124:443/
|     Line number: 175
|     Comment: 
|          //speedtest worker
|     
|     Path: https://198.248.86.124:443/
|     Line number: 176
|     Comment: 
|_         //data from worker
| http-security-headers: 
|   Strict_Transport_Security: 
|_    HSTS not configured in HTTPS Server
| http-headers: 
|   Server: nginx/1.18.0 (Ubuntu)
|   Date: Fri, 02 May 2025 23:40:36 GMT
|   Content-Type: text/html
|   Content-Length: 10382
|   Last-Modified: Wed, 15 Nov 2017 17:43:48 GMT
|   Connection: close
|   ETag: "5a0c7cd4-288e"
|   Accept-Ranges: bytes
|   
|_  (Request type: HEAD)
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
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
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-title: Speedtest | Kansas State University
|_http-mobileversion-checker: No mobile version detected.
|_http-errors: Couldn't find any error pages.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-methods: 
|_  Supported Methods: GET HEAD
| ssl-cert: Subject: commonName=speedtest.ksu.edu/organizationName=Kansas State University/stateOrProvinceName=Kansas/countryName=US
| Subject Alternative Name: DNS:speedtest.ksu.edu, DNS:speedtest.k-state.edu, DNS:www.speedtest.k-state.edu, DNS:www.speedtest.ksu.edu
| Issuer: commonName=InCommon RSA Server CA 2/organizationName=Internet2/countryName=US
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha384WithRSAEncryption
| Not valid before: 2024-07-15T00:00:00
| Not valid after:  2025-08-15T23:59:59
| MD5:     5cd9:c786:bc49:5498:55a4:465e:5852:a515
| SHA-1:   05ea:58a6:5548:a823:b6e4:8df4:1f00:e84a:fcf5:6e95
| SHA-256: 1f94:e36d:e720:16cb:40c4:9ac5:540a:111d:c55b:fc41:5780:3591:ab9b:90fa:3d80:32d9
| -----BEGIN CERTIFICATE-----
| MIIIFDCCBnygAwIBAgIQNFFMd5lOJakT3ak1NSaxFTANBgkqhkiG9w0BAQwFADBE
| MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSW50ZXJuZXQyMSEwHwYDVQQDExhJbkNv
| bW1vbiBSU0EgU2VydmVyIENBIDIwHhcNMjQwNzE1MDAwMDAwWhcNMjUwODE1MjM1
| OTU5WjBcMQswCQYDVQQGEwJVUzEPMA0GA1UECBMGS2Fuc2FzMSAwHgYDVQQKExdL
| YW5zYXMgU3RhdGUgVW5pdmVyc2l0eTEaMBgGA1UEAxMRc3BlZWR0ZXN0LmtzdS5l
| ZHUwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDC8ytISuHHxKrGXLd5
| 8B2tn1JvnsmeHiomnHMpjT6qmt6PJD8SVb8+yRvca373NBPKj0716jEw4j7sQ3HL
| Vla4GSgrJZb7X6Uq5Mq4KL5OzjnY9R1LimMDmMQIoMvskxNd5+FUUMyvaSMPOD2G
| T9F2YtRF4qCS49EdmhqWEXyBb4r8Da+MDKmSpeVsQOgqX77PPz5HvtYbwcEmVTOP
| fI5oojUPYcZfhoSEDKubQu5lKJC3KCOh4kW/o+3VOEuI7s9/HX39sQvYGIM1esC5
| uoIiqlM41ay0SmM518Evs3qBMfTNZZytTqUiWoO+5LhHLWqOl4XWTOmp/wGkkTZ9
| F4JGu9dBCMSW6+i50iIms+Eo4vFEv20VggDNuv0COp4NFF0JfLmZEs6CnUW13ce6
| lcskLpRiLrZxVWOnjLfGX8rnouWNacI0jgQ58Pzhu4tgHf3uarzVvWkzQg6o8nIu
| lJSC4XtW++F/95nKEKegdsXc+XHn6FuyhLLDkbNdoiByJuSvhqwm9sjmYbllGM14
| LYgFf9vqEVU+t8HlqHdWBUChq150IqUJV8QCEgrmq9BnHCh75EU2YN/wRZXjwALs
| hrLFjeH+e9LFSQPCEpQXyghAXKg/vLsIHJ4cDeNsKzo95XyC4CBSDZ6B7kNhpHMD
| mvRjpQN9weVC/hVn1+g4kNVvxwIDAQABo4IDaDCCA2QwHwYDVR0jBBgwFoAU70wA
| kqb7di5eleLJX4cbGdVN4tkwHQYDVR0OBBYEFDY+snkPJo1TM1yuBr+HE54hclhC
| MA4GA1UdDwEB/wQEAwIFoDAMBgNVHRMBAf8EAjAAMB0GA1UdJQQWMBQGCCsGAQUF
| BwMBBggrBgEFBQcDAjBJBgNVHSAEQjBAMDQGCysGAQQBsjEBAgJnMCUwIwYIKwYB
| BQUHAgEWF2h0dHBzOi8vc2VjdGlnby5jb20vQ1BTMAgGBmeBDAECAjBABgNVHR8E
| OTA3MDWgM6Axhi9odHRwOi8vY3JsLnNlY3RpZ28uY29tL0luQ29tbW9uUlNBU2Vy
| dmVyQ0EyLmNybDBwBggrBgEFBQcBAQRkMGIwOwYIKwYBBQUHMAKGL2h0dHA6Ly9j
| cnQuc2VjdGlnby5jb20vSW5Db21tb25SU0FTZXJ2ZXJDQTIuY3J0MCMGCCsGAQUF
| BzABhhdodHRwOi8vb2NzcC5zZWN0aWdvLmNvbTCCAX0GCisGAQQB1nkCBAIEggFt
| BIIBaQFnAHcA3dzKNJXX4RYF55Uy+sef+D0cUN/bADoUEnYKLKy7yCoAAAGQt8C2
| AwAABAMASDBGAiEA181/HaJoynjQDB1isL75luVCGvRxKkLjXBo3AOKhwMwCIQCT
| VnzS8/ff5TooakFsSwNRS6mxAOf3DLdqsailWTlkZgB1AA3h8jAr0w3BQGISCepV
| LvxHdHyx1+kw7w5CHrR+Tqo0AAABkLfAte8AAAQDAEYwRAIgd6M6phaAhkHD+Prh
| RHASmJ7cYXKse+yqvj/5HT0EU+wCICIPIP4Xw8cra9fEUwBwtAhG1+ogrzJ//APX
| yZTt7LM+AHUAEvFONL1TckyEBhnDjz96E/jntWKHiJxtMAWE6+WGJjoAAAGQt8C1
| 4wAABAMARjBEAiBuN/gzvvkIZ6DXMBA5txqXaITDkNLd80ez/DwQyw0L7AIgek0x
| oknqJ25rcCN+w361ZYaGmvMq/xPsEn83kewBQEwwZQYDVR0RBF4wXIIRc3BlZWR0
| ZXN0LmtzdS5lZHWCFXNwZWVkdGVzdC5rLXN0YXRlLmVkdYIZd3d3LnNwZWVkdGVz
| dC5rLXN0YXRlLmVkdYIVd3d3LnNwZWVkdGVzdC5rc3UuZWR1MA0GCSqGSIb3DQEB
| DAUAA4IBgQAakQD486vnIf8f72N/x+6bfiwaBiaBNyVd4U9CNBIUm75ObSDTWl5i
| PvAOS92lLoDyKmYY55nCoXTnG8ki3qYs6dWmMB3WdYR7FlPhYsz+TY1y9mxJshkB
| NoaWi1/+I/2VJ8mFnIwMkLKgOgYO6Qbs2EI6UqlPCOA1cXSPv63v45j/DThf+Mdk
| CDNMVlWvPXpoAQnxoKgiquS/3mg98n5MhDJ0mpp6rTdHPbsWiClaTdoYN/00ky6W
| R5grYsTXmWrEEywA2f3DAuZhWazylFEfEGVXkuS8hluxZdze63doQ28Q5V45vC9w
| aCHD65BngXXjik8OKg3qb0LzBVmrBVY57ZO+8agPDkBRfS3VFyaQx1BSArXNIyQn
| c45Q0VEVqGiK9GmdDaBAjgpDBOeErDV0N6nm8PLz54kE+RUjppLseb4a2u9qBeGf
| QXP4RVQt+82vBP69T7ZqyrEq6kEvbaGOZYXn+t15sgbIDX3v/SJCo1CITlHjB2Tb
| 9XekzCG5AZY=
|_-----END CERTIFICATE-----
|_http-malware-host: Host appears to be clean
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri May  2 19:41:25 2025 -- 1 IP address (1 host up) scanned in 72.78 seconds

```
