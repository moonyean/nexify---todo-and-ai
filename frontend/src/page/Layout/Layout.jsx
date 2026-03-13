import React from 'react';
import SideBar from '../SideBar/SideBar';
import './Layout.scss';

const Layout = ({ children }) => {
  return (
    <>
      {/* <SideBar className="sideBar_Container" /> */}
      <SideBar />
      <main>{children}</main>
    </>
  );
};

export default Layout;
