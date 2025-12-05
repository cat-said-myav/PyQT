from itertools import count

from PySide6 import QtWidgets, QtCore
from worker import SystemInfo
from graph import SystemWidget

class SystemMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__initSignals()
        self.thread = None
        self.setMinimumSize(290, 45)
        self.graph_dict = {}

    def __initUi(self):
        self.table = QtWidgets.QTableWidget(5, 1)
        self.table.horizontalHeader().hide()
        self.table.setVerticalHeaderLabels(["CPU", "RAM_usage", "RAM_free", "DISK_usage", "DISK_free"])
        self.table.setFixedSize(120, 160)
        for i in range(5):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem("0%"))
        self.labelDelay = QtWidgets.QLabel("Delay")
        self.spinDelay = QtWidgets.QSpinBox()
        self.spinDelay.setRange(1, 30)
        self.spinDelay.setSingleStep(1)
        self.engineButton = QtWidgets.QPushButton("Старт")
        self.engineButton.setCheckable(True)
        delay_layout = QtWidgets.QVBoxLayout()
        delay_layout.addWidget(self.labelDelay)
        delay_layout.addWidget( self.spinDelay)
        delay_layout.addWidget(self.engineButton)
        self.graphlayout = QtWidgets.QHBoxLayout()
        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(delay_layout)
        layout.addLayout(self.graphlayout)
        layout.addWidget(self.table)
        self.setLayout(layout)


    def __initSignals(self):
        self.engineButton.clicked.connect(self.__handleMainThread)
        self.spinDelay.valueChanged.connect(self.delayChange)

    def __handleMainThread(self, status):
        self.engineButton.setText("Стоп" if status else "Старт")
        if not status:
            self.thread.stop()
        else:
            self.thread = SystemInfo()
            self.thread.started.connect(self.createGraph)
            self.thread.systemInfoReceived.connect(lambda data: self.addValue(data))
            self.thread.finished.connect(self.finished)
            self.thread.start()

    def finished(self):
        self.engineButton.setChecked(False)
        self.engineButton.setText("Старт")
        self.clear()


    def clear(self):
        for i in range(5):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem("0%"))

        for i in self.graph_dict.keys():
            self.graph_dict[i].setValue(0)


    def addValue(self, data=dict):
        self.table.setItem(0,0,QtWidgets.QTableWidgetItem(f"{data['cpu']}%"))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem(f"{data['ram_usage']}%"))
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem(f"{data['ram_free']}"))
        self.table.setItem(3, 0, QtWidgets.QTableWidgetItem(f"{data['disk_usage']}%"))
        self.table.setItem(4, 0, QtWidgets.QTableWidgetItem(f"{data['disk_free']}%"))

        for i in data.keys():
            if i in self.graph_dict:
                self.graph_dict[i].setValue(data[i])
                self.graph_dict[i].setText(f"{i}: {data[i]}%")

    def createGraph(self):
        self.setMinimumSize(1000, 300)
        graph = ['cpu', 'ram_usage', 'ram_free', 'disk_usage', 'disk_free']
        for i in graph:
            if not i in self.graph_dict.keys():
                widget = SystemWidget(i)
                self.graph_dict[i] = widget
                self.graphlayout.addWidget(widget)

    def delayChange(self, delay):
        if delay > 0 and self.thread:
            self.thread.setDelay(delay)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = SystemMonitor()
    window.show()

    app.exec()