from fastapi import FastAPI
from app.api import payment

app = FastAPI(
  title="Mock Payment Service",
  description="Mock Payment API",
  version="1.0.0",
  openapi_tags=[
    {"name": "Payments", "description": "Endpoints for working with payments"}
  ]
)

app.include_router(payment.router, prefix="/payments", tags=["Payments"])