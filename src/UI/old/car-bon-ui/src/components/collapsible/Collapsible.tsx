import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet"

export default function CustomCollapsible( props: any ) {
  return (
    <Sheet>
      <SheetTrigger asChild>
        {props.TriggerButton}
      </SheetTrigger>
      <SheetContent
      side={props.SideToOpen}>
        <SheetHeader>
          <SheetTitle>{props.HeaderText}</SheetTitle>
          <SheetDescription>
            {props.Description}
          </SheetDescription>
        </SheetHeader>
        {props.CollapsibleContent}
        <SheetFooter>
          {/* <SheetClose asChild>
            <Button type="submit">Save changes</Button>
          </SheetClose> */}
          {props.FooterContent}
        </SheetFooter>
      </SheetContent>
    </Sheet>
  )
}
