"""Extract, clean, and report unique email addresses from a text document."""

from collections import Counter
from datetime import datetime
from pathlib import Path
import re


INPUT_FILE = Path(__file__).with_name("input_text.txt")
OUTPUT_FILE = Path(__file__).with_name("extracted_emails.txt")
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


def find_emails(text):
    """Find email addresses, normalise case, and retain their first-seen order."""
    matches = re.findall(EMAIL_PATTERN, text, flags=re.IGNORECASE)
    normalized = [email.lower() for email in matches]
    unique_emails = list(dict.fromkeys(normalized))
    return unique_emails, Counter(normalized)


def create_report(emails, frequencies, source_name):
    """Build a readable report with extracted addresses and occurrence counts."""
    lines = [
        "EMAIL EXTRACTION REPORT",
        f"Source file: {source_name}",
        f"Created: {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
        "=" * 55,
        f"Total matches found: {sum(frequencies.values())}",
        f"Unique email addresses found: {len(emails)}",
        "=" * 55,
    ]
    if emails:
        lines.append(f"{'#':<5}{'Email address':<38}{'Occurrences':>12}")
        lines.append("-" * 55)
        for number, email in enumerate(emails, start=1):
            lines.append(f"{number:<5}{email:<38}{frequencies[email]:>12}")
    else:
        lines.append("No email addresses were found in the source file.")
    return "\n".join(lines) + "\n"


def main():
    """Read input text, extract emails, save a report, and print the results."""
    if not INPUT_FILE.exists():
        print(f"Input file not found: {INPUT_FILE}")
        print("Create input_text.txt in this folder and run the program again.")
        return

    try:
        text = INPUT_FILE.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Could not read the input file: {error}")
        return

    emails, frequencies = find_emails(text)
    report = create_report(emails, frequencies, INPUT_FILE.name)

    try:
        OUTPUT_FILE.write_text(report, encoding="utf-8")
    except OSError as error:
        print(f"Could not save the report: {error}")
        return

    print("\n" + "=" * 55)
    print("EMAIL EXTRACTION COMPLETE")
    print("=" * 55)
    print(f"Found {sum(frequencies.values())} total match(es), including duplicates.")
    print(f"Unique email addresses: {len(emails)}")
    print(f"Saved detailed report to: {OUTPUT_FILE}")
    print("\nExtracted email addresses:")
    if emails:
        for number, email in enumerate(emails, start=1):
            print(f"{number}. {email} ({frequencies[email]} occurrence(s))")
    else:
        print("No email addresses were found.")


if __name__ == "__main__":
    main()
