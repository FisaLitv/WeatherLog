from getWeather import getWeather
import datamodel as dm
from datetime import datetime
import time
import logging


def print_app_name():
    """Prints the name of application"""
    print("""
    \n-----------
    \rWEATHER LOG
    \r-----------
    """)


def load_api_key():
    """Loads api key for OpenWeatherMap from file owm_api_key.txt"""
    with open("owm_api_key.txt") as file:
        api_key = file.read()
    return api_key


if __name__ == '__main__':
    print_app_name()
    logging.basicConfig(level=logging.INFO)
    logging.info("Weather Log started")
    lastMin = -1
    dm.init_DB()
    owm_api_key = load_api_key()

    while True:
        now = datetime.now()
        if lastMin != now.minute:
            lastMin = now.minute

            rsp_ok, tmpr, hum, ws, press = getWeather("Litvínov", owm_api_key)
            if rsp_ok:
                dm.insertData(tmpr, hum, ws, press, now)

        time.sleep(1)
