# Security Policy

## Supported Versions

The following table outlines which versions of this project are currently supported with security updates:

| Version | Status          | End of Support |
| ------- | --------------- | -------------- |
| Latest  | :white_check_mark: Supported | Current |
| Older versions | :x: Not supported | Upon new release |

We recommend always using the latest version from the `main` branch to receive all security updates and bug fixes.

## Reporting a Vulnerability

**Please do not open a public GitHub issue for security vulnerabilities.** Instead, use one of the following responsible disclosure methods:

### Private Security Reporting

1. **Email**: Contact the maintainer at [GitHub profile](https://github.com/bhuvan0x) for responsible disclosure details
2. **GitHub Security Advisory**: Use the [GitHub Security Advisory](https://github.com/bhuvan0x/Sharingan-Animation-in-Terminal/security/advisories) feature to report vulnerabilities privately

### What to Include

When reporting a vulnerability, please provide:

- A clear description of the security issue
- Steps to reproduce the vulnerability (if applicable)
- Affected version(s)
- Potential impact and severity assessment
- Any suggested fixes (if available)

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
- **Investigation**: We will investigate and assess the vulnerability within 7 days
- **Resolution**: We aim to address confirmed vulnerabilities as follows:
  - **Critical**: Patched and released within 7 days
  - **High**: Patched and released within 14 days
  - **Medium**: Patched and released within 30 days
  - **Low**: Addressed in the next routine release

### Disclosure Policy

- We ask that you do not publicly disclose the vulnerability until we have released a patch or made a security announcement
- Once a patch is released, we will credit the reporter in the release notes (if desired)
- We follow responsible disclosure principles and will work with you to determine an appropriate disclosure timeline

## Security Best Practices for Users

### Using This Project Safely

1. **Keep Python Updated**: Ensure you are using Python 3.9 or newer, as older versions may have security vulnerabilities
2. **Clone from Official Repository**: Always clone from the official GitHub repository to ensure code integrity
3. **Verify Releases**: For released versions, verify the commit hash against the official repository
4. **No Third-Party Dependencies**: This project has no external Python package dependencies, reducing the attack surface
5. **Review Code**: As an open-source project, users are encouraged to review the code for their own security assurance

## Dependencies and Supply Chain

- **Python Standard Library Only**: This project uses only the Python standard library, eliminating external dependency vulnerabilities
- **Minimal External Tools**: The project requires only a terminal with ANSI escape code support
- **No Network Communication**: The application does not communicate with external servers or services

## Security Considerations

### What This Project Does Not Do

- Does not collect, store, or transmit personal data
- Does not make network requests
- Does not require special system privileges
- Does not modify system files outside the application scope
- Does not execute arbitrary code from user input

### Terminal Compatibility

- The project supports standard ANSI terminal environments
- True-color support (24-bit color) is recommended but not required
- Use with caution on untrusted terminal emulators

## Contact

For security-related questions or concerns, please reach out to the maintainer:

- **GitHub**: [@bhuvan0x](https://github.com/bhuvan0x)
- **Repository**: [Sharingan-Animation-in-Terminal](https://github.com/bhuvan0x/Sharingan-Animation-in-Terminal)

---

**Last Updated**: 2026-09-10
