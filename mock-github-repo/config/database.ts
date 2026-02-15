/**
 * Database configuration – contains hardcoded secrets.
 * Triggers: Agent 2 (database_url, password_assignment, generic_secret).
 */

// VIOLATION (Agent 2): Hardcoded database URL (CRITICAL – database_url pattern)
const DATABASE_URL = "postgresql://admin:SuperSecretP@ss123@db.production.internal:5432/enterprise_crm";

// VIOLATION (Agent 2): Hardcoded MySQL connection (CRITICAL)
const LEGACY_DB = "mysql://root:legacy_pass_2024@legacy-db.internal:3306/old_crm";

// VIOLATION (Agent 2): Hardcoded MongoDB connection (CRITICAL)
const ANALYTICS_DB = "mongodb+srv://analyst:Str0ngPassword!@cluster0.mongodb.net/analytics";

// VIOLATION (Agent 2): Hardcoded Redis URL (CRITICAL)
const REDIS_URL = "redis://default:RedisP@ssw0rd@redis.internal:6379/0";

// VIOLATION (Agent 2): Password assignment (HIGH)
const DB_PASSWORD = "SuperSecretP@ss123";

// VIOLATION (Agent 2): Generic secret (HIGH)
const SESSION_SECRET = "a9f8d7e6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0";

// VIOLATION (Agent 2): Auth token (HIGH)
const AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

export const dbConfig = {
  host: 'db.production.internal',
  port: 5432,
  database: 'enterprise_crm',
  user: 'admin',
  // VIOLATION: Password in config object (HIGH)
  password: 'SuperSecretP@ss123',
};

export const redisConfig = {
  host: 'redis.internal',
  port: 6379,
  // VIOLATION: Password in config (HIGH)
  password: 'RedisP@ssw0rd',
};
