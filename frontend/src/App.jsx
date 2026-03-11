import { useEffect, useState } from "react";
import "./App.css";
import { AuthProvider } from "./provider/AuthContext";
import sideBar from "./page/sideBar";

function App() {
  const [count, setCount] = useState(0);

  return (
    <AuthProvider>
      <dv
      <SideBar />
    </AuthProvider>
  );
}

export default App;
