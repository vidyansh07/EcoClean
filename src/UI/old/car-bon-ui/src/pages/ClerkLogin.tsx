import { SignIn } from "@clerk/clerk-react";

export default function ClerkLogin() {
//   const { isLoaded, signIn } = useSignIn();

  return (
    <center className="flex min-h-screen justify-center items-center">
      <SignIn path="/login" signUpUrl="/register" />
    </center>
  );
}
