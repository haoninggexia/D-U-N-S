// ============================================================
//  CONFIG — contacts. Leave a value as "" and it simply won't be shown.
//  No fake contact details are displayed by default.
// ============================================================
const TELEGRAM_USERNAME = "haoninggexia";
const TELEGRAM_URL = "https://t.me/" + TELEGRAM_USERNAME;
const TELEGRAM_PHONE = "+86 189 5314 7694";
const CONTACT_EMAIL = "3085985620@qq.com";
const WECHAT_ID = "18953147694";
const QQ_NUMBER = "3085985620";

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

function copyText(text, okMsg) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(text).then(function () { return true; }).catch(function () { return false; });
  }
  return Promise.resolve(false);
}

function flash(btn, text, ok) {
  const old = btn.textContent;
  btn.textContent = text;
  if (ok) btn.classList.add("copied");
  setTimeout(function () { btn.textContent = old; btn.classList.remove("copied"); }, 1800);
}

function renderExtraContacts() {
  const box = document.getElementById("extraContacts");
  if (!box) return;
  const parts = [];
  if (WECHAT_ID) {
    parts.push('<p>微信 / WeChat: <strong>' + WECHAT_ID + '</strong><button type="button" class="mini-copy" data-copy="' + WECHAT_ID + '">复制</button></p>');
  }
  if (QQ_NUMBER) {
    parts.push('<p>QQ: <strong>' + QQ_NUMBER + '</strong><button type="button" class="mini-copy" data-copy="' + QQ_NUMBER + '">复制</button></p>');
  }
  if (CONTACT_EMAIL) {
    parts.push('<p>邮箱 / Email: <a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a></p>');
  }
  if (!parts.length) {
    parts.push('<p>不便使用 Telegram？填好上方信息后点「Copy the message instead」，可用任意方式发送。</p>');
  }
  box.innerHTML = parts.join("");
  box.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      copyText(btn.getAttribute("data-copy")).then(function (ok) {
        if (ok) flash(btn, "已复制", true);
        else window.prompt("复制这个号码 / Copy this ID:", btn.getAttribute("data-copy"));
      });
    });
  });
}

function tagTelegramLinks() {
  const ref = readSource();
  if (!ref) return;
  const msg = encodeURIComponent("Hi, I found you via " + ref + ". I'd like to check my D-U-N-S Number.");
  document.querySelectorAll('a[href^="https://t.me/' + TELEGRAM_USERNAME + '"]').forEach(function (a) {
    if (a.getAttribute("href").indexOf("?text=") === -1) a.setAttribute("href", TELEGRAM_URL + "?text=" + msg);
  });
}

// Fill the channel links with the completed enquiry, including its UTM source.
function prepareSendOptions() {
  const panel = document.getElementById("sendOptions");
  if (!panel) return;
  const msg = buildMessage();
  const tg = document.getElementById("sendTg");
  const mail = document.getElementById("sendMail");
  if (tg) tg.href = TELEGRAM_URL + "?text=" + encodeURIComponent(msg);
  if (mail && CONTACT_EMAIL) {
    mail.href = "mailto:" + CONTACT_EMAIL
      + "?subject=" + encodeURIComponent("D-U-N-S Number 咨询 / enquiry")
      + "&body=" + encodeURIComponent(msg);
  }
  panel.hidden = false;
  panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

document.addEventListener("DOMContentLoaded", function () {
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  readSource();
  renderExtraContacts();
  tagTelegramLinks();

  const copyBtn = document.getElementById("copyBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      copyText(TELEGRAM_PHONE).then(function (ok) {
        if (ok) flash(copyBtn, "Copied!", true);
        else window.prompt("复制号码 / Copy:", TELEGRAM_PHONE);
      });
    });
  }

  const form = document.getElementById("leadForm");
  const copyLead = document.getElementById("copyLead");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      prepareSendOptions();
    });
  }

  if (copyLead) {
    copyLead.addEventListener("click", function () {
      const msg = buildMessage();
      copyText(msg).then(function (ok) {
        if (ok) flash(copyLead, "Copied! 已复制咨询信息", true);
        else window.prompt("复制以下内容 / Copy this message:", msg);
      });
    });
  }

  const wechatBtn = document.getElementById("sendWechat");
  const hint = document.getElementById("sendHint");
  if (wechatBtn) {
    wechatBtn.addEventListener("click", function () {
      const text = "微信号 / WeChat ID: " + WECHAT_ID + "\n\n" + buildMessage();
      copyText(text).then(function (ok) {
        if (ok) {
          flash(wechatBtn, "已复制 ✓", true);
          if (hint) hint.textContent = "已复制咨询信息与微信号。请打开微信 → 添加 " + WECHAT_ID + " → 粘贴发送。";
        } else {
          window.prompt("复制后发给微信 " + WECHAT_ID + " / Copy and send on WeChat:", text);
        }
      });
    });
  }
});
