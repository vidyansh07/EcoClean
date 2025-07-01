"use client";
import { useAuth } from "../providers/AuthProvider/auth";
import { Link, useNavigate } from "react-router-dom";
import { SecureAuthCredentials } from "@/lib/Encryption";
import UserManager from "@/components/user-manager/UserManager";
import { LoginState } from "@/types/UserDetails";
import { Button, Input } from "rsuite";
// import PhoneNumberPicker from "@/components/phone-number-picker/PhoneNumberPicker"; // on register Page
import CryptoJS from "crypto-js";
import { useContext, useEffect, useRef, useState } from "react";
import { Logged_In_User_Context } from "@/Contexts/UserContext";
import { UserDetails } from "@/types/UserDetails";

const RANDOM_SALT = CryptoJS.lib.WordArray.random(128 / 8);

function Login() {
  const UserManagerSession = new UserManager();
  const UserContext = useContext(Logged_In_User_Context);
  let secureAuth = new SecureAuthCredentials(RANDOM_SALT.toString());
  const [isLoggedIn, setIsLoggedIn] = useState<LoginState>(
    LoginState.NotLoggedIn
  );
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const { setToken } = useAuth();
  const passRef = useRef<any>();
  const navigate = useNavigate();

  const handleHash = (token: any): string => {
    let hash = secureAuth.setHash(token);
    console.log(hash);
    console.log(token);
    return String(hash);
  };
  const handleLogin = (event: any) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    let passHash = handleHash(formData.get("password"));
    let username = String(formData.get("username"));
    let user_details: UserDetails = {
      username: username,
      password: passHash,
    };

    if (UserManagerSession.checkIfUserExists(user_details) != null) {
      LoginSucess(passHash);
    } else {
      setIsLoggedIn(LoginState.LoginFailure);
    }
  };

  const LoginSucess = (user_details: any) => {
    setToken(user_details.password);
    navigate("/", { replace: true });
    setIsLoggedIn(LoginState.LoginSuccess);
    UserContext.isLoggedIn = true;
    UserContext.username = user_details.username;
    UserContext.name;
  };

  useEffect(() => {
    if (isLoggedIn == LoginState.LoginFailure) {
      setErrorMessage(
        "Incorrect Username/Password Combination.\nPlease try Again."
      );
    }
  }, [isLoggedIn]);

  return (
    <div className="formContainer">
      <form onSubmit={(e) => handleLogin(e)} className="inputForm">
        <h1 className="boldHeader">Login</h1>
        {errorMessage != null ? (
          <div className="errorMessage">{errorMessage}</div>
        ) : (
          ""
        )}
        <div className="inuputContainer">
          <Input
            type="text"
            id="username"
            name="username"
            placeholder="Email or Phone Number"
            className="inputField"
          />
          <Input
            ref={passRef}
            type="password"
            id="password"
            name="password"
            placeholder="Password"
            className="inputField"
          />
        </div>
        <div className="submitContainer">
          <Button id="sumbitBtn" className="SubmitButton" type="submit">
            Submit
          </Button>
        </div>
        <div className="footer">
          <Link
            to="/register"
            className="inline-block align-baseline font-bold text-sm text-white hover:text-blue-800"
          />
        </div>
      </form>
    </div>
  );
}

export default Login;
