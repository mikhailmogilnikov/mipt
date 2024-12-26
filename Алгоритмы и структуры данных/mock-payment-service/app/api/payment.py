from fastapi import APIRouter, HTTPException
from app.schemas.payment import PaymentCreate, PaymentResponse

router = APIRouter()

payments = []

@router.post("/", response_model=PaymentResponse, status_code=201)
async def create_payment(payment: PaymentCreate):
    """
    New payment creation.
    """
    new_payment = {
        "id": len(payments) + 1,
        **payment.dict()
    }
    payments.append(new_payment)
    return new_payment

@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: int):
    """
    Get payment by ID.
    """
    for payment in payments:
        if payment["id"] == payment_id:
            return payment
    raise HTTPException(status_code=404, detail="Payment not found")
