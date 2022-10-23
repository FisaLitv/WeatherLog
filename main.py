import datamodel as dm
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
    dm.init_DB()

    app = QApplication([])
    app.setStyle('Fusion')
    my_app = MyApp(dm)
    my_app.central_widget.show()

    try:
        app.exec()
    except SystemExit:
        logging.info("Closing app window")

