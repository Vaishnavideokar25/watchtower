const toggle = document.getElementById("themeToggle");
const API_BASE = "http://127.0.0.1:8000";

toggle.onclick = () => {
  document.body.classList.toggle("light");
  toggle.textContent =
    document.body.classList.contains("light")
      ? "🌙 Dark Mode"
      : "☀️ Light Mode";
};
