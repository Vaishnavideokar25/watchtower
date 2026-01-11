console.log("Dashboard JS loaded");

/* ======================
   🔥 FIREBASE AUTH
====================== */
import {
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

import { auth } from "../firebase.js";

/* ======================
   🔐 AUTH GUARD (ONLY THIS)
====================== */
onAuthStateChanged(auth, (user) => {
  if (!user) {
    console.log("No user → redirecting to login");
    window.location.replace("../login/login.html");
  } else {
    console.log("User logged in:", user.email);
    loadDashboard(); // ✅ ONLY load after auth is ready
  }
});

/* ======================
   🌙 THEME TOGGLE
====================== */
const toggle = document.getElementById("themeToggle");
if (toggle) {
  toggle.onclick = () => {
    document.body.classList.toggle("light");
  };
}

/* ======================
   📊 DASHBOARD (DEMO MODE)
====================== */
function loadDashboard() {
  console.log("Loading dashboard in DEMO MODE");

  // Stats
  document.getElementById("pageCount").textContent = 2;
  document.getElementById("alertCount").textContent = 1;

  // Pages
  document.getElementById("pagesContainer").innerHTML = `
    <div class="page">
      <span>https://example.com/internships</span>
    </div>
    <div class="page">
      <span>https://example.com/results</span>
    </div>
  `;

  // Alerts
  document.getElementById("alertsContainer").innerHTML = `
    <div class="alert high">
      <strong>Deadline Updated</strong>
      <p>Internship application deadline changed to March 25</p>
    </div>
  `;
}

/* ======================
   🚪 LOGOUT (SAFE)
====================== */
window.logoutUser = function () {
  signOut(auth).then(() => {
    console.log("Logged out");
    window.location.replace("../login/login.html");
  });
};
