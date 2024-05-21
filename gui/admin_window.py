from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from gui.add_lesson_window import AddLessonWindow

class AdminWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Admin Dashboard')
        
        # Welcome label
        welcomeLabel = QLabel(f'Welcome {self.username}', self)
        welcomeLabel.setStyleSheet("font-size: 16px; font-weight: bold;")

        # Buttons
        addLessonButton = QPushButton('Add Lesson', self)
        modifyLessonButton = QPushButton('Modify Lesson', self)
        deleteLessonButton = QPushButton('Delete Lesson', self)
        checkPerformanceButton = QPushButton('Check Student Performance', self)

        # Connecting buttons to functions (placeholders for now)
        addLessonButton.clicked.connect(self.add_lesson)
        modifyLessonButton.clicked.connect(self.modify_lesson)
        deleteLessonButton.clicked.connect(self.delete_lesson)
        checkPerformanceButton.clicked.connect(self.check_performance)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(welcomeLabel)
        layout.addWidget(addLessonButton)
        layout.addWidget(modifyLessonButton)
        layout.addWidget(deleteLessonButton)
        layout.addWidget(checkPerformanceButton)

        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 300)  # Adjust size as needed

    def add_lesson(self):
        # Placeholder function
        print("Opening add lesson window")
        self.lesson_window = AddLessonWindow()
        self.lesson_window.show()

    def modify_lesson(self):
        # Placeholder function
        print("Modifying a lesson...")

    def delete_lesson(self):
        # Placeholder function
        print("Deleting a lesson...")

    def check_performance(self):
        # Placeholder function
        print("Checking student performance...")
