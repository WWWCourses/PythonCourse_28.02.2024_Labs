import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle('Login Form')

    def setupUI(self):
        # create UI widgets
        appTitle = qtw.QLabel('Login')
        appTitle.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)

        leUserName = qtw.QLineEdit()
        leUserPassword = qtw.QLineEdit()
        leUserPassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        btnLogin = qtw.QPushButton('Login')
        btnCancel = qtw.QPushButton('Cancel')

        hLayout = qtw.QHBoxLayout()
        hLayout.addWidget(btnLogin)
        hLayout.addWidget(btnCancel)

        # create Form Layout and add widgets:
        formLayout = qtw.QFormLayout()
        formLayout.addRow('User Name:', leUserName)
        formLayout.addRow('User Password:', leUserPassword)
        formLayout.addRow('', hLayout)
        formLayout.setVerticalSpacing(10)

        # main layout
        mainLayout = qtw.QVBoxLayout(self)
        mainLayout.addWidget(appTitle)
        mainLayout.addLayout(formLayout)
        mainLayout.addStretch(1)

        #############################################################################
        #                                                                           #
        #    HW: Implement signals and slots to print the text from leUserName      #
        #    and leUserPassword to the console when the Login button is clicked.    #
        #                                                                           #
        #############################################################################


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())