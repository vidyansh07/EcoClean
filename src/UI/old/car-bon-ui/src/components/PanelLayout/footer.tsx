import { Link } from "react-router-dom";
import CarBonLogo from "@/assets/car-bon-logo.svg?react";
import { Divider } from "rsuite";
import { useTheme } from "@/components/theme-provider";

export function Footer() {
  const theme = useTheme();
  console.log(theme)
  return (
    <footer className=" flex flex-col lg:flex-row justify-start items-center z-20 w-full bg-background/95 shadow backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="mx-4 md:mx-8 my-2 items-center justify-center">
        <CarBonLogo
          className="w-20 h-20"
          style={{
            filter: `invert(${theme?.theme == "dark" ? 0 : 1})`,
          }}
        />
      </div>
      <Divider className="hidden lg:block h-full" />
      <div className="flex flex-row items-stretch justify-evenly w-full my-12">
        <Link to="/">Home</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/account">Account</Link>
      </div>
    </footer>
  );
}
