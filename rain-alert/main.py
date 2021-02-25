import requests
import os
from twilio.rest import Client



OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "76b9233d1eb9b9e7aadfcdd0317c90b1"
parameters = {'appid': api_key,
              'lat': 25.792240,
              'lon': -80.134850,
              'units': 'imperial',
              'exclude': 'daily,minutely,current'}

# API Request for the local weather
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()

# Parsing the response from the website.
weather = response.json()
twelve_hour = weather['hourly'][:12]
umbrella = False

for weather_id in twelve_hour:
    if weather_id['weather'][0]['id'] < 700:
        umbrella = True

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)

print(umbrella)

