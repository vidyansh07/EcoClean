import { ModeToggle } from "@/components/theme-toggle/ThemeToggle";
import { UserNav } from "@/components/PanelLayout/user-nav";
import { SheetMenu } from "@/components/PanelLayout/sheet-menu";
// import { UserButton } from "@clerk/clerk-react";

interface NavbarProps {
  title: string;
}

export function Navbar({ title }: NavbarProps) {
  return (
    <header className="sticky top-0 z-10 w-full bg-background/95 shadow backdrop-blur supports-[backdrop-filter]:bg-background/60 dark:shadow-secondary">
      <div className="mx-4 sm:mx-8 flex h-14 items-center">
        <div className="flex items-center space-x-4 lg:space-x-0">
          <SheetMenu />
          <h1 className="font-bold">{title}</h1>
        </div>
        <div className="flex flex-1 items-center space-x-2 justify-end">
          <ModeToggle />
          {/* <UserButton /> */}
          <UserNav />
        </div>
      </div>
    </header>
  );
}
