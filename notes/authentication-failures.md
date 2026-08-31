# Authentication Failures

## Common Problems

* Plaintext password storage
* Weak passwords
* No brute-force protection
* Poor session management
* Authentication bypass
* User enumeration
* Insecure password reset

## Plaintext Passwords

Bad:

```text
alice → alice123
```

Passwords should be stored as secure hashes.

## Password Hashing

Use a password hashing function such as Werkzeug's password hashing utilities.

```python
generate_password_hash(password)
```

Verify with:

```python
check_password_hash(hash, password)
```

## Brute Force

An attacker repeatedly attempts passwords against `/login`.

Defenses:

* Rate limiting
* Monitoring
* Progressive delays / lockout policies
* MFA where appropriate

## User Enumeration

Avoid revealing whether a username exists.

Bad:

```text
User does not exist
```

Better:

```text
Invalid username or password
```

## Session Security

Check:

* Session invalidation on logout
* Secure cookie configuration
* Session fixation protection
* Session expiration
* Session theft protection

## Security Principle

> Authentication must securely verify identity without exposing credentials or providing an easy path to bypass or repeatedly attack the authentication mechanism.
