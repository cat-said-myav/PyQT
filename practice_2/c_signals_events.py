"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущий основной монитор
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore, QtGui
from ui.c_form import Ui_Form
import datetime




class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUI()
        self.initSignals()
        self.screen_geometry = QtWidgets.QApplication.primaryScreen().availableGeometry()

    def __initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def event(self, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.Resize:
            size = event.size().toTuple()
            print(datetime.datetime.now().strftime('%H:%M:%S'), f'new_size ----> : {size}')
        if event.type() == QtCore.QEvent.Move:
            old_pos = event.oldPos().toTuple()
            new_pos = event.pos().toTuple()
            print(datetime.datetime.now().strftime('%H:%M:%S'), f'old_pos {old_pos} ----> new_pos {new_pos}')

        return super().event(event)

    def initSignals(self) -> None:
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenter)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRT)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLT)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRB)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLB)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)

    def onPushButtonMoveCoords(self) -> None:
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onPushButtonCenter(self) -> None:
        x = (self.screen_geometry.width() - self.width()) // 2
        y = (self.screen_geometry.height() - self.height()) // 2
        self.move(x, y)
    def onPushButtonRT(self) -> None:
        x =(self.screen_geometry.right() - self.width())
        y = self.screen_geometry.top()
        self.move(x, y)

    def onPushButtonLT(self) -> None:
        x = self.screen_geometry.left()
        y = self.screen_geometry.top()
        self.move(x, y)

    def onPushButtonRB(self) -> None:
        x =(self.screen_geometry.right() - self.width())
        y = (self.screen_geometry.bottom() - self.height())
        self.move(x, y)

    def onPushButtonLB(self) -> None:
        x = self.screen_geometry.left()
        y = (self.screen_geometry.bottom() - self.height())
        self.move(x, y)

    def onPushButtonGetData(self) -> None:
        screen_count = len(QtWidgets.QApplication.screens())
        primary_screen = QtWidgets.QApplication.primaryScreen()
        center_x = self.x() + self.width() // 2
        center_y = self.y() + self.height() // 2

        self.ui.plainTextEdit.setPlainText(f"Время: {datetime.datetime.now().strftime('%H:%M:%S')}")
        self.ui.plainTextEdit.appendPlainText(f"Кол-во экранов: {screen_count}")
        self.ui.plainTextEdit.appendPlainText(f"Текущий основной монитор: {primary_screen.name()}")
        self.ui.plainTextEdit.appendPlainText(f"Разрешение экрана: {primary_screen.size().toTuple()}")
        self.ui.plainTextEdit.appendPlainText(f"Экран на котором окно находится: {window.screen().name()}")
        self.ui.plainTextEdit.appendPlainText(f"Размер окна: {window.size().toTuple()}")
        self.ui.plainTextEdit.appendPlainText(f"Минимальный размер окна: {window.minimumSize().toTuple()}\n")
        self.ui.plainTextEdit.appendPlainText(f"Текущее положение (координаты) окна: {window.pos().toTuple()}")
        self.ui.plainTextEdit.appendPlainText(f"Координаты центра приложения: {(center_x, center_y)}")
        self.ui.plainTextEdit.appendPlainText(f"Отслеживание состояния окна : \nсвернуто - {window.isMinimized()}\nразвёрнуто -{window.isMaximized()}\n"
                                              f"активно - {window.isActiveWindow()}\nотображено - {window.isVisible()}")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
