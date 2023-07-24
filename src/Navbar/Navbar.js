import '../App.css';
import styled from 'styled-components'
import useMediaQuery from '@mui/material/useMediaQuery';


import { Outlet, Link } from "react-router-dom";
import React, { useState, useEffect } from 'react';


export const Navbar = styled.nav `
    display: flex;
    justify-content: space-around;
    align-items: center;

    position: fixed;
    bottom: 0;
    background-color: #f0f0f0; /* Set your desired background color */
    border-top: 1px solid #ccc; /* Optional: Add a border at the top */
    button {
        padding: 12px;
        font-size: 14px;
        border: none;
        background: transparent;
        cursor: pointer;
    }
    button.active {
        color: #007bff; /* Set your desired active tab color */
    }
` 


const BottomNavBar = () => {
    const isDesktopDevice = useMediaQuery("(min-device-width: 780px)");
    const [activeTab, setActiveTab] = useState('Home');
    const [width, setWidth] = useState('')
    const [height, setHeight] = useState('')
    const [flexDirection, setFlexDirection] = useState('')

    const handleTabClick = (tabName) => {
        setActiveTab(tabName);
    };
    useEffect(() => {
        if (isDesktopDevice) {
          setWidth('150px');
          setHeight('100vh');
          setFlexDirection('column')
        } else {
          setWidth('100vw');
          setHeight('60px');
          setFlexDirection('row')
        }
      }, [isDesktopDevice]);

    return (
        <>
            <Navbar style={{ width:`${width}`, height: `${height}`, flexDirection: `${flexDirection}`}}>
                <Link to="/Projects">
                    <button
                        className={activeTab === 'myProjects' ? 'active' : ''}
                        onClick={() => handleTabClick('myProjects')}
                    >
                        My Projects
                    </button>
                </Link>
                <Link to="/Task">
                    <button
                        className={activeTab === 'newProject' ? 'active' : ''}
                        onClick={() => handleTabClick('newProject')}
                    >
                        New Project
                    </button>
                </Link>    
                <Link>
                    <button
                        className={activeTab === 'Rootmap' ? 'active' : ''}
                        onClick={() => handleTabClick('Rootmap')}
                    >
                        Rootmap
                    </button>
                </Link>    
                <Link>
                    <button
                        className={activeTab === 'Profile' ? 'active' : ''}
                        onClick={() => handleTabClick('Profile')}
                    >
                        Profile
                    </button>
                </Link>    
            </Navbar>
            <Outlet/>
        </> 
    );
};

export default BottomNavBar;
