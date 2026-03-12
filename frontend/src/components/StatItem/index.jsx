import React from 'react';

export const StateBox = ({ icon: Icon, stateTitle, stateValue }) => {
  return (
    <section>
      <div className="stat-header">
        <Icon /> <p>{stateTitle}</p>
      </div>
      <p>{stateValue}</p>
    </section>
  );
};
