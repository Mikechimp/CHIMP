```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/rp1/results/198.248.86.124/scans/_quick_tcp_nmap.txt" -oX "/home/kali/rp1/results/198.248.86.124/scans/xml/_quick_tcp_nmap.xml" 198.248.86.124
```

[/home/kali/rp1/results/198.248.86.124/scans/_quick_tcp_nmap.txt](file:///home/kali/rp1/results/198.248.86.124/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Fri May  2 18:59:37 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/kali/rp1/results/198.248.86.124/scans/_quick_tcp_nmap.txt -oX /home/kali/rp1/results/198.248.86.124/scans/xml/_quick_tcp_nmap.xml 198.248.86.124
Nmap scan report for 198.248.86.124
Host is up, received user-set (0.039s latency).
Scanned at 2025-05-02 18:59:37 EDT for 52s
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE    REASON          VERSION
80/tcp  open  tcpwrapped syn-ack ttl 128
|_http-server-header: nginx/1.18.0 (Ubuntu)
443/tcp open  tcpwrapped syn-ack ttl 128
|_http-server-header: nginx/1.18.0 (Ubuntu)
| tls-nextprotoneg: 
|_  http/1.1
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
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=5/2%OT=443%CT=%CU=%PV=N%G=N%TM=68154E8D%P=x86_64-pc-linux-gnu)
SEQ()
ECN(R=N)
T1(R=N)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=N)


TRACEROUTE (using port 443/tcp)
HOP RTT    ADDRESS
1   ... 30

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri May  2 19:00:29 2025 -- 1 IP address (1 host up) scanned in 52.35 seconds

```
