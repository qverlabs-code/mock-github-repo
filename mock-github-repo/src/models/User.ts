/**
 * User model interfaces and types.
 * Triggers: Agent 1 (PII model field discovery via TS interfaces).
 */

export interface User {
  id: number;
  full_name: string;
  email: string;
  phone: string;
  mobile: string;
  aadhaar_number: string;
  pan_card: string;
  date_of_birth: string;
  father_name: string;
  mother_name: string;
  address: string;
  pin_code: string;
  upi_id: string;
  passport: string;
  voter_id: string;
  driving_license: string;
  credit_card: string;
  bank_account: string;
  ifsc: string;
  gstin: string;
  epf_uan: string;
  esic: string;
  epic: string;
  ration_card: string;
  created_at: Date;
  updated_at: Date;
}

export type UserKYCStatus = 'pending' | 'verified' | 'rejected';

export interface KYCDocument {
  id: number;
  user_id: number;
  document_type: string;
  document_number: string;
  passport: string;
  voter_id: string;
  driving_license: string;
  aadhaar_number: string;
  pan_card: string;
  verification_status: UserKYCStatus;
}

export interface PaymentMethod {
  id: number;
  user_id: number;
  credit_card: string;
  debit_card: string;
  card_holder_name: string;
  upi_id: string;
  bank_account: string;
  ifsc: string;
  is_default: boolean;
}

export interface EmployeeRecord extends User {
  employee_id: string;
  department: string;
  designation: string;
  epf_uan: string;
  esic: string;
  bank_account: string;
  pan_number: string;
}
