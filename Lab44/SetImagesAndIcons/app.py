import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(500, 400, 400, 800)

        # Set image:
        self.imageLabel = qtw.QLabel('@@@@@@@@@@@@@@@@@@@@@', parent=self)
        self.imageLabel.setPixmap( qtg.QPixmap('./path_to_image') )

        # Set  application icon
        self.setWindowIcon(qtg.QIcon('./path_to_image'))




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())