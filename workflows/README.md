# AI Sales Outreach Automation (n8n Workflow)

This workflow automates personalized sales outreach emails using **Google Sheets + OpenAI + Gmail**, built in **n8n**.

It turns a spreadsheet of leads into AI-generated emails and sends them automatically once approved.

---

## What This Workflow Does

1. Monitors a Google Sheet for updates  
2. Checks approval status  
3. Generates a personalized email using AI  
4. Writes the email back to the sheet  
5. Sends the email via Gmail  
6. Marks the row as sent  

---

## Workflow Logic

Google Sheets Trigger
↓
Get Rows in Sheet
↓
IF (approved = YES AND sent_at is empty)
↓
Message a Model (OpenAI)
↓
Edit Fields
↓
Update Row (email_subject + email_body)
↓
Send Gmail Message
↓
Update Row (sent = YES, sent_at = timestamp)

---

## Required Google Sheet Columns

Your sheet must include these headers (exact names):

| Column Name     | Purpose |
|-----------------|--------|
| `Company_name`  | Company being contacted |
| `website`       | Company website |
| `contact_name`  | Person or team name |
| `email`         | Recipient email address |
| `approved`      | Must be `YES` to send |
| `sent_at`       | Must be empty before sending |
| `email_subject` | Filled automatically |
| `email_body`    | Filled automatically |

---

## AI Email Generation

The workflow uses OpenAI to generate:
- A personalized **email subject**
- A personalized **email body**

The AI is instructed to:
- Keep the subject short
- Start the email with “Hi {contact_name},”
- Avoid inventing specific company facts

---

## Gmail Integration

The Gmail node:
- Sends the email using your connected Google account
- Uses HTML formatting for line breaks
- Sends only if an email address exists

---

## Safety Checks

Emails will **NOT** be sent if:
- `approved` is not `YES`
- `sent_at` already has a value
- `email` field is empty

---

## Workflow File

**File:**  
`ai_outreach_automation.json`

Import this file into n8n to use the automation.

---

## How to Use

1. Import the workflow JSON into n8n  
2. Connect credentials:
   - Google Sheets
   - Gmail
   - OpenAI  
3. Set your Google Sheet as the data source  
4. Publish the workflow  
5. Update a row in the sheet → email sends automatically  

---

## Example Use Case

You maintain a lead list like:

| Company | Contact | Email | Approved |
|--------|---------|------|---------|
| Allbirds | Marketing Team | hello@company.com | YES |

Once approved, the system:
- Generates a tailored email  
- Sends it  
- Logs the send time  

---

## Notes

- Do not commit API keys to GitHub  
- Use environment variables for credentials if deploying  
- Adjust the AI prompt to match your brand voice  

---

## Built With

- [n8n](https://n8n.io/)
- OpenAI API
- Google Sheets API
- Gmail API
