# SWOPS Automation System

Last updated: 25 March 2026

## Overview

The `automation/` folder contains a Python-based system that connects the SWOPS website (swops.it) to Google Workspace and Netlify. It handles three core jobs:

1. **Google OAuth authentication** for the `hello@swops.it` account
2. **Registration sync** - pulling website signups from Netlify into a Google Sheet (runs hourly via Cowork scheduled task)
3. **Press outreach** - generating personalised Gmail drafts for journalists

All scripts authenticate via a single OAuth token stored locally. The sync runs automatically. Press drafts are created in Gmail Drafts for John to review and send manually - nothing is ever sent automatically.

## Critical Rules

- **DRAFTS ONLY** - never use `messages().send()`, only `drafts().create()`. John reviews and sends all emails himself.
- **NO NETLIFY DEPLOYS** without John saying "push" or "go".
- **NO GIT PUSH** without explicit confirmation from John.
- **NO EM DASHES** anywhere in copy or code.

---

## File Structure

```
automation/
├── authenticate.py              # One-time OAuth setup
├── config.json                  # Shared config (Sheet ID, Netlify tokens)
├── create_press_drafts.py       # Generates Gmail drafts for press outreach
├── setup_sheets.py              # One-time Google Sheet creation
├── sync_registrations.py        # Hourly Netlify -> Sheets sync (active)
└── credentials/
    ├── swops_oauth_credentials.json   # Google Cloud OAuth client config
    └── token.json                     # Saved auth token (auto-refreshes)
```
---

## 1. authenticate.py - One-Time OAuth Setup

**Purpose:** Authorises the automation scripts to access Google APIs on behalf of `hello@swops.it`.

**Google Cloud project:** `swops-automation` (Desktop app type OAuth credentials)

**Scopes granted:**
- `gmail.modify` - create and manage Gmail drafts
- `spreadsheets` - read/write Google Sheets
- `drive` - access Google Drive files
- `documents` - access Google Docs

**How it works:**
- Opens a browser window for Google sign-in
- You sign in as `hello@swops.it` and click "Allow"
- Saves the resulting token to `credentials/token.json`
- Subsequent scripts use this token and auto-refresh it when expired

**When to run:** Only once, unless the token is deleted or permissions are revoked. If scripts start failing with auth errors, re-run this.

```bash
cd automation && python authenticate.py
```
---

## 2. setup_sheets.py - Google Sheet Creation (One-Time, Already Run)

**Purpose:** Created the "Swops Registrations" Google Sheet that acts as the central registration database.

**Sheet ID:** `1c_XZby9Y8GufYFoQAYcOZTK3pWokzQg4KVIQWa7N8IQ`
**Sheet URL:** https://docs.google.com/spreadsheets/d/1c_XZby9Y8GufYFoQAYcOZTK3pWokzQg4KVIQWa7N8IQ

### Tab 1: Registrations

Actual column order (as written by sync_registrations.py):

| Col | Header | Source |
|-----|--------|--------|
| A | Timestamp | Netlify `created_at`, formatted "DD Mon YYYY HH:MM" |
| B | Name | Netlify `name` field (full name, not split) |
| C | Email | Netlify `email` (used as unique key for dedup) |
| D | Suburb | Netlify `suburb` |
| E | House Type | Netlify `house-type` |
| F | Bedrooms | Netlify `bedrooms` |
| G | People | Netlify `people` |
| H | Rating | Netlify `rating` |
| I | Song | Netlify `song` |
| J | Walk To | Netlify `walk-to` |
| K | Status | Set to "New" on import |
| L | Matched With | Manual - for recording swop matches |
| M | Notes | Manual - free text |
**Known issue:** setup_sheets.py created headers "First Name" and "Last Name" in columns B and C, but sync_registrations.py writes a single "Name" field to column B and "Email" to column C. The headers and data are misaligned from column B onward. The data is correct, the headers are wrong.

### Tab 2: Email Log

| Col | Header |
|-----|--------|
| A | Timestamp |
| B | To |
| C | Subject |
| D | Type |
| E | Draft ID |
| F | Sent |

Both tabs have bold headers with green background (#2E8033 approx).

**When to re-run:** Only if you need a fresh sheet. It creates a new one each time and updates `config.json` with the new ID.

```bash
cd automation && python setup_sheets.py
```
---

## 3. sync_registrations.py - Registration Sync (Active, Hourly)

**Purpose:** Pulls new form submissions from the Netlify registration form and adds them to the Google Sheet. This is the main recurring script.

**Schedule:** Runs every hour automatically via Cowork scheduled task. No manual intervention needed. John is also notified of new registrations directly by Netlify.

**How it works:**
1. Reads `config.json` for the Sheet ID and Netlify credentials
2. Fetches all submissions from Netlify's API for the registration form
3. Checks which emails already exist in column C to prevent duplicates
4. Appends any new registrations as rows with status "New"
5. Auto-refreshes the Google auth token if expired

**Netlify form ID:** `699bde0dda533f00080381f3`
**Netlify token:** stored in `config.json`

**Important:** This script does NOT create Gmail drafts or send any emails. It only syncs data into the sheet.

```bash
cd automation && python sync_registrations.py
```
---

## 4. create_press_drafts.py - Press Outreach Drafts (Completed, Not Recurring)

**Purpose:** Created 17 personalised Gmail drafts for media outreach. Nothing was sent - all drafts appeared in the Gmail Drafts folder of `hello@swops.it` for John to review.

**Status:** Script has been run. Drafts exist in Gmail. Running again will create duplicates.

**All emails include:**
- Personalised subject line and body per journalist/outlet
- Link to swops.it/press for full details and images
- Signature: John / Swops / swops.it
- From address: hello@swops.it

### Wave 1 Drafts (17 created)

| Outlet | Contact | Email | Angle |
|--------|---------|-------|-------|
| Broadsheet | Katya Wachtel | katya@broadsheet.com.au | Melbourne launch / editorial story |
| Broadsheet | Nick Connellan | nick.connellan@broadsheet.com.au | Domestic travel angle |
| Broadsheet | Audrey Payne | audrey@broadsheet.com.au | Food/neighbourhood angle |
| Broadsheet | Dan Cunningham | dan@broadsheet.com.au | National flag |
| Concrete Playground | Eliza Campbell | editorial@concreteplayground.com.au | King's Birthday editorial |
| Concrete Playground | Events desk | events@concreteplayground.com.au | Event listing submission |
| Urban List | Caity Stone | editormels@theurbanlist.com | King's Birthday weekend story |
| Urban List | Editorial desk | editorial@theurbanlist.com | Weekend escape story || Guardian Australia | Cait Kelly | cait.kelly@theguardian.com | Structural housing / renters locked out |
| Guardian Australia | Luke Henriques-Gomes | luke.henriques-gomes@theguardian.com | Housing inequality angle |
| Guardian Australia | Nino Bucci | nino.bucci@theguardian.com | Melbourne local angle |
| The Age | Elizabeth Redman | elizabeth.redman@nine.com.au | Rental property / housing beat |
| The Age | Alexandra Middleton | amiddleton@nine.com.au | Melbourne property angle |
| Domain | Jim Malo | jim.malo@nine.com.au | Rental market story |
| Domain | Editorial desk | editorial@domain.com.au | General pitch |
| The Australian | Rachel Baxendale | rbaxendale@theaustralian.com.au | Melbourne launch |
| Fashion Journal | Editorial desk | editorial@fashionjournal.com.au | Budget holiday / lifestyle |

**Pending update:** Once John finalises his founder quote for press.html, all 17 drafts need to be updated with the correct quote wording.
### Wave 2 Contacts (Drafts Not Yet Created)

From SWOPS-Media-Contacts_1.docx. These need new drafts written and created once the founder quote is finalised.

**Tier 1 - High Priority:**

| Outlet | Contact | Email |
|--------|---------|-------|
| 3AW Breakfast | Mark Davidson | mark.davidson@3aw.com.au |
| 3AW Breakfast | Sophie Klemens | sophie.klemens@3aw.com.au |
| ABC Radio Melbourne | Shelley Hadfield | hadfield.shelley@abc.net.au |
| ABC Radio Melbourne | Sarah Jaensch | jaensch.sarah@abc.net.au |
| AAP | Liz Hobday | lhobday@aap.com.au |
| Time Out Melbourne | Leah Glynn | leah.glynn@timeout.com |
| The Age | Sophie Aubrey | sophie.aubrey@theage.com.au |
| The Age | Weekend Events desk | weekendevents@theage.com.au |
| Herald Sun | Nick Papps | nick.papps@news.com.au |
| Herald Sun | Nui Te Koha | nui.tekoha@news.com.au |
| Broadsheet | Emma Joyce | emma.joyce@broadsheet.com.au |
| Urban List | Navarone Farrell | nfarrell@theurbanlist.com |
**Tier 2 - Worth Reaching:**

| Outlet | Contact | Email |
|--------|---------|-------|
| Secret Melbourne | Nicole de Souza | nicole.desouza@feverup.com |
| Sitchu | Kelsey Harrington | kelsey.harrington@sitchu.com |
| 9 Honey | Jabi | jabi@nine.com.au |
| Melbourning | - | hello@melbourning.com.au |
| Concrete Playground | Eliza Campbell (new email) | eliza.campbell@vinyl.media |

**Emails Still Needed (Research Required):**
- Alice Griffin, Junkee Editor-in-Chief - **TOP PRIORITY**
- Michael Janda, ABC News Business Editor - **TOP PRIORITY**
- Andrew Zuccala, Concrete Playground Melbourne Editor

**Contacts from Wave 1 that also need email research:**
- Greg Jericho - Guardian Australia Economist/Columnist
- Nick Bonyhady - The Age/SMH Reporter
- Orana Durney-Benson - Domain Reporter
- Samuel Yang - ABC News Reporter
- SMH Property desk (via Nine Entertainment)
- Crikey (via crikey.com.au)
- The Saturday Paper (via thesaturdaypaper.com.au)
- triple j / Hack (via abc.net.au/triplej/programs/hack)
- ABC Melbourne Radio (via abc.net.au/melbourne)
---

## 5. config.json - Shared Configuration

Stores IDs and tokens used across scripts:

```json
{
  "registration_sheet_id": "1c_XZby9Y8GufYFoQAYcOZTK3pWokzQg4KVIQWa7N8IQ",
  "netlify_form_id": "699bde0dda533f00080381f3",
  "netlify_token": "nfp_U5UfZgBkzT6Z27UAo1JS56xJFfyVXAmo0fcd"
}
```

Updated automatically by `setup_sheets.py` when a new sheet is created.

---

## 6. Credentials Folder

Both files are gitignored.

- `swops_oauth_credentials.json` - Google Cloud OAuth client config for the "swops-automation" project. This is the app identity, not the user token.
- `token.json` - The saved user auth token for `hello@swops.it`. Auto-refreshes when expired. Delete this and re-run `authenticate.py` if auth breaks.
---

## 7. Python Dependencies

```bash
pip install google-auth-oauthlib google-auth google-api-python-client
```

---

## 8. Press Release - Banked Changes (Not Yet Pushed)

These are not automation scripts, but they're tightly coupled with the press drafts workflow.

**press.html changes (banked locally, not deployed):**
- Black text on white background (was green on black)
- Font changed to Georgia, 'Times New Roman', serif (was Alfredino)
- Paragraph reorder: "So this King's Birthday..." moved before "Record rents..."
- John Pace named as founder with quote
- Contact line: "Contact: John Pace | hello@swops.it"
- Bug: title tag still has an em dash that needs fixing before push

**Swops-Press-Release.pdf:** Regenerated with ReportLab, matches press.html changes. Also banked.
**Blocker:** John said "i'll take a pass at the quote in the morning. it's not quite working for me as is." The current draft quote:

> "I kept watching people I work with miss out on something as simple as a long weekend away because they couldn't justify the cost. They're paying rent every week on a home they're not using, then paying again to stay somewhere else. It seemed like a solvable problem."

Once the quote is finalised:
1. Update press.html with the revised quote
2. Fix the em dash in the title tag
3. Regenerate Swops-Press-Release.pdf
4. Update all 17 existing Gmail drafts with the correct quote
5. Create new drafts for Wave 2 contacts
6. John approves and pushes to Netlify

---

## 9. Pending Automation Work

**Immediate (blocked on quote):**
- Finalise founder quote in press.html
- Update 17 existing Gmail drafts
- Create Gmail drafts for Wave 2 contacts (Tier 1 + Tier 2)
- Research missing email addresses (Alice Griffin, Michael Janda, Andrew Zuccala)
**Upcoming build work (not yet started):**
- GA4 setup - needs Measurement ID from John
- Meta Pixel setup - needs Pixel ID from John
- Welcome email copy (for new registrants)
- Swop agreement - web page + downloadable PDF
- Terms/Privacy page
- Photo upload system (post-registration, secure, no public photos)

**Fix:**
- Correct the sheet headers in "Swops Registrations" tab to match the actual column mapping from sync_registrations.py (Name instead of First Name/Last Name, etc.)

---

## 10. Google APIs Enabled

The swops-automation Google Cloud project has these APIs enabled:
- Gmail API
- Google Sheets API
- Google Drive API
- Google Docs API

The Docs API is authorised but not yet used by any script. It's available for future automation (e.g. generating swop agreements as Google Docs).

---

## .gitignore

The repo excludes: `automation/credentials/`, `automation/token*.json`, `.env`, `.DS_Store`
