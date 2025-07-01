import { Link } from "react-router-dom";
// import { Atom } from "lucide-react";
import CarBonLogo from "@/assets/car-bon-logo.svg";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Menu } from "@/components/PanelLayout/menu";
import { SidebarToggle } from "@/components/PanelLayout/sidebarToggle";
import { useState } from "react";
import { useTheme } from "@/components/theme-provider";

export function Sidebar({
  isOpen,
  setIsOpen,
}: {
  isOpen: boolean;
  setIsOpen: (state: boolean) => void;
}) {
  const [sidebarIsOpen, setSidebarIsOpen] = useState<boolean>(isOpen);
  const theme = useTheme()
  let set_is_sidebar_open = () => {
    setSidebarIsOpen(!sidebarIsOpen);
    setIsOpen(!sidebarIsOpen);
  };

  return (
    <aside
      className={cn(
        "fixed top-0 left-0 z-20 h-screen -translate-x-full lg:translate-x-0 transition-[width] ease-in-out duration-300",
        sidebarIsOpen ? "w-[90px]" : "w-72"
      )}
    >
      <SidebarToggle isOpen={sidebarIsOpen} setIsOpen={set_is_sidebar_open} />
      <div className="relative h-full flex flex-col px-3 py-4 overflow-y-auto shadow-md dark:shadow-zinc-800">
        <Button
          className={cn(
            "transition-transform ease-in-out duration-300 mb-1",
            sidebarIsOpen ? "translate-x-1" : "translate-x-0"
          )}
          variant="link"
          asChild
        >
          <Link to="/dashboard" className="flex items-center gap-2">
            <CarBonLogo className="w-20 h-20 mr-1" style = {{
              filter : `invert(${theme?.theme == "dark" ? 0: 1})`
            }}/>
            <h1
              className={cn(
                "font-bold text-lg whitespace-nowrap transition-[transform,opacity,display] ease-in-out duration-300",
                sidebarIsOpen
                  ? "-translate-x-96 opacity-0 hidden"
                  : "translate-x-0 opacity-100"
              )}
            >
              Car-Bon
            </h1>
          </Link>
        </Button>
        <Menu isOpen={!sidebarIsOpen} />
      </div>
    </aside>
  );
}
