import {
  Children,
  createContext,
  useCallback,
  useEffect,
  useState,
} from "react";

export const AuthContext = createContext();

export const AuthProvider = () => {
  const [user, setUSer] = useState(() => {
    try {
      const storedUser = localStorage.getItem("user");
      return storedUser ? JSON.parse(storedUser) : null;
    } catch (e) {
      console.error(e);
    }
  });

  const login = useCallback((userData) => {
    localStorage.setItem("user", JSON.stringify(userData));
    setUser(userData);
  }, []);

  const logout = useCallback(() => {
    localStorage.removeItem("user");
    localStorage.removeItem("token");
    setUser(null);
  }, []);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {Children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth는 AuthProvider 내에서 사용 가능");
  }
  return context;
};
