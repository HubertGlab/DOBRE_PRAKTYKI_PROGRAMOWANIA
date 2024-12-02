import unittest
from unittest.mock import MagicMock
from interface import *
from classes import *


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        # Tworzymy obiekt PaymentProcessor i mocka PaymentGateway
        self.processor = PaymentProcessor()
        self.gateway_mock = MagicMock()
        self.processor.gateway = self.gateway_mock

    def test_processPayment_successful(self):
        # Mockowanie poprawnego przetwarzania płatności
        self.gateway_mock.charge.return_value = TransactionResult(True, "tx123", "Payment processed successfully")

        result = self.processor.processPayment("user123", 100.0)

        self.assertTrue(result.success)
        self.assertEqual(result.transactionId, "tx123")
        self.assertEqual(result.message, "Payment processed successfully")
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_insufficient_funds(self):
        # Mockowanie niepowodzenia płatności
        self.gateway_mock.charge.side_effect = PaymentException("Insufficient funds")

        result = self.processor.processPayment("user123", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Insufficient funds", result.message)
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_network_error(self):
        # Mockowanie wyjątku NetworkException
        self.gateway_mock.charge.side_effect = NetworkException("Network error")

        result = self.processor.processPayment("user123", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Network error", result.message)
        self.gateway_mock.charge.assert_called_once_with("user123", 100.0)

    def test_processPayment_invalid_input(self):
        # Test dla nieprawidłowych danych wejściowych
        result = self.processor.processPayment("", 100.0)
        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Invalid payment details", result.message)

        result = self.processor.processPayment("user123", -50.0)
        self.assertFalse(result.success)
        self.assertEqual(result.transactionId, "")
        self.assertIn("Invalid payment details", result.message)


if __name__ == "__main__":
    unittest.main()
