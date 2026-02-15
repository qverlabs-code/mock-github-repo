"""
Notification service – more PII-in-logs violations.
Also contains hardcoded PII values (Agent 2).
"""

import logging

logger = logging.getLogger(__name__)

# VIOLATION (Agent 2): Hardcoded Aadhaar number (CRITICAL)
DEFAULT_TEST_AADHAAR = "298765432109"

# VIOLATION (Agent 2): Hardcoded PAN (CRITICAL)
ADMIN_PAN = "ABCPF1234A"

# VIOLATION (Agent 2): Hardcoded mobile number (HIGH)
SUPPORT_HOTLINE = "+919876543210"

# VIOLATION (Agent 2): Hardcoded email (HIGH)
NOTIFICATION_FROM = "noreply@company.com"

# VIOLATION (Agent 2): Hardcoded credit card for testing (CRITICAL)
TEST_CARD_NUMBER = "4532015112830366"

# VIOLATION (Agent 2): Hardcoded bank account (CRITICAL)
REFUND_ACCOUNT = "50100012345678"

# VIOLATION (Agent 2): Hardcoded UPI ID (HIGH)
COLLECTION_UPI = "business@oksbi"

# VIOLATION (Agent 2): Hardcoded GSTIN (HIGH)
COMPANY_GSTIN = "27AABCU9603R1ZP"

# VIOLATION (Agent 2): Hardcoded IFSC (HIGH)
PRIMARY_IFSC = "SBIN0001234"

# VIOLATION (Agent 2): Hardcoded passport (CRITICAL)
TEST_PASSPORT = "A1234567"

# VIOLATION (Agent 2): Hardcoded voter ID (HIGH)
TEST_VOTER_ID = "ABC1234567"

# VIOLATION (Agent 2): Hardcoded driving license (HIGH)
TEST_DL = "MH-0220140123456"

# VIOLATION (Agent 2): Hardcoded EPF UAN (HIGH)
TEST_EPF_UAN = "100123456789"

# VIOLATION (Agent 2): Hardcoded ESIC (HIGH)
TEST_ESIC = "12345678901234567"


def send_sms(phone: str, message: str):
    """Send SMS notification."""
    # VIOLATION (Agent 1): PII field name 'phone' in log
    logger.info(f"Sending SMS to phone: {phone}, message: {message[:50]}")

    # VIOLATION (Agent 1): Hardcoded mobile in log
    logging.debug(f"Fallback SMS to +919876543210 if primary fails")

    return True


def send_kyc_reminder(customer_data: dict):
    """Send KYC reminder – logs multiple PII types."""
    # VIOLATION (Agent 1): Logging aadhaar_number field (CRITICAL)
    logger.info(f"KYC reminder for aadhaar_number: {customer_data.get('aadhaar_number')}")

    # VIOLATION (Agent 1): Logging pan_card field (CRITICAL)
    logger.info(f"PAN verification pending for pan_card: {customer_data.get('pan_card')}")

    # VIOLATION (Agent 1): Logging email field (HIGH)
    logger.info(f"Email reminder sent to email: {customer_data.get('email')}")


def send_payment_confirmation(payment: dict):
    """Payment confirmation – leaks financial PII in logs."""
    # VIOLATION: Logging credit_card field (CRITICAL)
    logger.info(f"Payment confirmed, credit_card ending {payment.get('credit_card', '')[-4:]}")

    # But even the last 4 digits references the field name, which the scanner catches
    # VIOLATION: Logging bank_account field (CRITICAL)
    logging.info(f"Funds debited from bank_account: {payment.get('bank_account')}")

    # VIOLATION: Logging upi_id field (HIGH)
    logger.debug(f"UPI txn completed for upi_id: {payment.get('upi_id')}")
