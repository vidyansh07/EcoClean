import { Button } from "rsuite";
import { ArrowRightIcon } from "lucide-react";
import { useNavigate } from "react-router-dom";

export default function Landing() {
  let navigate = useNavigate();
  let handleLogin = () => {
    navigate("/login", { replace: true });
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-around overflow-hidden">
      <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
        Welcome to Car-Bon App.
      </h1>
      <div>
        <p>Login to Continue.</p>
        <Button
          appearance="primary"
          color="blue"
          endIcon={<ArrowRightIcon />}
          onClick={handleLogin}
        >
          Login
        </Button>
      </div>
    </div>
  );
}
