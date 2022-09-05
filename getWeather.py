# importing requests and json
import requests


def getWeather(city):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = city
    API_KEY = "fc1796c9e66a98785065c1e8456a131c"
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
    except:
        pass
    else:
        if response.status_code == 200:
            data = response.json()
            # print(data)
            main = data['main']
            wind = data['wind']
            temperature = main['temp']
            wind_speed = wind['speed']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            response_ok = True

            # print(f'{CITY:-^30}')
            # print(f'Teplota: {temperature} °C')
            # print(f'Vítr: {wind_speed} m/s')
            # print(f'Vlhkost: {humidity} %')
            # print(f'Tlak: {pressure} hPa')
            # print(f'Stav: {report[0]["description"]}')

        else:
            # showing the error message
            print("Error in the HTTP request nr: " + response.status_code)
            # TODO: save to file

    return response_ok, temperature, humidity, wind_speed, pressure
