import sys
# 1. import needed QtWidgets classes
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

# 2. the main app instance for our application.
app = QApplication(sys.argv)

# 3. Create Qt widget, which will be our main window.
window = QWidget()
window.setWindowTitle('Hello World')

btnOK = QPushButton('OK', window)
# btnOK.setText('OK')

print(window.height())
# 4. show the window
window.show()

# 5. Start the event loop
sys.exit(app.exec())
