// 💨 Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// ✅ Auto-close alerts after 5 seconds
setTimeout(() => {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
    alert.classList.add("fade");
    setTimeout(() => alert.remove(), 1000); // remove after fade
  });
}, 5000);

// 📅 Inject current year into footer
const footerYear = document.querySelector("#footer-year");
if (footerYear) {
  footerYear.textContent = new Date().getFullYear();
}
