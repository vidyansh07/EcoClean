import { TrendingUp } from "lucide-react";
import Kpi from "@/components/custom/kpi";
import { getCurrentPathName } from "@/routes/Breadcrumbs";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export default function Devices() {
  const device_id = getCurrentPathName();
  const chartData = [
    {
      device: device_id,
      type: "temprature",
      value: 23,
      max: 56.7,
    },
    {
      device: device_id,
      type: "carbon_monoxide",
      value: 29.6,
      max: 100,
    },
    {
      device: device_id,
      type: "humidity",
      value: 25,
      max: 100,
    },
  ];

  return (
    <Card className="flex flex-col my-20 sm:my-4">
      <CardHeader className="items-center pb-0">
        <CardTitle>Device ID : {device_id}</CardTitle>
        <CardDescription>
          Current Sensor Values for Device ID : {device_id}
        </CardDescription>
      </CardHeader>
      <CardContent className="flex flex-1 flex-col sm:flex-row  items-center pb-0">
        {chartData.map((i: any) => <Kpi data={i} />)}
      </CardContent>
      <CardFooter className="flex-col gap-2 text-sm">
        <div className="flex items-center gap-2 font-medium leading-none">
          Sensor Values Trend <TrendingUp className="h-4 w-4" />
        </div>
        <div className="leading-none text-muted-foreground">
          Current Sensor Values for Device ID : {device_id}
        </div>
      </CardFooter>
    </Card>
  );
}
