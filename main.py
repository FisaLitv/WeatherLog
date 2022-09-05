from getWeather import getWeather
from dbHandling import WeatherDbHandle
from datetime import datetime
import time


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    # TODO save start app to file
    lastMin = -1
    wthrDB = WeatherDbHandle("weather")

    while True:
        now = datetime.now()
        if lastMin != now.minute:
            lastMin = now.minute

            rsp_ok, tmpr, hum, ws, press = getWeather("Litvínov")
            if rsp_ok:
                wthrDB.insertData(tmpr, hum, ws, press, now)

        time.sleep(1)
