import { Label, PolarRadiusAxis, RadialBar, RadialBarChart } from "recharts";

import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";
import { title_case } from "@/lib/utils";

const chartConfig = {
  carbon_monoxide: {
    label: "carbon_monoxide",
    color: "hsl(var(--chart-1))",
  },
  humidity: {
    label: "humidity",
    color: "hsl(var(--chart-2))",
  },
  temprature: {
    label: "temprature",
    color: "hsl(var(--chart-3))",
  },
} satisfies ChartConfig;

export default function Kpi(params: any) {
  const chartData = [params.data];
  console.log(chartData);
  return (
    <ChartContainer
      config={chartConfig}
      className="mx-auto aspect-square w-full max-w-[250px]"
    >
      <RadialBarChart
        data={chartData}
        endAngle={0}
        startAngle={180}
        innerRadius={80}
        outerRadius={130}
      >
        <ChartTooltip
          cursor={false}
          content={<ChartTooltipContent hideLabel />}
        />
        <PolarRadiusAxis tick={false} tickLine={false} axisLine={false}>
          <Label
            content={({ viewBox }) => {
              if (viewBox && "cx" in viewBox && "cy" in viewBox) {
                return (
                  <text x={viewBox.cx} y={viewBox.cy} textAnchor="middle">
                    <tspan
                      x={viewBox.cx}
                      y={(viewBox.cy || 0) - 16}
                      className="fill-foreground text-2xl font-bold"
                    >
                      {chartData[0].value}
                    </tspan>
                    <tspan
                      x={viewBox.cx}
                      y={(viewBox.cy || 0) + 4}
                      className="fill-muted-foreground"
                    >
                      {title_case(chartData[0].type)}
                    </tspan>
                  </text>
                );
              }
            }}
          />
        </PolarRadiusAxis>
        <RadialBar
          dataKey="value"
          stackId="a"
          cornerRadius={5}
          fill="#8884d8"
          className="stroke-transparent stroke-2"
        />
        <RadialBar
          dataKey="max"
          fill="#3335"
          stackId="a"
          cornerRadius={5}
          className="stroke-transparent stroke-2"
        />
      </RadialBarChart>
    </ChartContainer>
  );
}
