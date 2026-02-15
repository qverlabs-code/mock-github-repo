"""
FastAPI routes – NO auth dependencies.
Triggers: Agent 3 (FastAPI decorator detection).
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class CustomerResponse(BaseModel):
    full_name: str
    aadhaar_number: str
    pan_card: str
    email: str
    mobile: str


class PaymentRequest(BaseModel):
    credit_card: str
    bank_account: str
    upi_id: str
    amount: float


# VIOLATION: Returns aadhaar + PAN without auth dependency (CRITICAL)
@app.get('/api/v2/customers/{customer_id}')
async def get_customer(customer_id: int):
    customer = await db.get_customer(customer_id)
    return {
        'full_name': customer.full_name,
        'aadhaar_number': customer.aadhaar_number,
        'pan_card': customer.pan_card,
        'email': customer.email,
        'passport': customer.passport,
        'credit_card': customer.credit_card,
    }


# VIOLATION: Bulk PII export without auth (CRITICAL)
@app.get('/api/v2/customers/export')
async def export_all_customers():
    customers = await db.get_all()
    return [{
        'name': c.full_name,
        'aadhaar_number': c.aadhaar_number,
        'bank_account': c.bank_account,
        'pan_card': c.pan_card,
    } for c in customers]


# VIOLATION: Accepts credit card + bank account without auth (CRITICAL)
@app.post('/api/v2/payments/process')
async def process_payment(payment: PaymentRequest):
    result = await payment_service.charge(
        credit_card=payment.credit_card,
        bank_account=payment.bank_account,
        upi_id=payment.upi_id,
    )
    return result


# VIOLATION: KYC data without auth (CRITICAL)
@app.get('/api/v2/customers/{customer_id}/kyc')
async def get_kyc_details(customer_id: int):
    kyc = await db.get_kyc(customer_id)
    return {
        'passport': kyc.passport,
        'voter_id': kyc.voter_id,
        'driving_license': kyc.driving_license,
        'aadhaar_number': kyc.aadhaar_number,
    }


# VIOLATION: Employee PII without auth (CRITICAL)
@app.get('/api/v2/employees/{emp_id}')
async def get_employee(emp_id: int):
    emp = await db.get_employee(emp_id)
    return {
        'aadhaar_number': emp.aadhaar_number,
        'pan_number': emp.pan_number,
        'epf_uan': emp.epf_uan,
        'esic': emp.esic,
        'bank_account': emp.bank_account,
    }


# VIOLATION: Returns PII, no consent middleware (MEDIUM with auth)
@app.get('/api/v2/customers/{customer_id}/profile')
async def get_profile(customer_id: int, token: str = Depends(verify_token)):
    # Has auth (Depends) but no consent check
    customer = await db.get_customer(customer_id)
    return {
        'full_name': customer.full_name,
        'email': customer.email,
        'aadhaar_number': customer.aadhaar_number,
    }


# LOW: No auth, no PII
@app.get('/api/v2/health')
async def health():
    return {'status': 'ok'}
