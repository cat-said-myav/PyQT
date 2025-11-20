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

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyCompany", "DialApp")

        self.lcd_modes = {
            "hex": QtWidgets.QLCDNumber.Mode.Hex,
            "dec": QtWidgets.QLCDNumber.Mode.Dec,
            "oct": QtWidgets.QLCDNumber.Mode.Oct,
            "bin": QtWidgets.QLCDNumber.Mode.Bin,
        }

        self.initUI()
        self.loadSettings()
        self.connectWidgets()

    def initUI(self):
        """Инициализация пользовательского интерфейса"""
        layout = QtWidgets.QVBoxLayout()


        self.dial = QtWidgets.QDial()
        self.dial.setRange(0, 100)
        self.dial.installEventFilter(self)

        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.setDigitCount(3)
        self.lcd.setMinimumHeight(60)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)

        self.cb = QtWidgets.QComboBox()
        self.cb.addItems(list(self.lcd_modes.keys()))

        # Добавление виджетов в layout
        layout.addWidget(self.dial)
        layout.addWidget(self.lcd)
        layout.addWidget(self.slider)
        layout.addWidget(self.cb)

        self.setLayout(layout)
        self.setWindowTitle("Dial-Slider-LCD Demo")

    def connectWidgets(self):

        self.dial.valueChanged.connect(self.onDialValueChanged)
        self.slider.valueChanged.connect(self.onSliderValueChanged)
        self.cb.currentTextChanged.connect(self.onModeChanged)

    def onDialValueChanged(self, value):
        print(f"Dial value changed: {value}")


        self.slider.blockSignals(True)
        self.slider.setValue(value)
        self.slider.blockSignals(False)

        self.updateLCD(value)

    def onSliderValueChanged(self, value):
        self.dial.blockSignals(True)
        self.dial.setValue(value)
        self.dial.blockSignals(False)

        self.updateLCD(value)

    def onModeChanged(self, mode):
        self.lcd.setMode(self.lcd_modes[mode])

        current_value = self.dial.value()
        self.updateLCD(current_value)

        # Сохранение настроек
        self.saveSettings()

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
        self.settings.setValue("dial_value", self.dial.value())
        self.settings.setValue("display_mode", self.cb.currentText())
        self.settings.sync()

    def loadSettings(self):
        dial_value = self.settings.value("dial_value", 0, type=int)
        self.dial.setValue(dial_value)

        display_mode = self.settings.value("display_mode", "dec")
        if display_mode in self.lcd_modes:
            self.cb.setCurrentText(display_mode)
            self.lcd.setMode(self.lcd_modes[display_mode])

        self.updateLCD(dial_value)

    def closeEvent(self, event):
        self.saveSettings()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()