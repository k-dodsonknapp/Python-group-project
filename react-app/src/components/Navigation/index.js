
import React, { useEffect, useState } from 'react';
import { NavLink, useParams } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import "./nav.css"
import { useSelector } from 'react-redux';
import SearchResults from '../SearchResults';

const Navigation = () => {
  // const session = useSelector(state => session.user)
  const [showMenu, setShowMenu] = useState(false)
  const [seeCategory, setSeeCategory] = useState(false)

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

  // const whichCategory(() => {
  //   const { category } = useParams();

  // })

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
            </div>
            <div className='profile-following-div'>
              <button id='profile-quickmenu' onClick={openMenu}>
                <img src='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg' style={{}}></img>
              </button>
            </div>
          </div>
          <div className="lower-nav">
            <div className='left-lower'>
              <div className='step-by-step-logo'>
                <NavLink to='/'>
                  <img src="https://www.instructables.com/assets/img/instructables-logo-v2.png" />
                  <p>step by step</p>
                </NavLink>
              </div>
              <div>
                <button>Projects</button>
                <button>Contests</button>
              </div>
            </div>
            <div className='right-lower'>
              <div>
                <NavLink to="/create">PUBLISH</NavLink>
              </div>
              <div className='search-field'>
                <SearchResults />
              </div>
            </div>
          </div>
        </ul>
      </nav>
      {showMenu && (
        <ul className='profile-options'>
          <div className='dropdown-div'>
            <li>
              <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "black" }}>
                Login
              </NavLink>
            </li>
            <li>
              <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
                Sign Up
              </NavLink>
            </li>
            <li>
              <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
                Users
              </NavLink>
            </li>
            <div className='nav-links'>
              <li>
                <LogoutButton />
              </li>
            </div>
          </div>
        </ul>
      )}
    </div>
  );
}

export default Navigation;
