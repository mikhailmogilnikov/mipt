from app.services.payment_service import PaymentService
from app.repositories.payment import PaymentRepository

def test_create_payment():
    repo = PaymentRepository()
    service = PaymentService(repo)

    payment_data = {"amount": 100, "currency": "USD"}
    payment = service.create_payment(payment_data)

    assert payment.id == 1
    assert payment.amount == 100
    assert payment.currency == "USD"
