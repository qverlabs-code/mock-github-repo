/**
 * Next.js Pages API route – NO session check.
 * Triggers: Agent 3 (Next.js Pages API detection – 'export default function').
 */

import type { NextApiRequest, NextApiResponse } from 'next';

// VIOLATION: Pages API route without getSession/NextAuth (CRITICAL)
// Detected as method 'ALL' – handles any HTTP method
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === 'GET') {
    const customers = await db.query('SELECT * FROM customers');
    // Handler references PII fields
    const response = customers.map((c: any) => ({
      full_name: c.full_name,
      aadhaar_number: c.aadhaar_number,
      pan_card: c.pan_card,
      email: c.email,
      mobile: c.mobile,
      passport: c.passport,
      credit_card: c.credit_card,
      bank_account: c.bank_account,
    }));
    return res.status(200).json(response);
  }

  if (req.method === 'POST') {
    const { aadhaar_number, pan_card, email, mobile, bank_account } = req.body;
    const customer = await db.query(
      'INSERT INTO customers (aadhaar_number, pan_card, email, mobile, bank_account) VALUES ($1, $2, $3, $4, $5)',
      [aadhaar_number, pan_card, email, mobile, bank_account]
    );
    return res.status(201).json(customer);
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
