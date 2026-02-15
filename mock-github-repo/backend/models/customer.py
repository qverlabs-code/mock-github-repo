"""
Customer ORM models – Indian enterprise CRM system.
Triggers: Agent 1 (PII model field discovery), Agent 2 (hardcoded PII).
"""

from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    """Core customer model with extensive PII fields."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True)
    phone = Column(String(20))
    mobile = Column(String(20))
    aadhaar_number = Column(String(12))
    pan_card = Column(String(10))
    date_of_birth = Column(Date)
    father_name = Column(String(200))
    mother_name = Column(String(200))
    address = Column(Text)
    pin_code = Column(String(6))
    city = Column(String(100))
    state = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class CustomerKYC(Base):
    """KYC documents – passport, voter ID, driving license."""
    __tablename__ = 'customer_kyc'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    passport = Column(String(10))
    voter_id = Column(String(10))
    driving_license = Column(String(20))
    ration_card = Column(String(15))
    epic = Column(String(10))
    verification_status = Column(String(20))


class CustomerFinancial(Base):
    """Financial details – bank, cards, UPI."""
    __tablename__ = 'customer_financial'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    bank_account = Column(String(20))
    ifsc = Column(String(11))
    credit_card = Column(String(20))
    debit_card = Column(String(20))
    upi_id = Column(String(100))
    gstin = Column(String(15))
    epf_uan = Column(String(12))
    esic = Column(String(17))
