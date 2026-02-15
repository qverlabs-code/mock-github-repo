/**
 * Express payment routes – mixed auth states.
 * Triggers: Agent 3 (CRITICAL for unprotected financial endpoints).
 */

import express from 'express';

const app = express();

// VIOLATION: Credit card + bank account endpoint without auth (CRITICAL)
app.post('/api/payments/process', async (req, res) => {
  const { credit_card, bank_account, upi_id, amount } = req.body;
  // Process payment with sensitive financial data
  const result = await paymentService.charge({
    credit_card,
    bank_account,
    upi_id,
    amount,
  });
  res.json(result);
});

// VIOLATION: Refund endpoint exposes bank_account without auth (CRITICAL)
app.post('/api/payments/refund', async (req, res) => {
  const { bank_account, ifsc, amount } = req.body;
  const result = await paymentService.refund({ bank_account, ifsc, amount });
  res.json(result);
});

// VIOLATION: Transaction history with card details – no auth (CRITICAL)
app.get('/api/payments/transactions/:userId', async (req, res) => {
  const transactions = await db.query(
    'SELECT credit_card, upi_id, amount, status FROM transactions WHERE user_id = $1',
    [req.params.userId]
  );
  res.json(transactions);
});

// VIOLATION: Invoice with GSTIN – no auth (HIGH)
app.get('/api/payments/invoice/:id', async (req, res) => {
  const invoice = await db.query('SELECT * FROM invoices WHERE id = $1', [req.params.id]);
  res.json({
    invoice_number: invoice.invoice_number,
    gstin: invoice.gstin,
    pan_card: invoice.pan_card,
    total: invoice.total_amount,
  });
});

// VIOLATION: Auth present but no consent check for PII (MEDIUM)
app.get('/api/payments/methods/:userId', verifyToken, async (req, res) => {
  const methods = await db.query(
    'SELECT credit_card, debit_card, upi_id, bank_account FROM payment_methods WHERE user_id = $1',
    [req.params.userId]
  );
  res.json(methods);
});

export default app;
