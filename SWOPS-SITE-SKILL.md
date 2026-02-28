# SWOPS SITE SKILL
Read this before doing any work on the SWOPS website.

---

## What SWOPS Is
Peer-to-peer home swapping platform for Australian renters. Verified renters exchange homes for short breaks. First swop: King's Birthday long weekend (6–8 June 2026), Melbourne ↔ Sydney only. Completely free for first wave of users. Anti-establishment, mutual aid energy — "between renters, for renters." Not another corporate platform.

---

## Brand Personality
Cheeky, confident, slightly punk. Nico's Deli energy. Speaks directly to frustrated renters. Copy is the personality — not interface gimmicks. Dry humour, plain language, no startup fluff.

---

## Site File
Single file: `/Users/yies/SWOPS/index.html`
All CSS is in a `<style>` block in the `<head>`. All JS is inline `<script>` at the bottom of `<body>`. No build tools, no frameworks, no npm. Just open in browser.

---

## Colours
- Background (primary): `#000` black
- Accent (primary): `#C8FF00` lime green
- All text is either black on lime or lime on black. No other colours.

---

## Typography
- **Body / everything**: `Alfredino` (loaded via @font-face from `SITE ASSETS/FONT/alfredino-semimono-font/alfredinosemirounded-semirounded.ttf`)
- Fallback: `sans-serif`
- Font sizes use `clamp()` for responsiveness throughout
- No other fonts. TT Trailers was considered but not used — Alfredino is the font.

---

## Image Caption / Location Overlay Convention
Text overlaid on images types on as you scroll to it — field report style. Uses `.typewriter` class with `data-text` attribute. IntersectionObserver triggers at 10% visibility. 55ms per character. Cursor blinks while typing, disappears when done. Always centred: `position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)`. Always `text-align: center`. Lime green, Alfredino font. **Font size: `clamp(22px, 2.5vw, 36px)`** — consistent across all image captions, do not deviate.

## Mobile / Responsive
Everything must be coded responsive for mobile from the start. Key rules:
- Use `clamp()` for all font sizes — already in use throughout
- Section padding should use `clamp()` too: e.g. `padding: clamp(60px, 8vw, 90px) clamp(24px, 6vw, 60px)`
- Typewriter captions: use `white-space: normal` on mobile and `text-align: center` so long strings wrap rather than overflow
- Images are inherently responsive (`width: 100%`) — no issues there
- Boomer Man animation may need to be disabled or scaled on very small screens
- Test at 390px width (iPhone) as minimum target

---


- Full-width sections stacked vertically, no sidebar layouts
- Sections alternate black and lime green backgrounds
- Images are full-bleed (`width: 100%`, `display: block`, `line-height: 0` on parent)
- Text sections use `padding: 90px 60px`, `display: flex`, `flex-direction: column`, `align-items: center`, `text-align: center`
- Max content width ~900–1200px inside text blocks
- No CSS grid or flexbox columns — everything stacks vertically

---

## Section Order (current build)
1. **Ticker tape** — sticky top, lime green, scrolling text about King's Birthday swop
2. **Hero** — full-viewport, black & white photo (man in store), SWOPS wordmark centred, Boomer Man cutout animates across
3. **S2** — lime green, headline: "You already pay for a holiday house, dummy."
4. **S3** — Ibis photo (hard-switches to boggle-eye version), "Say what now?" speech line
5. **S4** — black, copy block explaining how SWOPS works
6. **S5** — skateboarder photo, quote overlay: "Look at me. I am the house flipper now"
7. **S6** — lime green, copy: "A swop isn't a luxury holiday..."
8. **S7** — beach image sequence (3 images hard-switching, 1s each)
9. **S8** — black, registration form (NAME / EMAIL / CITY / YOUR HOUSE / YOUR IDEAL SWOP)
10. **S9** — full-bleed photo (couple eating), "Botany 2:12pm on a Sunday" centred in lime green

### Sections in mockup not yet built (from PNGs):
- Location caption sections (e.g. "Botany 2:12pm on a Sunday" + couple eating photo)
- "You've got enough lords in your life, so we're staying right out of it" copy section
- "Swanston St 4:23pm on a Friday" + Melbourne dog photo
- "Swops is about renters opening their doors to each other..." closing copy section

---

## Animation Conventions
- `steps(1, end)` for hard-cut frame switches (ibis boggle eye, beach sequence)
- Linear infinite for sliding animations (ticker, boomer man)
- Boomer Man: slides right to left across hero, `translateX(100vw)` to `translateX(-100%)`, 12s
- No easing, no fades — everything is instant/mechanical

---

## Asset Paths
All relative to `index.html`:
- Font: `SITE ASSETS/FONT/alfredino-semimono-font/alfredinosemirounded-semirounded.ttf`
- Images: `SITE ASSETS/IMAGES/[filename]`
- Wordmark: `SITE ASSETS/WORDMARK/SWOPS GREEN.png`
- Spaces in paths must be encoded as `%20` in HTML attributes

### Available images in SITE ASSETS/IMAGES:
BOOMER MAN.png, COUPLE EATING.jpeg, GIRL-SKATEBOARD.jpg, IBIS-2.jpg, IBIS-BOGGLE-2.jpg, IBIS-BOGGLE-FIXED.jpg, IBIS.jpeg, MAN BEACH 1.jpg, MAN BEACH 2.jpg, MAN STORE 1.jpg, MAN-STORE-4.jpg, MELBOURNE DOG.jpeg, WOMAN BEACH.jpeg

---

## Form (S8)
Fields: Name, Email, City (Melbourne/Sydney dropdown), Your house (textarea), Your ideal swop (textarea).
Styled as: fields separated by thin `1px` lime green horizontal lines, no input borders/boxes, Alfredino text, transparent background. Submit button: lime green background, black text, "I'M IN". On submit: form hides, success message appears.

---

## What NOT to Do
- Don't add new fonts
- Don't add purple, gradients, drop shadows, border-radius on inputs
- Don't add modals, accordions, or JS-heavy UI patterns
- Don't suggest a separate CSS file or build pipeline
- Don't use Inter, Roboto, or any Google Font
- Don't add headers/navbars — the ticker tape is the nav
- Don't make it look like a startup SaaS product

---

## Legal Language & Copy Guidelines

### Approved disclaimer copy (long form)
SWOPS is a matching service, not a tenancy product. Before you register for a swop, check your lease for any clauses about short-term guests or third-party access. If you're unsure, ask your property manager — framing it as "a friend staying while I'm away" is often the easiest approach. SWOPS doesn't provide legal advice and can't review your lease for you.

### Approved disclaimer copy (short — for site)
Check your lease before you swop. Most short-term guest stays are fine — but your lease is your responsibility, not ours.

### Approved terms/registration language
By registering, you confirm you have reviewed your tenancy agreement and satisfied yourself that participating is consistent with your obligations as a tenant. SWOPS facilitates introductions between renters; it does not create, modify, or take responsibility for any tenancy arrangement.

### Language to Avoid in All Copy

| Avoid | Why | Use instead |
|-------|-----|-------------|
| "Swap your home / house" | Implies exchange of property rights | "Stay in someone's place while they stay in yours" |
| "List your home" | Airbnb language; implies commercial offering | "Register your place" |
| "Host" / "guest" as fixed roles | Implies one-way arrangement | "Swopmates" — both are guests simultaneously |
| "Rent-free stay" | Could imply the stay substitutes for rent | "Stay without accommodation costs" |
| "Unlock the value of your rental" | Attractive copy but implies extracting value from a leased asset | "Make your rent work harder" or just "$100 holidays" |
| "Short-term accommodation" | Legal trigger phrase in most states | "A change of scene" / "a few nights away" |
| "Property" in agreement context | Signals a property transaction | "Home" — warmer and legally softer |
| Any mention of "exclusive" access | Directly maps to the exclusive possession test | "Access to" — with retained key language explicit |
