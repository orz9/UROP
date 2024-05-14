from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from gui.lesson_menu import LessonMenuWindow
from gui.no_user_window import NoUserWindow
from gui.message_window import showMessage
from gui.admin_window import AdminWindow
from mongoDB.db_utils import check_user, add_user


class LoginWindow(QWidget):
    def __init__(self, userAuthority):
        super().__init__()
        self.userAuthority = userAuthority
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Physics is fun')
        self.setWindowIcon(QIcon('resources/nuslogo.ico'))

        titleLabel = QLabel('Physics learning tool for VI students')
        titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        projectLabel = QLabel('Project from NUS ECE department')
        
        nameLabel = QLabel('Name:')
        self.nameEdit = QLineEdit()
        
        passwordLabel = QLabel('Password:')
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        # Initialize layouts
        mainLayout = QVBoxLayout()
        formLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()

        # Common buttons
        loginButton = QPushButton('Login')
        loginButton.clicked.connect(self.on_login)
        buttonLayout.addWidget(loginButton)

        exitButton = QPushButton('Exit')
        exitButton.clicked.connect(self.close)
        buttonLayout.addWidget(exitButton)

        # Conditional button for registration
        if self.userAuthority == "student":
            registerButton = QPushButton('Register')
            registerButton.clicked.connect(self.on_register)
            buttonLayout.insertWidget(buttonLayout.count() - 1, registerButton)  # Insert before the exit button

        formLayout.addWidget(nameLabel)
        formLayout.addWidget(self.nameEdit)
        formLayout.addWidget(passwordLabel)
        formLayout.addWidget(self.passwordEdit)

        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(projectLabel)
        mainLayout.addLayout(formLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 600, 200)



    def on_login(self):
        username = self.nameEdit.text()
        password = self.passwordEdit.text()
        user = check_user(username, self.userAuthority)
        if not username or not password:
            QMessageBox.critical(self, "Login Error", "Error! Empty username or password!")
            return
        else:
            if self.userAuthority == "student":
                if user and user.get('password') == password:
                    showMessage("Login successful!")
                    # Proceed to lesson menu window
                    self.close()
                    self.lesson_menu_window = LessonMenuWindow(username) # Open the lesson menu with username
                    self.lesson_menu_window.show()
                elif user:
                    showMessage("Incorrect password, please try again!", QMessageBox.Critical)
                else:
                    self.no_user_window = NoUserWindow(self.nameEdit.text(), self.passwordEdit.text())
                    self.no_user_window.show()
            elif self.userAuthority == "teacher":
                if user and user.get('password') == password:
                    showMessage("Login successfull!")
                    # Proceed to admin window
                    self.close()
                    self.admin_window = AdminWindow(username)
                    self.admin_window.show()
                elif user:
                    showMessage("Incorrect password, please try again!", QMessageBox.Critical)
                else:
                    showMessage("Unauthorized!", QMessageBox.Critical)
                    
            # if user and user.get('password') == password:
            #     showMessage("Login successful!")
            #     # Proceed to next window
            #     self.close()  # Close the login window
            #     if self.userAuthority == "student":
            #         self.lesson_menu_window = LessonMenuWindow(username)  # Open the lesson menu with username
            #         self.lesson_menu_window.show()
            #     else:
            #         self.admin_window = AdminWindow(username) # Open the admin window with username
            #         self.admin_window.show()
            # elif user:
            #     showMessage("Incorrect password, please try again!", QMessageBox.Critical)
            # else:
            #     self.no_user_window = NoUserWindow(self.nameEdit.text(), self.passwordEdit.text())
            #     self.no_user_window.show()

    def on_register(self):
        username = self.nameEdit.text()
        password = self.passwordEdit.text()
        if not username or not password:
            QMessageBox.critical(self, "Login Error", "Error! Empty username or password!")
            return
        else:
            if check_user(username, "student"): # Hardcoded because the program does not allow for admin registration
                showMessage("Existing user, please login!", QMessageBox.Warning)
            else:
                add_user(username, password, "student")
                showMessage("Successfully registered!")
                self.nameEdit.clear()
                self.passwordEdit.clear()
