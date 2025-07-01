from datetime import date
from enum import Enum
import json
import logging
import os
from typing import Union
from dateutil import parser
from fastapi import FastAPI, APIRouter, status
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse, Response
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

# from fastui import FastUI, AnyComponent, prebuilt_html, components as c
# from fastui.forms import SelectOption
# from fastui.components.display import DisplayMode, DisplayLookup
# from fastui.events import GoToEvent, BackEvent, AnyEvent
from mangum import Mangum
import uvicorn
from phonenumbers import country_code_for_region
from pycountry import countries
from dotenv import load_dotenv
from typing import Union, List
from pydantic import BaseModel

from .UI import ui_app
from .services import (
    secret_manager,
    dynamo,
    twilio_service,
    user_service,
    graph_service,
)
from .helpers import get_version

logger = logging.getLogger("index")

load_dotenv()

if "RUN_INSTANCE" in os.environ and os.environ["RUN_INSTANCE"].lower() == "local":
    TABLE_NAME = os.environ["TABLE_NAME"]
    ACCOUNT_SID = os.environ["ACCOUNT_SID"]
    AUTH_TOKEN = os.environ["AUTH_TOKEN"]
    NUMBER = os.environ["NUMBER"]
    BASE_PATH = "."
    origins = ["*"]
else:
    BASE_PATH = "."
    try:
        CAR_BON_SECRETS = json.loads(secret_manager.get_secret("Car-Bon-Secrets"))
        TABLE_NAME = CAR_BON_SECRETS["TABLE_NAME"]
        ACCOUNT_SID = CAR_BON_SECRETS["ACCOUNT_SID"]
        AUTH_TOKEN = CAR_BON_SECRETS["AUTH_TOKEN"]
        NUMBER = CAR_BON_SECRETS["NUMBER"]
        origins = CAR_BON_SECRETS["ALLOWED_URLS"].split(',') if "ALLOWED_URLS" in CAR_BON_SECRETS.keys() else ["*"]
    except Exception as e:
        logger.warn(f"Unable to get the secrets due to :\n {e}")()


class sensor_data(BaseModel):
    temperature: int
    CO: float
    humidity: int
    CO_PPM: float


class dynamo_result(BaseModel):
    sensor_values: sensor_data
    device_id: str
    timestamp: int


class metadata(BaseModel):
    count: int


class get_all_results_out(BaseModel):
    Results: List[dynamo_result]
    Metadata: metadata


class create_user_out(BaseModel):
    Item: user_service.user_class
    write_successful: bool


class chart_types(str, Enum):
    Bar_graph: str = "Bar"
    Line_graph: str = "Line"


class input_chart(BaseModel):
    start_date: date
    end_date: date
    chart_type: chart_types


app_version = get_version.current_app_version(
    os.path.join(BASE_PATH, "app/app_version")
)

description = """
## Car-Bon API
This API provides an interface to interact with Dynamo DB backend for edge Iot Devices.
This serves following Routers : 
- **DynamoDB** : This serves Dynamo DB access as endpoint. It allows following Functions : 
    - ***get_tables*** - Get tables based on given input value.
    - ***get_item*** - Get a single item from Table Car-Bon based on device_id and timestamp.
    - ***get_items*** - Get all the items from Table Car-Bon based on device_id and from_timestamp and to_timestamp. 
    - ***write_item*** - Write a value to Dynamo DB.
- **User** : This serves User Service as endpoint. It allows following Functions :
    - ***new*** - Create new user.
    - ***contacts*** - Get user contacts based on user ID.
- **Notify** : This serves notification Service as endpoint. It allows following Functions :
    - ***send_sms*** - sends sms to a user's primary phone number using Twillio API.
    - ***make_call*** - makes call to user's primary phone number and plays a predefined message with live stats using Twillio API.
- **Graph** : This serves notification Service as endpoint. It allows following Functions :
    - ***generate*** - Generate and return an interactive SVG for a given time of CO Data based on start_date and end_date inputs.
"""

app = FastAPI(
    title="Car-Bon-service",
    summary="This service acts as a gatekeeper bw aws backend and IOT devices trying to access it.",
    description=description,
    version=app_version,
    # root_path='/car-bon' # causing an issue with base path for openapi spec when cors enabled
)

app.mount("/dashboard/", WSGIMiddleware(ui_app.app.server))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

handler = Mangum(app)

dynamo_router = APIRouter(prefix="/Dynamo", tags=["DynamoDB"])

dynamo_class = dynamo.dynamo(table_name=TABLE_NAME)

twilio_router = APIRouter(prefix="/notify", tags=["Notify"])

twilio_class = twilio_service.twilio_service(
    account_sid_var=ACCOUNT_SID, auth_token_var=AUTH_TOKEN, number=NUMBER
)
twilio_class.get_client()

user_router = APIRouter(prefix="/user", tags=["User"])

user_service_class = user_service.user_service()

graph_router = APIRouter(prefix="/graph", tags=["Graph"])


@app.get("/visualize", include_in_schema=False)
async def serve():
    # return os.path.abspath(os.getcwd())
    return FileResponse(os.path.join(BASE_PATH, "app/UI/Basic/index.html"))


# @app.get("/ui", include_in_schema=False)
# def main_ui():
#     return [
#         c.Page(  # Page provides a basic container for components
#             components=[
#                 c.Heading(text="Users", level=2),  # renders `<h2>Users</h2>`
#                 c.Form(
#                     data=input_chart,
#                     submit_url="/graph/generate/",
#                     method="GET",
#                     display_mode="page",
#                     # form_fields=[
#                     #     c.FormFieldInput(
#                     #         title="start_date",
#                     #         name="start_date",
#                     #         html_type="datetime-local",
#                     #     ),
#                     #     c.FormFieldInput(
#                     #         title="end_date",
#                     #         name="end_date",
#                     #         html_type="datetime-local",
#                     #     ),
#                     #     c.FormFieldSelect(
#                     #         title="chart_type",
#                     #         name="chart_type",
#                     #         options=[
#                     #             SelectOption(value="Bar", label="Bar"),
#                     #             SelectOption(value="Line", label="Line"),
#                     #         ],
#                     #     ),
#                     # ],
#                 ),
#             ]
#         ),
#     ]


@dynamo_router.get("/tables", status_code=status.HTTP_200_OK)
def get_tables():
    return dynamo_class.get_tables()


@dynamo_router.get("/items/{item_id}/{timestamp}", status_code=status.HTTP_200_OK)
def get_item(item_id: str, timestamp: int, q: Union[str, None] = None):
    response = dynamo_class.get_dynamo_data(device_id=item_id, timestamp=timestamp)
    return response


@dynamo_router.get("/items", status_code=status.HTTP_200_OK)
def get_items(
    item_id: str, from_timestamp: int, to_timestamp: int
) -> get_all_results_out:
    response = dynamo_class.get_data_between_timestamps(
        device_id=item_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp
    )
    return get_all_results_out(**response)


@dynamo_router.get("/items/latest", status_code=status.HTTP_200_OK)
def get_latest_item(item_id: str):
    response = dynamo_class.get_last_Updated_value(item_id)
    return response


@dynamo_router.post("/item", status_code=status.HTTP_201_CREATED)
def write_item(item_id: str, Temp: str, Hum: str, CO: str):
    response = dynamo_class.update_table(device_id=item_id, Temp=Temp, Hum=Hum, CO=CO)
    return response


@twilio_router.post("/send_sms", status_code=status.HTTP_200_OK)
def send_sms(user_id: str, message: str):
    contacts = get_contacts(user_id)
    receiver = contacts["personal_contact"]
    message_resp = twilio_class.send_message(message, receiver)
    return message_resp


@twilio_router.post("/make_call", status_code=status.HTTP_200_OK)
def make_call(user_id: str):
    contacts = get_contacts(user_id)
    receiver = contacts["personal_contact"]
    message_resp = twilio_class.call_person(receiver)
    return message_resp


@user_router.post("/new", status_code=status.HTTP_201_CREATED)
def create_user(
    name: str, registered_device_id: str, personal_contact: str, country: Enum("COUNTRY_CODE_TO_REGION_CODE", {country.alpha_2: country.name for country in countries})  # type: ignore
) -> create_user_out:
    try:
        country_code = country_code_for_region(country.name)
        user_creation_response = user_service_class.create_user(
            name=name,
            device_id=registered_device_id,
            personal_contact=f"+{country_code}{personal_contact}",
            secondary_contacts=None,
        )
        return create_user_out(Item=user_creation_response, write_successful=True)
    except Exception as e:
        logger.error(f"Unable to Create User Due to following Error:\n{e}")
        return {
            "error": f"Unable to Create User Due to following Error:\n{e}",
            "message": e,
        }


@user_router.get("/contacts", status_code=status.HTTP_200_OK)
def get_contacts(user_id):
    user = user_service_class.get_user(user_id)
    return {
        "personal_contact": user.personal_contact,
        "secondary_contacts": user.secondary_contacts,
    }


@graph_router.get("/generate", status_code=status.HTTP_200_OK)
def graph_generator(
    start_date: str,
    end_date: str,
    graph_type: graph_service.graph_types = "Line",
    device: str = "ESP32",
):
    start_date_timestamp = int(parser.parse(start_date).timestamp())
    end_date_timestamp = int(parser.parse(end_date).timestamp())
    data: get_all_results_out = get_items(
        device, start_date_timestamp, end_date_timestamp
    )
    data = graph_service.generate_graph(data.model_dump_json(), graph_type, BASE_PATH)
    # html_content = open(file).read()
    # html_content_loaded : Response = html_content
    # headers = html_content_loaded.headers
    resp_headers = {
        # "Content-Type": headers["Content-Type"],
        # "Content-Length": headers["Content-Length"],
        "start_date": str(start_date_timestamp),
        "end_date": str(end_date_timestamp),
        "device_type": device,
    }
    response_out = {"base64_data": data}
    return JSONResponse(content=response_out, status_code=200, headers=resp_headers)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()

app.include_router(user_router)
app.include_router(twilio_router)
app.include_router(dynamo_router)
app.include_router(graph_router)
