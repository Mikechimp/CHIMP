```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/rp1/results/198.248.86.124/scans/_full_tcp_nmap.txt" -oX "/home/kali/rp1/results/198.248.86.124/scans/xml/_full_tcp_nmap.xml" 198.248.86.124
```

[/home/kali/rp1/results/198.248.86.124/scans/_full_tcp_nmap.txt](file:///home/kali/rp1/results/198.248.86.124/scans/_full_tcp_nmap.txt):

```
# Nmap 7.95 scan initiated Sat May  3 02:29:02 2025 as: /usr/lib/nmap/nmap --privileged -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/kali/rp1/results/198.248.86.124/scans/_full_tcp_nmap.txt -oX /home/kali/rp1/results/198.248.86.124/scans/xml/_full_tcp_nmap.xml 198.248.86.124
Increasing send delay for 198.248.86.124 from 0 to 5 due to 11 out of 17 dropped probes since last increase.
Increasing send delay for 198.248.86.124 from 5 to 10 due to 11 out of 22 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of 1946816634 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 1946816634 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 1946738776 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of 1946738776 microseconds.  Ignoring time.
Warning: 198.248.86.124 giving up on port because retransmission cap hit (6).
Nmap scan report for 198.248.86.124
Host is up, received user-set (0.18s latency).
Scanned at 2025-05-03 02:29:02 EDT for 52101s
Not shown: 61870 filtered tcp ports (no-response), 3663 closed tcp ports (reset)
PORT    STATE SERVICE  REASON          VERSION
80/tcp  open  http     syn-ack ttl 128 nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
| vulners: 
|   nginx 1.18.0: 
|     	2C119FFA-ECE0-5E14-A4A4-354A2C38071A	10.0	https://vulners.com/githubexploit/2C119FFA-ECE0-5E14-A4A4-354A2C38071A	*EXPLOIT*
|     	3F71F065-66D4-541F-A813-9F1A2F2B1D91	8.8	https://vulners.com/githubexploit/3F71F065-66D4-541F-A813-9F1A2F2B1D91	*EXPLOIT*
|     	NGINX:CVE-2022-41741	7.8	https://vulners.com/nginx/NGINX:CVE-2022-41741
|     	DF1BBDC4-B715-5ABE-985E-91DD3BB87773	7.8	https://vulners.com/githubexploit/DF1BBDC4-B715-5ABE-985E-91DD3BB87773	*EXPLOIT*
|     	CVE-2022-41741	7.8	https://vulners.com/cve/CVE-2022-41741
|     	NGINX:CVE-2021-23017	7.7	https://vulners.com/nginx/NGINX:CVE-2021-23017
|     	EDB-ID:50973	7.7	https://vulners.com/exploitdb/EDB-ID:50973	*EXPLOIT*
|     	CVE-2021-23017	7.7	https://vulners.com/cve/CVE-2021-23017
|     	B175E582-6BBF-5D54-AF15-ED3715F757E3	7.7	https://vulners.com/githubexploit/B175E582-6BBF-5D54-AF15-ED3715F757E3	*EXPLOIT*
|     	9A14990B-D52A-56B6-966C-6F35C8B8EB9D	7.7	https://vulners.com/githubexploit/9A14990B-D52A-56B6-966C-6F35C8B8EB9D	*EXPLOIT*
|     	25F34A51-EB79-5BBC-8262-6F1876067F04	7.7	https://vulners.com/githubexploit/25F34A51-EB79-5BBC-8262-6F1876067F04	*EXPLOIT*
|     	245ACDDD-B1E2-5344-B37D-5B9A0B0A1F0D	7.7	https://vulners.com/githubexploit/245ACDDD-B1E2-5344-B37D-5B9A0B0A1F0D	*EXPLOIT*
|     	1337DAY-ID-37837	7.7	https://vulners.com/zdt/1337DAY-ID-37837	*EXPLOIT*
|     	1337DAY-ID-36300	7.7	https://vulners.com/zdt/1337DAY-ID-36300	*EXPLOIT*
|     	00455CDF-B814-5424-952E-9088FBB2D42D	7.7	https://vulners.com/githubexploit/00455CDF-B814-5424-952E-9088FBB2D42D	*EXPLOIT*
|     	F7F6E599-CEF4-5E03-8E10-FE18C4101E38	7.5	https://vulners.com/githubexploit/F7F6E599-CEF4-5E03-8E10-FE18C4101E38	*EXPLOIT*
|     	E73E445F-0A0D-5966-8A21-C74FE9C0D2BC	7.5	https://vulners.com/githubexploit/E73E445F-0A0D-5966-8A21-C74FE9C0D2BC	*EXPLOIT*
|     	E5C174E5-D6E8-56E0-8403-D287DE52EB3F	7.5	https://vulners.com/githubexploit/E5C174E5-D6E8-56E0-8403-D287DE52EB3F	*EXPLOIT*
|     	DB6E1BBD-08B1-574D-A351-7D6BB9898A4A	7.5	https://vulners.com/githubexploit/DB6E1BBD-08B1-574D-A351-7D6BB9898A4A	*EXPLOIT*
|     	CVE-2023-44487	7.5	https://vulners.com/cve/CVE-2023-44487
|     	C9A1C0C1-B6E3-5955-A4F1-DEA0E505B14B	7.5	https://vulners.com/githubexploit/C9A1C0C1-B6E3-5955-A4F1-DEA0E505B14B	*EXPLOIT*
|     	BD3652A9-D066-57BA-9943-4E34970463B9	7.5	https://vulners.com/githubexploit/BD3652A9-D066-57BA-9943-4E34970463B9	*EXPLOIT*
|     	B0B1EF25-DE18-534A-AE5B-E6E87669C1D2	7.5	https://vulners.com/githubexploit/B0B1EF25-DE18-534A-AE5B-E6E87669C1D2	*EXPLOIT*
|     	B0208442-6E17-5772-B12D-B5BE30FA5540	7.5	https://vulners.com/githubexploit/B0208442-6E17-5772-B12D-B5BE30FA5540	*EXPLOIT*
|     	A820A056-9F91-5059-B0BC-8D92C7A31A52	7.5	https://vulners.com/githubexploit/A820A056-9F91-5059-B0BC-8D92C7A31A52	*EXPLOIT*
|     	A66531EB-3C47-5C56-B8A6-E04B54E9D656	7.5	https://vulners.com/githubexploit/A66531EB-3C47-5C56-B8A6-E04B54E9D656	*EXPLOIT*
|     	9814661A-35A4-5DB7-BB25-A1040F365C81	7.5	https://vulners.com/githubexploit/9814661A-35A4-5DB7-BB25-A1040F365C81	*EXPLOIT*
|     	788E0E7C-6F5C-5DAD-9E3A-EE6D8A685F7D	7.5	https://vulners.com/githubexploit/788E0E7C-6F5C-5DAD-9E3A-EE6D8A685F7D	*EXPLOIT*
|     	5A864BCC-B490-5532-83AB-2E4109BB3C31	7.5	https://vulners.com/githubexploit/5A864BCC-B490-5532-83AB-2E4109BB3C31	*EXPLOIT*
|     	40879618-C556-547C-8769-9E63E83D0B55	7.5	https://vulners.com/githubexploit/40879618-C556-547C-8769-9E63E83D0B55	*EXPLOIT*
|     	1F6E0709-DA03-564E-925F-3177657C053E	7.5	https://vulners.com/githubexploit/1F6E0709-DA03-564E-925F-3177657C053E	*EXPLOIT*
|     	17C6AD2A-8469-56C8-BBBE-1764D0DF1680	7.5	https://vulners.com/githubexploit/17C6AD2A-8469-56C8-BBBE-1764D0DF1680	*EXPLOIT*
|     	CVE-2021-3618	7.4	https://vulners.com/cve/CVE-2021-3618
|     	NGINX:CVE-2022-41742	7.1	https://vulners.com/nginx/NGINX:CVE-2022-41742
|     	CVE-2022-41742	7.1	https://vulners.com/cve/CVE-2022-41742
|     	95499236-C9FE-56A6-9D7D-E943A24B633A	6.9	https://vulners.com/githubexploit/95499236-C9FE-56A6-9D7D-E943A24B633A	*EXPLOIT*
|     	PACKETSTORM:167720	6.8	https://vulners.com/packetstorm/PACKETSTORM:167720	*EXPLOIT*
|     	NGINX:CVE-2024-7347	5.7	https://vulners.com/nginx/NGINX:CVE-2024-7347
|     	NGINX:CVE-2025-23419	5.3	https://vulners.com/nginx/NGINX:CVE-2025-23419
|_    	PACKETSTORM:162830	0.0	https://vulners.com/packetstorm/PACKETSTORM:162830	*EXPLOIT*
443/tcp open  ssl/http syn-ack ttl 128 nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
| vulners: 
|   nginx 1.18.0: 
|     	2C119FFA-ECE0-5E14-A4A4-354A2C38071A	10.0	https://vulners.com/githubexploit/2C119FFA-ECE0-5E14-A4A4-354A2C38071A	*EXPLOIT*
|     	3F71F065-66D4-541F-A813-9F1A2F2B1D91	8.8	https://vulners.com/githubexploit/3F71F065-66D4-541F-A813-9F1A2F2B1D91	*EXPLOIT*
|     	NGINX:CVE-2022-41741	7.8	https://vulners.com/nginx/NGINX:CVE-2022-41741
|     	DF1BBDC4-B715-5ABE-985E-91DD3BB87773	7.8	https://vulners.com/githubexploit/DF1BBDC4-B715-5ABE-985E-91DD3BB87773	*EXPLOIT*
|     	CVE-2022-41741	7.8	https://vulners.com/cve/CVE-2022-41741
|     	NGINX:CVE-2021-23017	7.7	https://vulners.com/nginx/NGINX:CVE-2021-23017
|     	EDB-ID:50973	7.7	https://vulners.com/exploitdb/EDB-ID:50973	*EXPLOIT*
|     	CVE-2021-23017	7.7	https://vulners.com/cve/CVE-2021-23017
|     	B175E582-6BBF-5D54-AF15-ED3715F757E3	7.7	https://vulners.com/githubexploit/B175E582-6BBF-5D54-AF15-ED3715F757E3	*EXPLOIT*
|     	9A14990B-D52A-56B6-966C-6F35C8B8EB9D	7.7	https://vulners.com/githubexploit/9A14990B-D52A-56B6-966C-6F35C8B8EB9D	*EXPLOIT*
|     	25F34A51-EB79-5BBC-8262-6F1876067F04	7.7	https://vulners.com/githubexploit/25F34A51-EB79-5BBC-8262-6F1876067F04	*EXPLOIT*
|     	245ACDDD-B1E2-5344-B37D-5B9A0B0A1F0D	7.7	https://vulners.com/githubexploit/245ACDDD-B1E2-5344-B37D-5B9A0B0A1F0D	*EXPLOIT*
|     	1337DAY-ID-37837	7.7	https://vulners.com/zdt/1337DAY-ID-37837	*EXPLOIT*
|     	1337DAY-ID-36300	7.7	https://vulners.com/zdt/1337DAY-ID-36300	*EXPLOIT*
|     	00455CDF-B814-5424-952E-9088FBB2D42D	7.7	https://vulners.com/githubexploit/00455CDF-B814-5424-952E-9088FBB2D42D	*EXPLOIT*
|     	F7F6E599-CEF4-5E03-8E10-FE18C4101E38	7.5	https://vulners.com/githubexploit/F7F6E599-CEF4-5E03-8E10-FE18C4101E38	*EXPLOIT*
|     	E73E445F-0A0D-5966-8A21-C74FE9C0D2BC	7.5	https://vulners.com/githubexploit/E73E445F-0A0D-5966-8A21-C74FE9C0D2BC	*EXPLOIT*
|     	E5C174E5-D6E8-56E0-8403-D287DE52EB3F	7.5	https://vulners.com/githubexploit/E5C174E5-D6E8-56E0-8403-D287DE52EB3F	*EXPLOIT*
|     	DB6E1BBD-08B1-574D-A351-7D6BB9898A4A	7.5	https://vulners.com/githubexploit/DB6E1BBD-08B1-574D-A351-7D6BB9898A4A	*EXPLOIT*
|     	CVE-2023-44487	7.5	https://vulners.com/cve/CVE-2023-44487
|     	C9A1C0C1-B6E3-5955-A4F1-DEA0E505B14B	7.5	https://vulners.com/githubexploit/C9A1C0C1-B6E3-5955-A4F1-DEA0E505B14B	*EXPLOIT*
|     	BD3652A9-D066-57BA-9943-4E34970463B9	7.5	https://vulners.com/githubexploit/BD3652A9-D066-57BA-9943-4E34970463B9	*EXPLOIT*
|     	B0B1EF25-DE18-534A-AE5B-E6E87669C1D2	7.5	https://vulners.com/githubexploit/B0B1EF25-DE18-534A-AE5B-E6E87669C1D2	*EXPLOIT*
|     	B0208442-6E17-5772-B12D-B5BE30FA5540	7.5	https://vulners.com/githubexploit/B0208442-6E17-5772-B12D-B5BE30FA5540	*EXPLOIT*
|     	A820A056-9F91-5059-B0BC-8D92C7A31A52	7.5	https://vulners.com/githubexploit/A820A056-9F91-5059-B0BC-8D92C7A31A52	*EXPLOIT*
|     	A66531EB-3C47-5C56-B8A6-E04B54E9D656	7.5	https://vulners.com/githubexploit/A66531EB-3C47-5C56-B8A6-E04B54E9D656	*EXPLOIT*
|     	9814661A-35A4-5DB7-BB25-A1040F365C81	7.5	https://vulners.com/githubexploit/9814661A-35A4-5DB7-BB25-A1040F365C81	*EXPLOIT*
|     	788E0E7C-6F5C-5DAD-9E3A-EE6D8A685F7D	7.5	https://vulners.com/githubexploit/788E0E7C-6F5C-5DAD-9E3A-EE6D8A685F7D	*EXPLOIT*
|     	5A864BCC-B490-5532-83AB-2E4109BB3C31	7.5	https://vulners.com/githubexploit/5A864BCC-B490-5532-83AB-2E4109BB3C31	*EXPLOIT*
|     	40879618-C556-547C-8769-9E63E83D0B55	7.5	https://vulners.com/githubexploit/40879618-C556-547C-8769-9E63E83D0B55	*EXPLOIT*
|     	1F6E0709-DA03-564E-925F-3177657C053E	7.5	https://vulners.com/githubexploit/1F6E0709-DA03-564E-925F-3177657C053E	*EXPLOIT*
|     	17C6AD2A-8469-56C8-BBBE-1764D0DF1680	7.5	https://vulners.com/githubexploit/17C6AD2A-8469-56C8-BBBE-1764D0DF1680	*EXPLOIT*
|     	CVE-2021-3618	7.4	https://vulners.com/cve/CVE-2021-3618
|     	NGINX:CVE-2022-41742	7.1	https://vulners.com/nginx/NGINX:CVE-2022-41742
|     	CVE-2022-41742	7.1	https://vulners.com/cve/CVE-2022-41742
|     	95499236-C9FE-56A6-9D7D-E943A24B633A	6.9	https://vulners.com/githubexploit/95499236-C9FE-56A6-9D7D-E943A24B633A	*EXPLOIT*
|     	PACKETSTORM:167720	6.8	https://vulners.com/packetstorm/PACKETSTORM:167720	*EXPLOIT*
|     	NGINX:CVE-2024-7347	5.7	https://vulners.com/nginx/NGINX:CVE-2024-7347
|     	NGINX:CVE-2025-23419	5.3	https://vulners.com/nginx/NGINX:CVE-2025-23419
|_    	PACKETSTORM:162830	0.0	https://vulners.com/packetstorm/PACKETSTORM:162830	*EXPLOIT*
|_http-title: Speedtest | Kansas State University
| tls-alpn: 
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
| tls-nextprotoneg: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
Aggressive OS guesses: Actiontec MI424WR-GEN3I WAP (96%), DD-WRT v24-sp2 (Linux 2.4.37) (96%), Linux 3.2 (94%), Linux 4.4 (92%), Microsoft Windows XP SP3 or Windows 7 or Windows Server 2012 (92%), Microsoft Windows XP SP3 (90%), VMware Player virtual NAT device (87%), BlueArc Titan 2100 NAS device (86%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.95%E=4%D=5/3%OT=80%CT=49%CU=%PV=N%DS=3%DC=T%G=N%TM=68168333%P=x86_64-pc-linux-gnu)
SEQ(SP=100%GCD=1%ISR=108%TI=I%II=I%SS=S%TS=U)
SEQ(SP=104%GCD=1%ISR=107%TI=I%II=I%SS=S%TS=U)
OPS(O1=M5B4%O2=M5B4%O3=M5B4%O4=M5B4%O5=M5B4%O6=M5B4)
WIN(W1=FAF0%W2=FAF0%W3=FAF0%W4=FAF0%W5=FAF0%W6=FAF0)
ECN(R=Y%DF=N%TG=80%W=FAF0%O=M5B4%CC=N%Q=)
T1(R=Y%DF=N%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=Y%DF=N%TG=80%W=FAF0%S=O%A=S+%F=AS%O=M5B4%RD=0%Q=)
T4(R=Y%DF=N%TG=80%W=7FFF%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=N)
T6(R=Y%DF=N%TG=80%W=7FFF%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=S)

Network Distance: 3 hops
TCP Sequence Prediction: Difficulty=256 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8080/tcp)
HOP RTT        ADDRESS
1   0.36 ms    192.168.211.2
2   ...
3   1242.82 ms 198.248.86.124

Read data files from: /usr/share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May  3 16:57:23 2025 -- 1 IP address (1 host up) scanned in 52101.59 seconds

```
