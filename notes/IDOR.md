# IDOR / Broken Access Control

## Severity
High

## Endpoint

GET /api/users/<user_id>

## Vulnerable Behavior

An authenticated user could modify the `user_id` parameter
and access another user's information.

## Attack

Alice is authenticated:

GET /api/users/1

Then modify the ID:

GET /api/users/2

## Result

Alice was able to access Bob's information.

## Root Cause

The backend retrieved the requested user without verifying
whether the authenticated user was authorized to access that
resource.

## Impact

Unauthorized disclosure of user information.

## Vulnerable Code

```python
user = User.query.get(user_id)