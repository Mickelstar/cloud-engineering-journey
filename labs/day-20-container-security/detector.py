
from urllib.parse import urlparse
import ipaddress
import re

SUSPICIOUS_WORDS = {
    "login", "verify", "account", "secure",
    "update", "password", "wallet", "confirm"
}


def analyze_url(url: str) -> dict:
    """Return an explainable heuristic risk assessment for a URL."""
    if not isinstance(url, str) or not url.strip():
        return {
            "risk_score": 0,
            "verdict": "invalid",
            "reasons": ["URL is empty or invalid"]
        }

    candidate = url.strip()
    if any(ord(char) < 32 for char in candidate):
        return {
            "risk_score": 0,
            "verdict": "invalid",
            "reasons": ["URL contains control characters"]
        }

    parsed = urlparse(candidate)

    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return {
            "risk_score": 0,
            "verdict": "invalid",
            "reasons": ["Expected an absolute HTTP or HTTPS URL"]
        }

    host = parsed.hostname.lower()
    reasons = []
    score = 0

    if parsed.scheme == "http":
        score += 15
        reasons.append("Uses unencrypted HTTP")

    try:
        ipaddress.ip_address(host)
        score += 25
        reasons.append("Uses an IP address instead of a domain")
    except ValueError:
        pass

    if "@" in parsed.netloc:
        score += 25
        reasons.append("Contains user-info syntax that may obscure the host")

    if host.startswith("xn--") or ".xn--" in host:
        score += 15
        reasons.append("Contains an internationalized/punycode hostname")

    if len(host) > 40:
        score += 10
        reasons.append("Hostname is unusually long")

    if host.count(".") >= 4:
        score += 10
        reasons.append("Hostname has many subdomain levels")

    if re.search(r"\d{5,}", host):
        score += 10
        reasons.append("Hostname contains a long digit sequence")

    path_and_query = f"{parsed.path} {parsed.query}".lower()
    matched_words = sorted(
        word for word in SUSPICIOUS_WORDS
        if word in path_and_query
    )

    if matched_words:
        score += min(30, 10 * len(matched_words))
        reasons.append(
            "Contains sensitive-action terms: " + ", ".join(matched_words)
        )

    score = min(score, 100)

    if score >= 50:
        verdict = "high-risk"
    elif score >= 25:
        verdict = "suspicious"
    else:
        verdict = "low-risk"

    if not reasons:
        reasons.append("No configured heuristic matched")

    return {
        "risk_score": score,
        "verdict": verdict,
        "reasons": reasons
    }


if __name__ == "__main__":
    samples = [
        "https://example.com",
        "http://192.0.2.10/login",
        "https://example.com/verify-account",
        "https://example.com"
    ]

    for sample in samples:
        print(f"\nURL: {sample}")
        print(analyze_url(sample))
