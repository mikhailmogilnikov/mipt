from app.models.payment import Payment
from app.repositories.payment import PaymentRepository

class PaymentService:
    def __init__(self, repository: PaymentRepository):
        self._repository = repository

    def create_payment(self, payment_data: dict) -> Payment:
        payment = Payment(**payment_data)
        return self._repository.create(payment)

    def get_payment(self, payment_id: int) -> Payment:
        payment = self._repository.get_by_id(payment_id)
        if not payment:
            raise ValueError("Payment not found")
        return payment
