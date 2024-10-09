import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.showTable()
        self.applyStyle()

    def showTable(self):
        data = [
            [1,2,3],
            [4,5,6]
        ]
        row_count = len(data)
        column_count = len(data[0])

        table = qtw.QTableWidget(self)
        table.setColumnCount(column_count)
        table.setRowCount(row_count)
        # table.setHorizontalHeaderLabels(['Column 1','Column 2'])
        table.setFixedSize(400,200)
         # Resize cells to fit content
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        # TODO why not works..
        table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)

         # Set the context menu policy to allow for custom context menus in this widget
        table.setContextMenuPolicy(qtc.Qt.ContextMenuPolicy.CustomContextMenu)
         # Connect the custom context menu requested signal to the context_actions method
        table.customContextMenuRequested.connect(self.context_actions)


        for row_idx,row in enumerate(data):
            for col_idx, el in enumerate(row):
                table.setItem(row_idx,col_idx, qtw.QTableWidgetItem(str(el)))

        self.table = table

    def context_actions(self, pos):
        menu = qtw.QMenu()

        # Get the index of the currently selected row
        current_row = self.table.currentRow()

        # Add action to insert a new row
        menu.addAction("Add Row Above", lambda: self.table.insertRow(current_row if current_row >= 0 else self.table.rowCount()))

        # Add action to remove the currently selected row
        menu.addAction("Remove Row", lambda: self.table.removeRow(current_row) if current_row >= 0 else None)

        # Execute the menu at the cursor position
        menu.exec(self.table.viewport().mapToGlobal(pos))

    def applyStyle(self):
        self.table.setAlternatingRowColors(True)
        with open('./main.css', "r") as f:
            style_sheet = f.read()

        self.setStyleSheet(style_sheet)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);
    window = MainWindow()
    window.show()
    sys.exit(app.exec())