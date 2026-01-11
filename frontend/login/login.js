import {
  GoogleAuthProvider,
  signInWithRedirect,
  getRedirectResult,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

import { auth } from "../firebase.js";

const provider = new GoogleAuthProvider();

// 🔵 Start login
document.getElementById("googleLogin").onclick = () => {
  signInWithRedirect(auth, provider);
};

// 🔁 Handle redirect result
getRedirectResult(auth).catch(console.error);

// 🔁 Redirect AFTER auth is restored
onAuthStateChanged(auth, (user) => {
  if (user) {
    window.location.replace("../Dashboard/index.html");
  }
});
