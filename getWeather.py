import requests
import logging


def getWeather(city, key):
    """Gets weather data from OpenWeatherMap"""
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    API_KEY = key   # saved in owm_api_key.txt "fc1796c9e66a98785065c1e8456a131c"
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
        logging.error(f"Exception while getting HTTP response: {type(err)} - {err}")
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
            logging.error("Error in the HTTP request nr: " + str(response.status_code))
            # TODO: save to file

    return response_ok, temperature, humidity, wind_speed, pressure
