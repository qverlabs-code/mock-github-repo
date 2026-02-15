/**
 * Next.js App Router – Payment endpoint without auth.
 * Triggers: Agent 3 (CRITICAL – credit_card, bank_account, upi_id).
 */

import { NextRequest, NextResponse } from 'next/server';

// VIOLATION: Payment methods without auth (CRITICAL)
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const userId = searchParams.get('userId');

  const methods = await db.query(
    'SELECT * FROM payment_methods WHERE user_id = $1',
    [userId]
  );

  return NextResponse.json({
    credit_card: methods.credit_card,
    debit_card: methods.debit_card,
    bank_account: methods.bank_account,
    ifsc: methods.ifsc,
    upi_id: methods.upi_id,
  });
}

// VIOLATION: Process payment without auth (CRITICAL)
export async function POST(request: NextRequest) {
  const body = await request.json();

  const result = await paymentService.process({
    credit_card: body.credit_card,
    bank_account: body.bank_account,
    upi_id: body.upi_id,
    amount: body.amount,
    gstin: body.gstin,
  });

  return NextResponse.json(result);
}
