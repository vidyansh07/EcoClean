import AdminPanelLayout from "@/components/PanelLayout/PanelLayout";
import { ContentLayout } from "@/components/PanelLayout/content_layout";
import { Logged_In_User_Context } from "@/Contexts/UserContext";
import { default_dummy_user } from "@/types/UserDetails";
import { Link, Outlet } from "react-router-dom";
import { SignedOut, SignedIn, RedirectToSignIn } from "@clerk/clerk-react";
import {
  Breadcrumbs,
  getCurrentPathName,
  defaultPath,
} from "@/routes/Breadcrumbs";
import { useUser } from "@clerk/clerk-react";

// export default function Layout({ children }: { children: React.ReactNode }) {
export default function Layout() {
  const { user } = useUser();
  const currentPath = getCurrentPathName();
  return (
    <Logged_In_User_Context.Provider value={default_dummy_user}>
      <SignedOut>
        <RedirectToSignIn />
      </SignedOut>
      <SignedIn>
        <AdminPanelLayout>
          <ContentLayout
            title={currentPath != undefined ? currentPath : defaultPath}
          >
            <Breadcrumbs />
            {currentPath == defaultPath ? (
              <div className="my-16">
                <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
                  Welcome {user?.firstName}
                </h1>
                <br />
                <h2 className="scroll-m-20 text-xl font-semibold tracking-tight lg:text-2xl">
                  This is your homepage, to check data go to Dashboard from
                  sidebar menu or{" "}
                  <Link to="/dashboard">
                    <u>click here</u>
                  </Link>
                </h2>
              </div>
            ) : (
              <Outlet />
            )}
          </ContentLayout>
        </AdminPanelLayout>
      </SignedIn>
    </Logged_In_User_Context.Provider>
  );
}
