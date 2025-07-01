from datetime import datetime, date, timedelta
from dash import Dash, html, dcc, callback, Output, Input
import dash_daq as daq
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from ..services import dynamo
import plotly.express as px
import pandas as pd

TABLE_NAME = "CarBon_Data"
DEVICE_ID = "ESP32"

myDB = dynamo.dynamo(TABLE_NAME)

CURRENT_VALUE = {
    "device_id": "ESP32",
    "timestamp": 1593541800,
    "sensor_values": {"CO": "0.57", "temperature": 0, "humidity": 0},
}

# CURRENT_VALUE = myDB.get_last_Updated_value(DEVICE_ID)

# print(CURRENT_VALUE)

theme = {
    "dark": True,
    "detail": "#007439",
    "primary": "#00EA64",
    "secondary": "#6E6E6E",
}

load_figure_template("darkly")


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY],
    requests_pathname_prefix="/dashboard",
)

app.layout = html.Div(
    [
        html.H1(children="CO Dashboard", style={"textAlign": "center"}),
        html.Div(
            [
                # daq.Gauge(
                #     showCurrentValue=True, id="hum-gauge", label="Humidity", value=6
                # ),
                daq.Gauge(
                    showCurrentValue=True,
                    id="co-gauge",
                    label="Carbon-Monoxide",
                    # value=float(CURRENT_VALUE["sensor_values"]["CO"])/10000,
                    value=9.6,
                ),
                # daq.Gauge(
                #     showCurrentValue=True, id="temp-gauge", label="Temprature", value=6
                # ),
            ],
            style={
                "display": "flex",
                "flex-direction": "row",
                "justify-content": "space-evenly",
            },
        ),
        html.Div(
            [
                dcc.DatePickerRange(
                    id="my-date-picker-range",
                    initial_visible_month=date.fromtimestamp(
                        CURRENT_VALUE["timestamp"]
                    ),
                    start_date=date.fromtimestamp(CURRENT_VALUE["timestamp"])
                    - timedelta(weeks=8),
                    end_date=date.fromtimestamp(CURRENT_VALUE["timestamp"]),
                ),
                dcc.Graph(id="graph-content"),
            ],
            style={"color": "#030303"},
            className="dash-bootstrap",
        ),
    ],
    style={
        "height": "100vh",
        "display": "flex",
        "flex-direction": "column",
        "justify-content": "space-evenly",
    },
)


@callback(
    Output("graph-content", "figure"),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
)
def update_graph(start_date, end_date):
    if start_date is not None:
        start_date_object = datetime.fromisoformat(start_date)
        start_date_string = start_date_object.strftime("%Y-%m-%d %H:%M:%S")
        # string_prefix = string_prefix + "Start Date: " + start_date_string + " | "
    if end_date is not None:
        end_date_object = datetime.fromisoformat(end_date)
        end_date_string = end_date_object.strftime("%Y-%m-%d %H:%M:%S")
        # string_prefix = string_prefix + "End Date: " + end_date_string
    print(int(start_date_object.timestamp()), int(end_date_object.timestamp()))
    data = myDB.get_data_between_timestamps(
        DEVICE_ID,
        int(start_date_object.timestamp()),
        int(end_date_object.timestamp()),
    )
    formatted_data = [
        {
            "time": datetime.fromtimestamp(item["timestamp"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "Carbon-Monoxide": float(item["sensor_values"]["CO"]),
        }
        for item in data["Results"]
    ]
    # print(formatted_data)
    # df = pd.read_csv("./data_input.csv")
    # dff = df[(df["date"] >= start_date_string) & (df["date"] <= end_date_string)]
    dff = pd.DataFrame(formatted_data)
    return px.line(
        dff, x="time", y="Carbon-Monoxide", range_y=0, template="plotly_dark"
    )


# except Exception as e:
#     print(e)


if __name__ == "__main__":
    app.run(debug=True)
