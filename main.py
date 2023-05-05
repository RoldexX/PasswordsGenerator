from PasswordGenerator import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
import sys


class Generator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Generator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Generator()
    application.show()

    sys.exit(app.exec())
