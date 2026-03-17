import React from 'react';
import { googleLogin } from '../../api/auth';

const Login = () => {
  const handleGoogleLogin = (e) => {
    e.preventDefault();
    googleLogin();
  };

  return (
    <main>
      <h4>Aura AI</h4>
      <p>Sign in with your Google account to continue</p>
      <form>
        <p>Welcome Back!😹</p>
        <button type="button" onClick={handleGoogleLogin}>
          Google Login
        </button>
      </form>
    </main>
  );
};

export default Login;
