import unittest
from src.wallet import WalletTracker

class TestWalletTracker(unittest.TestCase):
    def test_add_wallet(self):
        tracker = WalletTracker()
        result = tracker.add_wallet("0x1234567890abcdef1234567890abcdef12345678")
        self.assertEqual(result, "Added wallet: 0x1234567890abcdef1234567890abcdef12345678")

if __name__ == "__main__":
    unittest.main()
    def test_get_balance(self):
    tracker = WalletTracker()
    # Mock balance fetching (since we need a real address)
    self.assertIsInstance(tracker.get_balance("0x1234567890abcdef1234567890abcdef12345678"), float)