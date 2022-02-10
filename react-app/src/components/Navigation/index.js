
import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import "./nav.css"
import { useSelector } from 'react-redux';

const Navigation = () => {
  // const session = useSelector(state => session.user)
  const [showMenu, setShowMenu] = useState(false)

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  }

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu)
  }, [showMenu])

  return (
    <div className='navbar'>
      <nav>
        <ul>
          <div className='nav-container'>
            <div className='category-links'>
              {/* <li id="home-icon"> */}
              <NavLink to='/' exact={true} id="home-icon" activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                🏠
              </NavLink>
              {/* </li> */}
              <li>
                <NavLink to='/Circuits' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Circuits
                </NavLink>
              </li>
              <li>
                <NavLink to='/Workshop' exact={true} activeClassName='something' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Workshop
                </NavLink>
              </li>
              <li>
                <NavLink to='/Craft' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Craft
                </NavLink>
              </li>
              <li>
                <NavLink to='/Cooking' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Cooking
                </NavLink>
              </li>
              <li>
                <NavLink to='/Living' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Living
                </NavLink>
              </li>
              <li>
                <NavLink to='/Outside' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Outside
                </NavLink>
              </li>
              <li>
                <NavLink to='/Teachers' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Teachers
                </NavLink>
              </li>
              <div className=''>
                <button id='profile-quickmenu' onClick={openMenu}>profile</button>
              </div>
            </div>
          </div>
        </ul>
      </nav>
      {showMenu && (
        <ul className='profile-options'>
          <div className='dropdown-div'>
            <li>
              <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                Login
              </NavLink>
            </li>
            <li>
              <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                Sign Up
              </NavLink>
            </li>
            <li>
              <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                Users
              </NavLink>
            </li>
            <div className='nav-links'>
              <li>
                <LogoutButton />
              </li>
            </div>
            <li>Another hello</li>
          </div>
        </ul>
      )}
      {/* <div className='nav-links'>
              <li>
                <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Login
                  </NavLink>
                  </li>
                </div> */}
      {/* <div className='nav-links'>
        <li>
          <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
            Sign Up
          </NavLink>
        </li>
      </div>
      <div className='nav-links'>
        <li>
          <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
            Users
          </NavLink>
        </li>
      </div> */}
      {/* <div className='nav-links'>
        <li>
          <LogoutButton />
        </li>
      </div> */}
    </div>
  );
}

export default Navigation;
