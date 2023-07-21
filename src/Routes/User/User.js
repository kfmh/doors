// General imports
import React, { useEffect, useState } from "react";
import styled from 'styled-components'
import LoadingAnimation from '../../Components/LoadingAnimation'

import { useAuthState } from "react-firebase-hooks/auth";
import { useNavigate } from "react-router-dom";
import { NavLink } from "react-router-dom";
import { auth } from "../../Firebase/Firebase"
import { db, getDoc, getDocs, doc, collection, where, query } from "../../Firebase/Firebase";

export const User = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    min-height: 100vh;
    button {
      max-width: 300px;
      width: 60%;
    }
`



const UserPage = () => {
  const [user, loading, error] = useAuthState(auth);
  const navigate = useNavigate();
  const [document, setDocument] = useState('')
  const [data, setData] = useState(null);

  useEffect(() => {
      if (!user) {
        navigate("/Login");
        console.log("Signout successful");
      }
    }, [user, error, loading, navigate]);

    useEffect(() => {
          const fetchCollection = async () => {
            // Specify the collection to fetch
            const collectionRef = collection(db, "user", user.uid, "projects");
            try {
              // Fetch the collection
              const docSnapshot = await getDocs(collectionRef);
              // Extract the documents from the collection
              docSnapshot.docs.map((doc) => [setDocument(doc.data())]);
            } catch (error) {
              console.error('Error fetching collection:', error);
            }
          };
          fetchCollection()
        }, [ user ]);
    useEffect(() => {
          const fetchData = async () => {
              try {
                const docRef = doc(db, 'user', user.uid);
                const docSnapshot = await getDoc(docRef);
                
                if (docSnapshot.exists) {
                  setData(docSnapshot.data());
                  console.log("Landing page hook Loaded");
                } else {
                  console.log('Document does not exist');
                }
              } catch (error) {
                console.error('Error fetching document: ', error);
              }
            };
            fetchData()
        }, [ user ]);
        
        console.log(data.userName);

  return (
    <>
      { data ?
        <User>
          <h1 style={{textAlign: 'center'}}>{data.userName}</h1>
          <NavLink to="/Task">
            <button>Start Project</button>
          </NavLink>
          <div>
            <p>P1</p>
            <p>P2</p>
            <p>P3</p>
          </div>
        </User>
        :
        <LoadingAnimation/>
      }
    </>
  );
};

export default UserPage;
