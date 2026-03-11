import React from "react";

export const MenuBar = ({ icon: Icon, menuName, onHandleEvent }) => {
  return (
    <section onClick={onHandleEvent}>
      <Icon /> <span>{menuName}</span>
    </section>
  );
};
