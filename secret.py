import secrets
secret_key = secrets.token_urlsafe(32)  # Generates a 32-byte URL-safe string
print(secret_key)
