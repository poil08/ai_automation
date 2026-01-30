import csv
import sys

REQUIRED = [
    "Company_name",
    "website",
    "contact_name",
    "email",
    "approved",
    "sent_at",
    "email_subject",
    "email_body",
    "status",
]

def main(path: str) -> int:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)

    # Detect trailing/leading spaces
    stripped = [h.strip() for h in headers]
    if headers != stripped:
        print("Header whitespace detected!")
        for i, (orig, clean) in enumerate(zip(headers, stripped)):
            if orig != clean:
                print(f"  - Column {i+1}: '{orig}' -> '{clean}'")
        print("Fix: remove leading/trailing spaces in your Google Sheet headers.")
        return 1

    missing = [c for c in REQUIRED if c not in headers]
    if missing:
        print("Missing required columns:")
        for c in missing:
            print(f"  - {c}")
        return 1

    print("CSV headers look good.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_csv.py data/sample_leads.csv")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
