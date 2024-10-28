from interface import TransactionResult
from interface import TransactionStatus

class PaymentProcessor:

    def processPayment(self, userId: str, amount: float):
        if isinstance(userId, str) and userId and isinstance(amount, (int, float)) and amount > 0:
            return TransactionResult(True, "tx123", "Payment processed successfully")
        else:
            return TransactionResult(False, "", "Invalid payment details")

    def refundPayment(self, transactionId: str):
        if isinstance(transactionId, str) and transactionId:
            return TransactionResult(True, transactionId, "Refund processed successfully")
        else:
            return TransactionResult(False, "", "Invalid transaction ID")

    def getPaymentStatus(self, transactionId: str):
        if isinstance(transactionId, str) and transactionId:
            return TransactionStatus.PENDING
        else:
            return TransactionStatus.FAILED
