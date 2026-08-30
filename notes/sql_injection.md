# SQL Injection

## What is SQL Injection?

SQL Injection occurs when untrusted user input is directly inserted into a SQL query, allowing the input to alter the query's behavior.

## Vulnerable Code

```python
query = text(
    f"SELECT * FROM user WHERE username = '{username}'"
)
```

User input becomes part of the SQL query.

## Example Attack

```text
alice' OR '1'='1
```

Can result in:

```sql
SELECT * FROM user
WHERE username = 'alice' OR '1'='1'
```

Since `'1'='1'` is always true, unintended records may be returned.

## Root Cause

* SQL string concatenation/interpolation
* Untrusted input directly reaches SQL

## Impact

* Unauthorized data access
* Authentication bypass
* Data modification/deletion
* Database information disclosure

## Fix

Use parameterized queries:

```python
query = text("""
    SELECT * FROM user
    WHERE username = :username
""")

db.session.execute(
    query,
    {"username": username}
)
```

## Testing

```text
Normal input → Expected result
'             → Check for SQL errors
SQL logic     → Check whether query behavior changes
```

## Key Principle

> **Never concatenate untrusted input into SQL. Use parameterized queries.**
