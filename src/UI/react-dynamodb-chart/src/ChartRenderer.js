import React, { useEffect, useState } from 'react';
import Chart from 'chart.js/auto';

const ChartRenderer = ({ data }) => {
  const [chart, setChart] = useState(null);
  console.info(data)

  useEffect(() => {
    const canvas = document.querySelector('canvas');
    const ctx = canvas.getContext('2d');

    const newChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: data.map(item => item.timestamp),
        datasets: [{
          label: 'Carbon Monoxide',
          data: data.map(item => item.CO),
        }],
      },
    });

    setChart(newChart);
  }, [data]);

  return (
    <canvas width="100%" height="400px" />
  );
};

export default ChartRenderer;