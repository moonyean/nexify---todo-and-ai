import { useEffect, useState } from 'react';
import './App.css';
import { AuthProvider } from './provider/AuthContext';
// 중요: BrowserRouter를 가져오고, Navigate와 Route도 추가해야 합니다.
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import ModalCard from './components/Card';
import Layout from './page/Layout/Layout';
import Login from './page/Login/Login';
import AuthCallback from './page/Login/AuthCallback';

const isAuthenticated = () => {
  const token = localStorage.getItem('aura_token');
  return !!token;
};

const PrivateRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/login" replace />;
};

function App() {
  useEffect(() => {
    console.log('인증 여부:', isAuthenticated());
  }, []);
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/auth/callback" element={<AuthCallback />} />
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Layout />
              </PrivateRoute>
            }
          />
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
