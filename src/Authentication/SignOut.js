import React, { useEffect } from "react";
import { signOutUser, auth}  from "../Firebase/Firebase";
import { useNavigate } from "react-router-dom";
import { useAuthState } from "react-firebase-hooks/auth";

import styled from 'styled-components'

export const SignOutComponenet = styled.div`

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

function SignOut() {
    const [user, loading, error] = useAuthState(auth);
    const navigate = useNavigate();

    useEffect(() => {
        if (!user) {
          navigate("/");
          console.log("Signout successful");
        }
      }, [user, error, loading, navigate]);

  return (
    
    <SignOutComponenet >
      <div>
        <p>Are you sure you want to sign out?</p>
        <button onClick={() => signOutUser() }>
          Yes
        </button>
      </div>
    </SignOutComponenet>
  );
}
export default SignOut;