"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
from PySide6 import QtWidgets, QtCore
from a_threads import WeatherHandler


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__initSignals()
    def __initUi(self):
        self.labelLAT= QtWidgets.QLabel("LAT:")
        self.labelLON = QtWidgets.QLabel("LON:")
        self.lineLAT= QtWidgets.QLineEdit()
        self.lineLON = QtWidgets.QLineEdit()
        self.textWeather = QtWidgets.QTextEdit()
        self.textWeather.setReadOnly(True)
        self.buttonStart = QtWidgets.QPushButton("Старт")
        self.buttonStart.setCheckable(True)


        layoutLAT = QtWidgets.QHBoxLayout()
        layoutLAT.addWidget(self.labelLAT)
        layoutLAT.addWidget(self.lineLAT)

        layoutLON = QtWidgets.QHBoxLayout()
        layoutLON.addWidget(self.labelLON)
        layoutLON.addWidget(self.lineLON)



        layoutLAT_LON = QtWidgets.QHBoxLayout()
        layoutLAT_LON .addLayout(layoutLAT)
        layoutLAT_LON .addLayout(layoutLON)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layoutLAT_LON)
        layout.addWidget(self.textWeather)
        layout.addWidget(self.buttonStart)
        self.setLayout(layout)

    def __initSignals(self):
        self.buttonStart.clicked.connect(self.__handleMainThread)

    def __handleMainThread(self, status):
        self.buttonStart.setText("Стоп" if status else "Старт")
        if not status:
            self.thread.stop()
        else:
            if self.lineLAT.text().isdigit() and self.lineLON.text().isdigit():
                self.thread = WeatherHandler(lat=self.lineLAT.text(), lon=self.lineLON.text())
                self.thread.started.connect(lambda:self.__disableInput())
                self.thread.checked.connect(lambda data: self.appendWeatherMessage(data))
                self.thread.finished.connect(lambda: self.buttonStart.setChecked(False))
                self.thread.finished.connect(lambda: self.__disableInput(status=True))
                self.thread.finished.connect(lambda: self.buttonStart.setText("Старт"))
                self.thread.start()

    def appendWeatherMessage(self, text):
        self.textWeather.insertPlainText(f"{text}")

    def __disableInput(self, status=False):
        self.lineLON.setEnabled(status)
        self.lineLAT.setEnabled(status)

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()