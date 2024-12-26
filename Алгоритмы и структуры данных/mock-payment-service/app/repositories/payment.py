from typing import List, Optional
from app.models.payment import Payment

class PaymentRepository:
    def __init__(self):
        self._payments = []

    def create(self, payment: Payment) -> Payment:
        payment.id = len(self._payments) + 1
        self._payments.append(payment)
        return payment

    def get_by_id(self, payment_id: int) -> Optional[Payment]:
        return next((p for p in self._payments if p.id == payment_id), None)

    def list(self) -> List[Payment]:
        return self._payments
