from PyQt5.QtWidgets import QApplication
from gui.login_window import *

if __name__ == '__main__':
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
