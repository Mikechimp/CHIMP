```bash
sslscan --show-certificate --no-colour 198.248.86.124:443 2>&1
```

[/home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_sslscan.html](file:///home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_sslscan.html):

```
Version: 2.1.5
OpenSSL 3.5.0 8 Apr 2025

Connected to 198.248.86.124

Testing SSL server 198.248.86.124 on port 443 using SNI name 198.248.86.124

  SSL/TLS Protocols:
SSLv2     disabled
SSLv3     disabled
TLSv1.0   disabled
TLSv1.1   disabled
TLSv1.2   enabled
TLSv1.3   disabled

  TLS Fallback SCSV:
Server supports TLS Fallback SCSV

  TLS renegotiation:
Session renegotiation not supported

  TLS Compression:
Compression disabled

  Heartbleed:
TLSv1.2 not vulnerable to heartbleed

  Supported Server Cipher(s):
Preferred TLSv1.2  256 bits  ECDHE-RSA-AES256-GCM-SHA384   Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-CHACHA20-POLY1305   Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-ARIA256-GCM-SHA384      Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-GCM-SHA256   Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-ARIA128-GCM-SHA256      Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA384       Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-CAMELLIA256-SHA384  Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA256       Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-CAMELLIA128-SHA256  Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  ECDHE-RSA-AES256-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  128 bits  ECDHE-RSA-AES128-SHA          Curve 25519 DHE 253
Accepted  TLSv1.2  256 bits  AES256-GCM-SHA384
Accepted  TLSv1.2  64 bits   AES256-CCM8
Accepted  TLSv1.2  256 bits  AES256-CCM
Accepted  TLSv1.2  256 bits  ARIA256-GCM-SHA384
Accepted  TLSv1.2  128 bits  AES128-GCM-SHA256
Accepted  TLSv1.2  64 bits   AES128-CCM8
Accepted  TLSv1.2  128 bits  AES128-CCM
Accepted  TLSv1.2  128 bits  ARIA128-GCM-SHA256
Accepted  TLSv1.2  256 bits  AES256-SHA256
Accepted  TLSv1.2  256 bits  CAMELLIA256-SHA256
Accepted  TLSv1.2  128 bits  AES128-SHA256
Accepted  TLSv1.2  128 bits  CAMELLIA128-SHA256
Accepted  TLSv1.2  256 bits  AES256-SHA
Accepted  TLSv1.2  256 bits  CAMELLIA256-SHA
Accepted  TLSv1.2  128 bits  AES128-SHA
Accepted  TLSv1.2  128 bits  CAMELLIA128-SHA

  Server Key Exchange Group(s):
TLSv1.2  128 bits  secp256r1 (NIST P-256)
TLSv1.2  192 bits  secp384r1 (NIST P-384)
TLSv1.2  260 bits  secp521r1 (NIST P-521)
TLSv1.2  128 bits  x25519
TLSv1.2  224 bits  x448

  SSL Certificate:
    Certificate blob:
-----BEGIN CERTIFICATE-----
MIIIFDCCBnygAwIBAgIQNFFMd5lOJakT3ak1NSaxFTANBgkqhkiG9w0BAQwFADBE
MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSW50ZXJuZXQyMSEwHwYDVQQDExhJbkNv
bW1vbiBSU0EgU2VydmVyIENBIDIwHhcNMjQwNzE1MDAwMDAwWhcNMjUwODE1MjM1
OTU5WjBcMQswCQYDVQQGEwJVUzEPMA0GA1UECBMGS2Fuc2FzMSAwHgYDVQQKExdL
YW5zYXMgU3RhdGUgVW5pdmVyc2l0eTEaMBgGA1UEAxMRc3BlZWR0ZXN0LmtzdS5l
ZHUwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDC8ytISuHHxKrGXLd5
8B2tn1JvnsmeHiomnHMpjT6qmt6PJD8SVb8+yRvca373NBPKj0716jEw4j7sQ3HL
Vla4GSgrJZb7X6Uq5Mq4KL5OzjnY9R1LimMDmMQIoMvskxNd5+FUUMyvaSMPOD2G
T9F2YtRF4qCS49EdmhqWEXyBb4r8Da+MDKmSpeVsQOgqX77PPz5HvtYbwcEmVTOP
fI5oojUPYcZfhoSEDKubQu5lKJC3KCOh4kW/o+3VOEuI7s9/HX39sQvYGIM1esC5
uoIiqlM41ay0SmM518Evs3qBMfTNZZytTqUiWoO+5LhHLWqOl4XWTOmp/wGkkTZ9
F4JGu9dBCMSW6+i50iIms+Eo4vFEv20VggDNuv0COp4NFF0JfLmZEs6CnUW13ce6
lcskLpRiLrZxVWOnjLfGX8rnouWNacI0jgQ58Pzhu4tgHf3uarzVvWkzQg6o8nIu
lJSC4XtW++F/95nKEKegdsXc+XHn6FuyhLLDkbNdoiByJuSvhqwm9sjmYbllGM14
LYgFf9vqEVU+t8HlqHdWBUChq150IqUJV8QCEgrmq9BnHCh75EU2YN/wRZXjwALs
hrLFjeH+e9LFSQPCEpQXyghAXKg/vLsIHJ4cDeNsKzo95XyC4CBSDZ6B7kNhpHMD
mvRjpQN9weVC/hVn1+g4kNVvxwIDAQABo4IDaDCCA2QwHwYDVR0jBBgwFoAU70wA
kqb7di5eleLJX4cbGdVN4tkwHQYDVR0OBBYEFDY+snkPJo1TM1yuBr+HE54hclhC
MA4GA1UdDwEB/wQEAwIFoDAMBgNVHRMBAf8EAjAAMB0GA1UdJQQWMBQGCCsGAQUF
BwMBBggrBgEFBQcDAjBJBgNVHSAEQjBAMDQGCysGAQQBsjEBAgJnMCUwIwYIKwYB
BQUHAgEWF2h0dHBzOi8vc2VjdGlnby5jb20vQ1BTMAgGBmeBDAECAjBABgNVHR8E
OTA3MDWgM6Axhi9odHRwOi8vY3JsLnNlY3RpZ28uY29tL0luQ29tbW9uUlNBU2Vy
dmVyQ0EyLmNybDBwBggrBgEFBQcBAQRkMGIwOwYIKwYBBQUHMAKGL2h0dHA6Ly9j
cnQuc2VjdGlnby5jb20vSW5Db21tb25SU0FTZXJ2ZXJDQTIuY3J0MCMGCCsGAQUF
BzABhhdodHRwOi8vb2NzcC5zZWN0aWdvLmNvbTCCAX0GCisGAQQB1nkCBAIEggFt
BIIBaQFnAHcA3dzKNJXX4RYF55Uy+sef+D0cUN/bADoUEnYKLKy7yCoAAAGQt8C2
AwAABAMASDBGAiEA181/HaJoynjQDB1isL75luVCGvRxKkLjXBo3AOKhwMwCIQCT
VnzS8/ff5TooakFsSwNRS6mxAOf3DLdqsailWTlkZgB1AA3h8jAr0w3BQGISCepV
LvxHdHyx1+kw7w5CHrR+Tqo0AAABkLfAte8AAAQDAEYwRAIgd6M6phaAhkHD+Prh
RHASmJ7cYXKse+yqvj/5HT0EU+wCICIPIP4Xw8cra9fEUwBwtAhG1+ogrzJ//APX
yZTt7LM+AHUAEvFONL1TckyEBhnDjz96E/jntWKHiJxtMAWE6+WGJjoAAAGQt8C1
4wAABAMARjBEAiBuN/gzvvkIZ6DXMBA5txqXaITDkNLd80ez/DwQyw0L7AIgek0x
oknqJ25rcCN+w361ZYaGmvMq/xPsEn83kewBQEwwZQYDVR0RBF4wXIIRc3BlZWR0
ZXN0LmtzdS5lZHWCFXNwZWVkdGVzdC5rLXN0YXRlLmVkdYIZd3d3LnNwZWVkdGVz
dC5rLXN0YXRlLmVkdYIVd3d3LnNwZWVkdGVzdC5rc3UuZWR1MA0GCSqGSIb3DQEB
DAUAA4IBgQAakQD486vnIf8f72N/x+6bfiwaBiaBNyVd4U9CNBIUm75ObSDTWl5i
PvAOS92lLoDyKmYY55nCoXTnG8ki3qYs6dWmMB3WdYR7FlPhYsz+TY1y9mxJshkB
NoaWi1/+I/2VJ8mFnIwMkLKgOgYO6Qbs2EI6UqlPCOA1cXSPv63v45j/DThf+Mdk
CDNMVlWvPXpoAQnxoKgiquS/3mg98n5MhDJ0mpp6rTdHPbsWiClaTdoYN/00ky6W
R5grYsTXmWrEEywA2f3DAuZhWazylFEfEGVXkuS8hluxZdze63doQ28Q5V45vC9w
aCHD65BngXXjik8OKg3qb0LzBVmrBVY57ZO+8agPDkBRfS3VFyaQx1BSArXNIyQn
c45Q0VEVqGiK9GmdDaBAjgpDBOeErDV0N6nm8PLz54kE+RUjppLseb4a2u9qBeGf
QXP4RVQt+82vBP69T7ZqyrEq6kEvbaGOZYXn+t15sgbIDX3v/SJCo1CITlHjB2Tb
9XekzCG5AZY=
-----END CERTIFICATE-----
    Version: 2
    Serial Number: 34:51:4c:77:99:4e:25:a9:13:dd:a9:35:35:26:b1:15
    Signature Algorithm: sha384WithRSAEncryption
    Issuer: /C=US/O=Internet2/CN=InCommon RSA Server CA 2
    Not valid before: Jul 15 00:00:00 2024 GMT
    Not valid after: Aug 15 23:59:59 2025 GMT
    Subject: /C=US/ST=Kansas/O=Kansas State University/CN=speedtest.ksu.edu
    Public Key Algorithm: NULL
    RSA Public Key: (4096 bit)
      RSA Public-Key: (4096 bit)
      Modulus:
          00:c2:f3:2b:48:4a:e1:c7:c4:aa:c6:5c:b7:79:f0:
          1d:ad:9f:52:6f:9e:c9:9e:1e:2a:26:9c:73:29:8d:
          3e:aa:9a:de:8f:24:3f:12:55:bf:3e:c9:1b:dc:6b:
          7e:f7:34:13:ca:8f:4e:f5:ea:31:30:e2:3e:ec:43:
          71:cb:56:56:b8:19:28:2b:25:96:fb:5f:a5:2a:e4:
          ca:b8:28:be:4e:ce:39:d8:f5:1d:4b:8a:63:03:98:
          c4:08:a0:cb:ec:93:13:5d:e7:e1:54:50:cc:af:69:
          23:0f:38:3d:86:4f:d1:76:62:d4:45:e2:a0:92:e3:
          d1:1d:9a:1a:96:11:7c:81:6f:8a:fc:0d:af:8c:0c:
          a9:92:a5:e5:6c:40:e8:2a:5f:be:cf:3f:3e:47:be:
          d6:1b:c1:c1:26:55:33:8f:7c:8e:68:a2:35:0f:61:
          c6:5f:86:84:84:0c:ab:9b:42:ee:65:28:90:b7:28:
          23:a1:e2:45:bf:a3:ed:d5:38:4b:88:ee:cf:7f:1d:
          7d:fd:b1:0b:d8:18:83:35:7a:c0:b9:ba:82:22:aa:
          53:38:d5:ac:b4:4a:63:39:d7:c1:2f:b3:7a:81:31:
          f4:cd:65:9c:ad:4e:a5:22:5a:83:be:e4:b8:47:2d:
          6a:8e:97:85:d6:4c:e9:a9:ff:01:a4:91:36:7d:17:
          82:46:bb:d7:41:08:c4:96:eb:e8:b9:d2:22:26:b3:
          e1:28:e2:f1:44:bf:6d:15:82:00:cd:ba:fd:02:3a:
          9e:0d:14:5d:09:7c:b9:99:12:ce:82:9d:45:b5:dd:
          c7:ba:95:cb:24:2e:94:62:2e:b6:71:55:63:a7:8c:
          b7:c6:5f:ca:e7:a2:e5:8d:69:c2:34:8e:04:39:f0:
          fc:e1:bb:8b:60:1d:fd:ee:6a:bc:d5:bd:69:33:42:
          0e:a8:f2:72:2e:94:94:82:e1:7b:56:fb:e1:7f:f7:
          99:ca:10:a7:a0:76:c5:dc:f9:71:e7:e8:5b:b2:84:
          b2:c3:91:b3:5d:a2:20:72:26:e4:af:86:ac:26:f6:
          c8:e6:61:b9:65:18:cd:78:2d:88:05:7f:db:ea:11:
          55:3e:b7:c1:e5:a8:77:56:05:40:a1:ab:5e:74:22:
          a5:09:57:c4:02:12:0a:e6:ab:d0:67:1c:28:7b:e4:
          45:36:60:df:f0:45:95:e3:c0:02:ec:86:b2:c5:8d:
          e1:fe:7b:d2:c5:49:03:c2:12:94:17:ca:08:40:5c:
          a8:3f:bc:bb:08:1c:9e:1c:0d:e3:6c:2b:3a:3d:e5:
          7c:82:e0:20:52:0d:9e:81:ee:43:61:a4:73:03:9a:
          f4:63:a5:03:7d:c1:e5:42:fe:15:67:d7:e8:38:90:
          d5:6f:c7
      Exponent: 65537 (0x10001)
    X509v3 Extensions:
      X509v3 Authority Key Identifier:
        EF:4C:00:92:A6:FB:76:2E:5E:95:E2:C9:5F:87:1B:19:D5:4D:E2:D9
      X509v3 Subject Key Identifier:
        36:3E:B2:79:0F:26:8D:53:33:5C:AE:06:BF:87:13:9E:21:72:58:42
      X509v3 Key Usage: critical
        Digital Signature, Key Encipherment
      X509v3 Basic Constraints: critical
        CA:FALSE
      X509v3 Extended Key Usage:
        TLS Web Server Authentication, TLS Web Client Authentication
      X509v3 Certificate Policies:
        Policy: 1.3.6.1.4.1.6449.1.2.2.103
          CPS: https://sectigo.com/CPS
        Policy: 2.23.140.1.2.2
      X509v3 CRL Distribution Points:
        Full Name:
          URI:http://crl.sectigo.com/InCommonRSAServerCA2.crl

      Authority Information Access:
        CA Issuers - URI:http://crt.sectigo.com/InCommonRSAServerCA2.crt
        OCSP - URI:http://ocsp.sectigo.com
      CT Precertificate SCTs:
        Signed Certificate Timestamp:
            Version   : v1 (0x0)
            Log ID    : DD:DC:CA:34:95:D7:E1:16:05:E7:95:32:FA:C7:9F:F8:
                        3D:1C:50:DF:DB:00:3A:14:12:76:0A:2C:AC:BB:C8:2A
            Timestamp : Jul 15 18:56:18.435 2024 GMT
            Extensions: none
            Signature : ecdsa-with-SHA256
                        30:46:02:21:00:D7:CD:7F:1D:A2:68:CA:78:D0:0C:1D:
                        62:B0:BE:F9:96:E5:42:1A:F4:71:2A:42:E3:5C:1A:37:
                        00:E2:A1:C0:CC:02:21:00:93:56:7C:D2:F3:F7:DF:E5:
                        3A:28:6A:41:6C:4B:03:51:4B:A9:B1:00:E7:F7:0C:B7:
                        6A:B1:A8:A5:59:39:64:66
        Signed Certificate Timestamp:
            Version   : v1 (0x0)
            Log ID    : 0D:E1:F2:30:2B:D3:0D:C1:40:62:12:09:EA:55:2E:FC:
                        47:74:7C:B1:D7:E9:30:EF:0E:42:1E:B4:7E:4E:AA:34
            Timestamp : Jul 15 18:56:18.415 2024 GMT
            Extensions: none
            Signature : ecdsa-with-SHA256
                        30:44:02:20:77:A3:3A:A6:16:80:86:41:C3:F8:FA:E1:
                        44:70:12:98:9E:DC:61:72:AC:7B:EC:AA:BE:3F:F9:1D:
                        3D:04:53:EC:02:20:22:0F:20:FE:17:C3:C7:2B:6B:D7:
                        C4:53:00:70:B4:08:46:D7:EA:20:AF:32:7F:FC:03:D7:
                        C9:94:ED:EC:B3:3E
        Signed Certificate Timestamp:
            Version   : v1 (0x0)
            Log ID    : 12:F1:4E:34:BD:53:72:4C:84:06:19:C3:8F:3F:7A:13:
                        F8:E7:B5:62:87:88:9C:6D:30:05:84:EB:E5:86:26:3A
            Timestamp : Jul 15 18:56:18.403 2024 GMT
            Extensions: none
            Signature : ecdsa-with-SHA256
                        30:44:02:20:6E:37:F8:33:BE:F9:08:67:A0:D7:30:10:
                        39:B7:1A:97:68:84:C3:90:D2:DD:F3:47:B3:FC:3C:10:
                        CB:0D:0B:EC:02:20:7A:4D:31:A2:49:EA:27:6E:6B:70:
                        23:7E:C3:7E:B5:65:86:86:9A:F3:2A:FF:13:EC:12:7F:
                        37:91:EC:01:40:4C
      X509v3 Subject Alternative Name:
        DNS:speedtest.ksu.edu, DNS:speedtest.k-state.edu, DNS:www.speedtest.k-state.edu, DNS:www.speedtest.ksu.edu
  Verify m:
    unable to get local issuer certificate

  SSL Certificate:
Signature Algorithm: sha384WithRSAEncryption
RSA Key Strength:    4096

Subject:  speedtest.ksu.edu
Altnames: DNS:speedtest.ksu.edu, DNS:speedtest.k-state.edu, DNS:www.speedtest.k-state.edu, DNS:www.speedtest.ksu.edu
Issuer:   InCommon RSA Server CA 2

Not valid before: Jul 15 00:00:00 2024 GMT
Not valid after:  Aug 15 23:59:59 2025 GMT


```
