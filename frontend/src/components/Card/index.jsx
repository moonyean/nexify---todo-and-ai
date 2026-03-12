import React from 'react';

export const modalCard = ({ title, content }) => {
  return (
    <dialog>
      <h2>{title}</h2>
      <span>{content}</span>
    </dialog>
  );
};
