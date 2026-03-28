# SWOPS Context

## Critical Rules (Claude Must Follow)
- **DON'T BULLSHIT ME.** If you don't know something, say so. If you can't see something, say so. If you can't do something, say so. Never guess at something and present it like you know. Never waste my time by pretending. My time is the most precious thing I have.
- **NO EM DASHES** anywhere in copy or code. Never. Use a comma, full stop, or rewrite the sentence.
- **DO NOT PUSH TO GIT** without explicit confirmation from John. Always bank changes locally and wait. Never push speculatively.
- **DRAFTS ONLY** for Gmail — never use `messages().send()`, only `drafts().create()`. John reviews and sends all emails himself.
- **NO NETLIFY DEPLOYS** without John saying "push" or "go".

## About Swops
Swops privately matches renters with renters for short breaks in each other's homes. You stay in their place while they stay in yours. All free. All private.

First swop window: Inner North <-> Mornington, King's Birthday long weekend, June 6-8.

## Website
- Live site: https://swops.it
- Repo: GitHub -> Netlify auto-deploy
- Stack: Pure HTML/CSS/JS, no frameworks
- Font: Alfredino only
- Colours: #000 black and #C8FF00 lime green
- Animations: steps(1, end) hard cuts only
- Forms: Netlify form handling with fetch() AJAX

## Pages
- index.html -- Main site
- how-it-works.html -- Full explainer
- register.html -- Registration form (synced with index.html form)
- profiles.html -- Dummy profiles (password gate removed)
- privacy.html -- Minimal privacy policy
- success.html -- Form submission success
- press.html -- Press release page (CHANGES BANKED, NOT YET PUSHED -- see Press section)

## Accounts & Infrastructure

### Domain & Email
- Domain: swops.it
- Email: hello@swops.it (Google Workspace)

### Hosting
- GitHub -> Netlify auto-deploy
- Netlify form submissions enabled
- Netlify Form ID: 699bde0dda533f00080381f3
- Netlify Token: nfp_U5UfZgBkzT6Z27UAo1JS56xJFfyVXAmo0fcd (stored in automation/config.json)

### Social
- Instagram: @swops.it (professional account, connected to Meta Business Portfolio)
- Reddit: u/swopsit
- Facebook Page: Swops It (connected to Meta Business Portfolio)

### Meta Business Manager
- Business Portfolio name: swops.it
- Instagram @swops.it: connected, owned by swops.it portfolio
- Facebook Page: Swops It -- added to portfolio
- Ad Account: not yet set up (next step when ready to run ads)

## Automation & Backend

### Google Cloud Project
- Project: Swops Automation
- OAuth2 credentials: Desktop app type
- Credentials file: /Users/yies/SWOPS/automation/credentials/swops_oauth_credentials.json (gitignored)
- Token file: /Users/yies/SWOPS/automation/credentials/token.json (gitignored)
- APIs enabled: Gmail API, Google Sheets API, Google Drive API, Google Docs API

### Google Sheets Registration Database
- Sheet: "Swops Registrations"
- Sheet ID: 1c_XZby9Y8GufYFoQAYcOZTK3pWokzQg4KVIQWa7N8IQ
- Columns: Timestamp, Name, Email, Suburb, House Type, Bedrooms, People, Rating, Song, Walk To, Status, Matched With, Notes

### Registration Sync
- Script: /Users/yies/SWOPS/automation/sync_registrations.py
- Polls Netlify Forms API for new submissions, adds them to Google Sheets
- Runs every hour automatically via Cowork scheduled tasks
- Does NOT create Gmail drafts -- John handles email himself, Netlify notifies him of new registrations directly

### Automation Scripts
- authenticate.py -- One-time OAuth flow to generate token.json
- setup_sheets.py -- Created the Swops Registrations Google Sheet
- sync_registrations.py -- Hourly Netlify -> Sheets sync (active)
- create_press_drafts.py -- Created 17 personalised Gmail drafts for media outreach (completed, not recurring)
- config.json -- Netlify form ID + token, registration sheet ID

### .gitignore
Excludes: automation/credentials/, automation/token*.json, .env, .DS_Store

## Press & Media

### Press Release Page (press.html)
BANKED CHANGES -- NOT YET PUSHED:
- Black text on white background (was green on black)
- Font changed to Georgia, 'Times New Roman', serif (was Alfredino)
- Paragraph order: "So this King's Birthday..." moved before "Record rents..." paragraph
- John Pace named as founder with quote (see below)
- Contact line: "Contact: John Pace | hello@swops.it"
- Notes: "For interviews or further information, contact John Pace: hello@swops.it"
- Title tag still has em dash (needs fixing before push): <title>Swops -- Press Release</title>
- **John has NOT yet approved final quote wording** -- he said "i'll take a pass at the quote in the morning. it's not quite working for me as is"

### Founder Paragraph (press.html -- banked, not pushed)
Current draft (John to revise quote):
"Swops was founded by John Pace, a Melbourne producer who works closely with directors and other young creative talent. 'I kept watching people I work with miss out on something as simple as a long weekend away because they couldn't justify the cost,' says Pace. 'They're paying rent every week on a home they're not using, then paying again to stay somewhere else. It seemed like a solvable problem.'"

### Founder Framing Notes
John is a Melbourne producer (Hooves production company). The PR angle is John as an observer/builder -- he saw the problem through his work with young creative directors -- NOT as a renter with a grievance. This is deliberate to protect the aspirational image of Hooves.

### PDF (Swops-Press-Release.pdf)
Fully regenerated with ReportLab: black on white, Times-Roman, correct paragraph order, John Pace named, quote included.
BANKED -- NOT YET PUSHED.

### Gmail Press Drafts (created, not sent)
17 personalised drafts created via create_press_drafts.py in the Swops Gmail account.
Two angles used: culture/lifestyle and housing/cost of living.
All include link to https://swops.it/press

Contacts covered:
- Katya Wachtel, Nick Connellan, Audrey Payne, Dan Cunningham (Broadsheet)
- Eliza Campbell, events inbox (Concrete Playground)
- Caity Stone, editorial inbox (Urban List)
- Cait Kelly, Luke Henriques-Gomes, Nino Bucci (Guardian)
- Elizabeth Redman, Alexandra Middleton (The Age)
- Jim Malo, editorial inbox (Domain)
- Rachel Baxendale (The Australian)
- Fashion Journal editorial

### New Media Contacts (Tier 1/2 -- drafts not yet created)
From SWOPS-Media-Contacts_1.docx (12-page list, researched and tiered):

Tier 1 -- high priority, drafts needed:
- 3AW Breakfast: mark.davidson@3aw.com.au, sophie.klemens@3aw.com.au
- ABC Radio Melbourne: hadfield.shelley@abc.net.au, jaensch.sarah@abc.net.au
- Liz Hobday AAP: lhobday@aap.com.au
- Time Out Melbourne: leah.glynn@timeout.com
- Sophie Aubrey The Age: sophie.aubrey@theage.com.au
- Weekend Events The Age: weekendevents@theage.com.au
- Nick Papps Herald Sun: nick.papps@news.com.au
- Nui Te Koha Herald Sun: nui.tekoha@news.com.au
- Emma Joyce Broadsheet: emma.joyce@broadsheet.com.au
- Navarone Farrell Urban List: nfarrell@theurbanlist.com

Tier 2 -- worth reaching:
- Secret Melbourne: nicole.desouza@feverup.com
- Sitchu: kelsey.harrington@sitchu.com
- 9 Honey: jabi@nine.com.au
- Melbourning: hello@melbourning.com.au
- Eliza Campbell new email: eliza.campbell@vinyl.media

Emails still needed (research required):
- Alice Griffin (Junkee) -- TOP PRIORITY
- Michael Janda (ABC News) -- TOP PRIORITY
- Andrew Zuccala (Concrete Playground)

## Product Design -- Privacy & Trust Model

### Photos and home identification
The core privacy concern is not strangers seeing photos of a home -- it is a landlord or agent identifying a specific rental property from photos and using that as evidence of subletting. A photo posted to any profile, however gated, could be screenshotted and used against a renter.

### Current position: no photos
Swops currently uses text descriptions only. This lowers the barrier to joining (no photo required) but creates friction at the matching stage -- swoppers may be reluctant to agree to a video call based on text alone.

### Future direction: mutual interest gate
1. Register with text description only
2. Get matched by Swops based on location, window, household type
3. Both parties indicate mutual interest in each other's listing
4. Only at this point are photos or location details exchanged -- symmetrically
5. Video call to see the home live and confirm the swop
6. Swop confirmed

The mutual interest gate is symmetric -- you can't see their photos without them seeing yours.

### AI-altered vibe images (parked for future)
Style transfer approach -- retains character of a home but changes it enough to be unrecognisable to a landlord. Parked, requires build work.

### Why the video call is the real trust mechanism
Ephemeral -- nothing persists. Harder to use as evidence than a static photo. Lets both parties see the home and person in real time.

## Design Notes
- No overlays on images unless specified
- Typewriter effect: IntersectionObserver, 55ms per character
- Euro Slummer section: CSS grid two-column poster layout, lime bg
- Footer: hello@swops.it + link to privacy.html
- OG image: SITE ASSETS/IMAGES/OG-IMAGE-1200-x-630.jpg
- Favicon: lime green square SVG (#C8FF00)
- No em dashes anywhere in copy

### Mobile CSS Note
Browser silently drops some mobile CSS rules. Fix: add a second <style> block at the bottom of the file with !important overrides for mobile. This is the reliable approach for this codebase.

### INCOGNITO ABODE section (s-slummer) -- mobile fix applied and pushed
- `.s-slummer__title` bottom: 130px (was 90px), white-space: nowrap
- `.s-slummer__text` bottom: 32px, right: 28px
- Title font-size: clamp(28px, 8.5vw, 55px)

## Copy -- Current State

### S4 section (main pitch)
"Swops matches renters with renters for short breaks in each other's homes. You stay in their place while they stay in yours. All free. All private. All ruled totally legal by Judge Juicy."
Note: "totally legal" is under review -- see Legal Position below.

### s-slummer section (INCOGNITO ABODE)
Headline: INCOGNITO ABODE (static, position: absolute, bottom of section)
Eyebrow: "No public photos. No public profiles. All swops are private."

### How It Works page -- current copy
- The Call: "You choose who to chat to. It's a video call - you see their place, they see yours..."
- The Vibe: "The trust mechanism is the swap itself. You're in their home while they're in yours..."
- What About Your Lease: "People ask friends to housesit all the time without calling their landlord..."
- Bottom disclaimer removed.

## Judge Juicy

### Character
AI-generated peach-faced judge with a TOTALLY LEGAL stamp. Australian and Aboriginal flags in background. Created as a humorous legal mascot for Swops.

### Video files
- JUDGE JUICY STAMP 1-1 V4 AUDIO.mp4 -- current live version, has audio baked in
- Earlier versions (V2, V3) superseded

### Implementation
- Click-triggered overlay on the pulsating "Judge Juicy" text in S4 section
- Video plays on click, pauses and resets on dismiss (click anywhere)
- Text pulses in #a8d400 green
- Mobile: video scales to 100vw square

### Legal disclaimer (written, not yet implemented in video)
"Judge Juicy is not a judicial officer admitted to practice in any Australian state or territory. Her rulings are not legally binding in any court or tribunal. On the vibe of it though, she is correct."
(Reference: The Castle -- "on the vibe of it" -- deliberate)

### Song: Judge Juicy (Totally Legal)
Reggae song written for use with Judge Juicy video. Future plan: full AI music video. When audio is ready as separate file, use separate <audio> element + looping video.

## Legal Position

### Core argument
Housesitter framing: people ask friends to housesit all the time without calling their landlord. A swop is the same thing -- short stay, no money, someone you've met and vetted on a video call.

### Key points
- No money between parties = not subletting (commercial distinction does most of the work)
- No reported Australian case has treated a non-cash home swap as subletting
- "Clearly defensible territory" -- not case-law-settled, genuinely novel
- Video call establishes acquaintance status, strengthening the guest arrangement framing

### "Totally legal" -- current position
An overstatement. The honest position is "clearly defensible." Options: soften to "All approved by Judge Juicy" or keep with a light "we're not lawyers" footnote.

### Swop agreement clauses
1. Tenant retains keys throughout
2. Right to return -- tenant can re-enter at any time
3. No exclusive possession granted -- explicit in writing
4. Revocability -- either party can cancel at any time
5. Short fixed duration confirmed
6. Damage responsibility
7. House rules
8. No money changes hands between parties

## Pending Tasks

### Waiting on John
- **Quote revision** -- John said "i'll take a pass at the quote in the morning. it's not quite working for me as is." Once revised, update press.html and all 17 Gmail drafts before pushing.

### Banked -- Ready to Push Once Quote is Approved
- press.html (black on white, Georgia font, paragraph reorder, John Pace named + quote, fix em dash in title tag)
- Swops-Press-Release.pdf (regenerated with all above changes)

### Gmail Drafts -- To Create
After quote is finalised, create new drafts for contacts from the new media contacts list (not yet covered):
3AW Breakfast, ABC Radio Melbourne, Liz Hobday AAP, Time Out Melbourne, Sophie Aubrey The Age, Weekend Events The Age, Nick Papps Herald Sun, Nui Te Koha Herald Sun, Emma Joyce Broadsheet, Navarone Farrell Urban List, Secret Melbourne, Sitchu, 9 Honey, Melbourning, Eliza Campbell (new email)

### Gmail Drafts -- Update Existing 17
Once John's quote is finalised, update all 17 existing drafts with the correct quote and John's name.

### Research Still Needed
- Alice Griffin email (Junkee) -- TOP PRIORITY
- Michael Janda email (ABC News) -- TOP PRIORITY
- Andrew Zuccala email (Concrete Playground)

### Upcoming Build Work
- GA4 setup -- needs Measurement ID from John
- Meta Pixel setup -- needs Pixel ID from John
- Welcome email copy
- Swop agreement -- web page + downloadable PDF
- Terms/Privacy page
- Photo upload system (post-registration secure upload, no public photos)
- Judge Juicy disclaimer card (cut into video as title card)
- Judge Juicy audio separation (separate audio + looping video)
- Review "totally legal" in S4 copy
