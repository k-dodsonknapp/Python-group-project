
import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import "./nav.css"
// import { useSelector } from 'react-redux';
import SearchResults from '../SearchResults';

const Navigation = () => {
  // const session = useSelector(state => session.user)
  const [showMenu, setShowMenu] = useState(false)
  // const [seeCategory, setSeeCategory] = useState(false)

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
                <NavLink to='/projects/1' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Circuits
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/2' exact={true} activeClassName='something' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Workshop
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/3' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Craft
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/4' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Cooking
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/5' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Living
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/6' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Outside
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/7' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Teachers
                </NavLink>
              </li>
            </div>
            <div className='profile-following-div'>
              <button id='profile-quickmenu' onClick={openMenu}>
                <img src='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg' alt=''></img>
              </button>
            </div>
          </div>
          <div className="lower-nav">
            <div className='left-lower'>
              <div className='step-by-step-logo'>
                <NavLink to='/'>
                  <img src="https://www.instructables.com/assets/img/instructables-logo-v2.png" alt=''/>
                  <p>step by step</p>
                </NavLink>
              </div>
              {/* <div>
                <button>Projects</button>
                <button>Contests</button>
              </div> */}
            </div>
            <div className='right-lower'>
              <div>
                <NavLink to="/create">PUBLISH</NavLink>
              </div>
              <div>
                <SearchResults />
              </div>
            </div>
          </div>
        </ul>
      </nav>
      {showMenu && (
        <ul className='profile-options'>
          <div className='dropdown-div'>
            <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Login
                </li>
              </div>
            </NavLink>
            <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Sign Up
                </li>
              </div>
            </NavLink>
            {/* <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Users
                </li>
              </div>
            </NavLink> */}
            <div className='dropdown-btns'>
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
