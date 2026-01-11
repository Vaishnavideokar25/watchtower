const API_BASE = "http://127.0.0.1:8000";

const themeToggle = document.getElementById("themeToggle");
themeToggle.onclick = () => {
  document.body.classList.toggle("light");
  themeToggle.textContent =
    document.body.classList.contains("light")
      ? "🌙 Dark Mode"
      : "☀️ Light Mode";
};

// DEMO UPDATE
const btn = document.getElementById("simulateBtn");
const content = document.getElementById("demoContent");

let updated = false;

btn.onclick = () => {
  if(updated) return;

  content.innerHTML = `
    <div class="icon">🚀</div>
    <h2>Internship Program</h2>
    <p class="muted">Applications Open</p>
    <p><b>Deadline:</b> March 25, 2026</p>
  `;

  btn.textContent = "✔ Update Detected";
  btn.classList.add("alert");
  updated = true;
};
