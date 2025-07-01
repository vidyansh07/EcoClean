import {
    Cpu,
    Settings,
    LayoutGrid,
    LucideIcon
} from "lucide-react";
// import { menu_items } from "@/config/menu.json"

type Submenu = {
    href: string;
    label: string;
    active: boolean;
};

type Menu = {
    href: string;
    label: string;
    active: boolean;
    icon: LucideIcon
    submenus: Submenu[];
};

type Group = {
    groupLabel: string;
    menus: Menu[];
};

export function getMenuList(pathname: string): Group[] {
    // menu_items.forEach(i => {
    //     i.menus.forEach(j => {
    //         j.active = pathname.includes(`${j.href}`)
    //     })
    // })
    // return menu_items
    return [
        {
            groupLabel: "",
            menus: [
                {
                    href: "/dashboard",
                    label: "Dashboard",
                    active: pathname.includes("/dashboard"),
                    icon: LayoutGrid,
                    submenus: []
                }
            ]
        },
        {
            groupLabel: "Devices",
            menus: [
                {
                    href: "",
                    label: "My Devices",
                    active: pathname.includes("/posts"),
                    icon: Cpu,
                    submenus: [
                        {
                            href: "/device/esp32",
                            label: "ESP 32",
                            active: pathname === "/device/esp32"
                        },
                        {
                            href: "/device/raspi",
                            label: "raspi",
                            active: pathname === "/device/raspi"
                        }
                    ]
                },
                // {
                //     href: "/categories",
                //     label: "Categories",
                //     active: pathname.includes("/categories"),
                //     icon: Bookmark,
                //     submenus: []
                // },
                // {
                //     href: "/tags",
                //     label: "Tags",
                //     active: pathname.includes("/tags"),
                //     icon: Tag,
                //     submenus: []
                // }
            ]
        },
        {
            groupLabel: "Settings",
            menus: [
                {
                    href: "/account",
                    label: "Account",
                    active: pathname.includes("/account"),
                    icon: Settings,
                    submenus: []
                }
            ]
        }
    ];
}