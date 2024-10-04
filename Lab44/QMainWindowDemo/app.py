import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.setupMenuBar()
        self.setupToolbar()
        self.setupDockWidget()
        self.setupStatusBar()

    def setupMenuBar(self):
        # get the menu bar
        menubar = self.menuBar()

        # add menu items
        file_menu = menubar.addMenu('&File')
        edit_menu = menubar.addMenu('E&dit')
        help_menu = menubar.addMenu('Hel&p')

        # add actions
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')

        # add separator
        file_menu.addSeparator()

        quit_action = file_menu.addAction('Quit', self.close)
        undo_action = edit_menu.addAction('Undo', self.text_edit.undo)

        # create a QAction manually
        redo_action = qtg.QAction('Redo', self)
        redo_action.triggered.connect(self.text_edit.redo)

        # Actions, which opens custom dialog
        edit_menu.addAction(redo_action)
        edit_menu.addAction('Set Font…', self.set_font)
        edit_menu.addAction('Settings…', self.show_settings)

    def setupToolbar(self):
        toolbar = self.addToolBar('File')

        toolbar.setMovable(False)
        toolbar.setFloatable(False)

        toolbar.setAllowedAreas(
          qtc.Qt.ToolBarArea.TopToolBarArea |
          qtc.Qt.ToolBarArea.BottomToolBarArea
        )

        self.help_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton),
            'Help',
            self  # important to pass the parent!
        )

        # add signal
        self.help_action.triggered.connect(lambda _: qtw.QMessageBox.information(self,'Not Implemented','Sorry, no help yet!'))

        toolbar.addAction(self.help_action)

    def setupDockWidget(self):
        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        # set dock widget to move and float (but not closeable)
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )


    def setupStatusBar(self):
        # create status bar widget and atach it to main window:
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)

        charcount_label = qtw.QLabel("chars: 0")
        self.text_edit.textChanged.connect(
          lambda: charcount_label.setText( "chars: " + str(len(self.text_edit.toPlainText())) )
        )
        self.status_bar.addPermanentWidget(charcount_label)


    def set_font(self):
        # show temporary message for 3 second:
        self.status_bar.showMessage('Font is setup!!!',3000)
        print('set font')

    def show_settings(self):
        print('show_settings')

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())