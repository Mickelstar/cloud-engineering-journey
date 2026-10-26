# Day 19 — Phishing Detector Evaluation

## Objective
Evaluate the Day 18 rule-based URL detector against a small labelled synthetic dataset and measure its classification performance.

## Implementation
- Created a 10-sample CSV dataset with five benign-labelled and five phishing-labelled examples.
- Reused the Day 18 detector.
- Classified `suspicious` and `high-risk` results as positive detections.
- Calculated confusion-matrix counts, accuracy, precision, recall, and false-positive rate.

## Results

| Metric | Result |
|---|---:|
| True positives | 3 |
| True negatives | 5 |
| False positives | 0 |
| False negatives | 2 |
| Accuracy | 80% |
| Precision | 100% |
| Recall | 60% |
| False-positive rate | 0% |

## Findings
The detector missed two phishing-labelled samples because their scores were below the suspicious threshold. Sensitive terms alone did not always generate enough risk points to trigger detection.

## Limitations
This is a small synthetic dataset designed to test the prototype's behavior. The labels are illustrative, not verified threat intelligence. These metrics do not establish real-world detection performance, and a low-risk result does not prove a URL is safe.

## Run

```powershell
py evaluate.py
py -m unittest discover -s tests -v
```

## Security Lesson
Evaluation reveals weaknesses that individual unit tests may not expose. Recall and false negatives matter when assessing a detector intended to identify potential phishing URLs.