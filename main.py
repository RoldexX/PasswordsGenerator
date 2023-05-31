from PasswordGenerator import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
import sys

from PasswordGenerateFunc import password_generator
from MD5 import md5
from SHA256 import hash_password as sha256


class PassGenerator(QtWidgets.QMainWindow):
    acsept_simvols = 'ABCD'
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
        self.ui.pushButton_generate_hash.clicked.connect(self.Generate_hash)
        self.ui.acsept_simvols.setText(self.acsept_simvols)

    def Generate(self):
        """
        Генерирует пароль в зависимости от выбранных настроек
        и отображет его в текстовом поле.
        Помимо пароля, также генерируется его хэш.
        """
        password_length = self.ui.spinBox_passlength.value()
        self.acsept_simvols = self.ui.acsept_simvols.text()
        password = password_generator(length=password_length, characters=self.acsept_simvols)

        self.ui.textEdit_password_generated.setText(password)

        if self.ui.radioButton_md5.isChecked():
            hash_text = md5(password=password)
        else:
            hash_text = sha256(password=password)

        self.ui.textEdit_hash.setText(hash_text)

    def Generate_hash(self):
        password = self.ui.textEdit_password_generated.toPlainText()
        if self.ui.radioButton_md5.isChecked():
            hash_text = md5(password=password)
        else:
            hash_text = sha256(password=password)

        self.ui.textEdit_hash.setText(hash_text)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = PassGenerator()
    application.show()

    sys.exit(app.exec())
