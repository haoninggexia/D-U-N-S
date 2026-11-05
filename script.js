// ============================================================
//  CONFIG — fill in optional China-friendly contacts here.
//  Leave a value as "" and it simply won't be shown on the site.
//  No fake contact details are displayed by default.
// ============================================================
const TELEGRAM_USERNAME = "haoninggexia";
const TELEGRAM_URL = "https://t.me/" + TELEGRAM_USERNAME;
const TELEGRAM_PHONE = "+86 189 5314 7694";
const CONTACT_EMAIL = "";   // e.g. "hello@example.com"
const WECHAT_ID = "";       // e.g. "duns_helper"
const QQ_NUMBER = "";       // e.g. "123456789"

// ------------------------------------------------------------
//  Source attribution: keep the first UTM/ref the visitor arrived
//  with, so every enquiry tells you which channel produced it.
// ------------------------------------------------------------
function readSource() {
  const p = new URLSearchParams(window.location.search);
  const incoming = p.get("utm_source") || p.get("ref") || p.get("source");
  if (incoming) {
    try { sessionStorage.setItem("duns_ref", incoming.slice(0, 60)); } catch (e) {}
  }
  let ref = "";
  try { ref = sessionStorage.getItem("duns_ref") || ""; } catch (e) {}
  if (!ref && document.referrer) {
    try { ref = "referral:" + new URL(document.referrer).hostname.replace(/^www\./, ""); } catch (e) {}
  }
  return ref.slice(0, 60);
}

function sourceLine() {
  const ref = readSource();
  return ref ? "\n来源 / Source: " + ref : "";
}

function buildMessage() {
  const company = (document.getElementById("fCompany") || {}).value || "";
  const country = (document.getElementById("fCountry") || {}).value || "";
  const purpose = (document.getElementById("fPurpose") || {}).value || "";
  const deadline = (document.getElementById("fDeadline") || {}).value || "";
  return [
    "Hi, I'd like to check my company's D-U-N-S Number.",
    "公司英文名 / Company legal name: " + (company.trim() || "—"),
    "国家地区 / Country: " + (country.trim() || "—"),
    "用途 / Needed for: " + purpose,
    "期望时间 / Deadline: " + (deadline.trim() || "不限 / flexible"),
    "请先帮我确认是否已有编码、以及能否适用快速通道。",
    "Please confirm whether a record already exists and whether the fast route applies." + sourceLine()
  ].join("\n");
}

function renderExtraContacts() {
  const box = document.getElementById("extraContacts");
  if (!box) return;
  const parts = [];
  if (WECHAT_ID) parts.push("<p>微信 / WeChat: <strong>" + WECHAT_ID + "</strong></p>");
  if (QQ_NUMBER) parts.push("<p>QQ: <strong>" + QQ_NUMBER + "</strong></p>");
  if (CONTACT_EMAIL) parts.push('<p>Email: <a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + "</a></p>");
  if (!parts.length) {
    parts.push('<p>不便使用 Telegram？填好上方信息后点「Copy the message instead」，可用任意方式发送。</p>');
  }
  box.innerHTML = parts.join("");
}

function tagTelegramLinks() {
  const ref = readSource();
  if (!ref) return;
  const msg = encodeURIComponent("Hi, I found you via " + ref + ". I'd like to check my D-U-N-S Number.");
  document.querySelectorAll('a[href^="https://t.me/' + TELEGRAM_USERNAME + '"]').forEach(function (a) {
    if (a.getAttribute("href").indexOf("?text=") === -1) a.setAttribute("href", TELEGRAM_URL + "?text=" + msg);
  });
}

function flash(btn, text, ok) {
  const old = btn.textContent;
  btn.textContent = text;
  if (ok) btn.classList.add("copied");
  setTimeout(function () { btn.textContent = old; btn.classList.remove("copied"); }, 1800);
}

document.addEventListener("DOMContentLoaded", function () {
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  readSource();
  renderExtraContacts();
  tagTelegramLinks();

  const copyBtn = document.getElementById("copyBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", async function () {
      try {
        await navigator.clipboard.writeText(TELEGRAM_PHONE);
        flash(copyBtn, "Copied!", true);
      } catch (e) {
        flash(copyBtn, TELEGRAM_PHONE, false);
      }
    });
  }

  const form = document.getElementById("leadForm");
  const copyLead = document.getElementById("copyLead");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      window.open(TELEGRAM_URL + "?text=" + encodeURIComponent(buildMessage()), "_blank", "noopener");
    });
  }

  if (copyLead) {
    copyLead.addEventListener("click", async function () {
      const msg = buildMessage();
      try {
        await navigator.clipboard.writeText(msg);
        flash(copyLead, "Copied! 已复制咨询信息", true);
      } catch (err) {
        window.prompt("复制以下内容 / Copy this message:", msg);
      }
    });
  }
});
