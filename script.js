// ============================================================
//  CONFIG — your Telegram contact
// ============================================================
const TELEGRAM_PHONE = "+86 189 5314 7694";

document.addEventListener("DOMContentLoaded", function () {
  // Footer year
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Copy phone number button
  const copyBtn = document.getElementById("copyBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", async function () {
      try {
        await navigator.clipboard.writeText(TELEGRAM_PHONE);
        copyBtn.textContent = "Copied!";
        copyBtn.classList.add("copied");
        setTimeout(() => {
          copyBtn.textContent = "Copy phone number";
          copyBtn.classList.remove("copied");
        }, 1800);
      } catch (e) {
        copyBtn.textContent = TELEGRAM_PHONE;
      }
    });
  }
});
