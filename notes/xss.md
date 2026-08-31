# Cross-Site Scripting (XSS)

## What is XSS?

XSS occurs when untrusted user input is rendered by a browser as executable HTML/JavaScript.

## Vulnerable Code

```html
{{ message | safe }}
```

Using `safe` bypasses Jinja's normal escaping.

## Example

```html
<script>alert("XSS")</script>
```

If executed by the browser → XSS confirmed.

## Root Cause

Untrusted input is rendered as HTML/JavaScript instead of being escaped.

## Types

* Stored XSS — payload is stored and executed when viewed.
* Reflected XSS — payload is reflected immediately in the response.
* DOM XSS — client-side JavaScript inserts unsafe input into the DOM.

## Fix

Use automatic HTML escaping:

```html
{{ message }}
```

Avoid `|safe` for untrusted content.

## Impact

* Execute JavaScript in a victim's browser
* Modify page content
* Perform actions as the victim within the application's permissions
* Potentially access data available to client-side code

## Key Principle

> Treat user-controlled content as data, not executable HTML/JavaScript.
