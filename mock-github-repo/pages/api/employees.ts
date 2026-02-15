/**
 * Next.js Pages API – Employee endpoint without auth.
 * Triggers: Agent 3 (CRITICAL – aadhaar, pan, bank_account, epf_uan).
 */

import type { NextApiRequest, NextApiResponse } from 'next';

// VIOLATION: No getServerSession / NextAuth check (CRITICAL)
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === 'GET') {
    const employees = await db.query('SELECT * FROM hr_employees');
    return res.status(200).json(employees.map((e: any) => ({
      employee_name: e.employee_name,
      aadhaar_number: e.aadhaar_number,
      pan_number: e.pan_number,
      epf_uan: e.epf_uan,
      esic: e.esic,
      bank_account: e.bank_account,
      ifsc: e.ifsc,
      credit_card: e.credit_card,
    })));
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
