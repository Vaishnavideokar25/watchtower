const API_BASE = "http://127.0.0.1:8000";

/* =====================
   KEYWORD SELECTION
===================== */

const selected = document.getElementById("selected");
const input = document.getElementById("customInput");
const addBtn = document.getElementById("addKeyword");

// Add keyword tag
function addTag(text) {
  text = text.trim().toLowerCase();

  // prevent duplicates
  if ([...selected.children].some(s => s.textContent === text)) return;

  const span = document.createElement("span");
  span.className = "tag";
  span.textContent = text;
  selected.appendChild(span);
}

// ✅ EVENT DELEGATION → chips clickable
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("chip")) {
    const keyword = e.target.textContent.replace("+", "").trim();
    addTag(keyword);
    e.target.classList.add("active");
  }
});

// Add custom keyword
addBtn.onclick = () => {
  if (input.value.trim()) {
    addTag(input.value);
    input.value = "";
  }
};

/* =====================
   SUBMIT PAGE
===================== */

document.getElementById("startMonitoring").onclick = async () => {
  const urlInput = document.getElementById("urlInput");
  const url = urlInput.value.trim();

  const keywords = [...document.querySelectorAll("#selected span")]
    .map(s => s.textContent)
    .join(",");

  // ❌ Empty URL
  if (!url) {
    alert("Please enter a website URL.");
    urlInput.focus();
    return;
  }

  // ❌ Invalid URL
  try {
    new URL(url);
  } catch {
    alert("Please enter a valid URL (example: https://example.com)");
    urlInput.focus();
    return;
  }

  // ❌ No keywords
  if (!keywords) {
    alert("Please select at least one keyword to monitor.");
    return;
  }

  // ✅ Send to backend
  const form = new FormData();
  form.append("url", url);
  form.append("uid", "demouser");
  form.append("keywords", keywords);

  try {
    const res = await fetch(`${API_BASE}/monitor/add`, {
      method: "POST",
      body: form
    });

    if (!res.ok) {
      alert("Backend error. Is the server running?");
      return;
    }

    alert("Page added successfully!");
    window.location.href = "../Dashboard/index.html";

  } catch (err) {
    alert("Cannot connect to backend (server not running?)");
  }
};
