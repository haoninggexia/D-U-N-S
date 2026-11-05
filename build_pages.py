# -*- coding: utf-8 -*-
"""
build_pages.py — regenerate the long-tail guide pages for D-U-N-S Helper.

Usage:  python build_pages.py
Output: guides/*.html  (committed to the repo, so GitHub Pages needs no build step)

To add a new keyword page: copy one entry in PAGES, change the file name,
title, description, body and FAQ, then re-run this script and add the URL
to sitemap.xml (or re-run with UPDATE_SITEMAP = True).
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://haoninggexia.github.io/D-U-N-S/"

HOME = "index.html"
ZH = "zh.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="{{LANG}}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{TITLE}}</title>
  <meta name="description" content="{{DESC}}" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <link rel="canonical" href="{{CANONICAL}}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="D-U-N-S Helper" />
  <meta property="og:title" content="{{TITLE}}" />
  <meta property="og:description" content="{{DESC}}" />
  <meta property="og:url" content="{{CANONICAL}}" />
  <meta property="og:image" content="{{BASE}}og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{{TITLE}}" />
  <meta name="twitter:description" content="{{DESC}}" />
  <meta name="twitter:image" content="{{BASE}}og-image.png" />
  <meta name="theme-color" content="#0b1f3a" />
  <link rel="stylesheet" href="{{PREFIX}}styles.css" />
  <link rel="stylesheet" href="{{PREFIX}}article.css" />
  <script type="application/ld+json">
{{FAQ_JSON}}
  </script>
  <script type="application/ld+json">
{{BREADCRUMB_JSON}}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{{PREFIX}}{{HOME}}">D&#8209;U&#8209;N&#8209;S<span>Helper</span></a>
      <nav class="nav">
        <a href="{{PREFIX}}{{HOME}}#compare">{{NAV_COMPARE}}</a>
        <a href="{{PREFIX}}{{HOME}}#guides">{{NAV_GUIDES}}</a>
        <a href="{{PREFIX}}{{HOME}}#pricing">{{NAV_PRICING}}</a>
        <a class="lang-switch" href="{{PREFIX}}{{ZH}}">{{NAV_LANG}}</a>
        <a class="nav-cta" href="{{CTA_LINK}}">{{NAV_CTA}}</a>
      </nav>
    </div>
  </header>

  <main class="container article-wrap">
    <div class="breadcrumb"><a href="{{PREFIX}}{{HOME}}">{{CRUMB_HOME}}</a><span>&rsaquo;</span><a href="{{PREFIX}}{{HOME}}#guides">{{CRUMB_GUIDES}}</a><span>&rsaquo;</span>{{SHORT_TITLE}}</div>

    <article class="article">
      <header class="article-head">
        <h1>{{H1}}</h1>
        <p class="article-lead">{{LEAD}}</p>
        <p class="article-meta">D-U-N-S Helper &middot; {{UPDATED_LABEL}} {{DATE}} &middot; {{READ_TIME}} {{MIN_LABEL}}</p>
      </header>

{{BODY}}

      <div class="article-cta">
        <h2>{{CTA_H2}}</h2>
        <p>{{CTA_P}}</p>
        <a class="btn btn-primary" href="{{CTA_LINK}}">{{CTA_BTN}} &rarr;</a>
      </div>

      <section class="article-faq">
        <h2>{{FAQ_HEADING}}</h2>
        <div class="faq-list">
{{FAQ_HTML}}
        </div>
      </section>

      <section class="related">
        <h2>{{RELATED_HEADING}}</h2>
        <ul>
{{RELATED_HTML}}
        </ul>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <div>
        <div class="brand">D&#8209;U&#8209;N&#8209;S<span>Helper</span></div>
        <p class="footer-note">Independent assistance service for D-U-N-S Number lookup and applications. Not affiliated with Dun &amp; Bradstreet, Apple or Google.</p>
        <p class="footer-links"><a href="{{PREFIX}}{{HOME}}">Home</a> · <a href="{{PREFIX}}{{ZH}}">中文页面</a> · <a href="{{PREFIX}}{{HOME}}#compliance">Disclosure</a></p>
      </div>
      <div class="footer-contact">
        <p>Get in touch:</p>
        <a class="tg-link" href="https://t.me/haoninggexia" target="_blank" rel="noopener">t.me/haoninggexia</a>
        <p class="tg-phone-footer">+86 189 5314 7694 (Telegram)</p>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>&copy; <span id="year"></span> D-U-N-S Helper. All rights reserved.</span>
      <span><a href="{{PREFIX}}{{HOME}}#compliance">Disclosure</a></span>
    </div>
  </footer>
  <script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Content. Each page targets ONE search intent. Bodies are intentionally
# different (no spun template text) — thin doorway pages get filtered by Google.
# ---------------------------------------------------------------------------
PAGES = [
{
  "file": "guides/apple-developer-duns.html",
  "lang": "en",
  "short": "Apple Developer D-U-N-S",
  "title": "D-U-N-S Number for Apple Developer Program: Timing, Rules & Rejections",
  "h1": "D-U-N-S Number for the Apple Developer Program",
  "lead": "Enrolling as an organization means Apple verifies your legal entity against the Dun & Bradstreet database. Here is exactly what it checks, how long each route takes, and why a valid-looking number still gets rejected.",
  "desc": "Apple Developer Program organization enrollment requires a D-U-N-S Number. Learn the real timelines (30 / 8 / 5 business days), the exact-match rules, and how to fix common DUNS rejections.",
  "date": "November 2026",
  "read": 6,
  "cta_h2": "Stuck on Apple's organization enrollment?",
  "cta_p": "Send us your company legal name and country. We check whether a record already exists and confirm the realistic timeline before you pay anything.",
  "cta_btn": "Check my company",
  "body": """
<h2>Why Apple asks for a D-U-N-S Number</h2>
<p>When you enroll in the Apple Developer Program as an <strong>organization</strong> rather than an individual, Apple has to confirm that the entity signing its legal agreements actually exists. Instead of building its own worldwide company registry, Apple validates your details against the Dun &amp; Bradstreet (D&amp;B) database using the nine-digit D-U-N-S Number.</p>
<p>Apple is explicit about who qualifies: your business must be a legal entity (a corporation, limited liability company, limited partnership and so on). <strong>DBA names, trade names, fictitious businesses and branches are not accepted.</strong> Individual developer accounts do not need a D-U-N-S Number at all. Government organizations may opt out.</p>
<p>This is why the number is a gating item: no valid, matching D-U-N-S record means no organization account, which means no App Store publishing under a company name and no team member management.</p>

<h2>Where the number actually comes from</h2>
<p>The D-U-N-S Number is assigned and maintained by Dun &amp; Bradstreet, not by Apple. Apple's own support page tells you to <em>look up your organization first</em> — D&amp;B may already have assigned one for free — and only submit a request if no record is found. The lookup asks for the legal entity name, headquarters address, mailing address and a work contact.</p>
<div class="callout"><p><strong>Most teams skip this step.</strong> They assume they need a brand-new number, submit a fresh application, and then wait weeks for D&amp;B to re-verify a record that may already exist. Checking first is the single highest-leverage thing you can do.</p></div>

<h2>The three timelines nobody puts in the same table</h2>
<div class="table-scroll"><table>
<thead><tr><th>Route</th><th>Typical time</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>D&amp;B standard free application</td><td>Up to 30 business days</td><td>Free</td></tr>
<tr><td>D&amp;B paid expedite (offered at checkout)</td><td>Up to 8 business days</td><td>About $229</td></tr>
<tr><td>Apple's D-U-N-S lookup / request channel</td><td>Up to 5 business days to receive the number</td><td>Free</td></tr>
<tr><td>Locate an already-existing record</td><td>Often minutes</td><td>Assistance fee, if you use a service</td></tr>
</tbody></table></div>
<p>Apple's Chinese support page adds one detail many paid "expediting" offers quietly omit: <strong>expediting the D-U-N-S creation process does not shorten the wait</strong> Apple describes. In other words, paying to rush a form does not necessarily move you to the front of the queue.</p>
<p>Even after you have the nine digits, allow time for the record to propagate before Apple can validate it, and remember Apple runs its own review on top. Budget a buffer rather than planning a launch around a best case.</p>

<h2>Why Apple rejects a number that looks valid</h2>
<ul>
<li><strong>Name mismatch.</strong> The legal name in your Apple enrollment must match the D&amp;B record. A translated name, an abbreviation or a pinyin-only version is a classic cause of "unable to verify".</li>
<li><strong>Address mismatch.</strong> A D-U-N-S Number identifies an entity <em>at a specific location</em>. Using a headquarters number for a branch, or an old registered address, can fail validation.</li>
<li><strong>Wrong entity type.</strong> Sole proprietors, DBAs and branches are not accepted for organization enrollment.</li>
<li><strong>Someone else's number.</strong> Copying a parent company's or a partner's D-U-N-S will not pass.</li>
<li><strong>Too fresh.</strong> A newly created record may not yet be visible to Apple's verification system.</li>
<li><strong>Unreachable contact.</strong> D&amp;B may phone to confirm business type, headcount or registration documents. A missed call restarts the clock.</li>
</ul>

<h2>A checklist before you press Enroll</h2>
<ol>
<li>Search for an existing record under the <em>exact</em> registered legal name.</li>
<li>Confirm the English legal name, street address, city, province/state and postcode match your registration documents character for character.</li>
<li>Use a work email and a phone number that will actually be answered during business hours.</li>
<li>Confirm the entity type is a legal entity, not a DBA or branch.</li>
<li>Have the business registration document ready in case D&amp;B calls.</li>
<li>Wait for the record to sync before submitting the Apple form; do not resubmit repeatedly.</li>
</ol>
<div class="callout warn"><p><strong>Do not submit duplicate applications.</strong> A second request while the first is pending can freeze the case or create conflicting records — the opposite of what you need when you have a deadline.</p></div>

<h2>If you are blocked right now</h2>
<p>Start by establishing which of two situations you are in: the record exists but you cannot find it, or it genuinely does not exist yet. The fixes are completely different. An existing-record lookup is usually fast; a genuinely new D&amp;B record is bound by D&amp;B's own verification timeline and no third party can honestly promise otherwise.</p>
<p class="source-list">Official references: <a href="https://developer.apple.com/support/D-U-N-S/" target="_blank" rel="nofollow noopener">Apple Developer — D-U-N-S Number</a> · <a href="https://developer.apple.com/cn/support/D-U-N-S/" target="_blank" rel="nofollow noopener">Apple 开发者 — D-U-N-S 编号（中文）</a> · <a href="https://www.dnb.com/en-us/smb/duns/get-a-duns.html" target="_blank" rel="nofollow noopener">D&amp;B — How to Get a D-U-N-S Number</a></p>
""",
  "faq": [
    ("Is a D-U-N-S Number required for an individual Apple Developer account?", "No. It is only required when enrolling as an organization (company or educational institution). Individual accounts do not need one."),
    ("How long until Apple can validate my D-U-N-S Number?", "D&B may take up to 5 business days to issue a number through Apple's channel, and a newly created record needs time to propagate before Apple's verification can see it. Apple then runs its own review."),
    ("Can I use my parent company's D-U-N-S Number?", "No. Apple validates the legal entity that is signing the agreement. A number belonging to a different entity or a different physical location will be rejected."),
    ("Is the Apple D-U-N-S Number different from a normal one?", "No. There is one D&B database and one number per entity per location. The same number is used for Apple, Google Play, supplier onboarding and tenders."),
    ("Does paying D&B for expedited service guarantee a faster Apple approval?", "D&B's expedited option shortens its own processing to about 8 business days, but Apple states that expediting the D-U-N-S creation process does not shorten the wait it describes. Apple's review is separate."),
  ],
},
{
  "file": "guides/duns-number-fast.html",
  "lang": "en",
  "short": "Get a DUNS fast",
  "title": "How to Get a D-U-N-S Number Fast (2026): 4 Routes Compared",
  "h1": "How to Get a D-U-N-S Number Fast",
  "lead": "The free official route can take 30 business days. But in most cases the delay is not D&B being slow — it is people applying for a number their company already has. Here is how to tell which situation you are in.",
  "desc": "Compare all four ways to get a D-U-N-S Number fast in 2026: D&B free (30 days), D&B expedite (8 days / ~$229), Apple's lookup channel (5 days), and finding an existing record in minutes.",
  "date": "November 2026",
  "read": 6,
  "cta_h2": "Find out which route applies to you",
  "cta_p": "One message with your company name and country is enough for us to confirm whether a fast route is realistic for your entity — before any payment.",
  "cta_btn": "Check eligibility",
  "body": """
<h2>First: are you applying, or looking up?</h2>
<p>This is the question that decides everything. Dun &amp; Bradstreet maintains a global database of business records, and it assigns D-U-N-S Numbers to entities as part of building that database — often without the business owner ever being told. A large share of companies that "need a DUNS number" simply need to <strong>find the one they already have</strong>.</p>
<p>If a record exists, no application, no verification call and no 30-day wait is required. If it genuinely does not exist, D&amp;B must create and authenticate a new record, and that process has a floor no third party can remove.</p>

<h2>All four routes, side by side</h2>
<div class="table-scroll"><table>
<thead><tr><th>Route</th><th>Time</th><th>Cost</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>D&amp;B free application</td><td>Up to 30 business days</td><td>$0</td><td>No deadline, brand-new entity</td></tr>
<tr><td>D&amp;B expedited option (shown at checkout)</td><td>Up to 8 business days</td><td>~$229</td><td>New entity with a real deadline</td></tr>
<tr><td>Apple Developer lookup / request channel</td><td>Up to 5 business days</td><td>$0</td><td>Only while enrolling in Apple's program</td></tr>
<tr><td>Locate &amp; validate an existing record</td><td>Often minutes</td><td>Assistance fee if outsourced</td><td>Most registered companies</td></tr>
</tbody></table></div>
<p>Costs and timelines above come from D&amp;B's own "How to Get a D-U-N-S Number" page and Apple's D-U-N-S support page. D&amp;B also notes that a representative may call to validate your information before the number is emailed to you.</p>

<h2>Why the free route takes so long</h2>
<p>The form itself takes a few minutes. The wait is verification: matching the legal name against registration records, confirming the physical address, possibly calling the business, de-duplicating against existing records, then creating and propagating the new entry. Any mismatch sends you back to the start. That is why "fill the form perfectly" advice only helps so much.</p>
<div class="callout"><p><strong>Reframe the cost.</strong> If a $50,000 contract or an App Store launch is blocked, the relevant number is not the $0 fee of the free form — it is the value of three to six weeks of delay.</p></div>

<h2>When a fast route does NOT apply</h2>
<p>Be skeptical of anyone promising "instant DUNS" in every case. A genuinely fast outcome usually depends on at least one of these being true, and a reputable service will check before charging:</p>
<ul>
<li>The company already has a D&amp;B record that can be located and validated.</li>
<li>The legal name, address and registration details are consistent and verifiable.</li>
<li>The entity is a real, active legal entity (not a DBA, branch or shell).</li>
<li>The jurisdiction has adequate D&amp;B coverage.</li>
<li>No D&amp;B verification call or additional documentation is required for that case.</li>
</ul>
<p>If a new record really is required, the honest answer is the D&amp;B timeline. We state that up front rather than after payment.</p>

<h2>A 60-second decision guide</h2>
<ol>
<li><strong>Already have a vendor portal, government filing, or past D&amp;B email?</strong> Search there first — the number may be in an old PDF.</li>
<li><strong>Applying for Apple as an organization?</strong> Use Apple's lookup before D&amp;B's general form.</li>
<li><strong>Brand-new company, no deadline?</strong> Submit the free D&amp;B application and get the details exactly right.</li>
<li><strong>Brand-new company, hard deadline?</strong> Consider D&amp;B's own expedited option, then plan for Apple/Google's separate verification time.</li>
<li><strong>Deadline this week and unsure whether a record exists?</strong> Get the existence question answered first. It is the only step that can compress weeks into minutes.</li>
</ol>

<h2>What you need ready, whichever route you take</h2>
<p>Legal business name (exactly as registered), registered address including postcode, business phone, owner / legal representative name, legal structure, year established, primary industry and employee count. For non-English registrations, prepare a consistent English rendering — inconsistent translations are one of the most common causes of verification delays.</p>
<div class="callout warn"><p>Avoid submitting a second application while the first is pending. Duplicate requests can freeze the case, and a D-U-N-S Number is permanent — it does not expire and is not reissued on request.</p></div>
""",
  "faq": [
    ("What is the fastest legitimate way to get a D-U-N-S Number?", "If your company already has a D&B record, locating and validating it is the fastest legitimate route and can take minutes. If a new record must be created, D&B's own expedited option is about 8 business days."),
    ("Is the D-U-N-S Number free?", "Yes. D&B issues the standard number free of charge. Fees come from optional expedited processing or from third-party lookup and assistance services."),
    ("Can a third party really get a brand-new D-U-N-S Number instantly?", "No. A new record is created and authenticated by D&B. Any service claiming to bypass that for a genuinely new entity should be treated with caution."),
    ("Does a D-U-N-S Number expire?", "No. It is a permanent identifier for a business entity at a location, though D&B may mark a record inactive if the business closes or changes structure."),
    ("Is DUNS the same as a UEI or an EIN?", "No. The US federal government replaced DUNS with the UEI for SAM.gov in 2022, and an EIN is a tax ID. DUNS remains the identifier used by Apple, Google Play and many international procurement processes."),
  ],
},
{
  "file": "guides/duns-lookup.html",
  "lang": "en",
  "short": "Find existing DUNS",
  "title": "How to Find Your Existing D-U-N-S Number (Free Lookup Guide)",
  "h1": "How to Find a D-U-N-S Number You Already Have",
  "lead": "Dun & Bradstreet assigns D-U-N-S Numbers while building its business database. Many companies discover they have had one for years. Here is where to look, how to verify it is the right one, and what to do if the search returns nothing.",
  "desc": "Most registered companies already have a D-U-N-S Number. Learn the free places to look it up, how to verify entity/address match, and what to do when the D&B or Apple lookup returns no result.",
  "date": "November 2026",
  "read": 5,
  "cta_h2": "Can't find your record?",
  "cta_p": "Send us the exact legal name and country. We check for an existing record and confirm the timeline before you decide anything.",
  "cta_btn": "Look up my company",
  "body": """
<h2>Why you may already have one</h2>
<p>A D-U-N-S Number is not something a business necessarily "applies for". It is D&amp;B's identifier for a legal entity at a specific location, created as part of maintaining a global business database. Records are frequently created from public registrations, credit and trade data, or because a customer, lender or platform requested verification. The owner is rarely notified.</p>
<p>D&amp;B's own guidance says: <strong>before you register, check whether you already have one.</strong> It will not issue a duplicate. Apple gives the same advice for organization enrollment.</p>

<h2>Six places to look before you apply</h2>
<ol>
<li><strong>D&amp;B's free D-U-N-S lookup tool</strong> — search by legal name, address or phone. Try both the full legal name and any historical name.</li>
<li><strong>Apple's D-U-N-S lookup</strong> during organization enrollment — it searches the same D&amp;B data and can surface the number directly.</li>
<li><strong>Old emails from D&amp;B</strong> — search your inbox and the previous owner's/accountant's inbox for "D-U-N-S", "D&B" or a nine-digit number.</li>
<li><strong>Vendor onboarding paperwork</strong> — supplier questionnaires, W-9 equivalents, credit applications and procurement portals often record it.</li>
<li><strong>Invoices, contracts and tender documents</strong> — especially from multinationals, US government-related work or international logistics.</li>
<li><strong>Your company website footer or About page</strong> — some firms publish their DUNS for credibility.</li>
</ol>
<div class="callout"><p>Search by <em>address and phone</em> as well as by name. A lookup commonly fails because the name on file uses a different English translation or a former registered name, while the address still matches.</p></div>

<h2>How to verify the number is the right one</h2>
<p>Finding nine digits is not the same as having a usable number. Check four things:</p>
<ul>
<li><strong>Entity:</strong> the record belongs to the legal entity that will sign the agreement, not a parent, subsidiary, branch or former company.</li>
<li><strong>Location:</strong> D-U-N-S is assigned per physical location. A different registered address may need a different number.</li>
<li><strong>Name and address format:</strong> what is in D&amp;B must match what you type into Apple / Google / a vendor form, character for character.</li>
<li><strong>Status:</strong> the record should be active and its details current. Outdated details can be corrected through D&amp;B's D-U-N-S Manager or support.</li>
</ul>

<h2>If the lookup returns nothing — or the wrong company</h2>
<p>Try the full legal name exactly as registered, historical names, and alternate English transliterations. If a similarly named company appears, do not use its number; a wrong entity is worse than no number. If there is genuinely no record, you are in the "new record" path: D&amp;B must create and authenticate it, which takes up to 30 business days free or about 8 business days with D&amp;B's paid expedite.</p>
<div class="callout warn"><p>Do not fire off a duplicate application while an earlier request is pending. Duplicate or conflicting requests can freeze the case for days and may create messy records that later cause Apple verification failures.</p></div>

<h2>What to send someone who is helping you</h2>
<p>To make a lookup actually work, prepare: the exact registered legal name (and its English rendering), registered address with postcode, business phone, country, and what you need the number for. The last item matters because Apple, Google Play and procurement portals each validate slightly different fields.</p>
""",
  "faq": [
    ("Is the D-U-N-S lookup free?", "Yes. D&B offers a free lookup tool, and Apple's lookup during organization enrollment is free too. Third-party services charge for convenience, verification and support."),
    ("Why can't I find my company in the D&B database?", "Common reasons are a name that differs from the registered version, an outdated address or phone, a very new company, or limited D&B coverage in your jurisdiction. Try searching by address and phone."),
    ("Can one company have more than one D-U-N-S Number?", "Each physical location of a business can have its own number. One legal entity at one address should normally have one."),
    ("Can I use a D-U-N-S Number I found on another company's website?", "No. It identifies that legal entity only, and platform verification will reject a mismatch."),
    ("My D&B record has the wrong address. What now?", "Request an update through D&B's D-U-N-S Manager or contact D&B support. Allow time for the change to propagate before submitting it to Apple or Google."),
  ],
},
{
  "file": "guides/google-play-duns.html",
  "lang": "en",
  "short": "Google Play DUNS",
  "title": "D-U-N-S Number for Google Play: Organization Account Verification",
  "h1": "D-U-N-S Number for Google Play Developer Accounts",
  "lead": "Google verifies organization developers against the same Dun & Bradstreet database Apple uses. If you are registering a Play Console account under a company name, here is what gets checked and how to avoid a stalled verification.",
  "desc": "Does Google Play require a D-U-N-S Number? What organization developer accounts must provide, which details Google verifies, typical timelines, and fixes for failed verification.",
  "date": "November 2026",
  "read": 5,
  "cta_h2": "Play Console verification stuck?",
  "cta_p": "Send us your legal entity name and country. We confirm whether a matching D&B record exists and what timeline is realistic.",
  "cta_btn": "Check my company",
  "body": """
<h2>Does Google Play require a D-U-N-S Number?</h2>
<p>For <strong>organization</strong> developer accounts, Google asks for a D-U-N-S Number as part of verifying that the business behind the account is real. Personal / individual developer accounts do not need one. Google has been tightening identity verification for organization accounts over the last few years, so a D-U-N-S Number is now a practical prerequisite for publishing under a company name.</p>
<p>As with Apple, the number is not issued by Google. It comes from the Dun &amp; Bradstreet database, and Google validates the details you supply against that record.</p>

<h2>What gets verified</h2>
<ul>
<li><strong>Legal entity name</strong> — must match the D&amp;B record and your registration documents.</li>
<li><strong>Registered address</strong> — a D-U-N-S Number identifies an entity at a specific location; a mismatch here is a common failure.</li>
<li><strong>Contact details</strong> — a working business email and phone that can be reached during verification.</li>
<li><strong>Entity type</strong> — a real legal entity, not a trade name, DBA or branch.</li>
</ul>
<p>Because Google and Apple both read from the same D&amp;B record, <strong>fixing your D&amp;B profile once fixes both</strong>. Conversely, a stale record will cause the same rejection on both stores.</p>

<h2>Typical timeline</h2>
<div class="table-scroll"><table>
<thead><tr><th>Step</th><th>Time</th></tr></thead>
<tbody>
<tr><td>Find an existing D-U-N-S record</td><td>Often minutes</td></tr>
<tr><td>Request a new D&amp;B record (free)</td><td>Up to 30 business days</td></tr>
<tr><td>D&amp;B expedited option</td><td>Up to 8 business days</td></tr>
<tr><td>Google's own organization verification</td><td>Separate review after the number is available; allow a buffer</td></tr>
</tbody></table></div>
<p>Plan backwards from your release date. A newly created D&amp;B record also needs time to propagate before a platform can validate it.</p>

<h2>Why verification fails</h2>
<ol>
<li>The English legal name in Play Console differs from the D&amp;B record (translation, abbreviation, pinyin, "Ltd" vs "Co., Ltd").</li>
<li>The registered address changed and D&amp;B still holds the old one.</li>
<li>The number belongs to a parent, a branch, or a second office.</li>
<li>The record is brand new and not yet visible to Google's check.</li>
<li>The business phone goes unanswered during a verification call.</li>
</ol>
<div class="callout warn"><p>Repeatedly resubmitting with slightly different spellings tends to make things worse. Fix the underlying D&amp;B record, then submit once with the exact values.</p></div>

<h2>The practical sequence</h2>
<p>Look up your existing record first. If it exists, copy the legal name and address <em>from the D&amp;B record</em> into Play Console rather than the other way round. If it is out of date, request an update from D&amp;B and wait for propagation. Only if no record exists should you submit a new application — and then use D&amp;B's official form with details copied verbatim from your registration documents.</p>
""",
  "faq": [
    ("Do individual Google Play developers need a D-U-N-S Number?", "No, it applies to organization/company developer accounts."),
    ("Can I use the same D-U-N-S Number for Apple and Google Play?", "Yes. Both platforms validate against the same D&B database. One number per legal entity per location serves both."),
    ("Why does Google say my D-U-N-S Number is invalid?", "Most often the legal name or registered address in Play Console does not exactly match the D&B record, or the number belongs to a different entity/location."),
    ("How long does Google Play organization verification take?", "It is a separate review from D&B. Getting the number is the long pole: minutes if a record exists, up to 30 business days if a new one must be created. Allow extra time for Google's own check."),
    ("Is the D-U-N-S Number free?", "Yes, D&B issues it free. Any cost is for expedited processing or third-party lookup and assistance."),
  ],
},
{
  "file": "guides/duns-bianhao-jiaji.html",
  "lang": "zh",
  "short": "邓白氏编码加急时效",
  "title": "邓白氏编码（DUNS）加急要多久？2026 各通道时效对比与避坑清单",
  "h1": "邓白氏编码加急要多久？",
  "lead": "官方免费通道最长 30 个工作日，官方付费加急仍需约 8 个工作日，苹果开发者通道约 5 个工作日。但很多企业根本不用「申请」——编码早就存在，只是没找到。先分清这两种情况，再谈加急。",
  "desc": "邓白氏编码（DUNS）加急到底要多久？官方免费 30 个工作日、付费加急 8 个工作日、苹果通道 5 个工作日、已有编码检索几分钟。附材料清单、五大常见坑与适用边界。",
  "date": "2026 年 11 月",
  "read": 7,
  "cta_h2": "先确认你的企业属于哪种情况",
  "cta_p": "把公司英文名（与营业执照一致）和所在国家发给我们，我们先查是否已有编码、能否适用快速通道，并告知真实时效，确认后再决定是否继续。",
  "cta_btn": "免费预检",
  "body": """
<h2>第一步：你是「新申请」还是「查已有编码」？</h2>
<p>这是决定时效的关键。邓白氏（Dun &amp; Bradstreet, D&amp;B）维护的是全球企业数据库，DUNS 编码是它给「某一地址上的某一法人实体」分配的九位标识。很多企业在被大客户、平台或金融机构核验时，就已经被建过档，企业主本人却完全不知道。</p>
<p>苹果官方帮助页也明确建议：<strong>注册前先查询你的组织是否已有 D-U-N-S 编号</strong>，查不到再提交申请。跳过这一步，就会为一份本已存在的记录再等上几周。</p>

<h2>四条通道的时效与成本（2026）</h2>
<div class="table-scroll"><table>
<thead><tr><th>通道</th><th>典型耗时</th><th>费用</th><th>适用情况</th></tr></thead>
<tbody>
<tr><td>邓白氏官网标准免费申请</td><td>最长约 30 个工作日</td><td>免费</td><td>全新主体、没有截止日期</td></tr>
<tr><td>邓白氏官方付费加急（结账页可选）</td><td>约 8 个工作日</td><td>约 $229</td><td>确实需要新建记录且有 deadline</td></tr>
<tr><td>苹果开发者 D-U-N-S 检索 / 申请通道</td><td>约 5 个工作日收到编码</td><td>免费</td><td>仅在申请苹果企业账号时可用</td></tr>
<tr><td>检索并核验已存在的编码</td><td>通常几分钟</td><td>视是否委托协助</td><td>大多数已注册企业</td></tr>
</tbody></table></div>
<div class="callout warn"><p><strong>注意：</strong>苹果中文支持页明确写着「对 D-U-N-S 编号创建流程进行加急不会缩短此等待时间」。也就是说，花钱催表单，不等于能插队。任何声称「全新主体也能秒出」的说法都值得怀疑。</p></div>
<p>另外要预留两段独立时间：编码创建后需要同步到各平台数据库，苹果 / Google 还会再做一次自己的主体审核。整个企业账号开通的时间线，不等于拿到九位数字的时间线。</p>

<h2>申请前材料清单</h2>
<div class="table-scroll"><table>
<thead><tr><th>项目</th><th>填写要求</th></tr></thead>
<tbody>
<tr><td>企业法定名称</td><td>与营业执照完全一致；英文名需固定一种译法，不用缩写、不用纯拼音</td></tr>
<tr><td>注册地址</td><td>精确到门牌号，含省市与邮编；与工商登记一致</td></tr>
<tr><td>企业联系电话</td><td>工作时间内有人接听，邓白氏可能来电核验</td></tr>
<tr><td>法人 / 负责人姓名</td><td>与登记信息一致</td></tr>
<tr><td>法律形式、成立年份、行业、员工数</td><td>按实际填写，前后一致</td></tr>
<tr><td>营业执照扫描件</td><td>清晰、完整、在有效期内，备用于核验</td></tr>
</tbody></table></div>

<h2>五个最常见的坑</h2>
<ol>
<li><strong>英文名不一致。</strong>「有限公司」译成 Ltd / Co., Ltd. / Limited 混用，或用拼音代替，会被判为不同主体。</li>
<li><strong>重复提交。</strong>第一份申请还在处理中又提交一次，可能导致请求被冻结或产生冲突记录。</li>
<li><strong>漏接核验电话。</strong>邓白氏可能来电确认业务类型、员工数或要求补充注册文件，漏接就重新排队。</li>
<li><strong>地址 / 主体不符。</strong>用总公司或分公司的编码去注册，或使用旧的注册地址，苹果会返回「无法验证」。</li>
<li><strong>拿到编码就立刻提交。</strong>新建记录需要时间同步，太早填进苹果后台容易被判无效。</li>
</ol>

<h2>快速通道的适用边界</h2>
<p>负责任的服务方会先做预检。通常只有在以下情况成立时，才可能把「几周」压缩到「几分钟」：企业已存在于 D&amp;B 数据库、名称与地址可核验、主体为真实存续的法人实体（非个体工商户挂名、非虚构商号、非分公司）、所在地区数据覆盖完整、且该案例不需要额外电话或文件核验。</p>
<p>如果确实需要新建记录，真实时效就是邓白氏的时效，任何第三方都无法绕过其核验流程。我们会在开始前把这个结论讲清楚，而不是收钱后再解释。</p>

<h2>一句话决策</h2>
<ul>
<li>有旧合同 / 供应商入库记录 / 历史 D&amp;B 邮件 → 先翻档案，很可能编码就在里面。</li>
<li>正在申请苹果企业账号 → 先走苹果的官方检索页。</li>
<li>新公司、无截止日期 → 官网免费申请，把资料填准。</li>
<li>新公司、有硬截止日期 → 考虑邓白氏官方加急，并给平台审核留缓冲。</li>
<li>本周就要、又不确定有没有编码 → 先把「是否存在」这个问题查清楚，这是唯一能把几周压到几分钟的环节。</li>
</ul>
<p class="source-list">官方参考：<a href="https://developer.apple.com/cn/support/D-U-N-S/" target="_blank" rel="nofollow noopener">Apple 开发者 — D-U-N-S 编号</a> · <a href="https://www.dandb.com/free-duns-number/" target="_blank" rel="nofollow noopener">D&amp;B — How to Get a D-U-N-S Number</a></p>
""",
  "faq": [
    ("邓白氏编码是免费的吗？", "是。邓白氏官方发放的标准 DUNS 编码免费。收费的是官方加急选项，或第三方提供的检索、核对与申请协助服务——不是编码本身。"),
    ("邓白氏编码多久能拿到？", "官方标准通道最长约 30 个工作日，官方付费加急约 8 个工作日，苹果开发者通道约 5 个工作日。若企业已有编码，检索核验通常几分钟即可完成。"),
    ("加急真的能缩短苹果的等待吗？", "苹果中文支持页明确说明，对 D-U-N-S 编号创建流程进行加急不会缩短其等待时间。苹果的主体审核是独立流程。"),
    ("为什么我查不到自己的公司？", "常见原因是英文名与登记译法不一致、地址或电话已变更、公司成立时间很短，或该地区 D&B 数据覆盖有限。可尝试用地址和电话反查。"),
    ("DUNS 编码会过期吗？", "不会。它是企业实体在某地址的永久标识；企业注销或主体结构重大变更时，D&B 可能把记录标记为非活跃。"),
    ("一个公司可以有多个 DUNS 编码吗？", "每个实际经营地址可以有独立编码；同一地址上的单一法人实体通常只应有一个，不要重复申请。"),
  ],
},
{
  "file": "guides/pingguo-kaifazhe-duns.html",
  "lang": "zh",
  "short": "苹果 DUNS 驳回排查",
  "title": "苹果开发者企业账号 DUNS 编码被驳回？常见原因逐条排查",
  "h1": "苹果开发者企业账号 DUNS 被驳回？逐条排查",
  "lead": "「Unable to verify」不一定是你的编码错了。苹果校验的是法人实体名称、地址、主体类型与 D&B 档案是否逐字一致。下面按现象给排查顺序。",
  "desc": "苹果开发者企业账号提示 DUNS 编码无法验证？整理名称不一致、地址不符、主体类型不符、编码未同步、错用他人编码等常见原因与对应处理步骤。",
  "date": "2026 年 11 月",
  "read": 6,
  "cta_h2": "卡在苹果审核这一步？",
  "cta_p": "发来公司法定名称、注册地址和所在国家，我们先核对 D&B 档案与苹果表单是否一致，并确认真实时效。",
  "cta_btn": "帮我排查",
  "body": """
<h2>苹果到底在校验什么</h2>
<p>以企业身份加入 Apple Developer Program 时，苹果要用 D-U-N-S 编号去邓白氏（D&amp;B）数据库确认：签协议的是一个真实存在的<strong>法人实体</strong>。编号本身由 D&amp;B 分配和维护，苹果只是读取比对。所以「编号正确但被驳回」几乎总是<strong>档案信息不一致</strong>，而不是九位数字写错了。</p>
<p>苹果还明确了主体资格：个人开发者不需要 DUNS；企业和教育机构必须提供其法人实体对应的编码；<strong>DBA、虚构商号、商号和分公司不被接受</strong>；政府组织可选择不提供。</p>

<h2>按现象排查</h2>
<div class="table-scroll"><table>
<thead><tr><th>现象</th><th>最可能的原因</th><th>处理</th></tr></thead>
<tbody>
<tr><td>提示 Unable to verify / 无法验证</td><td>法定名称或地址与 D&amp;B 档案不一致</td><td>以 D&amp;B 档案里的写法为准，回头改苹果表单，而不是反复改编码</td></tr>
<tr><td>编码查得到，但苹果说无效</td><td>记录刚创建尚未同步，或档案被标记为非活跃</td><td>等待同步后再提交一次；不要重复申请新编码</td></tr>
<tr><td>系统显示的是另一家相似公司</td><td>英文名译法、历史名称或拼音导致匹配错误</td><td>用完整法定名称 + 地址 + 电话反查，确认统一社会信用代码对应的主体</td></tr>
<tr><td>用总公司编码提交子公司申请</td><td>主体不符</td><td>改用申请主体自己的编码；每个地址 / 法人实体对应自己的 DUNS</td></tr>
<tr><td>个体工商户 / 分公司被拒</td><td>主体类型不符合苹果要求</td><td>改用符合条件的法人实体，或改注册个人开发者账号</td></tr>
<tr><td>申请长期无进展</td><td>漏接邓白氏核验电话、营业执照未补充、重复提交导致冻结</td><td>保持电话畅通，补齐注册文件，避免同一主体并行多份申请</td></tr>
</tbody></table></div>

<h2>三步定位法</h2>
<ol>
<li><strong>先定主体。</strong>确认申请主体是法人实体，且不是 DBA / 分公司。这一步不成立，后面全白做。</li>
<li><strong>再定档案。</strong>查 D&amp;B 里是否存在该主体的记录，逐字抄下法定英文名、街道地址、省市、邮编和电话。</li>
<li><strong>最后对齐表单。</strong>把苹果后台的 Legal Entity Name 与 Address 改成与档案完全一致，并检查联系人电话可接通。</li>
</ol>
<div class="callout"><p>顺序很重要：很多人一被驳回就重新申请编码，结果产生重复请求、档案更乱。<strong>先把「已有档案」读出来，再去改表单。</strong></p></div>

<h2>时间线要分开算</h2>
<p>拿到编码 ≠ 账号开通。邓白氏下发编码可能需要约 5 个工作日（苹果通道）或更久；新记录还需要同步时间；苹果随后再做一次独立的人工审核。苹果中文支持页还特别说明：对 D-U-N-S 创建流程做加急，并不会缩短其等待时间。排期时给三段各留缓冲，别把上架日压在最后一天。</p>

<h2>提交前最后核对清单</h2>
<ul>
<li>法定名称：与营业执照及 D&amp;B 档案完全一致，英文译法固定一种</li>
<li>地址：精确到门牌号，含省市邮编，与登记一致</li>
<li>主体类型：法人实体，非个人 / DBA / 分公司</li>
<li>编码：属于本主体、本地址，且状态有效</li>
<li>联系人：企业邮箱 + 工作时间内可接通的电话</li>
<li>营业执照扫描件：清晰、在有效期内，随时可补</li>
<li>不重复提交：上一份申请未结案前不再开新申请</li>
</ul>
<p class="source-list">官方参考：<a href="https://developer.apple.com/cn/support/D-U-N-S/" target="_blank" rel="nofollow noopener">Apple 开发者 — D-U-N-S 编号（中文）</a> · <a href="https://developer.apple.com/support/D-U-N-S/" target="_blank" rel="nofollow noopener">Apple Developer — D-U-N-S Number</a></p>
""",
  "faq": [
    ("苹果提示 DUNS 无法验证，是不是编码错了？", "多数情况下是法定名称或注册地址与 D&B 档案不一致，而不是九位数字填错。应以档案内容为准修改苹果表单。"),
    ("个人开发者需要 DUNS 编码吗？", "不需要。只有以组织（公司、教育机构）身份加入 Apple Developer Program 才需要。"),
    ("可以用总公司或分公司的 DUNS 吗？", "不可以。DUNS 对应特定地址上的特定法人实体，苹果要求使用为其法人实体注册的编号，且不接受分公司注册。"),
    ("刚拿到的编码为什么苹果查不到？", "新建记录需要时间同步到苹果可读取的数据库。等待后再提交，不要重复申请。"),
    ("被驳回后应该立刻重新申请编码吗？", "不建议。重复申请可能冻结流程或产生冲突记录。先核对已有档案与表单字段是否一致。"),
    ("苹果审核还要多久？", "苹果的主体审核独立于邓白氏流程。拿到编码后还要预留苹果自己的审核时间，且官方说明加急创建流程不会缩短其等待时间。"),
  ],
},
]

# Cross-links shown at the bottom of every guide.
RELATED = [
  ("D-U-N-S Number for Apple Developer Program", "apple-developer-duns.html"),
  ("How to get a D-U-N-S Number fast — 4 routes compared", "duns-number-fast.html"),
  ("Find your existing D-U-N-S Number (free lookup)", "duns-lookup.html"),
  ("D-U-N-S Number for Google Play", "google-play-duns.html"),
  ("邓白氏编码加急要多久？", "duns-bianhao-jiaji.html"),
  ("苹果企业账号 DUNS 被驳回排查", "pingguo-kaifazhe-duns.html"),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def faq_json(p):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in p["faq"]
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def breadcrumb_json(p):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": BASE_URL + "#guides"},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": p["canonical"]},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render(p):
    slug = os.path.splitext(os.path.basename(p["file"]))[0]
    prefix = "../"
    cta_link = "../index.html?utm_source=guide_" + slug + "&utm_medium=internal#contact"

    faq_html = "\n".join(
        '          <details><summary>' + esc(q) + '</summary><p>' + esc(a) + '</p></details>'
        for q, a in p["faq"]
    )
    related_html = "\n".join(
        '          <li><a href="' + f + '">' + esc(label) + '</a></li>'
        for label, f in RELATED if f != os.path.basename(p["file"])
    )

    zh = p["lang"] == "zh"
    labels = {
        "{{NAV_COMPARE}}": "时效对比" if zh else "Why us",
        "{{NAV_GUIDES}}": "专题指南" if zh else "Guides",
        "{{NAV_PRICING}}": "费用" if zh else "Pricing",
        "{{NAV_LANG}}": "English" if zh else "中文",
        "{{NAV_CTA}}": "免费预检" if zh else "Get started",
        "{{CRUMB_HOME}}": "首页" if zh else "Home",
        "{{CRUMB_GUIDES}}": "专题指南" if zh else "Guides",
        "{{UPDATED_LABEL}}": "更新于" if zh else "Updated",
        "{{MIN_LABEL}}": "分钟阅读" if zh else "min read",
        "{{FAQ_HEADING}}": "常见问题" if zh else "Frequently asked questions",
        "{{RELATED_HEADING}}": "相关指南" if zh else "Related guides",
    }

    out = TEMPLATE
    pairs = {
        "{{LANG}}": "zh-CN" if zh else "en",
        "{{TITLE}}": esc(p["title"]),
        "{{DESC}}": esc(p["desc"]),
        "{{CANONICAL}}": p["canonical"],
        "{{BASE}}": BASE_URL,
        "{{PREFIX}}": prefix,
        "{{HOME}}": HOME,
        "{{ZH}}": ZH,
        "{{SHORT_TITLE}}": esc(p["short"]),
        "{{H1}}": esc(p["h1"]),
        "{{LEAD}}": esc(p["lead"]),
        "{{DATE}}": p["date"],
        "{{READ_TIME}}": str(p["read"]),
        "{{BODY}}": p["body"],
        "{{CTA_H2}}": esc(p["cta_h2"]),
        "{{CTA_P}}": esc(p["cta_p"]),
        "{{CTA_BTN}}": esc(p["cta_btn"]),
        "{{CTA_LINK}}": cta_link,
        "{{FAQ_HTML}}": faq_html,
        "{{FAQ_JSON}}": faq_json(p),
        "{{BREADCRUMB_JSON}}": breadcrumb_json(p),
        "{{RELATED_HTML}}": related_html,
    }
    for k, v in labels.items():
        out = out.replace(k, v)
    for k, v in pairs.items():
        out = out.replace(k, v)
    return out


def main():
    for p in PAGES:
        p["canonical"] = BASE_URL + p["file"]
        path = os.path.join(ROOT, p["file"].replace("/", os.sep))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render(p))
        print("wrote", p["file"])
    print("done:", len(PAGES), "pages")


if __name__ == "__main__":
    main()
