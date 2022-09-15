from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QTimer
from getWeather import GetWeather
import logging


class MyApp(QWidget):
    def __init__(self, data_model):
        super().__init__()
        self.get_weather = GetWeather()
        self.window_width = 1200
        self.window_height = 800
        self.setMinimumSize(self.window_width, self.window_height)
        self.killThread = False

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.call_get_weather(data_model))
        self.timer.start(10000)

        # thread1 = GetWeather()

        layout_vertical = QVBoxLayout()

        self.text_edit = self.create_and_init_text_edit()

        def button_clicked1():
            self.text_edit.append("------------------------")
            for item in data_model.load_data():
                self.text_edit.append("{} - {}".format(item.datetime, item.price))

        button1 = QPushButton()
        button1.setText("Test 1")
        button1.resize(64, 32)
        button1.clicked.connect(button_clicked1)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button1)

        layout_vertical.addLayout(hbox)
        layout_vertical.addWidget(self.text_edit)

        self.setLayout(layout_vertical)

    @staticmethod
    def create_and_init_text_edit():
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setLineWrapMode(QTextEdit.NoWrap)
        text_edit.setMaximumHeight(500)
        # text_edit.setMaximumWidth(400)
        return text_edit

    def call_get_weather(self, data_model):
        tmpr, hum, ws, press = self.get_weather.get_weather(data_model)
        self.text_edit.append(f"Temperature: {tmpr}°C, Humidity: {hum} %, "
                              f"Wind speed {ws} m/s, Pressure {press} hPa")
