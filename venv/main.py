import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QMainWindow)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec_())

    