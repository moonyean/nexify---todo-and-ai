import { useEffect, useState } from 'react';
import './App.css';
import { AuthProvider } from './provider/AuthContext';
import ModalCard from './components/Card';
import Layout from './page/Layout/Layout';

function App() {
  return (
    <>
      <AuthProvider>
        <Layout />
      </AuthProvider>
    </>
  );
}

export default App;
