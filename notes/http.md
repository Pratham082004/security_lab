# HTTP Security Fundamentals

## What is HTTP?

HTTP (Hypertext Transfer Protocol) is the protocol used for
communication between clients and servers.

Typical flow:

Client
  ↓
HTTP Request
  ↓
Server
  ↓
HTTP Response
  ↓
Client

---

## HTTP Request

Example:

POST /login HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "username": "alice",
    "password": "alice123"
}

A request contains:

- HTTP method
- URL/path
- Headers
- Cookies
- Query parameters
- Request body

---

## HTTP Methods

### GET

Used to retrieve data.

Example:

GET /api/users/1

### POST

Used to create data or perform an action.

Example:

POST /login

### PUT

Usually used to replace/update a resource.

### PATCH

Usually used to partially update a resource.

### DELETE

Used to delete a resource.

---

## HTTP Response

Example:

HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "username": "alice"
}

A response contains:

- Status code
- Response headers
- Cookies
- Response body

---

## Important Status Codes

### 200 OK

Request succeeded.

### 201 Created

A resource was successfully created.

### 400 Bad Request

The request is malformed or invalid.

### 401 Unauthorized

The client is not authenticated.

Meaning:

"Who are you?"

### 403 Forbidden

The client is authenticated but does not have permission.

Meaning:

"I know who you are, but you're not allowed."

### 404 Not Found

Requested resource does not exist.

### 405 Method Not Allowed

HTTP method is not supported by the endpoint.

### 429 Too Many Requests

Rate limit exceeded.

### 500 Internal Server Error

Server-side error.

---

# HTTP Headers

Headers provide additional information about requests
and responses.

Important security-related headers include:

- Content-Type
- Authorization
- Cookie
- Set-Cookie
- Origin
- Referer
- Host
- User-Agent

---

# Cookies

Cookies allow the server to associate requests with a client/session.

Example:

Cookie: session=abc123

The browser automatically sends the cookie with
subsequent requests.

Important cookie security attributes:

- HttpOnly
- Secure
- SameSite

---

# Trust Boundary

Anything controlled by the client should be considered
untrusted.

Do NOT blindly trust:

- URL parameters
- Query parameters
- JSON body
- Cookies
- HTTP headers
- Hidden form fields
- Frontend validation
- Client-side role information

Security decisions must be enforced on the server.

---

# Security Mindset

For every request ask:

WHO is making the request?

WHAT are they trying to do?

WHICH resource are they accessing?

WHAT input do they control?

IS the action authorized?

WHAT happens if the client lies?