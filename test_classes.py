import unittest
from unittest.mock import MagicMock

from classes import PaymentProcessor
from interface import TransactionResult, NetworkException, PaymentException


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()
        self.gateway_mock = MagicMock()
        self.processor.gateway = self.gateway_mock

    def test_processPayment_successful(self):
        self.gateway_mock.charge.return_value = TransactionResult(
            True, "tx123", "Payment processed successfully"
        )

        result = self.processor.processPayment("user123", 100.0)

        self.assertTrue(result.success)
        self.assertEqual(result.transactionId, "tx123")
        self.assertEqual(result.message, "Payment processed successfully")
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_insufficient_funds(self):
        self.gateway_mock.charge.side_effect = PaymentException("Insufficient funds")

        result = self.processor.processPayment("user123", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Insufficient funds", result.message)
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_network_error(self):
        self.gateway_mock.charge.side_effect = NetworkException("Network error")

        result = self.processor.processPayment("user123", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Network error", result.message)
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_invalid_input(self):
        result = self.processor.processPayment("", 100.0)
        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Invalid payment details", result.message)

        result = self.processor.processPayment("user123", -50.0)
        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Invalid payment details", result.message)

    def test_imports(self):
        assert PaymentProcessor
        assert TransactionResult
        assert NetworkException
        assert PaymentException


if __name__ == "__main__":
    unittest.main()
