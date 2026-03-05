import { useEffect, useState } from "react";
import "./App.css";
import { AuthProvider } from "./provider/AuthContext";

function App() {
  const [count, setCount] = useState(0);

  return (
    <AuthProvider>
      <>
        <h1>test</h1>
      </>
    </AuthProvider>
  );
}

export default App;
