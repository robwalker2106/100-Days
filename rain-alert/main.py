import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "76b9233d1eb9b9e7aadfcdd0317c90b1"
parameters = {'appid': api_key,
              'lat': 25.792240,
              'lon': -80.134850,
              'units': 'imperial'}

# API Request for the local weather
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()

# Parsing the response from the website.
weather = response.json()
weather_hourly = weather['hourly']

print(weather)
print(weather_hourly)
