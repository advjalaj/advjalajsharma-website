# advjalajsharma.in

Website of Jalaj Sharma, Advocate (Delhi NCR). Plain static site, no build step. Hosted on Netlify, deployed automatically from the `main` branch. Domain: advjalajsharma.in (GoDaddy DNS → Netlify).

## Files
- `index.html` — home page. English by default; the English | हिंदी switch shows the whole page in one language at a time (`.e` / `.h` spans).
- `cheque-bounce-what-to-do.html`, `cheque-bounce-kya-kare.html` — English and Hindi cheque bounce articles (linked as language alternates).
- `assets/site.css`, `assets/site.js` — shared styles, language switch, disclaimer and consultation form.
- `assets/jalaj-sharma.jpg` (owner's portrait), `assets/share.jpg` (link preview), `assets/favicon.svg`.
- `backend/consultation-form.gs` — Google Apps Script that receives the consultation form: emails the details to advjalaj107@gmail.com and saves uploaded documents to a private Google Drive folder ("Website consultation requests"). Not served publicly (blocked in `netlify.toml`).
- `sitemap.xml`, `robots.txt`.

## Consultation form
The form posts to the Apps Script web-app URL set in `data-endpoint` on `<form id="cform">` in `index.html`. If empty, visitors see a message asking them to call or WhatsApp.

## Content rules
No client names or case details, no testimonials, no success claims, no "best lawyer" wording, no "free consultation" or "24/7" (Bar Council of India Rule 36). Practice described as "litigation before the courts and tribunals of Delhi NCR". Only original text and the owner's own images. Font: Hind (Google Fonts, SIL Open Font License).

## Workflow
Changes are prepared on a `preview-*` branch and shown as a preview first; they are merged to `main` (live) only after the owner approves.
