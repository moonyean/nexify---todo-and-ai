import { useAuth } from "../../contexts";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export const RequireAuth = ({ children }) => {
  const { loggedUser } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!loggedUser) navigate(-1);
  }, [loggedUser, navigate]);

  return <>{children}</>;
};
