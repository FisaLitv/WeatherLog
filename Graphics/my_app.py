from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, \
    QTextEdit, QPushButton, QLabel, QGroupBox, QRadioButton
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
        # self.setMinimumSize(self.window_width, self.window_height)
        self.killThread = False

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.call_get_weather(data_model, self.city))
        self.timer.start(10000)

        def button_clicked1():
            self.call_get_weather(data_model, self.city)

# Set layout
        self.central_widget = QWidget()
        self.central_widget.setMinimumSize(600, 300)
        self.central_widget.setGeometry(100, 100, self.window_width, self.window_height)
        self.central_widget.setWindowTitle('Weather log')

        main_vertical_layout = QVBoxLayout(self.central_widget)
        main_vertical_layout.setContentsMargins(15, 15, 15, 15)
        main_vertical_layout.setStretch(0, 0)
        main_vertical_layout.setStretch(1, 1)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.setSpacing(15)

        info_grid_layout = QGridLayout()
        info_grid_layout.setColumnMinimumWidth(0, 120)
        info_grid_layout.setColumnMinimumWidth(1, 120)

        setup_grid_layout = QGridLayout()
        timing_layout = QHBoxLayout()
        timing_group = QGroupBox("Časování")
        timing_group.setLayout(timing_layout)

        horizontal_layout.addLayout(info_grid_layout)
        horizontal_layout.addLayout(setup_grid_layout)
        horizontal_layout.addStretch()

        main_vertical_layout.addLayout(horizontal_layout)

        self.central_widget.setLayout(main_vertical_layout)

# Create widgets
        self.info_label = QLabel(f"Počasí v {self.city}")
        self.info_label.setFont(QFont('Arial', 20))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.label_time = QLabel("Poslední aktualizace: --.--.  --:--:--")
        self.label_temp = QLabel("Teplota: --°C")
        self.label_wind = QLabel("Vítr: -- m/s")
        self.label_hum = QLabel("Vlhkost: -- %")
        self.label_press = QLabel("Tlak: -- hPa")

        ten_sec_radio_button = QRadioButton("10 sekund")
        ten_sec_radio_button.setChecked(True)
        ten_sec_radio_button.toggled.connect(lambda: self.timing_change(ten_sec_radio_button))
        one_min_radio_button = QRadioButton("1 minuta")
        one_min_radio_button.toggled.connect(lambda: self.timing_change(one_min_radio_button))
        ten_min_radio_button = QRadioButton("10 minut")
        ten_min_radio_button.toggled.connect(lambda: self.timing_change(ten_min_radio_button))
        update_button = QPushButton("Aktualizovat")
        update_button.resize(64, 32)
        update_button.clicked.connect(button_clicked1)
        timing_layout.addWidget(ten_sec_radio_button)
        timing_layout.addWidget(one_min_radio_button)
        timing_layout.addWidget(ten_min_radio_button)

        self.text_edit = self.create_and_init_text_edit()


# Insert widgets to layout
        info_grid_layout.addWidget(self.info_label, 0, 0, 1, 1)
        info_grid_layout.addWidget(self.label_time, 1, 0, 1, 2)
        info_grid_layout.addWidget(self.label_temp, 2, 0, 1, 1)
        info_grid_layout.addWidget(self.label_wind, 2, 1, 1, 1)
        info_grid_layout.addWidget(self.label_press, 3, 0, 1, 1)
        info_grid_layout.addWidget(self.label_hum, 3, 1, 1, 1)
        setup_grid_layout.addWidget(timing_group, 1, 0, 1, 1)
        setup_grid_layout.addWidget(update_button, 2, 0, 1, 1)

        main_vertical_layout.addWidget(self.text_edit)


    @staticmethod
    def create_and_init_text_edit():
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setLineWrapMode(QTextEdit.NoWrap)
        # text_edit.setMaximumHeight(500)
        # text_edit.setMaximumWidth(400)
        return text_edit

    def timing_change(self, radio_button):
        if radio_button.text() == "10 sekund":
            if radio_button.isChecked():
                self.text_edit.append("radio_button 10 sec")
        if radio_button.text() == "1 minuta":
            if radio_button.isChecked():
                self.text_edit.append("radio_button 1 min")
        if radio_button.text() == "10 minut":
            if radio_button.isChecked():
                self.text_edit.append("radio_button 10 min")

    def call_get_weather(self, data_model, city):
        time, tmpr, hum, ws, press = self.get_weather.get_weather(data_model, city)
        self.label_time.setText(f"Poslední aktualizace: {time.day}.{time.month}.  {time.hour}:{time.minute}:{time.second}")
        self.label_temp.setText(f"Teplota: {tmpr}°C")
        self.label_wind.setText(f"Vítr: {ws} m/s")
        self.label_hum.setText(f"Vlhkost: {hum} %")
        self.label_press.setText(f"Tlak: {press} hPa")
        # self.text_edit.append(f"Grid layout: {self.info_grid_layout.columnStretch(0)}")
