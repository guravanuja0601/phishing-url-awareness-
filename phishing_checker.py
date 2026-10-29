import re
from urllib.parse import urlparse

INFO_MESSAGES = (
    "No URL entered.",
    "Could not identify",
    "This text is not a valid URL format.",
    "No listed warning signs"
)

REASONS = {
    "@": "Some URLs can hide the real destination before the @ symbol.",
    "Unusually long URL": "Long URLs can make the destination harder to recognize.",
    "IP address": "An IP address instead of a familiar domain deserves extra checking.",
    "hostname segments": "Many subdomains can make a URL confusing.",
    "punycode": "Punycode can represent international characters that resemble other characters.",
    "Uses HTTP": "HTTP does not encrypt the connection like HTTPS. HTTPS alone does not prove trust."
}


def inspect_url(raw_url):
    """Check URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP; HTTPS alone does not prove trust.")

    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


def has_warnings(findings):
    """Return True when findings contain actual warning signs."""
    return not any(
        message.startswith(INFO_MESSAGES)
        for message in findings
    )


def main():
    print("=" * 42)
    print("     EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 42)
    print("Text checks only. This program never opens URLs.")

    while True:
        raw_url = input("\nEnter a sample URL (or q to quit): ")

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\n--- RESULT ---")
        for item in findings:
            print("- " + item)

            for key, reason in REASONS.items():
                if key.lower() in item.lower():
                    print("  Hint: " + reason)
                    break

        if has_warnings(findings):
            print(
                "\nREVIEW CAREFULLY: "
                + str(len(findings))
                + " warning sign(s) found."
            )
        else:
            print("\nNo warning signs reported by these checks.")

        print("Remember: no automated text check guarantees safety.")


if __name__ == "__main__":
    main()