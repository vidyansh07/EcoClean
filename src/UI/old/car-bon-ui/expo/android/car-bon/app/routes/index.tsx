import { RouterProvider, createBrowserRouter } from "react-router-dom";
// import { useAuth } from "../providers/AuthProvider/auth";
import Layout from "@/components/PanelLayout/Layout";
// import Home from "../pages/Home";
// import { ProtectedRoute } from "./ProtectedRoute";
import ClerkAuth from "../pages/ClerkAuth";
import ClerkLogin from "../pages/ClerkLogin";
import ClerkDefault from "../pages/ClerkDefault";
import Devices from "@/pages/Devices";
// import Login from "../pages/Login";
// import Register from "../pages/Register";
// import Logout from "../pages/Logout";
// import Landing from "../pages/Landing";
import { UserProfile } from "@clerk/clerk-react";

const Routes = () => {
  // Define public routes accessible to all users
  const routesForPublic = [
    {
      path: "/service",
      element: <div>Service Page</div>,
    },
    {
      path: "/about-us",
      element: <div>About Us</div>,
    },
  ];

  // Define routes accessible only to authenticated users
  const routesForAuthenticatedOnly = [
    {
      path: "/login/*",
      element: <ClerkLogin />, //<Login />,
    },
    {
      path: "/register",
      element: <ClerkAuth />, //<Register />,
    },
    {
      path: "/",
      element: <Layout />, // Wrap the component in ProtectedRoute
      children: [
        {
          path: "/dashboard",
          element: <ClerkDefault />,
        },
        {
          path: "/account",
          element: (
            <center className="my-5">
              <UserProfile />
            </center>
          ),
        },
        {
          path: "/device/*",
          element: (
            <div>
              <Devices />
            </div>
          ),
        },
      ],
    },
  ];

  // Define routes accessible only to non-authenticated users
  // const routesForNotAuthenticatedOnly = [

  // ];

  // Combine and conditionally include routes based on authentication status
  const router = createBrowserRouter([
    ...routesForPublic,
    ...routesForAuthenticatedOnly,
  ]);

  // Provide the router configuration using RouterProvider
  return <RouterProvider router={router} />;
};

export default Routes;
