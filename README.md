# AI Sales Outreach Automation

This project automates personalized sales outreach using **AI + Google Sheets + Gmail**, built in **n8n**.

It turns a spreadsheet of leads into AI-generated emails and sends them automatically once approved.

---

## What This Project Does

This system:

- Monitors a Google Sheet for approved leads
- Uses AI to generate personalized outreach emails
- Writes the generated emails back into the sheet
- Sends emails via Gmail
- Logs when each email was sent

No manual copy/paste. No repetitive writing.

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| **n8n** | Workflow automation engine |
| **OpenAI API** | AI-generated email content |
| **Google Sheets API** | Lead database & tracking |
| **Gmail API** | Sending emails automatically |

---

## Workflow Overview

Google Sheets Trigger
↓
Check if lead is approved
↓
Generate email with AI
↓
Write subject & body to sheet
↓
Send email via Gmail
↓
Mark as sent with timestamp

---

## Project Structure

ai_automation/
├── workflows/     # n8n workflow export
├── data/          # Sample lead data
├── docs/          # Workflow documentation
├── README.md
└── .env.example   # Environment variable template

---

## Workflow File

The main automation lives here:
workflows/ai_outreach_automation.json
Import this into n8n to run the automation.

---

## Required Google Sheet Columns

| Column Name     | Purpose |
|-----------------|--------|
| Company_name    | Company being contacted |
| website         | Company website |
| contact_name    | Person or team name |
| email           | Recipient email address |
| approved        | Must be `YES` to send |
| sent_at         | Must be empty before sending |
| email_subject   | Filled automatically |
| email_body      | Filled automatically |

---

## How to Run

1. Import the workflow JSON into n8n
2. Connect credentials:
   - OpenAI
   - Google Sheets
   - Gmail
3. Set your Google Sheet
4. Publish the workflow
5. Approve a row in the sheet → email sends automatically

---

## Security Note

Never commit API keys to GitHub.  
Use environment variables or n8n credential storage.

---

## Example Use Case

A marketing or sales team can manage leads in a spreadsheet and automatically send AI-personalized outreach once a lead is approved.

---

## Scripts

- `scripts/validate_csv.py` — validates column names (catches trailing space bugs)
- `scripts/make_sample_leads.py` — generates `data/sample_leads.csv`
- `scripts/redact_workflow.py` — creates a safe workflow export for GitHub

---

## License

MIT License
