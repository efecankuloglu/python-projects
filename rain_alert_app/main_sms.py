import requests
from twilio.rest import Client

api_key = ""
account_sid = ""
auth_token = ""

parameters = {
    "lat": 41.616756,
    "lon": 41.636745,
    "appid": api_key,
    "units": "metric",
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status
weather_data = response.json()["hourly"]

will_rain = False

for i in range(12):
    if int(weather_data[i]["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella.",
                     from_="",
                     to=''
                 )
    print(message.status)
