import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";
import { title_case } from "@/lib/utils";
import { useLocation, Link } from "react-router-dom";
import 'core-js/features/array/at'; //polyfill 

export const defaultPath = "Car-bon"

export function getPathNames() {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter((x) => x);
  pathnames.unshift("Home");
  return pathnames;
}

export function getCurrentPathName(){
  const pathnames = getPathNames()
  const currentPath = pathnames.length > 1 ? pathnames.at(-1) : defaultPath
  return title_case(currentPath)
}

export function Breadcrumbs() {
  const pathnames = getPathNames();
  return (
    <Breadcrumb>
      <BreadcrumbList>
        {pathnames.map((value, index) => {
          console.log(value);
          const last = index === pathnames.length - 1;
          const to =
            value === "Home"
              ? "/"
              : `/${pathnames.slice(0, index + 1).join("/")}`;
          // const routeName = routes.find((route) => route.path === to)?.name;

          return (
            <>
              {last ? (
                <BreadcrumbItem>
                  <BreadcrumbPage>{title_case(value)}</BreadcrumbPage>
                </BreadcrumbItem>
              ) : (
                <>
                  <BreadcrumbItem>
                    <BreadcrumbLink asChild>
                      <Link to={to}>{title_case(value)}</Link>
                    </BreadcrumbLink>
                  </BreadcrumbItem>
                  <BreadcrumbSeparator />
                </>
              )}
            </>
          );
        })}
      </BreadcrumbList>
    </Breadcrumb>
  );
}
