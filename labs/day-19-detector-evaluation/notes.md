# Day 19 — Lab Notes

## Work Completed
- Created a labelled synthetic URL dataset.
- Built a repeatable evaluation script.
- Reused the Day 18 detector without duplicating its implementation.
- Calculated classification metrics and inspected missed detections.

## Observed Results
- Accuracy: 80%
- Precision: 100%
- Recall: 60%
- False positives: 0
- False negatives: 2

## Main Finding
The detector missed two phishing-labelled samples with scores of 20 and 10. This highlights a limitation of relying on simple keyword-based heuristics and a fixed risk threshold.

## Limitations
The dataset contains only 10 synthetic examples. Results are useful for demonstrating evaluation methods but are not representative of real-world performance.

## Next Improvements
- Add more diverse benign and phishing-like examples.
- Test threshold changes against both false positives and false negatives.
- Preserve explainable reasons for each prediction.
- Avoid treating a low-risk verdict as a safety guarantee.