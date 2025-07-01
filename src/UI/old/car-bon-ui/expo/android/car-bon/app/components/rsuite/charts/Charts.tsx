"use client";
import * as React from "react";
import {
  BarChart,
  FunnelChart,
  LineChart,
  MapChart,
  PieChart,
  RadarChart,
  SankeyChart,
  ScatterChart,
  TreeChart,
  TreemapChart,
} from "@rsuite/charts";

const RenderLineChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <LineChart ref={ref} name={name} data={data} />;
  }
);

const RenderFunnelChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <FunnelChart ref={ref} name={name} data={data} />;
  }
);

const RenderBarChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <BarChart ref={ref} name={name} data={data} />;
  }
);

const RenderMapChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <MapChart ref={ref} name={name} data={data} />;
  }
);

const RenderPieChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <PieChart ref={ref} name={name} data={data} />;
  }
);

const RenderRadarChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <RadarChart ref={ref} name={name} data={data} />;
  }
);

const RenderSankeyChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <SankeyChart ref={ref} name={name} data={data} />;
  }
);

const RenderScatterChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <ScatterChart ref={ref} name={name} data={data} />;
  }
);

const RenderTreeChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <TreeChart ref={ref} name={name} data={data} />;
  }
);

const RenderTreemapChart = React.forwardRef(
  ({ name, data }: { name: any; data: any }, ref) => {
    return <TreemapChart ref={ref} name={name} data={data} />;
  }
);

export {
  RenderBarChart,
  RenderFunnelChart,
  RenderLineChart,
  RenderMapChart,
  RenderPieChart,
  RenderRadarChart,
  RenderSankeyChart,
  RenderScatterChart,
  RenderTreeChart,
  RenderTreemapChart,
};
