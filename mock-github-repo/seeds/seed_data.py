"""
Seed data script with hardcoded PII values.
Agent 2 categorizes as 'seed' file (+0.1 confidence boost).
"""

import psycopg2

# VIOLATION (Agent 2): Database URL (CRITICAL)
DATABASE_URL = "postgresql://admin:SeedPass123@localhost:5432/enterprise"

# VIOLATION (Agent 2): Hardcoded PII values in seed data (CRITICAL for sensitive types)

SEED_CUSTOMERS = [
    {
        'name': 'Vikram Singh',
        'aadhaar': '298765432109',       # CRITICAL: Hardcoded Aadhaar
        'pan': 'ABCPS1234A',              # CRITICAL: Hardcoded PAN
        'email': 'vikram@example.com',     # HIGH: Hardcoded email
        'mobile': '+919876543210',         # HIGH: Hardcoded mobile
        'passport': 'A1234567',            # CRITICAL: Hardcoded passport
        'credit_card': '4532015112830366', # CRITICAL: Hardcoded credit card
        'bank_account': '50100012345678',  # CRITICAL: Hardcoded bank account
        'voter_id': 'ABC1234567',          # HIGH: Hardcoded voter ID
        'driving_license': 'MH-0220140123456',  # HIGH: Hardcoded DL
        'upi_id': 'vikram@oksbi',          # HIGH: Hardcoded UPI
        'gstin': '27ABCPS1234A1ZP',        # HIGH: Hardcoded GSTIN
        'ifsc': 'SBIN0001234',             # HIGH: Hardcoded IFSC
        'epf_uan': '100123456789',          # HIGH: Hardcoded EPF UAN
        'esic': '12345678901234567',        # HIGH: Hardcoded ESIC
        'epic': 'DEF2345678',              # HIGH: Hardcoded EPIC
        'ration_card': 'MH1234567890',     # HIGH: Hardcoded ration card
        'pin_code': '400001',              # Can match pin_code pattern
    },
    {
        'name': 'Neha Gupta',
        'aadhaar': '345678901234',
        'pan': 'BCDPG5678B',
        'email': 'neha@example.com',
        'mobile': '+918765432109',
        'passport': 'B2345678',
        'credit_card': '5212345678901234',
        'bank_account': '60200023456789',
    },
]

# VIOLATION: Hardcoded employee PII in seed script
SEED_EMPLOYEES = [
    {
        'name': 'Suresh Reddy',
        'aadhaar_number': '456789012345',
        'pan_number': 'CDEQH9012C',
        'bank_account': '70300034567890',
        'ifsc': 'HDFC0001234',
        'epf_uan': '100234567890',
        'esic': '23456789012345678',
        'credit_card': '371234567890123',
    },
]

# VIOLATION: AWS credentials in seed script (CRITICAL)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def seed_database():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    for customer in SEED_CUSTOMERS:
        # VIOLATION (Agent 1): Logging PII during seeding
        print(f"Seeding customer: {customer['name']}, Aadhaar: {customer['aadhaar']}")

        cur.execute("""
            INSERT INTO customers (name, aadhaar_number, pan_card, email, mobile)
            VALUES (%s, %s, %s, %s, %s)
        """, (customer['name'], customer['aadhaar'], customer['pan'],
              customer['email'], customer['mobile']))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    seed_database()
