# Authorization / Access Control

## Definition

Authorization determines what an authenticated user
is allowed to do.

Question:

"Are you allowed to perform this action?"

---

# Authentication vs Authorization

Authentication:

"Who are you?"

Authorization:

"What are you allowed to access?"

Example:

Alice successfully logs in.

Authentication:

Alice = user ID 1

Authorization:

Can Alice access user ID 2?

If no:

403 Forbidden

---

# Authorization Flow

Request
  ↓
Authentication
  ↓
Identify current user
  ↓
Identify requested resource
  ↓
Check permissions
  ↓
Allow / Deny

---

# Object-Level Authorization

Object-level authorization determines whether a user
can access a specific resource.

Example:

GET /api/users/2

The server must determine:

Current user = Alice

Requested resource = Bob

Is Alice allowed to access Bob?

If not:

403 Forbidden

---

# IDOR

Insecure Direct Object Reference occurs when an application
allows a user to access another user's resource by changing
an object identifier.

Example:

GET /api/users/1

↓

GET /api/users/2

If Alice is authenticated as user 1 and can retrieve
user 2's information, the application has an access
control vulnerability.

---

# Function-Level Authorization

Function-level authorization controls access to
specific application functionality.

Example:

GET /api/admin/users

Normal user:

403 Forbidden

Administrator:

200 OK

---

# Role-Based Access Control

RBAC assigns permissions based on user roles.

Example:

Alice → user
Bob → user
Charlie → admin

Possible policy:

user:

- Access own profile
- Edit own profile

admin:

- Access user management
- Access all users
- Perform administrative actions

---

# Authorization Must Be Server-Side

Never rely on frontend authorization.

Example:

Frontend:

if (user.role === "admin") {
    showAdminPanel();
}

This is NOT security.

An attacker can directly send:

GET /api/admin/users

The backend must independently verify the user's
permissions.

---

# Common Authorization Failures

- IDOR
- Missing ownership checks
- Missing role checks
- Privilege escalation
- Horizontal privilege escalation
- Vertical privilege escalation
- Admin endpoints exposed to normal users
- Authorization enforced only in frontend
- Inconsistent authorization between endpoints

---

# Horizontal Privilege Escalation

One normal user accesses another normal user's resources.

Example:

Alice → Bob's profile

Both have the same role.

---

# Vertical Privilege Escalation

A lower-privileged user accesses functionality belonging
to a higher-privileged role.

Example:

Normal user → Admin endpoint

---

# Authorization Testing

For every endpoint ask:

WHO is making the request?

WHAT action are they performing?

WHICH resource are they accessing?

WHAT role does the user have?

DOES THE USER OWN THE RESOURCE?

IS THE USER AUTHORIZED FOR THIS ACTION?

---

# Testing Matrix

Example:

| User | Resource | Expected |
|------|----------|----------|
| Alice | Alice | 200 |
| Alice | Bob | 403 |
| Bob | Alice | 403 |
| User | Admin endpoint | 403 |
| Admin | Admin endpoint | 200 |

---

# Important Status Codes

401 Unauthorized:

User is not authenticated.

403 Forbidden:

User is authenticated but does not have permission.

---

# Security Principle

Never trust the client to determine what it is
allowed to access.

The backend must enforce authorization on every
protected resource and action.