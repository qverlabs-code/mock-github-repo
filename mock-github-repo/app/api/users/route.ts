/**
 * Next.js App Router API – NO getServerSession / NextAuth.
 * Triggers: Agent 3 (Next.js App Router detection).
 * Route path extracted from file path: /api/users
 */

import { NextRequest, NextResponse } from 'next/server';

// VIOLATION: Next.js App Router GET without getServerSession/NextAuth (CRITICAL)
// Handler references: aadhaar_number, pan_card, bank_account, credit_card
export async function GET(request: NextRequest) {
  const users = await db.query('SELECT * FROM customers');

  const response = users.map((user: any) => ({
    id: user.id,
    full_name: user.full_name,
    aadhaar_number: user.aadhaar_number,
    pan_card: user.pan_card,
    email: user.email,
    phone: user.phone,
    bank_account: user.bank_account,
    credit_card: user.credit_card,
  }));

  return NextResponse.json(response);
}

// VIOLATION: POST without auth – creates user with PII (CRITICAL)
export async function POST(request: NextRequest) {
  const body = await request.json();

  const user = await db.query(
    `INSERT INTO customers (full_name, aadhaar_number, pan_card, email, phone, bank_account)
     VALUES ($1, $2, $3, $4, $5, $6) RETURNING *`,
    [body.full_name, body.aadhaar_number, body.pan_card, body.email, body.phone, body.bank_account]
  );

  return NextResponse.json(user, { status: 201 });
}
