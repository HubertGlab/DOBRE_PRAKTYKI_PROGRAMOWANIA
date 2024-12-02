from enum import Enum
import random


class NetworkException(Exception):
    pass


class PaymentException(Exception):
    pass


class RefundException(Exception):
    pass


class TransactionResult:
    def __init__(self, success, transactionId, message=""):
        self.success = success
        self.transactionId = transactionId
        self.message = message


class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PaymentGateway:
    def charge(self, userId: str, amount: float):
        if not isinstance(userId, str) or not userId:
            raise PaymentException("Invalid user ID")
        if not isinstance(amount, (float)) or amount <= 0:
            raise PaymentException("Invalid amount")
        if random.choice([True, False]):
            raise NetworkException("Network error during charge")
        if random.choice([True, False]):
            raise PaymentException("Payment processing failed")

        return TransactionResult(True, "charge_tx123", "Charge successful")

    def refund(self, transactionId):
        if not isinstance(transactionId, str) or not transactionId:
            raise RefundException("Invalid transaction ID")

        if random.choice([True, False]):
            raise NetworkException("Network error during refund")
        if random.choice([True, False]):
            raise RefundException("Refund processing failed")

        return TransactionResult(True, transactionId, "Refund successful")

    def getStatus(self, transactionId):
        if not isinstance(transactionId, str) or not transactionId:
            raise NetworkException("Invalid transaction ID")

        if random.choice([True, False]):
            raise NetworkException("Network error retrieving status")
        return random.choice([TransactionStatus.PENDING, TransactionStatus.COMPLETED, TransactionStatus.FAILED])