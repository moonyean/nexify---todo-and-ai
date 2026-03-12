import { useEffect, useState } from 'react';
import './App.css';
import { AuthProvider } from './provider/AuthContext';
import SideBar from './page/sideBar'; // sideBar 컴포넌트 import 추가
import ModalCard from './components/Card';

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <h1>hello</h1>
        <SideBar />
        <ModalCard title="Test" content="테스트용임" />
        <h1>alkdfa</h1>
      </AuthProvider>
    </div>
  );
}

export default App;
