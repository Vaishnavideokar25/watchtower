import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyCKNeQcAT2vdP47cCPyJe0Ittjn3131fg4",
  authDomain: "watchtower-backend.firebaseapp.com",
  projectId: "watchtower-backend",
  appId: "1:411346606582:web:bc4bbe11c6b258c9868fd7"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
