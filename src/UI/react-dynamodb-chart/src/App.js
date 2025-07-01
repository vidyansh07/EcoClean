import React, { useState } from 'react';
import DynamoDbDataFetcher from './DynamoDbDataFetcher';
import ChartRenderer from './ChartRenderer';
// import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  console.log(data)
  return (
      <div>
        <DynamoDbDataFetcher
          tableName="car-bon"
          device_id="ESP32"
          setData={setData}
        />
        <ChartRenderer
          data={data}
        />
      </div>
  );
}

export default App;
