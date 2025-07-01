"use client";
// import { useRef } from "react";
// import PhoneNumberPicker from "@/components/phone-number-picker/PhoneNumberPicker";
import { Button, Input } from "rsuite";
export default function Register() {
  return (
    <div className="RegisterContainer">
      <div className="Header">
        <h1>Register</h1>
      </div>
      <div className="inputForm">
        <Input
          type="text"
          className="inputField"
          placeholder="Enter your Email"
        />
        <Input
          type="password"
          className="inputField"
          placeholder="Enter your Password"
        />
        <Input
          type="text"
          className="inputField"
          placeholder="Register your device ID"
        />
        <label htmlFor="phoneNumberInput"></label>
        {/* <PhoneNumberPicker
          placeholder="Enter yoru phone number"
          name="phoneNumberInput"
        /> */}
        <Button
          id="Submit"
          name="submit"
          type="submit"
          className="SubmitButton"
        >
          Submit
        </Button>
      </div>
    </div>
  );
}
