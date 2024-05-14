from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from mongoDB.db_utils import add_user
from gui.message_window import showMessage

class RegisterWindow(QWidget):
    def __init__(self, username="", password=""):
        super().__init__()
        self.initUI(username, password)

    def initUI(self, username, password):
        self.setWindowTitle("Register")
        
        nameLabel = QLabel('Name:')
        self.nameEdit = QLineEdit()
        self.nameEdit.setText(username)
        
        passwordLabel = QLabel('Password:')
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setText(password)
        
        registerButton = QPushButton('Register')
        registerButton.clicked.connect(self.on_register)
        
        layout = QVBoxLayout()
        layout.addWidget(nameLabel)
        layout.addWidget(self.nameEdit)
        layout.addWidget(passwordLabel)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(registerButton)
        
        self.setLayout(layout)

    def on_register(self):
        username = self.nameEdit.text()
        password = self.passwordEdit.text()
        add_user(username, password, "student")
        showMessage("Successfully registered!")
        self.close()
