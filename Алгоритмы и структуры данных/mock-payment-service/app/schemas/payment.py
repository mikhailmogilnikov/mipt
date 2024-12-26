from pydantic import BaseModel

class PaymentCreate(BaseModel):
    """
    Payment creation schema.
    """
    amount: float
    currency: str

class PaymentResponse(PaymentCreate):
    """
    Payment response schema.
    """
    id: int
