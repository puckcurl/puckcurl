import { lazy } from "react";

import constants from "@constants";
import { AppLayout } from "@layouts";
import ErrorView from "@views/ErrorView";
import HomeView from "@views/HomeView/HomeView";
import NotFoundView from "@views/NotFoundView";
import { SkeletonTheme } from "react-loading-skeleton";
import {
  Outlet,
  RouterProvider,
  ScrollRestoration,
  createBrowserRouter,
} from "react-router-dom";
import { ToastContainer } from "react-toastify";

const Charities = lazy(() => import("@views/Charities"));
const Disclaimer = lazy(() => import("@views/Disclaimer"));
const Donations = lazy(() => import("@views/Donations"));
const Plan = lazy(() => import("@views/Plan"));
const Privacy = lazy(() => import("@views/Privacy"));

function Root() {
  return (
    <>
      <SkeletonTheme
        baseColor="var(--color-dark-amethyst-900)"
        highlightColor="var(--color-dark-amethyst-800)"
      >
        <ScrollRestoration />
        <Outlet />
        <ToastContainer
          position="top-right"
          pauseOnFocusLoss={false}
          toastClassName="text-sm"
          closeOnClick
          pauseOnHover
        />
      </SkeletonTheme>
    </>
  );
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorView />,
    children: [
      {
        element: <AppLayout />,
        children: [
          { index: true, element: <HomeView /> },
          { path: constants.ROUTES.charities, element: <Charities /> },
          { path: constants.ROUTES.disclaimer, element: <Disclaimer /> },
          { path: constants.ROUTES.donations, element: <Donations /> },
          { path: constants.ROUTES.plan, element: <Plan /> },
          { path: constants.ROUTES.privacy, element: <Privacy /> },
          { path: "*", element: <NotFoundView /> },
        ],
      },
    ],
  },
]);

export default function App() {
  return <RouterProvider router={router} />;
}
