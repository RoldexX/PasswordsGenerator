from PasswordGenerator import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets
import sys

from PasswordGenerateFunc import password_generator
from MD5 import md5
from SHA256 import hash_password as sha256


class PassGenerator(QtWidgets.QMainWindow):
    acsept_simvols = 'ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz-_$*0123456789'
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
        self.ui.statusbar.showMessage('Готов к работе')

    def Generate(self):
        """
        Генерирует пароль в зависимости от выбранных настроек
        и отображет его в текстовом поле.
        Помимо пароля, также генерируется его хэш с помощью
        выбранного алгоритма и отображет его в текстовом поле.
        """
        password_length = self.ui.spinBox_passlength.value()
        self.acsept_simvols = self.ui.acsept_simvols.text()
        password = password_generator(length=password_length, characters=self.acsept_simvols)

        self.ui.textEdit_password_generated.setText(password)

        if self.ui.radioButton_md5.isChecked():
            hash_text = md5(password=password)
            hash_algoritm = 'MD5'
        else:
            hash_text = sha256(password=password)
            hash_algoritm = 'SHA256'

        self.ui.lineEdit_hash.setText(hash_text)
        self.ui.statusbar.showMessage(f'Пароль и хеш {hash_algoritm} сгенерированны')

    def Generate_hash(self):
        """
        Генерирует хэш заданного пароля с помощью
        выбранного алгоритма и отображет его в текстовом поле.
        """
        password = self.ui.textEdit_password_generated.toPlainText()
        if self.ui.radioButton_md5.isChecked():
            hash_text = md5(password=password)
            hash_algoritm = 'MD5'
        else:
            hash_text = sha256(password=password)
            hash_algoritm = 'SHA256'

        self.ui.lineEdit_hash.setText(hash_text)
        self.ui.statusbar.showMessage(f'Хеш {hash_algoritm} сгенерирован')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = PassGenerator()
    application.show()

    sys.exit(app.exec())
