"""
Customer service layer – contains PII-in-logs violations.
Triggers: Agent 1 (PII-in-Logs detection – CRITICAL + HIGH findings).
"""

import logging
from backend.models.customer import Customer, CustomerKYC, CustomerFinancial

logger = logging.getLogger(__name__)


def create_customer(data: dict) -> Customer:
    """Create a new customer record."""
    # VIOLATION: Logging Aadhaar number (CRITICAL - highly sensitive PII in logs)
    logger.info(f"Creating customer with Aadhaar: {data['aadhaar_number']}")

    customer = Customer(**data)

    # VIOLATION: Logging PAN card (CRITICAL)
    logging.info(f"Customer created - PAN: {customer.pan_card}, Name: {customer.full_name}")

    return customer


def verify_kyc(customer_id: int, documents: dict):
    """Verify customer KYC documents."""
    # VIOLATION: Logging passport number (CRITICAL)
    logger.info(f"KYC verification started for passport {documents.get('passport')}")

    # VIOLATION: Logging credit card (CRITICAL)
    logger.warning(f"Payment method on file: card {documents.get('credit_card')}")

    # VIOLATION: Logging bank account (CRITICAL)
    logging.debug(f"Bank account {documents.get('bank_account')} linked to IFSC {documents.get('ifsc')}")

    # VIOLATION: Logging voter ID (HIGH)
    logger.info(f"Voter ID verified: {documents.get('voter_id')}")

    # VIOLATION: Logging driving license (HIGH)
    logger.info(f"DL verification for {documents.get('driving_license')}")

    return True


def search_customer(query: str):
    """Search customers by various identifiers."""
    # VIOLATION: Logging email (HIGH)
    logger.info(f"Searching for customer with email: {query}")

    # VIOLATION: Logging mobile number (HIGH)
    logging.info(f"SMS notification sent to mobile {query}")

    # VIOLATION: Logging UPI ID (HIGH)
    logger.debug(f"UPI payment initiated for {query}")

    return []


def process_payment(customer_id: int, payment_data: dict):
    """Process a payment transaction."""
    # VIOLATION: Using print() with PII (catches print() calls too)
    print(f"Processing payment for customer {customer_id}")
    print(f"Card: {payment_data['credit_card']}, Amount: {payment_data['amount']}")

    # VIOLATION: Logging GSTIN (HIGH)
    logger.info(f"Tax invoice generated for GSTIN: {payment_data.get('gstin')}")

    # VIOLATION: Logging EPF UAN (HIGH)
    logging.info(f"Salary credited to EPF UAN: {payment_data.get('epf_uan')}")

    # VIOLATION: Logging ESIC (HIGH)
    logger.debug(f"ESIC contribution for {payment_data.get('esic')}")


def handle_error(customer_id: int, error: Exception):
    """Error handler that leaks PII in error logs."""
    # VIOLATION: Logging Aadhaar in error context (CRITICAL)
    logger.error(f"Error processing customer {customer_id}, Aadhaar: 234567890123")

    # VIOLATION: Logging PAN in exception (CRITICAL)
    logging.exception(f"Payment failed for PAN ABCDE1234F: {error}")

    # VIOLATION: Logging credit card in error (CRITICAL)
    logger.critical(f"Transaction failed for card 4111111111111111")


def export_customer_data(customer_id: int):
    """Export customer data – logs everything."""
    # VIOLATION: Multiple PII types in a single log line
    logger.info(
        f"Exporting data: aadhaar_number=234567890123, "
        f"pan_card=ABCDE1234F, mobile=+919876543210, "
        f"email=test@example.com, bank_account=12345678901234"
    )

    # VIOLATION: Logging ration_card (HIGH)
    logger.debug(f"Ration card on file: MH123456789012")

    # VIOLATION: Logging EPIC number (HIGH)
    logger.info(f"EPIC verified: ABC1234567")
