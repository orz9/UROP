from PyQt5.QtWidgets import QApplication
from gui.user_window import UserWindow

if __name__ == '__main__':
    app = QApplication([])
    window = UserWindow()
    window.show()
    app.exec_()
