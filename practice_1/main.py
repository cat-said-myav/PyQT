import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Простейшее окно')
window.show()

sys.exit(app.exec())


