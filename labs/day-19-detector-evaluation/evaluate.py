
import csv
import sys
from pathlib import Path

# Reuse the Day 18 detector without copying its implementation.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DAY18_DIR = PROJECT_ROOT / "labs" / "day-18-phishing-detector"
sys.path.insert(0, str(DAY18_DIR))

from detector import analyze_url

DATASET = Path(__file__).with_name("dataset.csv")


def evaluate_dataset():
    counts = {
        "TP": 0, "TN": 0, "FP": 0, "FN": 0
    }

    with DATASET.open(newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            actual = row["label"].strip().lower()
            result = analyze_url(row["url"])
            predicted = (
                "phishing"
                if result["verdict"] in {"suspicious", "high-risk"}
                else "benign"
            )

            if actual == "phishing" and predicted == "phishing":
                counts["TP"] += 1
            elif actual == "benign" and predicted == "benign":
                counts["TN"] += 1
            elif actual == "benign" and predicted == "phishing":
                counts["FP"] += 1
            elif actual == "phishing" and predicted == "benign":
                counts["FN"] += 1
            else:
                raise ValueError(f"Unexpected label: {actual}")

            print(
                f"{actual:8} | {predicted:8} | "
                f"{result['risk_score']:3} | {row['url']}"
            )

    total = sum(counts.values())
    precision_denominator = counts["TP"] + counts["FP"]
    recall_denominator = counts["TP"] + counts["FN"]

    precision = (
        counts["TP"] / precision_denominator
        if precision_denominator else 0.0
    )
    recall = (
        counts["TP"] / recall_denominator
        if recall_denominator else 0.0
    )
    accuracy = (counts["TP"] + counts["TN"]) / total if total else 0.0

    print("\nConfusion matrix counts:")
    for name, value in counts.items():
        print(f"{name}: {value}")

    print(f"\nAccuracy:  {accuracy:.1%}")
    print(f"Precision: {precision:.1%}")
    print(f"Recall:    {recall:.1%}")
    print(f"False-positive rate: "
          f"{counts['FP'] / (counts['FP'] + counts['TN']):.1%}"
          if counts["FP"] + counts["TN"] else
          "False-positive rate: undefined (no benign samples)")

    return counts


if __name__ == "__main__":
    evaluate_dataset()
