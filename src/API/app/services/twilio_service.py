# Download the helper library from https://www.twilio.com/docs/python/install
from datetime import datetime
import os
from typing import Optional
from twilio.rest import Client
from twilio.rest.api.v2010.account.call import CallInstance
from twilio.twiml.voice_response import VoiceResponse
from pydantic import BaseModel


class twilio_response_subresource_uris(BaseModel):
    notifications: Optional[str]
    recordings: Optional[str]
    feedback: Optional[str]
    feedback_summaries: Optional[str]
    payments: Optional[str]
    events: Optional[str]
    siprec: Optional[str]
    streams: Optional[str]
    user_defined_message_subscriptions: Optional[str]
    user_defined_messages: Optional[str]
    media: Optional[str]


class twilio_call_response_out(BaseModel):
    account_sid: Optional[str]
    answered_by: Optional[str]
    api_version: Optional[str]
    caller_name: Optional[str]
    date_created: Optional[str]
    date_updated: Optional[str]
    duration: Optional[str]
    end_time: Optional[str]
    forwarded_from: Optional[str]
    from_formatted: Optional[str]
    phone_number_sid: Optional[str]
    sid: Optional[str]
    start_time: Optional[str]
    status: Optional[str]
    to: Optional[str]
    to_formatted: Optional[str]
    uri: Optional[str]
    queue_time: Optional[str]


class twilio_sms_response_out(BaseModel):
    message_body : Optional[str]
    sender : Optional[str]
    receiver : Optional[str]
    date_updated : Optional[datetime]
    error_message : Optional[str]
    status : Optional[str]
    sid : Optional[str]
    date_sent : Optional[datetime]
    date_created : Optional[datetime]
    error_code : Optional[str]
    api_version : Optional[str]
   

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


class twilio_service:
    def __init__(self, account_sid_var, auth_token_var, number):
        self.account_sid = account_sid_var
        self.auth_token = auth_token_var
        self.number = number
        self.data_base_dir = "./data/voice_responses"
        self.default_message = "Hey there, This is an Automated call form your car. The Gas Level in your car has exceeded the threshold. Presence of Human or animal was detected in the car. Please open the Car-Bon app and click on Open window button."

    def get_client(self):
        self.client: Client = Client(self.account_sid, self.auth_token)

    def generate_voice_response(self, response_name, response_message):
        os.makedirs(self.data_base_dir, exist_ok=True)
        response = VoiceResponse()
        response_text = response.say(response_message)
        # with open(f"{self.data_base_dir}/{response_name}.xml", "w+") as v_resp:
        #     v_resp.write(response.to_xml())
        out_response = {"response": response, "response_name": response_name}
        return out_response

    def send_message(self, message, receiver):
        message_response = self.client.messages.create(
            body=message,
            from_=self.number,
            to=receiver,
        )
        message_data = message_response.__dict__
        message_response_out = twilio_sms_response_out(
            message_body = message_data["body"],
            sender = message_data["from_"],
            receiver = message_data["to"],
            date_updated = message_data["date_updated"],
            error_message = message_data["error_message"],
            status = message_data["status"],
            sid = message_data["sid"],
            date_sent = message_data["date_sent"],
            date_created = message_data["date_created"],
            error_code = message_data["error_code"],
            api_version = message_data["api_version"],
        )
        return message_response_out

    def call_person(self, receiver):
        message_twiml = self.generate_voice_response(
            "runtime_response", self.default_message
        )
        message_response: CallInstance = self.client.calls.create(
            twiml=message_twiml["response"], to=receiver, from_=self.number
        )
        message_data = message_response.__dict__
        message_response_out = twilio_call_response_out(
            account_sid = message_data["account_sid"],
            answered_by = message_data["answered_by"],
            api_version = message_data["api_version"],
            caller_name = message_data["caller_name"],
            date_created = message_data["date_created"],
            date_updated = message_data["date_updated"],
            duration = message_data["duration"],
            end_time = message_data["end_time"],
            forwarded_from = message_data["forwarded_from"],
            from_formatted = message_data["from_formatted"],
            phone_number_sid = message_data["phone_number_sid"],
            sid = message_data["sid"],
            start_time = message_data["start_time"],
            status = message_data["status"],
            to = message_data["to"],
            to_formatted = message_data["to_formatted"],
            uri = message_data["uri"],
            queue_time = message_data["queue_time"],
        )
        return message_response_out


# twilio_test = twilio_service(ACCOUNT_SID, AUTH_TOKEN, NUMBER)

# twilio_test.get_client()

# # message_response = twilio_test.send_message(
# #     "Hey there this sent from your car. please open the widow.", "+919254566303"
# # )

# message_response = twilio_test.call_person("+919992371909")

# output = message_response

# print(output.model_dump_json(indent = 2))
