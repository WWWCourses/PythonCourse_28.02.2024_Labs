import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

import db

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle('Login Form')

        self.conn = db.make_connection('test','test1234', 'pyqt_users_db')

    def setupUI(self):
        # create UI widgets
        appTitle = qtw.QLabel('Login')
        appTitle.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)

        self.leUserName = qtw.QLineEdit()
        self.leUserPassword = qtw.QLineEdit()
        self.leUserPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        btnLogin = qtw.QPushButton('Login')
        btnCancel = qtw.QPushButton('Cancel')

        hLayout = qtw.QHBoxLayout()
        hLayout.addWidget(btnLogin)
        hLayout.addWidget(btnCancel)

        # create Form Layout and add widgets:
        formLayout = qtw.QFormLayout()
        formLayout.addRow('User Name:', self.leUserName)
        formLayout.addRow('User Password:', self.leUserPassword)
        formLayout.addRow('', hLayout)
        formLayout.setVerticalSpacing(10)

        # main layout
        mainLayout = qtw.QVBoxLayout(self)
        mainLayout.addWidget(appTitle)
        mainLayout.addLayout(formLayout)
        mainLayout.addStretch(1)

        btnLogin.clicked.connect(self.onBtnLogin)


    def onBtnLogin(self):
        user_name = self.leUserName.text()
        user_pass = self.leUserPassword.text()

        print(f'user name: {user_name}')
        print(f'user pass: {user_pass}')

        db.authenticate(self.conn, user_name, user_pass)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())