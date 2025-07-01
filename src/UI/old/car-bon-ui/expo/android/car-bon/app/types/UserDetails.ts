export interface UserDetails {
    name?: string;
    username: string;
    password?: string
    isLoggedIn?: boolean;
}

export const default_dummy_user: UserDetails = {
    name: "Default User",
    username: "dummy_email@dummy.com",
    isLoggedIn: false
}

export enum LoginState {
    LoginSuccess = "Login Success",
    NotLoggedIn = "Not Logged In",
    LoginFailure = "Login Failure",
}