import { Link } from "react-router-dom";
import { MenuIcon } from "lucide-react";
// import { Atom } from "lucide-react";
import CarBonLogo from "@/assets/car-bon-logo.svg";
import { Button } from "@/components/ui/button";
import { Menu } from "@/components/PanelLayout/menu";
import {
  Sheet,
  SheetHeader,
  SheetContent,
  SheetTrigger,
} from "@/components/ui/sheet";
import { useTheme } from "@/components/theme-provider";

export function SheetMenu() {
  const theme = useTheme()
  return (
    <Sheet>
      <SheetTrigger className="lg:hidden" asChild>
        <Button className="h-8" variant="outline" size="icon">
          <MenuIcon size={20} />
        </Button>
      </SheetTrigger>
      <SheetContent className="sm:w-72 px-3 h-full flex flex-col" side="left">
        <SheetHeader>
          <Button
            className="flex justify-center items-center pb-2 pt-1"
            variant="link"
            asChild
          >
            <Link to="/dashboard" className="flex items-center gap-2">
              {/* <Atom className="w-6 h-6 mr-1" /> */}
              <CarBonLogo
                className="w-20 h-20 mr-1"
                style={{
                  filter: `invert(${theme?.theme == "dark" ? 0 : 1})`,
                }}
              />
              <h1 className="font-bold text-lg">Car-Bon</h1>
            </Link>
          </Button>
        </SheetHeader>
        <Menu isOpen />
      </SheetContent>
    </Sheet>
  );
}
