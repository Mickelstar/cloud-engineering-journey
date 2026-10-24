
import unittest

from detector import analyze_url


class TestURLDetector(unittest.TestCase):
    def test_benign_https_url(self):
        result = analyze_url("https://example.com")
        self.assertEqual(result["risk_score"], 0)
        self.assertEqual(result["verdict"], "low-risk")

    def test_http_ip_and_login_is_high_risk(self):
        result = analyze_url("http://192.0.2.10/login")
        self.assertEqual(result["risk_score"], 50)
        self.assertEqual(result["verdict"], "high-risk")
        self.assertEqual(len(result["reasons"]), 3)

    def test_sensitive_terms_add_risk(self):
        result = analyze_url("https://example.com/verify-account")
        self.assertEqual(result["risk_score"], 20)
        self.assertIn("sensitive-action terms: account, verify", result["reasons"][0])

    def test_empty_input_is_invalid(self):
        result = analyze_url("")
        self.assertEqual(result["verdict"], "invalid")

    def test_relative_url_is_invalid(self):
        result = analyze_url("/login")
        self.assertEqual(result["verdict"], "invalid")

    def test_control_characters_are_invalid(self):
        result = analyze_url("https://example.com/\nlogin")
        self.assertEqual(result["verdict"], "invalid")

    def test_score_stays_within_bounds(self):
        result = analyze_url("http://192.0.2.10/login/verify/account/password")
        self.assertGreaterEqual(result["risk_score"], 0)
        self.assertLessEqual(result["risk_score"], 100)

    def test_invalid_input_has_reason(self):
        result = analyze_url("")
        self.assertTrue(result["reasons"])


if __name__ == "__main__":
    unittest.main()
