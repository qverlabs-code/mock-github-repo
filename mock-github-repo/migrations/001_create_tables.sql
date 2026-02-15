-- Migration file with hardcoded PII in seed inserts.
-- Agent 2 categorizes as 'migration' file.

CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(200) NOT NULL,
    email VARCHAR(200),
    phone VARCHAR(20),
    aadhaar_number VARCHAR(12),
    pan_card VARCHAR(10),
    passport VARCHAR(10),
    voter_id VARCHAR(10),
    driving_license VARCHAR(20),
    upi_id VARCHAR(100),
    bank_account VARCHAR(20),
    ifsc VARCHAR(11),
    credit_card VARCHAR(20),
    gstin VARCHAR(15),
    epf_uan VARCHAR(12),
    esic VARCHAR(17),
    epic VARCHAR(10),
    ration_card VARCHAR(15),
    pin_code VARCHAR(6),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- VIOLATION (Agent 2): Hardcoded PII in INSERT statements
INSERT INTO customers (full_name, email, phone, aadhaar_number, pan_card, passport, bank_account, credit_card)
VALUES
    ('Rajesh Kumar', 'rajesh@example.com', '+919876543210', '298765432109', 'ABCPF1234A', 'A1234567', '50100012345678', '4532015112830366'),
    ('Priya Sharma', 'priya@example.com', '+919123456789', '345678901234', 'BCDPG5678B', 'B2345678', '60200023456789', '5212345678901234'),
    ('Amit Patel', 'amit@example.com', '+918765432109', '456789012345', 'CDEQH9012C', 'C3456789', '70300034567890', '371234567890123');

-- Admin user with credentials
-- VIOLATION: Hardcoded password
INSERT INTO users (email, password_hash, role)
VALUES ('admin@company.com', 'pbkdf2:sha256:AdminP@ss2024!', 'superadmin');
