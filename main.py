from datamodel import WeatherDbHandle
import logging
from Graphics.my_app import MyApp
from PyQt5.QtWidgets import QApplication


def print_app_name():
    """Prints the name of application"""
    print("""
    \n-----------
    \rWEATHER LOG
    \r-----------
    """)


if __name__ == '__main__':
    print_app_name()
    logging.basicConfig(level=logging.INFO)
    logging.info("Weather Log started")
    wthrDB = WeatherDbHandle("weather")

    app = QApplication([])
    my_app = MyApp(wthrDB)
    my_app.show()

    try:
        app.exec()
    except SystemExit:
        logging.info("Closing app window")

