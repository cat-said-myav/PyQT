from PySide6 import QtCore
import psutil
import time

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None
        self.__status = 1

    def stop(self):
        self.__status = False

    def setDelay(self, text):
            self.delay = text

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while self.__status:
            try:
                monitor_dict = {}
                cpu_value = psutil.cpu_percent()
                ram_value = psutil.virtual_memory()
                ram_value_usage = round(ram_value.used / ram_value.total * 100, 2)
                ram_value_free = round(ram_value.free / ram_value.total * 100, 2)

                disk_value = psutil.disk_usage("/")
                disk_value_usage = round(disk_value.used / disk_value.total * 100, 2)
                disk_value_free = round(disk_value.free/ disk_value.total * 100, 2)
                monitor_dict['cpu'] = cpu_value
                monitor_dict['ram_usage'] = ram_value_usage
                monitor_dict['ram_free'] = ram_value_free
                monitor_dict['disk_usage'] = disk_value_usage
                monitor_dict['disk_free'] = disk_value_free
                self.systemInfoReceived.emit(monitor_dict)
                time.sleep(self.delay)
            except Exception:
                traceback.print_exc()
                self.stop()

