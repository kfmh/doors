// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// import { getAnalytics }  from "firebase/analytics";
import config            from "../firebaseConfig.json";

import { getAuth,
  signInWithEmailAndPassword,
  signOut, } from "firebase/auth"

import { getFirestore,
  doc, 
  getDoc,
  getDocs,
  collection,
  query, 
  where,
  // setDoc,
  // updateDoc
} from "firebase/firestore"

console.log(config);
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: config.apiKey,
  authDomain: config.authDomain,
  projectId: config.projectId,
  storageBucket: config.storageBucket,
  messagingSenderId: config.messagingSenderId,
  appId: config.appId,
  measurementId: config.measurementId,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
// const analytics = getAnalytics(app);
// logEvent(analytics, 'notification_received');

const logInWithEmailAndPassword = async (email, password) => {
  try {
    await signInWithEmailAndPassword(auth, email, password);
  } catch (err) {
    console.error(err);
    alert(err.message);
  }
};

const signOutUser = () => {
  signOut(auth);
};


export {
  query, where,
  collection,
  doc,
  getDoc,
  getDocs,
  auth,
  db,
  logInWithEmailAndPassword,
  signOutUser,
};