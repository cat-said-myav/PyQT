from PySide6 import QtWidgets
from ui.window_ui  import Ui_Form

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.__initUI()

    def __initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.setWindowTitle('Основное окно')
        # self.resize(400, 200)
        # self.move(50, 50)
        # self.lineEditLogin = QtWidgets.QLineEdit()
        # self.lineEditLogin.setPlaceholderText("Введите Ваше Имя")
        #
        # self.lineEditPassword = QtWidgets.QLineEdit()
        # self.lineEditPassword.setPlaceholderText("Введите Ваш пароль")
        # self.lineEditPassword.echoMode(QtWidgets.QLineEdit.EchoMode.Password)
        #
        # self.pbok = QtWidgets.QPushButton("OK")
        # self.pbcancel = QtWidgets.QPushButton("Cancel")
        #
        # spacer = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        #
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.show()

    app.exec()



