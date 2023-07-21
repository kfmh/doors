import '../App.css';

import { Outlet, Link } from "react-router-dom";
import React, { useState } from 'react';



const BottomNavBar = () => {
  const [activeTab, setActiveTab] = useState('Home');

  const handleTabClick = (tabName) => {
    setActiveTab(tabName);
  };

  return (
    <>
        <nav className="bottom-nav-bar">
            <Link>
                <button
                    className={activeTab === 'Home' ? 'active' : ''}
                    onClick={() => handleTabClick('Home')}
                >
                    Home
                </button>
            </Link>
            <Link>
                <button
                    className={activeTab === 'Explore' ? 'active' : ''}
                    onClick={() => handleTabClick('Explore')}
                >
                    Explore
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
        </nav>
        <Outlet/>
    </>
  );
};

export default BottomNavBar;
