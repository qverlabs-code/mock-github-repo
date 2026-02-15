"""
Flask API routes – NO @login_required decorators.
Triggers: Agent 3 (Flask route detection, missing auth – CRITICAL/HIGH).
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# ──── CRITICAL: Sensitive PII endpoints WITHOUT @login_required ────

# VIOLATION: Returns aadhaar, pan without auth (CRITICAL)
@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = db.get_customer(customer_id)
    return jsonify({
        'full_name': customer.full_name,
        'aadhaar_number': customer.aadhaar_number,
        'pan_card': customer.pan_card,
        'email': customer.email,
        'phone': customer.phone,
        'bank_account': customer.bank_account,
    })


# VIOLATION: Bulk export with PII – no auth (CRITICAL)
@app.route('/api/customers/export', methods=['GET'])
def export_customers():
    customers = db.get_all_customers()
    return jsonify([{
        'name': c.full_name,
        'aadhaar_number': c.aadhaar_number,
        'pan_card': c.pan_card,
        'passport': c.passport,
        'credit_card': c.credit_card,
    } for c in customers])


# VIOLATION: Financial data endpoint – no auth (CRITICAL)
@app.route('/api/customers/<int:customer_id>/financial', methods=['GET'])
def get_financial_data(customer_id):
    data = db.get_financial(customer_id)
    return jsonify({
        'bank_account': data.bank_account,
        'ifsc': data.ifsc,
        'credit_card': data.credit_card,
        'upi_id': data.upi_id,
        'gstin': data.gstin,
    })


# VIOLATION: KYC documents – no auth (CRITICAL)
@app.get('/api/customers/<int:customer_id>/kyc')
def get_kyc(customer_id):
    kyc = db.get_kyc(customer_id)
    return jsonify({
        'passport': kyc.passport,
        'voter_id': kyc.voter_id,
        'driving_license': kyc.driving_license,
        'aadhaar_number': kyc.aadhaar_number,
    })


# VIOLATION: Search by PII – no auth (HIGH)
@app.post('/api/customers/search')
def search_customers():
    email = request.json.get('email')
    mobile = request.json.get('mobile')
    results = db.search(email=email, mobile=mobile)
    return jsonify(results)


# VIOLATION: Employee PII – no auth (CRITICAL)
@app.route('/api/employees', methods=['GET'])
def list_employees():
    employees = db.get_all_employees()
    return jsonify([{
        'name': e.employee_name,
        'aadhaar_number': e.aadhaar_number,
        'pan_number': e.pan_number,
        'epf_uan': e.epf_uan,
        'esic': e.esic,
        'bank_account': e.bank_account,
    } for e in employees])


# VIOLATION: Payroll with bank details – no auth (CRITICAL)
@app.route('/api/employees/<int:emp_id>/payroll', methods=['GET'])
def get_payroll(emp_id):
    payroll = db.get_payroll(emp_id)
    return jsonify({
        'pan_number': payroll.pan_number,
        'epf_uan': payroll.epf_uan,
        'esic': payroll.esic,
        'bank_account': payroll.bank_account,
        'net_salary': str(payroll.net_salary),
    })


# ──── LOW: No auth, but no PII in handler ────

@app.route('/api/status', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})


@app.route('/api/products', methods=['GET'])
def list_products():
    products = db.get_products()
    return jsonify(products)
