import csv
from pathlib import Path

OUT = Path("data/sample_leads.csv")

ROWS = [
    {
        "Company_name": "Allbirds",
        "website": "https://www.allbirds.com",
        "contact_name": "Marketing Team",
        "email": "test+allbirds@example.com",
        "approved": "YES",
        "sent_at": "",
        "email_subject": "",
        "email_body": "",
        "status": "",
    },
    {
        "Company_name": "Pattern",
        "website": "https://pattern.com",
        "contact_name": "Revenue Ops",
        "email": "test+pattern@example.com",
        "approved": "YES",
        "sent_at": "",
        "email_subject": "",
        "email_body": "",
        "status": "",
    },
    {
        "Company_name": "Warby Parker",
        "website": "https://www.warbyparker.com",
        "contact_name": "Growth Team",
        "email": "test+warby@example.com",
        "approved": "",
        "sent_at": "",
        "email_subject": "",
        "email_body": "",
        "status": "",
    },
]

FIELDS = list(ROWS[0].keys())

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(ROWS)
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
