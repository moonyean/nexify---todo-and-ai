import React from 'react';

// Component names must start with a capital letter so React treats them
// as custom components rather than HTML tags. We'll also provide a default
// export for easier importing elsewhere.
export const ModalCard = ({ title, content }) => {
  return (
    <section>
      <h2>{title}</h2>
      <span>{content}</span>
      <button>X Dismiss</button>
    </section>
  );
};

export default ModalCard;
