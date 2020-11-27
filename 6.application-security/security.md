## Application Security

#### Django Security Features

- Cross site scripting (XSS) protection: This security prevents malicious user from injecting client-side scripts in a website to hijack a user's session.

- SQL injection protection: Inserting user input into database has high security implications. Django queryset does parameterization to prevent these attacks.

- Hypertext Transfer Protocol Secure (SSL/HTTPS) enforces secure communication for a website. No http is allowed.

- Cross site request forgery (CSRF) protection: This prevents malicious user from impersonating a website's user.

#### Security features

- Authentication - Django also comes with auth out of the box but implementing it to meet the requirements of the application is also important.
- Authorisation - Django's permissions can be used for Authorisation or extended to fit requirements.
- Sensitive Data Exposure. Prevent exposure of sensitive data. Could be tokenization, encription and more.
- Security Misconfiguration. Though Django comes with useful security features, there will not be effective if not configured correctly.
- Using Components with Known Vulnerabilities. We made use of tools built by others to build software and those tools could have security vulnerabilities that affect our website.
