import React from "react";
import { MenuBar } from "../components";
import { IoHome } from "react-icons/io5";

const sideBar = () => {
  return (
    <aside>
      <h1>hello</h1>
      <MenuBar
        icon={IoHome}
        menuName={"hello"}
        onHandleEvent={function () {
          console.log("hello");
        }}
      />
    </aside>
  );
};

export default sideBar;
