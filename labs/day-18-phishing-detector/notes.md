# Day 18 — Lab Notes

## What I learned
- URL parsing helps separate a URL's scheme, hostname, path, and query.
- Multiple weak signals can be combined into a transparent risk score.
- Invalid input should be handled explicitly.
- Automated tests make detector behavior repeatable and easier to maintain.

## Validation Results
- Sample execution completed.
- Automated tests: 8 passed, 0 failures.
- High-risk sample: HTTP + IP-address hostname + sensitive-action term produced a score of 50.
- HTTPS baseline sample produced a score of 0.

## Limitations
- Heuristic scoring can produce false positives and false negatives.
- The detector does not confirm whether a URL is malicious.
- No external URLs were visited as part of validation.

## Next Improvements
- Evaluate against a labelled synthetic dataset.
- Measure false positives and false negatives.
- Expand test cases for malformed and deceptive URLs.
- Improve URL normalization and hostname validation.