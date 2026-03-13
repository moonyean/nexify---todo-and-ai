import React from 'react';
import { MenuBar } from '../../components';
import { IoHome, IoChatboxEllipses } from 'react-icons/io5';
import './SideBar.scss';
import { FaUser } from 'react-icons/fa';
import { MdOutlineLogout } from 'react-icons/md';

// const SideBar = ({ className }) => {
const SideBar = () => {
  return (
    <aside className="sideBar_Container">
      <section className="sideBar_top">
        <div className="profile_container">
          <img
            src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Unsplash의Alex Knight"
          />
          <div className="profile">
            <p>Aura AI</p>
            <p>Personal Assistant</p>
          </div>
        </div>
        <div className="profile_container">
          <img
            src="https://images.unsplash.com/photo-1529539795054-3c162aab037a?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            alt="Unsplash의Desola Lanre-Ologun"
          />
          <div className="profile">
            <p>userName</p>
            <p>userEmail</p>
          </div>
        </div>
      </section>

      <section className="sideBar_middle">
        <MenuBar
          icon={IoHome}
          menuName={'Home'}
          onHandleEvent={function () {
            console.log('hello');
          }}
        />
        <MenuBar
          icon={IoChatboxEllipses}
          menuName={'Chat'}
          onHandleEvent={function () {
            console.log('hello');
          }}
        />
        <MenuBar
          icon={FaUser}
          menuName={'Profile'}
          onHandleEvent={function () {
            console.log('hello');
          }}
        />
      </section>

      <section className="sideBar_bottom">
        <MenuBar
          icon={MdOutlineLogout}
          menuName={'Logout'}
          onHandleEvent={function () {
            console.log('hello');
          }}
        />
      </section>
    </aside>
  );
};

export default SideBar;
