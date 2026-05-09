# IP / privacy safety rules (non-negotiable)

This repo lives on personal devices and personal accounts only. It is private.

## Never commit

- PHI of any kind
- Member IDs, claim IDs, encounter IDs
- Employer SQL, stored procedures, business logic
- Power BI screenshots or DAX expressions from work
- Internal URLs, internal architecture diagrams
- Slack / Teams / email content from work
- Vendor contracts, internal documents
- Employer credentials of any kind
- Any data you cannot independently re-derive from public sources

## Healthcare topics: public data only

- MIMIC-IV / eICU (with DUA, do not redistribute raw data)
- CMS SynPUF, SyntheticMass, Synthea
- MedMCQA, MedQA, PubMedQA, MMLU-clinical
- USPSTF / CDC / NICE / WHO public guidelines (verify license per source)

## Process rules

- Personal device, personal accounts, personal time only
- VERIFY employment IP / moonlighting clause in writing with HR/legal before any artifact release
- Re-check public dataset DUAs before each release
- Run a secrets scan before any artifact release
- Do not train or finetune on employer data, even if "anonymized"

## VERIFY items requiring legal/HR judgment (not automatable)

- Employer IP assignment clause interpretation
- Moonlighting policy interpretation
- Whether a specific public dataset's DUA permits a specific use
- Patent / publication clearance with employer if any overlap
