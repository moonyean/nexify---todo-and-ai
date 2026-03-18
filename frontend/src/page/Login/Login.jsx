import React from 'react';
import { googleLogin } from '../../api/auth';
import './login.scss';

const Login = () => {
  const handleGoogleLogin = (e) => {
    e.preventDefault();
    googleLogin();
  };

  return (
    <main>
      <h4>Aura AI</h4>
      <p>Your Personal AI Assistant</p>
      <form>
        <p>Welcome Back!😹</p>

        <button type="button" onClick={handleGoogleLogin}>
          <img
            src="https://developers.google.com/identity/images/branding_guideline_sample_lt_rd_sl.svg"
            alt="https://developers.google.com/identity/branding-guidelines?hl=ko"
          />
          Continue With Google
        </button>
      </form>
    </main>
  );
};

export default Login;
