from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from .lesson_menu import LessonMenuWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Physics is fun')  # Set the window title
        self.setWindowIcon(QIcon('resources/nuslogo.ico'))  # Set the window icon

        titleLabel = QLabel('Physics learning tool for VI students', self)
        titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        projectLabel = QLabel('Project from NUS ECE department', self)
        
        nameLabel = QLabel('Name:', self)
        self.nameEdit = QLineEdit(self)
        
        passwordLabel = QLabel('Password:', self)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        
        loginButton = QPushButton('Login', self)
        exitButton = QPushButton('Exit', self)

        # Layouts
        mainLayout = QVBoxLayout()
        formLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()

        # Add widgets to form layout
        formLayout.addWidget(nameLabel)
        formLayout.addWidget(self.nameEdit)
        formLayout.addWidget(passwordLabel)
        formLayout.addWidget(self.passwordEdit)

        # Add buttons to button layout
        buttonLayout.addWidget(loginButton)
        buttonLayout.addWidget(exitButton)

        # Add widgets to main layout
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(projectLabel)
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(buttonLayout)

        # Set main layout on the application window
        self.setLayout(mainLayout)
        self.setWindowTitle('Physics Learning Tool')
        self.setGeometry(300, 300, 600, 200)  # Modify as needed for your display