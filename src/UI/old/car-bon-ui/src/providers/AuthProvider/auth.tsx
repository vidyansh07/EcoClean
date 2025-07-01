import axios from "axios";
import { createContext, useContext, useEffect, useMemo, useState } from "react";
import { SecureLocalStorage } from "@/lib/Encryption";

const secureSession = new SecureLocalStorage("car-bon");
const STORAGE_KEY_NAME = "security_token";
const AuthContext = createContext<any>("");

const AuthProvider = ({ children }: { children: any }) => {
  // State to hold the authentication token
  const [token, setToken_] = useState(
    secureSession.getKeyFromStorage(STORAGE_KEY_NAME)
  );

  // Function to set the authentication token
  const setToken = (newToken: any) => {
    setToken_(newToken);
  };

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
      secureSession.setValueToStorage(STORAGE_KEY_NAME, { token: token });
    } else {
      delete axios.defaults.headers.common["Authorization"];
      secureSession.removeKeyFromStorage(STORAGE_KEY_NAME);
    }
  }, [token]);

  // Memoized value of the authentication context
  const contextValue = useMemo(
    () => ({
      token,
      setToken,
    }),
    [token]
  );

  // Provide the authentication context to the children components
  return (
    <AuthContext.Provider value={contextValue}>{children}</AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};

export default AuthProvider;
