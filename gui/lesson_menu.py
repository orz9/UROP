from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QButtonGroup
from mongoDB.db_utils import get_lessons

class LessonMenuWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lesson Menu')
        layout = QVBoxLayout()
        welcomeLabel = QLabel(f'Welcome {self.username}', self)
        welcomeLabel.setStyleSheet("font-size: 16px; font-weight: bold;")

        label = QLabel('Please select your lesson', self)
        layout.addWidget(label)

        self.buttonGroup = QButtonGroup(self)
        lessons = get_lessons()
        if not lessons:
            # If no lessons are found, display a message
            noLessonLabel = QLabel('No lessons available, please contact the teacher', self)
            layout.addWidget(noLessonLabel)
        else:
            for lesson in lessons:
                lessonName = lesson.get('topic', 'Untitled Topic') # Using default name 'Untitled Topic' if 'topic' is missing
                btn = QRadioButton(lessonName, self)
                self.buttonGroup.addButton(btn)
                layout.addWidget(btn)

        confirmButton = QPushButton('Confirm', self)
        confirmButton.clicked.connect(self.confirmSelection)
        layout.addWidget(confirmButton)

        self.setLayout(layout)

    def confirmSelection(self):
        selectedButton = self.buttonGroup.checkedButton()
        if selectedButton:
            print(f"Selected: {selectedButton.text()}")
        else:
            print("No selection made.")
