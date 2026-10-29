Test Results

Python version used: 3.13.12 | Operating system: Kali Linux | Date: 2026-10-29

#| Input| Expected result| Actual result| Pass/Fail
1| "https://www.example.com/login"| No listed warning signs| No listed warning signs| PASS
2| "http://192.0.2.10/account"| IP address + HTTP| IP address + HTTP| PASS
3| "http://example.com@sample.invalid/login"| @ symbol + HTTP| @ symbol + HTTP| PASS
4| "https://a.b.c.d.e.example.invalid/login"| Many hostname segments| Many hostname segments| PASS
5| "https://xn--example.invalid/"| Punycode-style hostname| Punycode-style hostname| PASS

Notes

The program checks URL text for common warning signs without opening websites. I learned that IP addresses, unusual hostname patterns, and HTTP can deserve closer inspection. No warning signs does not guarantee that a URL is safe.
