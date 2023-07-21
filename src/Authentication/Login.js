import React, { useEffect, useState } from "react";
import { auth, logInWithEmailAndPassword} from "../Firebase/Firebase";
import { useNavigate } from "react-router-dom";
import { useAuthState } from "react-firebase-hooks/auth";

import styled from 'styled-components'

export const LoginComponenet = styled.div`

  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;

  div {
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    text-align: center;
    background-color: #dcdcdc;
    padding: 30px;
  }
  input {
    padding: 10px;
    font-size: 18px;
    margin-bottom: 10px;
  }
  button {
    border-radius: 10px;
    padding: 10px;
    font-size: 18px;
    margin-bottom: 10px;
    border: none;
    color: white;
    background-color: black;
  }
`

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [user, loading, error] = useAuthState(auth);
  const navigate = useNavigate();

  useEffect(() => {
    if (user) {
      navigate("/User");
      console.log("Login successful");
    }
  }, [user, error, loading, navigate]);


  return (
    
    <LoginComponenet >
      <div>
        <form> 
          <input
            autoComplete="new-password"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="E-mail Address"
          />
          <input
            autoComplete="new-password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </form>
        <button onClick={() => logInWithEmailAndPassword(email, password)}>
          Login
        </button>
      </div>
    </LoginComponenet>
  );
}
export default Login;