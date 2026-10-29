# EWB Phishing URL Awareness Checker

## Overview
Phishing is a cyberattack in which attackers use deceptive links to trick people into revealing sensitive information. This Python program checks URL text for selected warning signs and helps users learn basic phishing awareness.

## Features
- Detects the @ symbol in a URL
- Flags unusually long URLs (over 100 characters)
- Identifies IPv4 addresses used as hostnames
- Flags hostnames with many subdomains
- Detects punycode-style hostnames (xn--)
- Flags URLs using HTTP
- Handles malformed URL input
- Explains warnings with simple hints
- Supports repeated checks and quitting with q

## Requirements
- Python 3.10 or later
- No additional packages required

## How to Run

On Kali Linux, macOS, or Linux:

```bash
python3 phishing_checker.py
```

On Windows:

```bash
python phishing_checker.py
```

Enter a sample URL when prompted. Type `q` to quit.

## Example Output

```text
EWB Phishing URL Awareness Checker
Text checks only. This program never opens URLs.

--- RESULT ---
- Uses HTTP; HTTPS alone does not prove trust.
```

Actual output may vary depending on the input.

## Testing
Five test cases are documented in `tests/test_samples.md`. The test table records the input, expected result, actual result, and pass/fail status.

## Screenshots
- Sample run: `screenshots/sample_run.png`
- Test results: `screenshots/test_results.png`

## Improvements
1. Added a loop so multiple URLs can be checked without restarting the program.
2. Added warning explanations and handling for malformed URL input.
3. Improved output formatting and added a summary of warning signs.

## Limitations
This is an educational tool that checks URL text only. It does not open URLs, perform live scanning, or guarantee that a URL is safe. A URL with no listed warning signs may still be malicious.

## Ethical Use
Use harmless sample URLs for testing. Do not collect credentials, visit suspicious websites, or test systems without permission.

## Author
Anuja Gurav
EWB Courses - Cybersecurity Mini Project