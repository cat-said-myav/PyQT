"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        l = QtWidgets.QVBoxLayout()

        self.lcd_modes = {
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "dec": QtWidgets.QLCDNumber.Mode.Dec,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
        }

        self.dial = QtWidgets.QDial()
        self.dial.valueChanged.connect(self.onValueChanged)
        self.dial.installEventFilter(self)
        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.display(14)
        self.lcd.setMinimumHeight(60)
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.onValueChanged)
        self.cb = QtWidgets.QComboBox()
        self.cb.addItems(list(self.lcd_modes.keys()))
        self.cb.currentTextChanged.connect(lambda mode: self.lcd.setMode(self.lcd_modes[mode]))

        l.addWidget(self.dial)
        l.addWidget(self.lcd)
        l.addWidget(self.slider)
        l.addWidget(self.cb)

        self.setLayout(l)

        self.settings = QtCore.QSettings("MyCompany", "DialApp")
        self.loadSettings()
    def onValueChanged(self, value):
        self.dial.setValue(value)
        self.slider.setValue(value)
        self.updateLCD(value)

    def updateLCD(self, value):
        self.lcd.display(value)

    def eventFilter(self, watched, event):
        if watched == self.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Minus:
                new_value = self.dial.value() - 1
                if new_value >= self.dial.minimum():
                    self.dial.setValue(new_value)
                    print(f"Key '-': Dial value changed to {new_value}")
                return True

            elif event.key() == QtCore.Qt.Key.Key_Plus:
                new_value = self.dial.value() + 1
                if new_value <= self.dial.maximum():
                    self.dial.setValue(new_value)
                    print(f"Key '+': Dial value changed to {new_value}")
                return True

        return super().eventFilter(watched, event)

    def saveSettings(self):
        self.settings.setValue("display_mode", self.cb.currentText())
        self.settings.setValue("lcd_value", self.dial.value())

    def loadSettings(self):

        saved_mode = self.settings.value("display_mode")
        if saved_mode and saved_mode in self.lcd_modes:
            self.cb.setCurrentText(saved_mode)
            self.lcd.setMode(self.lcd_modes[saved_mode])

        saved_value = self.settings.value("lcd_value")
        if saved_value:
            try:
                value = int(saved_value)
                self.dial.setValue(value)
                self.slider.setValue(value)
                self.lcd.display(value)
            except ValueError:
                pass

    def closeEvent(self, event):
        self.saveSettings()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
