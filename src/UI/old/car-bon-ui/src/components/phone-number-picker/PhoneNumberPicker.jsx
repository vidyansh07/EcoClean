import "intl-tel-input/build/css/intlTelInput.css";
import ReactIntlTelInput from "react-intl-tel-input-v2";
import { useState, useRef } from "react";
import { Message } from "rsuite";

export default function PhoneNumberPicker(props) {
  // let / = null;
  const phoneInputField = useRef(null);
  const [isValid, setIsValid] = useState(null);
  const [phoneNumber, setPhoneNumber] = useState(null);
  const inputProps = {
    placeholder: props.placeholder,
  };

  let isValidNumber = (number) => {
    if (number == "") {
      return null;
    }
    try {
      let phNumber = Number(number);
      if (phNumber.length() < 9 || phNumber.length() > 11) {
        return false;
      }
      return true;
    } catch (e) {
      return false;
    }
  };

  const intlTelOpts = {
    preferredCountries: ["in"],
    validationNumberType: "MOBILE",
    useFullscreenPopup: true,
    strictMode: true,
  };

  const onChange = (number) => {
    let phNumber = number.phone;
    setPhoneNumber(phNumber);
    setIsValid(isValidNumber(phNumber));
  };

  return (
    <div>
      <ReactIntlTelInput
        ref={phoneInputField}
        inputProps={inputProps}
        value={{ iso2: "in", dialCode: "91" }}
        intlTelOpts={intlTelOpts}
        onChange={onChange}
        // onReady={onReady}
      />
      {isValid != null ? (
        <Message
          showIcon
          type={isValid ? "success" : "error"}
          header={isValid ? "Success" : "Info"}
        >
          Phone number in E.164 format: <strong>{phoneNumber}</strong>
        </Message>
      ) : (
        ""
      )}
    </div>
  );
}
