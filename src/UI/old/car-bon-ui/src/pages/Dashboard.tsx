"use client";
import Data_Fetcher from "@/components/data-fetcher/DataFetcher";

export default function Dashboard() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-start p-24">
      <div>
        <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
          Car-Bon DashBoard
        </h1>
      </div>
      <div>
        <Data_Fetcher />
      </div>
    </main>
  );
}
