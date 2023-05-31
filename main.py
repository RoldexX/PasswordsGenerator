from PasswordGenerator import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
import sys


class PassGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        super(PassGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        """
        Метод, инициализирующий пользовательский интерфейс.
        Устанавливает обработчик событий для кнопки Generate.
        """
        self.ui.pushButton_generate.clicked.connect(self.Generate)

    def Generate(self):
        """
        Генерирует пароль в зависимости от выбранных настроек
        и отображет его в текстовом поле.
        Помимо пароля, также генерируется его хэш.
        """
        password_length = self.ui.spinBox_passlength.value()

        if self.ui.radioButton_md5.isChecked():
            password = f'MD5 {password_length}'
        else:
            password = f'SHA256 {password_length}'

        self.ui.textEdit_password.setText(password)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = PassGenerator()
    application.show()

    sys.exit(app.exec())
