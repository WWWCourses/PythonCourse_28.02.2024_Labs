import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        btn = qtw.QPushButton('Click me')
        btnClose = qtw.QPushButton('Close')
        btnGetText = qtw.QPushButton('Get Text')
        self.le1 = qtw.QLineEdit()

        ml = qtw.QVBoxLayout(self)
        ml.addWidget(btn)
        ml.addWidget(btnClose)
        ml.addWidget(self.le1)
        ml.addWidget(btnGetText)
        self.setGeometry(300, 400, 300, 300)



        # Handle click event on button
        ## connect clicked signal on btn to onClick
        btn.clicked.connect( self.onClick )
        btnClose.clicked.connect(self.close)
        # self.le1.editingFinished.connect( self.onEditingFinished )
        self.le1.textChanged.connect( self.onTextChange)
        btnGetText.clicked.connect( self.le1.clear )

    def onGetTextClick(self):
        # get le text and print
        # le_text = self.le1.text()
        # print(le_text)
        self.le1.setText('Maria')

    @qtc.pyqtSlot(bool)
    def onClick(self, param):
        print('onClick is called!')
        print(param)


    def onEditingFinished(self):
        print('onEditingFinished is called!')

    @qtc.pyqtSlot(str)
    def onTextChange(self, param):
        print('onTextChange is called!')
        print(param)





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())