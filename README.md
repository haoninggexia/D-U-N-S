# D-U-N-S Helper — Landing Site

A single-page website to promote your D-U-N-S Number application assistance service,
with a Telegram QR code on the index page so visitors can contact you directly.

## Files
- `index.html` — the page (content + layout)
- `styles.css` — styling
- `script.js` — Telegram QR code generation and config

## Set up your Telegram QR code
Open `script.js` and change the first line:

```js
const TELEGRAM_USERNAME = "your_telegram_username";
```

Replace `your_telegram_username` with your real Telegram username **without** the `@`.
For example, if your link is `https://t.me/duns_helper`, use `"duns_helper"`.

The site will then:
- Show a scannable QR code linking to `https://t.me/<your_username>`
- Display the link as text and a "Copy" button
- Point the header/footer links to your Telegram

## Run locally
Just open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

## Deploy (list on Google)
Upload the files to any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages, or your own server).

### SEO assets included
- `index.html` — enriched meta tags (canonical, robots, bilingual keywords,
  Open Graph, Twitter Card, hreflang) plus JSON-LD structured data
  (`ProfessionalService` + `FAQPage`) for rich search results.
- `robots.txt` — allows crawling and points to the sitemap.
- `sitemap.xml` — declares the page and its language alternates.
- `og-image.png` — 1200×630 branded social-share image.

### Get indexed faster (do this after every deploy)
1. Go to [Google Search Console](https://search.google.com/search-console).
2. Add the property `https://haoninggexia.github.io/D-U-N-S/` (URL-prefix).
3. Verify ownership (HTML file or meta-tag method).
4. In **Sitemaps**, submit: `sitemap.xml`.
5. In **URL Inspection**, paste the page URL and click **Request indexing**.
6. Optional but recommended: also submit the sitemap to
   [Bing Webmaster Tools](https://www.bing.com/webmasters) (powers Yahoo/Bing
   and is reused by many engines).

Tip: keep `og:image`, `canonical`, and the `sitemap.xml` URLs in sync with the
real domain if you later move off GitHub Pages.

## Notes
- The QR code is generated in the browser using the `qrcodejs` CDN library (needs internet).
- This is an assistance service and is not affiliated with Dun & Bradstreet.
