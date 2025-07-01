import { Button } from "@/components/ui/button";
import { Menu } from "lucide-react";

export default function HamburgerMenu() {
    return (
        <Button variant="outline" size="icon">
            <Menu />
        </Button>
    )
}