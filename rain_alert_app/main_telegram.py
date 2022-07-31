import requests

api_key = ""
token = ""
userID = ""
message = "It's going to rain today. Remember to bring an umbrella."

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

print(will_rain)

if will_rain:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {'chat_id': userID, 'text': message}
    requests.post(url, data)
