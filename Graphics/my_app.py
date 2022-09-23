from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from getWeather import GetWeather
import logging


class MyApp(object):
    def __init__(self, data_model):
        super().__init__()
        self.get_weather = GetWeather()
        self.city = "Litvínov"
        self.window_width = 1200
        self.window_height = 800
        #self.setMinimumSize(self.window_width, self.window_height)
        self.killThread = False

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.call_get_weather(data_model, self.city))
        self.timer.start(10000)


        def button_clicked1():
            self.text_edit.append("------------------------")
            # for item in data_model.load_data():
                # self.text_edit.append("{} - {}".format(item.datetime, item.price))

# Set layout
        self.central_widget = QWidget()
        self.central_widget.setMinimumSize(600, 300)
        self.central_widget.setGeometry(100, 100, self.window_width, self.window_height)
        self.central_widget.setWindowTitle('Weather log')

        self.main_vertical_layout = QVBoxLayout(self.central_widget)
        self.main_vertical_layout.setContentsMargins(15, 15, 15, 15)
        self.main_vertical_layout.setStretch(0, 0)
        self.main_vertical_layout.setStretch(1, 1)

        self.horizontal_Layout = QHBoxLayout()
        self.horizontal_Layout.setSpacing(15)
        # self.horizontal_Layout.set

        self.info_grid_layout = QGridLayout()
        self.info_grid_layout.setColumnMinimumWidth(0, 120)
        self.info_grid_layout.setColumnMinimumWidth(1, 120)
        # self.info_grid_layout.setContentsMargins(15, 15, 15, 15)

        self.setup_grid_layout = QGridLayout()

        self.horizontal_Layout.addLayout(self.info_grid_layout)
        self.horizontal_Layout.addLayout(self.setup_grid_layout)
        self.horizontal_Layout.addStretch()

        self.main_vertical_layout.addLayout(self.horizontal_Layout)

        self.central_widget.setLayout(self.main_vertical_layout)

# Create widgets
        self.info_label = QLabel(f"Počasí v {self.city}")
        self.info_label.setFont(QFont('Arial', 20))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.label_time = QLabel("Poslední aktualizace: --.--.  --:--:--")
        self.label_temp = QLabel("Teplota: --°C")
        self.label_wind = QLabel("Vítr: -- m/s")
        self.label_hum = QLabel("Vlhkost: -- %")
        self.label_press = QLabel("Tlak: -- hPa")

        self.button1 = QPushButton("Aktualizovat")
        self.button1.resize(64, 32)
        self.button1.clicked.connect(button_clicked1)

        self.text_edit = self.create_and_init_text_edit()


# Insert widgets to layout
        self.info_grid_layout.addWidget(self.info_label, 0, 0, 1, 1)
        self.info_grid_layout.addWidget(self.label_time, 1, 0, 1, 2)
        self.info_grid_layout.addWidget(self.label_temp, 2, 0, 1, 1)
        self.info_grid_layout.addWidget(self.label_wind, 2, 1, 1, 1)
        self.info_grid_layout.addWidget(self.label_press, 3, 0, 1, 1)
        self.info_grid_layout.addWidget(self.label_hum, 3, 1, 1, 1)
        self.setup_grid_layout.addWidget(self.button1, 2, 0, 1, 1)

        self.main_vertical_layout.addWidget(self.text_edit)


    @staticmethod
    def create_and_init_text_edit():
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setLineWrapMode(QTextEdit.NoWrap)
        # text_edit.setMaximumHeight(500)
        # text_edit.setMaximumWidth(400)
        return text_edit

    def call_get_weather(self, data_model, city):
        time, tmpr, hum, ws, press = self.get_weather.get_weather(data_model, city)
        self.label_time.setText(f"Poslední aktualizace: {time.day}.{time.month}.  {time.hour}:{time.minute}:{time.second}")
        self.label_temp.setText(f"Teplota: {tmpr}°C")
        self.label_wind.setText(f"Vítr: {ws} m/s")
        self.label_hum.setText(f"Vlhkost: {hum} %")
        self.label_press.setText(f"Tlak: {press} hPa")
        # self.text_edit.append(f"Grid layout: {self.info_grid_layout.columnStretch(0)}")
