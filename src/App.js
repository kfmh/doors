// General imports
import './App.css';
import LoadingAnimation from './Components/LoadingAnimation'

// Component specific imports
import { useEffect, useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Landing      from "./Routes/Landing/Landing"
import User         from "./Routes/User/User"
import Projects     from "./Routes/Projects/Projects"
import Login        from "./Authentication/Login"
import SignOut      from "./Authentication/SignOut"
import ProjectForm  from "./Components/ProjectTask/Task"

// import Signout     from "./Authentication/Signout"
// import useMediaQuery from '@mui/material/useMediaQuery';
import Navbar from "./Navbar/Navbar"

import { 
  getAuth,
  onAuthStateChanged 
 } from 'firebase/auth';


function App() {
  const [authLoaded, setAuthLoaded] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [user, setUser] = useState('')
  const auth = getAuth();
  useEffect(() => {
      onAuthStateChanged(auth, (user) => {
      if (user) {
          setIsLoggedIn(true)
          setUser(user)
      } else {
          setIsLoggedIn(false)
      }
      setAuthLoaded(true)
      });
  })
  return (
    <>
      { authLoaded ?
        <BrowserRouter>
          <Routes>
            <Route path="/" element={ isLoggedIn ? <Navbar/> : null}>
              <Route index element={<Landing user={user}/>} />
              <Route path="/User" element={<User user={user} isLoggedIn={isLoggedIn}/>} />
              <Route path="/Projects" element={<Projects user={user} isLoggedIn={isLoggedIn}/>} />
              <Route path="/Login" element={<Login/>} />
              <Route path="/SignOut" element={<SignOut/>} />
              <Route path="/Task" element={<ProjectForm user={user}/>} />
            </Route>
          </Routes>
        </BrowserRouter>
        :
        <LoadingAnimation/>
      }
    </>
  );
}

export default App;
