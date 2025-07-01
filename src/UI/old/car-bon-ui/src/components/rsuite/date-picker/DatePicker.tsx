import { useState } from "react";
import { DateRangePicker } from "rsuite";
import { addDays } from "date-fns";

import { Range } from "@/types/date_range_type";

export default function Date_Picker(props: any) {
  const [_, setDateRange] = useState("");

  let update_date_range = (value: any) => {
    setDateRange(value);
    props.update_fn(value);
  };

  const predefinedRanges: Range[] | any = [
    {
      label: "Today",
      value: [new Date(), new Date()],
      placement: "left",
    },
    {
      label: "Yesterday",
      value: [addDays(new Date(), -1), addDays(new Date(), -1)],
      placement: "left",
    },
    {
      label: "Last 7 Days",
      value: [addDays(new Date(), -7), new Date()],
      placement: "left",
    },
    {
      label: "Last 30 Days",
      value: [addDays(new Date(), -30), new Date()],
      placement: "left",
    },
  ];

  return (
    <div>
      <DateRangePicker
        showOneCalendar
        ranges={predefinedRanges}
        format="MM/dd/yyyy HH:mm"
        onOk={update_date_range}
      />
    </div>
  );
}
