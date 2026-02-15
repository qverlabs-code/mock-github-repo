/**
 * User service – contains PII-in-logs violations.
 * Triggers: Agent 1 (console.log / logger calls with PII field names).
 */

import { User, KYCDocument, PaymentMethod } from '../models/User';

const logger = {
  info: (msg: string) => console.log(`[INFO] ${msg}`),
  warn: (msg: string) => console.warn(`[WARN] ${msg}`),
  error: (msg: string) => console.error(`[ERROR] ${msg}`),
  debug: (msg: string) => console.debug(`[DEBUG] ${msg}`),
};

export async function createUser(userData: User): Promise<User> {
  // VIOLATION: Logging aadhaar_number (CRITICAL)
  console.log(`Creating user with aadhaar_number: ${userData.aadhaar_number}`);

  // VIOLATION: Logging pan_card (CRITICAL)
  logger.info(`User PAN verification: pan_card = ${userData.pan_card}`);

  // VIOLATION: Logging email (HIGH)
  console.log(`Welcome email sent to: ${userData.email}`);

  return userData;
}

export async function verifyKYC(userId: number, docs: KYCDocument): Promise<boolean> {
  // VIOLATION: Logging passport (CRITICAL)
  logger.info(`Verifying passport: ${docs.passport} for user ${userId}`);

  // VIOLATION: Logging credit_card (CRITICAL)
  console.log(`Payment verification - credit_card on file: ${docs.aadhaar_number}`);

  // VIOLATION: Logging voter_id (HIGH)
  logger.debug(`Voter ID check: ${docs.voter_id}`);

  // VIOLATION: Logging driving_license (HIGH)
  console.log(`DL verification: ${docs.driving_license}`);

  return true;
}

export async function processPayment(payment: PaymentMethod): Promise<void> {
  // VIOLATION: Logging bank_account (CRITICAL)
  logger.info(`Processing payment from bank_account: ${payment.bank_account}`);

  // VIOLATION: Logging credit_card (CRITICAL)
  console.log(`Charging credit_card: ${payment.credit_card}`);

  // VIOLATION: Logging upi_id (HIGH)
  logger.info(`UPI payment from upi_id: ${payment.upi_id}`);

  // VIOLATION: Logging ifsc (HIGH)
  console.debug(`IFSC code: ${payment.ifsc}`);
}

export async function handleUserError(user: Partial<User>, error: Error): Promise<void> {
  // VIOLATION: Multiple PII fields in error log (CRITICAL)
  logger.error(
    `Error for user: aadhaar_number=${user.aadhaar_number}, ` +
    `pan_card=${user.pan_card}, mobile=${user.mobile}, ` +
    `email=${user.email}, bank_account=${user.bank_account}`
  );

  // VIOLATION: Logging with literal PII values (CRITICAL)
  console.error(`Critical error - Aadhaar: 298765432109, PAN: ABCPF1234A`);
}

export async function exportUserData(userId: number): Promise<void> {
  // VIOLATION: Logging gstin (HIGH)
  logger.info(`Exporting tax data - gstin for user ${userId}`);

  // VIOLATION: Logging epf_uan (HIGH)
  console.log(`EPF data export: epf_uan for employee ${userId}`);

  // VIOLATION: Logging esic (HIGH)
  logger.debug(`ESIC records for esic: ${userId}`);

  // VIOLATION: Logging ration_card (HIGH)
  console.log(`Subsidy verification - ration_card for user ${userId}`);

  // VIOLATION: Logging epic (HIGH)
  logger.info(`Electoral verification - epic number check for ${userId}`);
}
