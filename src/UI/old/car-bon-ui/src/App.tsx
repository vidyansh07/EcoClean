import { ThemeProvider } from "@/components/theme-provider";
import "rsuite/dist/rsuite-no-reset.min.css";
import "./App.css";
import AuthProvider from "./providers/AuthProvider/auth";
import { ModeToggle } from "@/components/theme-toggle/ThemeToggle";
import Routes from "./routes";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <AuthProvider>
        <div className="absolute top-0 right-0 p-4">
          <ModeToggle />
        </div>
        <Routes />
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
