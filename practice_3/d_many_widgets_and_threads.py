"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_wiget import Window as WorkerOne
from c_wheatherapi_widget import Window as WorkerTwo

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__initSignals()
        self.initTread()

    def __initUi(self):
        self.buttonWeather = QtWidgets.QPushButton("Запустить Weather")
        self.buttonSysInfo = QtWidgets.QPushButton("Запустить SysInfo")
        self.buttonCloseALL = QtWidgets.QPushButton("Закрыть окна")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.buttonWeather)
        layout.addWidget(self.buttonSysInfo)
        layout.addWidget(self.buttonCloseALL)
        self.setLayout(layout)

    def initTread(self):
        self.sysInfo_thread = WorkerOne()
        self.weather_thread = WorkerTwo()

    def __initSignals(self):
        self.buttonWeather.clicked.connect(self.startWeather)
        self.buttonSysInfo.clicked.connect(self.startSysInfo)
        self.buttonCloseALL.clicked.connect(self.closeAll)

    def startSysInfo(self):
        self.sysInfo_thread.show()

    def startWeather(self):
        self.weather_thread.show()

    def closeAll(self):
            if self.sysInfo_thread.isEnabled():
                self.sysInfo_thread.close()
            if self.weather_thread.isEnabled():
                self.weather_thread.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()