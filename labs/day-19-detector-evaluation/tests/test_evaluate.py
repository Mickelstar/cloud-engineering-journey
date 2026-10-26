
import unittest

from evaluate import evaluate_dataset


class TestDatasetEvaluation(unittest.TestCase):
    def test_dataset_has_expected_sample_counts(self):
        counts = evaluate_dataset()

        self.assertEqual(sum(counts.values()), 10)
        self.assertEqual(counts["TP"] + counts["FN"], 5)
        self.assertEqual(counts["TN"] + counts["FP"], 5)

    def test_confusion_matrix_counts_are_nonnegative(self):
        counts = evaluate_dataset()

        for value in counts.values():
            self.assertGreaterEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
