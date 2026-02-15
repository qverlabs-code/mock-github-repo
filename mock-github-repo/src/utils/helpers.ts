/**
 * Utility helpers – contains hardcoded PII and secrets.
 * Triggers: Agent 2 (hardcoded PII + secrets + high entropy strings).
 */

// VIOLATION (Agent 2): Hardcoded Aadhaar in utility code (CRITICAL)
export const DEFAULT_AADHAAR = "298765432109";

// VIOLATION (Agent 2): Hardcoded PAN (CRITICAL)
export const COMPANY_PAN = "AAACB1234F";

// VIOLATION (Agent 2): Hardcoded credit card for testing (CRITICAL)
export const TEST_VISA = "4532015112830366";
export const TEST_MASTERCARD = "5212345678901234";
export const TEST_AMEX = "371234567890123";

// VIOLATION (Agent 2): Hardcoded bank account (CRITICAL)
export const ESCROW_ACCOUNT = "50100012345678";

// VIOLATION (Agent 2): Generic API key (HIGH)
const api_key = "sk_live_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnop";

// VIOLATION (Agent 2): High entropy string with 'secret' keyword
// Shannon entropy > 4.5 + 'secret' keyword → high_entropy_string detection
const webhook_secret = "aB3cD4eF5gH6iJ7kL8mN9oP0qR1sT2uV3wX4yZ5aB6cD7eF8gH9i";

// VIOLATION (Agent 2): Bearer token (HIGH)
const bearer_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U";

// VIOLATION (Agent 2): High entropy string with 'credential' keyword
const credential = "x8K2mP4nQ6rS8tU0vW2xY4zA6bC8dE0fG2hI4jK6lM8nO0pQ2r";

// VIOLATION (Agent 2): Password in code (HIGH)
const adminPassword = "Str0ng_Admin_P@ssw0rd_2024!";

// Formatting helpers
export function formatAadhaar(aadhaar: string): string {
  // VIOLATION: Log with PII field reference
  console.log(`Formatting aadhaar: ${aadhaar}`);
  return `${aadhaar.slice(0, 4)} ${aadhaar.slice(4, 8)} ${aadhaar.slice(8)}`;
}

export function maskPAN(pan_card: string): string {
  console.log(`Masking pan_card: ${pan_card}`);
  return `${pan_card.slice(0, 2)}****${pan_card.slice(-2)}`;
}

export function maskCreditCard(credit_card: string): string {
  console.log(`Masking credit_card: ${credit_card}`);
  return `****-****-****-${credit_card.slice(-4)}`;
}

export function validateMobile(mobile: string): boolean {
  console.log(`Validating mobile: ${mobile}`);
  return /^\+91[6-9]\d{9}$/.test(mobile);
}
