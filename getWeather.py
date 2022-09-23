# importing requests and json
import requests
import logging
from datetime import datetime


class GetWeather:
    def __init__(self):
        """Loads api key for OpenWeatherMap from file owm_api_key.txt"""
        self.api_key = ""
        with open("owm_api_key.txt") as file:
            self.api_key = file.read()

    def getWeather(self, time, city):
        """Gets weather data from OpenWeatherMap"""
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = city
        API_KEY = self.api_key  # saved in owm_api_key.txt "fc1796c9e66a98785065c1e8456a131c"
        UNITS = "metric"
        LANG = "cz"
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=" + UNITS + "&lang=" + LANG

        response_ok = False
        temperature = 0.0
        humidity = 0
        wind_speed = 0.0
        pressure = 0

        # HTTP request
        try:
            response = requests.get(URL)
        except BaseException as err:
            logging.error(f"\n{time.day}.{time.month} {time.hour}:{time.minute}"
                          f" - Exception while getting HTTP response: {type(err)} - {err}")
        else:
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                wind = data['wind']
                temperature = main['temp']
                wind_speed = wind['speed']
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                response_ok = True

            else:
                # showing the error message
                print("Error in the HTTP request nr: " + str(response.status_code))
                # TODO: save to file

        return response_ok, temperature, humidity, wind_speed, pressure

    def get_weather(self, data_model, city):
        logging.info("get_weather called")
        now = datetime.now()
        rsp_ok, tmpr, hum, ws, press = self.getWeather(now, city)
        if rsp_ok:
            data_model.insertData(tmpr, hum, ws, press, now)
        return now, tmpr, hum, ws, press
