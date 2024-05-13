from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from gui.register_window import RegisterWindow

class NoUserWindow(QWidget):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.initUI()

    def initUI(self):
        self.setWindowTitle("No user found!")
        label = QLabel("No user found! Would you like to register?")

        yesButton = QPushButton("Yes")
        yesButton.clicked.connect(self.on_yes)
        noButton = QPushButton("No")
        noButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(yesButton)
        layout.addWidget(noButton)

        self.setLayout(layout)

    def on_yes(self):
        self.register_window = RegisterWindow(self.username, self.password)
        self.register_window.show()
        self.close()
