import React from 'react';
import styled from 'styled-components'
import { NavLink } from "react-router-dom";

export const Landing = styled.div`
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background-color: black;
    color: white;
    header {
        background-color: #007bff;
        padding: 15px 10% 15px 20px;
        display: flex;
        justify-content: end;
    }
    main {
        display: flex;
        justify-content: center;
        width: 60%;
        margin: 0 auto;
    }
    button {
        width: 300px;
        height: 40px;
        border-radius: 20px;
        background-color: white;
        font-size: 1.3rem;
    }
    #Hero { 
        h1 {
            font-size: 3rem;
        }
    }
`

export const LinK =  styled(NavLink)`
    color: white;
    text-decoration: none;
    font-weight: 200;
    font-size: 1.3rem;
    letter-spacing: 2px;
`

export const CTA = styled.section`
    
`

const LandingPage = () => {
  return (
    <Landing>
        <header>
            <LinK to="/Login">Login</LinK>
        </header>
      <main>
        <section id="Hero">
          <h1>Start growing your bext project now</h1>
          <p>Plant a seed to create the future. With rootmap your project is structured for efficiant growth</p>
          <button>Sign Up Now</button>
        </section>
      </main>
      <footer>
      </footer>
    </Landing>
  );
};

export default LandingPage;
