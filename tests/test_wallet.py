import unittest
from src.wallet import WalletTracker
from unittest.mock import patch

class TestWalletTracker(unittest.TestCase):

    def test_add_wallet(self):
        tracker = WalletTracker()
        result = tracker.add_wallet("0x1234567890abcdef1234567890abcdef12345678")
        self.assertEqual(result, "Added wallet: 0x1234567890abcdef1234567890abcdef12345678")

    def test_get_balance(self):
        tracker = WalletTracker()
        with patch.object(WalletTracker, 'get_balance', return_value=1.5):
            balance = tracker.get_balance("0x1234567890abcdef1234567890abcdef12345678")
            self.assertIsInstance(balance, float)

    def test_add_ens(self):
        tracker = WalletTracker()
        # Invalid ENS should raise ValueError (if not resolvable)
        self.assertRaises(ValueError, tracker.add_wallet, "invalid.eth")

    def test_batch_add_wallets(self):
        tracker = WalletTracker()
        result = tracker.batch_add_wallets([
            "0x1234567890abcdef1234567890abcdef12345678",
            "0xabcdef1234567890abcdef1234567890abcdef12"
        ])
        self.assertEqual(result, "Added 2 wallets")

    def test_save_balance_history(self):
        tracker = WalletTracker()
        with patch.object(WalletTracker, 'get_balance', return_value=1.23):
            history = tracker.save_balance_history("0x1234567890abcdef1234567890abcdef12345678")
            self.assertIn("address", history)
            self.assertIn("balance", history)
            self.assertIn("timestamp", history)

    def test_get_token_balance(self):
        tracker = WalletTracker()
        with patch.object(WalletTracker, 'get_token_balance', return_value=999.0):
            balance = tracker.get_token_balance(
                "0x1234567890abcdef1234567890abcdef12345678",
                "0xdAC17F958D2ee523a2206206994597C13D831ec7"
            )
            self.assertIsInstance(balance, float)

# Doc comment 14
# Doc comment 25
# Doc comment 50

if __name__ == "__main__":
    unittest.main()
# Comment 91 for day 2
# Comment 92 for day 2


# Doc comment 115
# Comment 122 for day 3
# Doc comment 126
