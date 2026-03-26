# SWOPS SITE SKILL
Read this before doing any work on the SWOPS website.

---

## What SWOPS Is
Peer-to-peer home swapping platform for Australian renters. SWOPS privately matches renters with renters for short breaks in each other's homes. You stay in their place while they stay in yours — simultaneously, same weekend. No public listings. No public profiles. Between renters, for renters.

**First swop:** King's Birthday long weekend, 6-8 June 2026. Melbourne + Sydney. Intra-city swops only to start — cross-river, cross-town — before opening up interstate.

**Free for first wave.** No fees for King's Birthday drop. Future swops will cost a flat $100 per house.

**Legal framing:** Exchanges are "reciprocal guest stays" — simultaneous, non-commercial, reciprocal. NOT subletting. NOT Airbnb. The platform is a matching service, not a tenancy product.

**Protection fund:** $5,000 seeded by founders. Up to $500 per incident for minor damage that can't be resolved between swoppers. Discretionary, not insurance.

---

## Brand Personality
Cheeky, confident, slightly punk. Nico's Deli energy. Speaks directly to frustrated renters who are paying a lot and getting the raw end of the deal — NOT people in housing stress. Dry humour, plain language, no startup fluff. Anti-establishment without being aggressive. Copy is the personality — not interface gimmicks.

**Never say:** "innovative," "seamless," "community-driven," "disrupting," or any aspirational startup language.
**Never use:** Oxford commas. Em dashes — use a regular dash instead.
**Never say "drop"** — say "swop" instead (except the one sneaker reference on the how-it-works page).
**Say "swoppers"** — double p.

---

## File Structure
```
/Users/yies/SWOPS/
├── index.html          — main single-page site
├── how-it-works.html   — explanation page, linked from S4
├── pricing.html        — "Free For Now" page
├── register.html       — standalone registration form
├── success.html        — post-registration success page
├── SWOPS-SITE-SKILL.md — this file
├── SWOPS-STRATEGY.md   — business strategy reference
├── SWOPS_Legal_Analysis.md — legal position reference
└── SITE ASSETS/
    ├── FONT/alfredino-semimono-font/alfredinosemirounded-semirounded.ttf
    ├── IMAGES/         — see image list below
    └── WORDMARK/SWOPS GREEN.png
```

All CSS is in a `<style>` block in `<head>`. All JS is inline `<script>` at bottom of `<body>`. No build tools, no frameworks, no npm. Edit with Desktop Commander edit_block tool.

**Deployed:** GitHub → Netlify auto-deploy. GitHub: https://github.com/ArllaAlways/swops. Live: swops.it. Push to deploy — costs Netlify credits, so batch changes before pushing.

---

## Colours
- Background (primary): `#000` black
- Accent (primary): `#C8FF00` lime green
- All text is either black on lime or lime on black. No other colours. No gradients. No purple. No shadows.

---

## Typography
- **One font only:** `Alfredino` loaded via @font-face
- Path: `SITE ASSETS/FONT/alfredino-semimono-font/alfredinosemirounded-semirounded.ttf`
- Fallback: `sans-serif`
- **All body copy is the same size:** `clamp(20px, 2.4vw, 34px)` — do not deviate for body text
- Section labels (how-it-works page): `clamp(13px, 1vw, 16px)` uppercase, 0.5 opacity
- Image captions/typewriter: `clamp(22px, 2.5vw, 36px)` — consistent, do not deviate
- Font sizes use `clamp()` for responsiveness throughout — no fixed px sizes for text

---

## Section Order (index.html — current build)
1. **Ticker** — sticky top, lime bg, scrolling: "First swop Kings Birthday long weekend 6-8 June 2026  Melbourne + Sydney  More dates TBC"
2. **Hero** — full-viewport, woman in store + man in store hard-switching, SWOPS wordmark centred, Boomer Man cutout slides right-to-left
3. **S2** — lime bg, headline: "If you rent, you already pay for a holiday house, dummy. / You just can't use it yet."
4. **S3** — Ibis photo hard-switching to boggle-eye version, "Say what now?" caption
5. **S4** — black bg, copy: "SWOPS privately matches renters with renters for short breaks in each other's homes. You stay in their place while they stay in yours. / We're starting with intra-city swops to begin - cross-river, cross-town - before we open up interstate. / No public listings. No public profiles. No fees. Between renters, for renters." + "How it works" button → how-it-works.html
6. **S5** — skateboarder photo (two-frame animation), typewriter: "Look at me. I am the house flipper now"
7. **S6** — lime bg, copy: "A swop isn't a luxury holiday. It's waking up in St Kilda instead of Brunswick for a weekend and seeing what happens. It's going to bed in Katoomba when your bedroom is in Bronte. / Because why not? You already paid for accom." + typewriter: "LET YOUR RENT TAKE YOU PLACES."
8. **S7** — beach 3-image sequence hard-switching, typewriter: "North Coast 11:40am on a Monday"
9. **S10a** — black bg, copy: "You've got enough lords in your life, so we're staying right out of it. / The spirit of Swops is peer-to-peer reciprocity..." + Jay Z quote
10. **S9** — couple eating photo, typewriter: "Botany 2:12pm on a Sunday"
11. **RALLY** — lime bg (reuses s2 class), copy: "Australian housing is rigged against renters. / Let's at least get some free accom out of it."
12. **S11** — Melbourne dog photo, typewriter: "Swanston St 4:23pm on a Friday"
13. **S8** — black bg, registration form + disclaimer
14. **S10b** — PARKED/empty, content moved to how-it-works.html

---

## Available Images
Path prefix: `SITE ASSETS/IMAGES/` — encode spaces as `%20` in HTML

| File | Used in |
|------|---------|
| BOOMER MAN.png | Hero animation |
| WOMAN STORE.jpeg | Hero bg 1 |
| MAN STORE 1.jpg | Hero bg 2 |
| IBIS-2.jpg | S3 base |
| IBIS-BOGGLE-2.jpg | S3 boggle (desktop) |
| IBIS-9-16.jpg | S3 base (mobile) |
| IBIS-BOGGLE-V2-9-16.jpg | S3 boggle (mobile) |
| GIRL-SKATEBOARD.jpg | S5 frame 1 |
| GIRL-SKATEBOARDING-LICK-2.jpg | S5 frame 2 |
| MAN BEACH 1.jpg | S7 frame 1 |
| WOMAN BEACH.jpeg | S7 frame 2 |
| MAN BEACH 2.jpg | S7 frame 3 |
| COUPLE EATING.jpeg | S9 desktop |
| COUPLE EATING MOBILE.jpeg | S9 mobile |
| MELBOURNE DOG.jpeg | S11 desktop |
| MAN-DOG-MOBILE-9-16.jpg | S11 mobile |

Unused but available: IBIS-BOGGLE-FIXED.jpg, IBIS-BOGGLE-9-16.jpg, IBIS BOGGLE EYE.jpeg, IBIS.jpeg, MAN-STORE-4.jpg, GIRL SKATEBOARD UPSCALEDGIRL-SKATEBOARD.jpg, GIRL SKATEBOARDING LICK.jpeg, MELBOURNE-DOG-MOBILE.jpg

---

## Navigation (Hamburger Menu)
Fixed top-right. Opens full-screen overlay. Links:
1. How it works → how-it-works.html
2. Pricing → pricing.html
3. Register Interest → #register (anchor on S8)
4. How we got here → about overlay (founder story, currently parked)

JS closes menu when any `<a>` link is clicked.

---

## Animation Conventions
- `steps(1, end)` for all hard-cut frame switches (ibis, beach, skateboarder, hero backgrounds)
- `linear infinite` for sliding animations (ticker, boomer man)
- No easing, no fades — everything is instant/mechanical
- IntersectionObserver at 10% visibility triggers typewriter, 55ms per character

### Boomer Man (hero)
- Slides right to left: `translateX(100vw)` → `translateX(-100%)`
- Desktop: 12s cycle
- Mobile: 10s cycle, `animation-delay: -2s` (enters frame earlier)
- JS sync: animations only start after boomer PNG confirmed loaded (`.hero-ready` class added to `.hero` section)
- All three animations (boomer, bg1, bg2) start simultaneously via JS
- Mobile background switch at 47% of cycle

### Hero backgrounds
- Desktop: 12s, switch at 47.5%
- Mobile: 10s, switch at 47%, `animation-delay: -2s` (matches boomer)

---

## Form (S8 — Registration)
Fields: Name, Email, Your suburb (text input), Your house (textarea), Your ideal swop (textarea).
Styled as: fields separated by `1px` lime green horizontal lines, no input borders/boxes, Alfredino text, transparent background. Submit: lime bg, black text, "I'M IN". On submit: form hides, success message appears. Netlify form with `name="registration"` and `action="/success"`.

---

## Other Pages

### how-it-works.html
Black bg, Alfredino, lime text. Sections separated by faint dividers. Sections: How it works / What's a swop window? / The match / The call / The swop / What it costs / A note on your lease. CTA button: "I'm in" → index.html#register.

### pricing.html
Black bg. Headline: "Free For Now". Body: "Swops are free for our first wave of friends. We'll get to money later, but for now we just want to hang out at yours and you at ours."

### register.html
Standalone version of the registration form. Same styling as S8.

---

## Known Issues / To Do
- S4 "Get matched with someone in your city" — should say "your suburb" (not yet updated in how-it-works.html flow text)
- About overlay ("How we got here") — founder story is parked/hidden, needs rewriting before re-enabling
- Register Interest nav link was previously broken — fixed with `#register` anchor and JS closes menu on link click — confirm working
- Font size normalisation done on index.html — check how-it-works.html and other pages are consistent
- No `$100` pricing anywhere now — all references removed, confirm clean across all pages

---

## What NOT to Do
- Don't add new fonts
- Don't add purple, gradients, drop shadows, or border-radius on inputs
- Don't add modals, accordions, or JS-heavy UI patterns
- Don't suggest a separate CSS file or build pipeline
- Don't use Inter, Roboto, or any Google Font
- Don't add headers/navbars — the ticker tape is the nav
- Don't make it look like a startup SaaS product
- Never use Oxford commas
- Never use em dashes — use a regular dash instead
- Don't use the word "drop" — say "swop"
- Don't say "swap" in legal copy — say "reciprocal guest stay" or "short stay"
- Don't say "most leases" — say "many leases"
- Don't use "exclusive access" — maps to exclusive possession test
- Don't use "short-term accommodation" — legal trigger phrase
- Don't use "host" / "guest" as fixed roles — both are swoppers

---

## Legal Language Quick Reference

### Short disclaimer (site footer/form)
"Check your lease before you swop. Many short-term guest stays are fine, but your lease is your responsibility, not ours."

### Terms/registration language
"By registering, you confirm you have reviewed your tenancy agreement and satisfied yourself that participating is consistent with your obligations as a tenant. SWOPS facilitates introductions between renters; it does not create, modify, or take responsibility for any tenancy arrangement."

### Full legal doc
See SWOPS_Legal_Analysis.md for detailed analysis of subletting vs guest stay distinction, Swan v Uecker precedent and why it doesn't apply, HomeExchange comparable, and key risks.
