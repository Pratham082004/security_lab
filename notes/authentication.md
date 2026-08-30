# Authentication

## Definition

Authentication is the process of determining who a user is.

Question:

"Who are you?"

Example:

Alice provides:

username = alice
password = ********

The server verifies the credentials and identifies
the user as Alice.

---

# Authentication Flow

User
  ↓
Username + Password
  ↓
POST /login
  ↓
Server
  ↓
Verify credentials
  ↓
Create authenticated session
  ↓
Session Cookie
  ↓
Browser

---

# Our Lab Implementation

Login request:

POST /login

{
    "username": "alice",
    "password": "alice123"
}

The server verifies the user and stores:

session["user_id"] = user.id

The browser then sends the session cookie with
future requests.

---

# Authentication vs Authorization

Authentication:

"Who are you?"

Authorization:

"Are you allowed to do this?"

Example:

Alice logs in successfully.

Authentication:

Alice is authenticated.

Authorization:

Can Alice access Bob's profile?

Authentication can be working perfectly while
authorization is completely broken.

---

# Authentication States

Unauthenticated:

GET /api/users/1

Response:

401 Unauthorized

Authenticated:

Alice logs in.

session["user_id"] = 1

Alice can now access authenticated endpoints.

---

# Session

A session allows the server to remember that a user
has authenticated.

Example:

Login
  ↓
session["user_id"] = 1
  ↓
Browser receives session cookie
  ↓
Browser sends cookie
  ↓
Server identifies Alice

---

# Important Authentication Security Issues

## Weak Passwords

Weak passwords are easier to guess or brute-force.

---

## Plaintext Password Storage

Our lab currently stores passwords directly.

Example:

password = "alice123"

This is intentionally insecure.

Production applications should use strong password
hashing algorithms.

---

## Brute Force

An attacker repeatedly attempts passwords against
the login endpoint.

Defenses include:

- Rate limiting
- Account lockout policies
- Strong password requirements
- Monitoring
- MFA

---

## Session Security

Sessions should be protected against:

- Session theft
- Session fixation
- Session leakage

Cookies should generally use appropriate:

- HttpOnly
- Secure
- SameSite

attributes.

---

## Authentication Checklist

When reviewing authentication, check:

- Can users log in securely?
- Are passwords securely hashed?
- Is brute force possible?
- Is MFA available where appropriate?
- Are sessions invalidated on logout?
- Are session cookies protected?
- Can sessions be hijacked?
- Can authentication be bypassed?
- Are password reset flows secure?
- Are authentication errors revealing sensitive information?

---

# Key Principle

Authentication establishes identity.

It does NOT automatically grant permission.