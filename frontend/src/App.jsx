import { useEffect, useState } from 'react';
import './App.css';
import { AuthProvider } from './provider/AuthContext';
import ModalCard from './components/Card';
import Layout from './page/Layout/Layout';
import Login from './page/Login/Login';

function App() {
  return (
    <>
      <AuthProvider>
        <Login />
        {/* <Layout /> */}
      </AuthProvider>
    </>
  );
}

export default App;
