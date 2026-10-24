# Day 18 — Phishing URL Detection Prototype

## Objective
Build a Python-based URL risk detector that uses explainable heuristics to identify potentially suspicious URLs.

## Features
- Accepts absolute HTTP and HTTPS URLs.
- Rejects empty, malformed, relative, and control-character-containing inputs.
- Assigns risk points for unencrypted HTTP, IP-address hosts, user-info syntax, punycode hostnames, unusually long hostnames, excessive subdomains, long digit sequences, and sensitive-action terms.
- Returns a risk score, verdict, and human-readable reasons.
- Caps the risk score at 100.

## Risk Classification
- **Low-risk:** score below 25
- **Suspicious:** score from 25 to 49
- **High-risk:** score of 50 or above
- **Invalid:** input fails basic URL validation

## Validation
The detector executed against four sample URLs. Automated tests were run using Python's `unittest` framework.

**Result:** 8 tests passed; 0 failures.

Test coverage includes baseline HTTPS input, a high-risk HTTP/IP example, sensitive-action terms, empty input, relative URLs, control characters, score bounds, and explanatory reasons.

## Limitations
This is an educational, rule-based prototype. It does not query threat-intelligence feeds, inspect website content, or verify domain reputation. A low-risk verdict does not establish that a URL is safe. False positives and false negatives are possible.

## Run
From this directory:

```powershell
py detector.py
py -m unittest discover -s tests -v
```

Use `python` instead of `py` if that is the working Python command on your system.

## Security Takeaway
Explainable heuristics provide a useful starting point for URL triage, but the score must not be treated as proof that a website is malicious or trustworthy.