// General imports
import React, { useEffect, useState } from "react";
import styled from 'styled-components'
import LoadingAnimation from '../../Components/LoadingAnimation'
import { auth } from "../../Firebase/Firebase"
import { getProjects, getUserInfo } from "../../Firebase/FetchData"

import MapProjects  from "../../Components/ProjectTask/MapProjects"
import { useAuthState } from "react-firebase-hooks/auth";
import { useNavigate } from "react-router-dom";
import { NavLink } from "react-router-dom";

export const User = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    min-height: 100vh;
    #button {
      border: 2px solid #00bfff;
      text-decoration: none;
      color: white;
      padding: 10px;
      border-radius: 10px;
    }
`



const UserPage = () => {
  const navigate = useNavigate();
  const [projects, setProjects] = useState('')
  const [userInfo, setUserInfo] = useState(null);
  
  const [user, loading, error] = useAuthState(auth);
  useEffect(() => {
      if (!user) {
        navigate("/Login");
        console.log("Signout successful");
      }
    }, [user, error, loading, navigate]);

    useEffect(() => {
    const fetchData = async () => {
      try {
        // Call getProjects with the necessary props
        await getProjects({ user: { uid: `${user.uid}` }, setProjects });
              getUserInfo({ user: { uid: `${user.uid}` }, setUserInfo });
      } catch (error) {
        console.error('Error while fetching projects:', error);
      }
    };

      fetchData();
    }, [user.uid]);


  return (
    <>
      { userInfo && projects ?
        <User>
          <h1 style={{textAlign: 'center'}}>{userInfo.userName}</h1>
          <NavLink id="button" to="/Task">
            Start Project
          </NavLink>
          <div>
            <MapProjects projects={projects}/>
          </div>
        </User>
        :
        <LoadingAnimation/>
      }
    </>
  );
};

export default UserPage;
