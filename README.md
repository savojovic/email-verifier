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

## Command-line Arguments

- `email`: Specify an email address to verify.
- `--update`: Update the blacklist file from the remote URL.
- `--create`: Create a new blacklist file if it doesn't exist.

## Examples

- Verify an email address:
  ```bash
  python verifyer.py john.doe@example.com
  ```
  This command checks if `john.doe@example.com` is a valid email address, verifies the mail server, and checks if the domain is in the blacklist.

- Update the blacklist file:
  ```bash
  python verifyer.py --update
  ```
  This command downloads the latest blacklist file from the remote URL and updates the local file.

- Create a new blacklist file:
  ```bash
  python verifyer.py --create
  ```
  This command downloads the blacklist file if it doesn't already exist locally.

- Verify an email address and update the blacklist file:
  ```bash
  python verifyer.py john.doe@example.com --update
  ```
  This command updates the blacklist file and then verifies the email address `john.doe@example.com`.

## Acknowledgments

- Blacklist data from [wesbos/burner-email-providers](https://github.com/wesbos/burner-email-providers).
