import { useEffect, useState } from "react";
import "./App.css";
import { AuthProvider } from "./provider/AuthContext";
import SideBar from "./page/sideBar";  // sideBar 컴포넌트 import 추가

function App() {
  return (
    <div className="App">    
      <AuthProvider>
        <h1>hello</h1>
        <SideBar></SideBar>
      </AuthProvider>
    </div>

  );   
}

export default App;
