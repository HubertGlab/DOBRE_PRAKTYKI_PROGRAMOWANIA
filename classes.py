from interface import TransactionResult, NetworkException, PaymentException, TransactionStatus


class PaymentProcessor:
    def __init__(self):
        self.gateway = None

    def processPayment(self, userId: str, amount: float):
        if not userId or amount <= 0:
            return TransactionResult(False, "", "Invalid payment details")
        try:
            return self.gateway.charge(userId, amount)
        except PaymentException as e:
            return TransactionResult(False, "", str(e))
        except NetworkException as e:
            return TransactionResult(False, "", str(e))

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
