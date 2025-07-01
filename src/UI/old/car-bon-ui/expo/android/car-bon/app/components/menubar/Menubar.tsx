import {
    Menubar,
    MenubarContent,
    MenubarItem,
    MenubarMenu,
    MenubarSeparator,
    MenubarShortcut,
    MenubarTrigger,
} from "@/components/ui/menubar";

export default function CustomMenubar() {
    return (
        <Menubar>
            <MenubarMenu>
                <MenubarTrigger>File </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>
                        New Tab <MenubarShortcut> ⌘T </MenubarShortcut>
                    </MenubarItem>
                    <MenubarItem> New Window </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Share </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Print </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Menu </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>
                        New Tab <MenubarShortcut> ⌘T </MenubarShortcut>
                    </MenubarItem>
                    <MenubarItem> New Window </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Share </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Print </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Docs </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>
                        New Tab <MenubarShortcut> ⌘T </MenubarShortcut>
                    </MenubarItem>
                    <MenubarItem> New Window </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Share </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Print </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Home </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>
                        New Tab <MenubarShortcut> ⌘T </MenubarShortcut>
                    </MenubarItem>
                    <MenubarItem> New Window </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Share </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Print </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Help </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>
                        New Tab <MenubarShortcut> ⌘T </MenubarShortcut>
                    </MenubarItem>
                    <MenubarItem> New Window </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Share </MenubarItem>
                    <MenubarSeparator />
                    <MenubarItem>Print </MenubarItem>
                </MenubarContent>
            </MenubarMenu>
        </Menubar>
    );
}
