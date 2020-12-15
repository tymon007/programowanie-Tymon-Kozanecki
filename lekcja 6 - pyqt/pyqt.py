from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 500)
    win.setWindowTitle("Aplikacja Tymona")

    label = QtWidgets.QLabel(win)
    label.setText("hmmmmmmmmmmmmmmmmmmmmmmmm")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())

window()