import { useState, useEffect } from "react";
import Date_Picker from "@/components/rsuite/date-picker/DatePicker";
import { RenderLineChart } from "@/components/rsuite/charts/Charts";

export default function Data_Fetcher(props: any) {
  const [coData, setCoData] = useState([
    [0, 1],
    [2, 3],
  ]);

  // DONE: add dates states here as variables
  // CANCEL: pass date vars as props to datepicker
  // DONE: use useEffect to fetch data and render Linechart

  let currentTime = new Date();
  let prevTime = new Date();
  prevTime.setTime(currentTime.getTime() - 5);

  const [times, setTimes] = useState([
    prevTime.getTime(),
    currentTime.getTime(),
  ]);

  const Device_Id = props.Item ?? "ESP32";
  // let base_url = "http://localhost:8000";
  let base_url = "https://wnscghtuqzqlnlmthgpyhzdmby0cbgps.lambda-url.us-east-1.on.aws";

  let url = `${base_url}/Dynamo/items?item_id=${Device_Id}&from_timestamp=${times[0]}&to_timestamp=${times[1]}`;

  const currentHeaders = new Headers();
  currentHeaders.append("Accept", "application/json");
  currentHeaders.append("Access-Control-Allow-Origin", "*");

  const requestOptions = {
    method: "GET",
    headers: currentHeaders,
  };

  useEffect(() => {
    fetch(url, requestOptions).then(async (i) => {
      let results = JSON.parse(await i.text());
      console.log(await results);
      setCoData([
        ...results.Results.map((val :any ) => [
          new Date(val.timestamp * 1000).toDateString(),
          Number(val.sensor_values.CO_PPM.toFixed(4)),
        ]),
      ]);
    });
  }, [times]);

  //   setCoData = JSON.parse(result).map(i=> return [i.timestamp, i.sensor_values.CO_PPM])
  return (
    <div className="p-5">
      <div className="p-12">
        <Date_Picker
          update_fn={(args: any) =>
            setTimes([...args.map((i: any) => new Date(i).getTime() / 1000)])
          }
        />
      </div>
      <div>
        <RenderLineChart data={[...coData]} name="CO Level" />
      </div>
    </div>
  );
}
