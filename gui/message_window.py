from PyQt5.QtWidgets import QMessageBox

def showMessage(message, type=QMessageBox.Information):
    msg = QMessageBox()
    msg.setIcon(type)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
