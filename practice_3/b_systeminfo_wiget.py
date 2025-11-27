"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets, QtCore
from a_threads import SystemInfo


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.initTread()
        self.__initSignal()
        self.setMinimumSize(290, 45)

    def __initUi(self):
        self.labelCPU = QtWidgets.QLabel()
        self.labelRAM = QtWidgets.QLabel()
        self.labelDelay = QtWidgets.QLabel("Delay")
        self.spinDelay = QtWidgets.QSpinBox()

        delay_layout = QtWidgets.QHBoxLayout()
        delay_layout.addWidget(self.labelDelay)
        delay_layout.addWidget( self.spinDelay)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelCPU)
        layout.addWidget(self.labelRAM)
        layout.addLayout(delay_layout)
        self.setLayout(layout)

    def initTread(self):
        self.worker = SystemInfo()
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()

    def __initSignal(self):
        self.thread.started.connect(self.worker.start)
        self.worker.systemInfoReceived.connect(self.setCpuMemory)
        self.spinDelay.valueChanged.connect(self.setDelay)

    def setCpuMemory(self, data):
        self.labelCPU.setText(f"CPU: {data[0]}%")
        self.labelRAM.setText(f"RAM: {data[1]}%")

    def setDelay(self, delay):
            if delay > 0:
                self.worker.setDelay(delay)

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()