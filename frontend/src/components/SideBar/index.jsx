import React from "react";
import "./index.scss";

export const MenuBar = ({ icon: Icon, menuName, onHandleEvent }) => {
  return (
    <section onClick={onHandleEvent} className={`${menuName === "Logout" ? "loginMenu" : ""} menu-bar-container`}>
      <Icon className="menu-icon" /> <span>{menuName}</span>
    </section>
  );
};
