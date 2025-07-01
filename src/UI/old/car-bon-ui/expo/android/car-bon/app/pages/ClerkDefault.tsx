import Landing from "./Landing";
// import Home from "./Home";
import Dashboard from "./Dashboard";
import { SignedIn, SignedOut } from "@clerk/clerk-react";

export default function ClerkDefault() {
  return (
    <>
      <SignedOut>
        <Landing />
      </SignedOut>
      <SignedIn>
        <Dashboard />
      </SignedIn>
    </>
  );
}
