/**
 * Next.js App Router – KYC endpoint without auth.
 * Triggers: Agent 3 (CRITICAL – passport, voter_id, driving_license).
 */

import { NextRequest, NextResponse } from 'next/server';

// VIOLATION: KYC data without NextAuth session (CRITICAL)
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const customerId = searchParams.get('customerId');

  const kyc = await db.query(
    'SELECT * FROM customer_kyc WHERE customer_id = $1',
    [customerId]
  );

  return NextResponse.json({
    passport: kyc.passport,
    voter_id: kyc.voter_id,
    driving_license: kyc.driving_license,
    aadhaar_number: kyc.aadhaar_number,
    pan_card: kyc.pan_card,
    epic: kyc.epic,
  });
}

// VIOLATION: Submit KYC documents without auth (CRITICAL)
export async function POST(request: NextRequest) {
  const body = await request.json();

  const result = await db.query(
    `INSERT INTO customer_kyc (customer_id, passport, voter_id, driving_license, aadhaar_number)
     VALUES ($1, $2, $3, $4, $5)`,
    [body.customer_id, body.passport, body.voter_id, body.driving_license, body.aadhaar_number]
  );

  return NextResponse.json({ success: true }, { status: 201 });
}
