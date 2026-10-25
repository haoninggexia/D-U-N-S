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
Upload the three files to any static host:
- GitHub Pages, Netlify, Vercel, Cloudflare Pages, or your own web server.
- Submit the site to Google Search Console and request indexing so it appears in search.

## Notes
- The QR code is generated in the browser using the `qrcodejs` CDN library (needs internet).
- This is an assistance service and is not affiliated with Dun & Bradstreet.
