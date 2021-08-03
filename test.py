import unittest
from fraudulent_activity_notification import calc_median, notify_fraudulent_activity

class TestFraudulentActivity(unittest.TestCase):
    "Test Fraudulent Activity."

    def test_median_odd(self):
        median = calc_median([1, 2, 3])
        self.assertEqual(median, 2)

    def test_median_even(self):
        median = calc_median([1, 2, 3, 4])
        self.assertEqual(median, 2.5)

    def test_median_one(self):
        median = calc_median([1])
        self.assertEqual(median, 1)

    def test_median_two(self):
        median = calc_median([1, 2])
        self.assertEqual(median, 1.5)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            calc_median([])

    def test_notify_fraudulent_activity(self):
        notice = notify_fraudulent_activity([10, 20, 30, 40, 50], 3, 5)
        self.assertEqual(notice, 1)
