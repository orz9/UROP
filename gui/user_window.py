from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from gui.login_window import LoginWindow

class UserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User Selection')
        self.setWindowIcon(QIcon('resources/nuslogo.ico'))

        titleLabel = QLabel('Physics learning tool for VI students')
        titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        projectLabel = QLabel('Project from NUS ECE department')

        studentButton = QPushButton('Login as Student')
        studentButton.clicked.connect(self.set_student)
        teacherButton = QPushButton('Login as Teacher')
        teacherButton.clicked.connect(self.set_teacher)

        layout = QVBoxLayout()
        layout.addWidget(titleLabel)
        layout.addWidget(projectLabel)
        layout.addWidget(studentButton)
        layout.addWidget(teacherButton)

        self.setLayout(layout)

    def set_student(self):
        self.userAuthority = "student"
        # Proceed to login window
        self.login_window = LoginWindow(self.userAuthority)
        self.login_window.show()
        self.close()

    def set_teacher(self):
        self.userAuthority = "teacher"
        # Proceed to login window
        self.login_window = LoginWindow(self.userAuthority)
        self.login_window.show()
        self.close()
