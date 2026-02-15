/**
 * Express user routes – NO authentication middleware.
 * Triggers: Agent 3 (API endpoint scan – CRITICAL/HIGH for unprotected PII endpoints).
 */

import express from 'express';

const router = express.Router();

// ──── CRITICAL: Sensitive PII endpoint WITHOUT auth ────

// VIOLATION: Returns aadhaar, pan, bank_account – no auth middleware (CRITICAL)
router.get('/api/users/:id', async (req, res) => {
  const user = await db.query('SELECT * FROM customers WHERE id = $1', [req.params.id]);
  // Handler references PII fields:
  const response = {
    name: user.full_name,
    aadhaar_number: user.aadhaar_number,
    pan_card: user.pan_card,
    bank_account: user.bank_account,
    credit_card: user.credit_card,
    passport: user.passport,
  };
  res.json(response);
});

// VIOLATION: Returns financial PII – no auth (CRITICAL)
router.get('/api/users/:id/financial', async (req, res) => {
  const data = await db.query('SELECT * FROM customer_financial WHERE customer_id = $1', [req.params.id]);
  res.json({
    bank_account: data.bank_account,
    ifsc: data.ifsc,
    credit_card: data.credit_card,
    upi_id: data.upi_id,
    gstin: data.gstin,
  });
});

// VIOLATION: KYC endpoint – sensitive docs without auth (CRITICAL)
router.get('/api/users/:id/kyc', async (req, res) => {
  const kyc = await db.query('SELECT * FROM customer_kyc WHERE customer_id = $1', [req.params.id]);
  res.json({
    passport: kyc.passport,
    voter_id: kyc.voter_id,
    driving_license: kyc.driving_license,
    aadhaar_number: kyc.aadhaar_number,
  });
});

// VIOLATION: Bulk user export – no auth, returns PII (CRITICAL)
router.get('/api/users/export', async (req, res) => {
  const users = await db.query('SELECT full_name, email, phone, aadhaar_number, pan_card FROM customers');
  res.json(users);
});

// VIOLATION: Search endpoint – no auth, handles email + mobile (HIGH)
router.post('/api/users/search', async (req, res) => {
  const { email, mobile, pin_code } = req.body;
  const results = await db.query(
    'SELECT * FROM customers WHERE email = $1 OR mobile = $2',
    [email, mobile]
  );
  res.json(results);
});

// ──── MEDIUM: Has auth but NO consent verification ────

// VIOLATION: Auth present but no consent check (MEDIUM)
router.get('/api/users/:id/profile', requireAuth, async (req, res) => {
  const user = await db.query('SELECT * FROM customers WHERE id = $1', [req.params.id]);
  // Returns PII without consent verification
  res.json({
    full_name: user.full_name,
    email: user.email,
    phone: user.phone,
    aadhaar_number: user.aadhaar_number,
    pan_card: user.pan_card,
  });
});

// ──── LOW: No auth but no PII detected ────

// VIOLATION: No auth middleware, but no PII (LOW)
router.get('/api/products', async (req, res) => {
  const products = await db.query('SELECT * FROM products');
  res.json(products);
});

// VIOLATION: No auth on health check (LOW)
router.get('/api/health', (req, res) => {
  res.json({ status: 'ok', uptime: process.uptime() });
});

export default router;
