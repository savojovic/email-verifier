# Email Verification Tool

This script verifies the validity of email addresses and checks if they belong to temporary or disposable email providers. It uses DNS queries to check for mail server existence and maintains a blacklist of known disposable email domains.

## Features

- Validates email format using regular expressions.
- Checks for mail server existence using DNS MX records.
- Verifies if an email domain is listed in a blacklist of disposable email providers.
- Can update the blacklist file from a remote URL.

## Usage

### Prerequisites

- Python 3.x
- Required Python packages: `dnspython`, `requests`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/savojovic/email-verifier.git
   cd email-verifier