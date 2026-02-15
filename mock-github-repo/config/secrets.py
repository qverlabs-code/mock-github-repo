"""
Application secrets – hardcoded credentials.
Triggers: Agent 2 (all secret pattern types).
"""

# VIOLATION (Agent 2): AWS Access Key (CRITICAL – aws_access_key pattern)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

# VIOLATION (Agent 2): AWS Secret Key (CRITICAL – aws_secret_key pattern)
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# VIOLATION (Agent 2): GitHub Personal Access Token (HIGH – github_token pattern)
GITHUB_TOKEN = "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij"

# VIOLATION (Agent 2): Generic API key (HIGH)
ANTHROPIC_API_KEY = "sk-ant-api03-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx"

# VIOLATION (Agent 2): Another API key pattern
RAZORPAY_API_KEY = "rzp_live_ABCDEFGHIJklmnop"
RAZORPAY_SECRET = "ABCDEFGHIJklmnopqrstuvwx"

# VIOLATION (Agent 2): Password assignment (HIGH)
SMTP_PASSWORD = "EmailP@ssw0rd2024!"

# VIOLATION (Agent 2): Database URL (CRITICAL)
DATABASE_URL = "postgresql://admin:ProdP@ss2024@db.company.com:5432/production"

# VIOLATION (Agent 2): JWT Secret (HIGH – generic_secret pattern)
JWT_SECRET = "super-secret-jwt-key-that-should-not-be-here-in-code-abc123def456"

# VIOLATION (Agent 2): Access token (HIGH)
SUPABASE_SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxmZnRtd3Vxd3BmaHRmeHFpYnFhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTIzMDQwMCwiZXhwIjoyMDM0ODA2NDAwfQ.example_signature_here_1234567890"

# VIOLATION (Agent 2): Encryption key (HIGH)
VAULT_ENCRYPTION_KEY = "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2"

# VIOLATION (Agent 2): Webhook secret (HIGH)
STRIPE_WEBHOOK_SECRET = "whsec_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij"
