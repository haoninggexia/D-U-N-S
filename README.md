# D-U-N-S Helper — landing site

Static site promoting an independent D-U-N-S Number lookup / application
assistance service. Deployed on GitHub Pages at
`https://haoninggexia.github.io/D-U-N-S/`.

## Pages

| File | Purpose | Language |
| --- | --- | --- |
| `index.html` | Main landing page (English) | en |
| `zh.html` | Main landing page (Chinese) | zh-CN |
| `guides/apple-developer-duns.html` | DUNS for Apple Developer enrollment | en |
| `guides/duns-number-fast.html` | "How to get DUNS fast" route comparison | en |
| `guides/duns-lookup.html` | Find an existing DUNS number | en |
| `guides/google-play-duns.html` | DUNS for Google Play organization accounts | en |
| `guides/duns-bianhao-jiaji.html` | 邓白氏编码加急时效对比 | zh-CN |
| `guides/pingguo-kaifazhe-duns.html` | 苹果企业账号 DUNS 驳回排查 | zh-CN |

Each guide targets one distinct search intent and links back to the landing
pages with a UTM-tagged CTA, so enquiries carry their acquisition source.

## Config — contacts

Open `script.js` and edit the CONFIG block at the top:

```js
const TELEGRAM_USERNAME = "haoninggexia";
const CONTACT_EMAIL = "";   // e.g. "hello@example.com"
const WECHAT_ID = "";       // e.g. "duns_helper"
const QQ_NUMBER = "";       // e.g. "123456789"
```

Empty values are simply not rendered. **Add a WeChat ID or an email address if
you want Chinese leads to convert** — Telegram alone loses most of them.
The lead form also offers a "copy the message" button that works without any
backend, so a static site can still capture enquiries.

## Source attribution

Any link into the site may carry `?utm_source=...` (or `?ref=...`). The first
value is stored in `sessionStorage` and appended to the enquiry message, and
all Telegram links get a pre-filled opener. Example:

```
https://haoninggexia.github.io/D-U-N-S/?utm_source=zhihu&utm_medium=answer
```

Use a different `utm_source` per channel to see which ones actually produce
leads. No analytics backend is required.

## Regenerating guide pages

```bash
python build_pages.py
```

`build_pages.py` holds the shared HTML template plus the content of all six
guides. To add a keyword page: copy an entry in `PAGES`, change the file name,
title, description, body and FAQ, re-run the script, then add the URL to
`sitemap.xml`. Generated HTML is committed, so GitHub Pages does not need a
build step.

## Run locally

```bash
python -m http.server 8000
# http://localhost:8000  and  http://localhost:8000/zh.html
```

## SEO assets

- `index.html` / `zh.html` — canonical + reciprocal hreflang, Open Graph,
  Twitter Card, `ProfessionalService` and `FAQPage` JSON-LD. FAQ JSON-LD
  matches the visible FAQ exactly (Google requires this).
- `guides/*.html` — `FAQPage` + `BreadcrumbList` JSON-LD, internal cross-links.
- `robots.txt`, `sitemap.xml` — 8 URLs, update `lastmod` when pages change.
- `og-image.png` — 1200x630 share image.
- Google site verification meta tag is already present in both landing pages.

### After every deploy

1. Google Search Console → URL Inspection → paste the URL → **Request indexing**
   for `index.html`, `zh.html` and each new guide.
2. Search Console → **Sitemaps** → resubmit `sitemap.xml`.
3. Bing Webmaster Tools → submit the same sitemap (feeds Bing / Yahoo and is
   reused by several other engines).
4. Baidu 资源搜索平台 → 普通收录 → 手动提交中文页面 URLs (GitHub Pages is
   reachable but Baidu indexing is slow; Chinese Q&A backlinks help more).

## Disclosure

Independent third-party assistance service. Not affiliated with, endorsed by,
or acting on behalf of Dun & Bradstreet, Apple or Google. D-U-N-S is a
registered trademark of Dun & Bradstreet. The number is assigned and maintained
by D&B. We do not sell numbers, create fictitious entities, fabricate
registration documents, or bypass verification requirements.
