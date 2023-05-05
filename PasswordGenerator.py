# Form implementation generated from reading ui file 'PasswordGenerator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 178)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_algoritm = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_algoritm.setObjectName("label_algoritm")
        self.horizontalLayout.addWidget(self.label_algoritm)
        self.radioButton_md5 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_md5.setChecked(True)
        self.radioButton_md5.setObjectName("radioButton_md5")
        self.horizontalLayout.addWidget(self.radioButton_md5)
        self.radioButton_sha256 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_sha256.setObjectName("radioButton_sha256")
        self.horizontalLayout.addWidget(self.radioButton_sha256)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_passlength = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_passlength.setObjectName("label_passlength")
        self.horizontalLayout.addWidget(self.label_passlength)
        self.spinBox_passlength = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_passlength.setMaximum(1024)
        self.spinBox_passlength.setProperty("value", 32)
        self.spinBox_passlength.setDisplayIntegerBase(10)
        self.spinBox_passlength.setObjectName("spinBox_passlength")
        self.horizontalLayout.addWidget(self.spinBox_passlength)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_password = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_password.setObjectName("textEdit_password")
        self.horizontalLayout_2.addWidget(self.textEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_3.addWidget(self.pushButton_close)
        self.pushButton_generate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.horizontalLayout_3.addWidget(self.pushButton_generate)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_algoritm.setText(_translate("MainWindow", "Алгоритм генерации:"))
        self.radioButton_md5.setText(_translate("MainWindow", "MD5"))
        self.radioButton_sha256.setText(_translate("MainWindow", "SHA256"))
        self.label_passlength.setText(_translate("MainWindow", "Длинна пароля:"))
        self.pushButton_close.setText(_translate("MainWindow", "Закрыть программу"))
        self.pushButton_generate.setText(_translate("MainWindow", "Сгенерировать пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
