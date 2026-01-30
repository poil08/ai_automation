import json
import re
from pathlib import Path

INP = Path("workflows/n8n_ai_sales_outreach_workflow.json")
OUT = Path("workflows/n8n_ai_sales_outreach_workflow.redacted.json")

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
KEY_RE = re.compile(r"sk-[A-Za-z0-9]{10,}")  # catches OpenAI-style keys

def scrub(obj):
    if isinstance(obj, dict):
        return {k: scrub(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scrub(x) for x in obj]
    if isinstance(obj, str):
        s = EMAIL_RE.sub("redacted@example.com", obj)
        s = KEY_RE.sub("sk-REDACTED", s)
        return s
    return obj

def main():
    data = json.loads(INP.read_text(encoding="utf-8"))
    redacted = scrub(data)
    OUT.write_text(json.dumps(redacted, indent=2), encoding="utf-8")
    print(f"Wrote redacted workflow to {OUT}")

if __name__ == "__main__":
    main()
