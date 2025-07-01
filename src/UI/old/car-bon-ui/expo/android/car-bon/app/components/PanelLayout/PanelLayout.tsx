"use client";

import { cn } from "@/lib/utils";
import { Footer } from "@/components/PanelLayout/footer";
import { Sidebar } from "@/components/PanelLayout/sidebar";
import { useState } from "react";
// import { useSidebarToggle } from "@/hooks/use-sidebar-toggle";

export default function AdminPanelLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sidebar, setSidebar] = useState<boolean>(false);

  return (
    <>
      <Sidebar isOpen={sidebar} setIsOpen={setSidebar} />
      <main
        className={cn(
          "min-h-[calc(100vh_-_56px)] bg-zinc-50 dark:bg-zinc-900 transition-[margin-left] ease-in-out duration-300",
          sidebar ? "lg:ml-[90px]" : "lg:ml-72"
        )}
      >
        {children}
      </main>
      <footer
        className={cn(
          "transition-[margin-left] ease-in-out duration-300",
          sidebar ? "lg:ml-[90px]" : "lg:ml-72"
        )}
      >
        <Footer />
      </footer>
    </>
  );
}
