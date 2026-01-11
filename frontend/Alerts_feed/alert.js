const API_BASE = "http://127.0.0.1:8000";
let ALL_ALERTS = [];

async function loadAlerts(priority = "ALL") {
  const res = await fetch(`${API_BASE}/alerts/`);
  ALL_ALERTS = await res.json();

  const container = document.getElementById("alertsContainer");
  container.innerHTML = "";

  ALL_ALERTS
    .filter(a => priority === "ALL" || a.priority === priority)
    .forEach(a => {
      container.innerHTML += `
        <section class="alert-card">
          <div class="tags">
            <span class="tag ${a.priority.toLowerCase()}">${a.priority}</span>
            <span class="tag date">📅 ${a.date}</span>
          </div>
          <h2>${a.title}</h2>
          <p>${a.why}</p>
          <div class="ai-box">
            <p><b>Action:</b> ${a.action}</p>
            <button class="primary" onclick="addToCalendar('${a.title}','${a.date}')">
              📅 Add to Calendar
            </button>
          </div>
        </section>
      `;
    });
}

// FILTER BUTTONS
document.querySelectorAll(".filter").forEach(btn => {
  btn.onclick = () => {
    document.querySelectorAll(".filter").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    loadAlerts(btn.textContent.toUpperCase());
  };
});

// GOOGLE CALENDAR (REAL GOOGLE TECH ✅)
function addToCalendar(title, date) {
  const d = date.replace(/-/g, "");
  const url =
    `https://calendar.google.com/calendar/render?action=TEMPLATE` +
    `&text=${encodeURIComponent(title)}` +
    `&dates=${d}/${d}`;

  window.open(url, "_blank");
}

loadAlerts();
