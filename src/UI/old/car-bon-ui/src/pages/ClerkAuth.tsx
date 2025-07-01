import { SignUp } from "@clerk/clerk-react";

export default function ClerkAuth() {
  return (
    <center className="flex min-h-screen items-center justify-center">
      <SignUp path="/register" signInUrl="/login" />
    </center>
  );
}
