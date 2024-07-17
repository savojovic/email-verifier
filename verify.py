import argparse
import re
import dns.resolver
import requests

BLACKLIST_FILE_PATH = "./emails.txt"
BLACKLIST_FILE_URL = "https://raw.githubusercontent.com/wesbos/burner-email-providers/master/emails.txt"


def isTempOrDisposable(domain):
    try:
        with open(BLACKLIST_FILE_PATH, 'r', encoding='utf-8') as file:
            blacklistDomains = {line.strip() for line in file}
        return domain in blacklistDomains
    except FileNotFoundError:
        print(f"File {BLACKLIST_FILE_PATH} not found. Try running with --create")
    except IOError as e:
        print(f"Error reading from {BLACKLIST_FILE_PATH}: {e}")
    return False


def check_mx_records(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [record.exchange.to_text() for record in mx_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout) as e:
        print(f"Error resolving MX records for {domain}: {e}")
        return None


def verify(email):
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    if not email_pattern.match(email):
        print(f"{email} is not a valid email address")
        return

    print(f"{email} has a valid format, checking the existence of mail server...")
    _, domain = email.split('@')
    mx_record = check_mx_records(domain)

    if mx_record is None:
        print(f"Unable to find mail server for {domain}")
        return

    print(f"{domain} is a valid domain. Checking if the email is temporary or disposable...")
    if isTempOrDisposable(domain):
        print(f"Domain {domain} of email {email} is blacklisted. It is probably a temporary or disposable email!")
    else:
        print(f"{email} is not temporary or disposable!")


def updateBlackListFile():
    print("Downloading new file...")
    try:
        response = requests.get(BLACKLIST_FILE_URL)
        response.raise_for_status()
        with open(BLACKLIST_FILE_PATH, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully to {BLACKLIST_FILE_PATH}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file from {BLACKLIST_FILE_URL}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Verify an email address.")
    parser.add_argument('email', help='Email address to verify', nargs='?')
    parser.add_argument('--update', action='store_true', help='Update blacklist file')
    parser.add_argument('--create', action='store_true', help='Create blacklist file')

    args = parser.parse_args()

    if not args.email and not args.update:
        parser.print_help()
        return

    if args.update or args.create:
        updateBlackListFile()

    if args.email:
        verify(args.email)


if __name__ == "__main__":
    main()
