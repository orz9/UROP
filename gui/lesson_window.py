from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from mongoDB.db_utils import get_lesson_content
from gui.quiz_window import QuizWindow

class LessonWindow(QWidget):
    def __init__(self, lessonChosen, username):
        super().__init__()
        self.lessonChosen = lessonChosen
        self.username = username
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.lessonChosen)
        layout = QVBoxLayout(self)

        # Fetch content from database
        lesson_content = get_lesson_content(self.lessonChosen)

        # Display the lesson content
        self.contentLabel = QLabel(lesson_content, self)
        self.contentLabel.setWordWrap(True)
        layout.addWidget(self.contentLabel)

        # Buttons
        playAgainButton = QPushButton("Play Again", self)
        quizButton = QPushButton("Quiz", self)
        backButton = QPushButton("Back", self)

        # Button Layout
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(playAgainButton)
        buttonLayout.addWidget(quizButton)
        buttonLayout.addWidget(backButton)

        layout.addLayout(buttonLayout)

        # Connect buttons
        playAgainButton.clicked.connect(self.playAgain)
        quizButton.clicked.connect(self.startQuiz)
        backButton.clicked.connect(self.go_back)

        self.setLayout(layout)

    def playAgain(self):
        # Placeholder for replaying the lesson
        QMessageBox.information(self, "Play Again", "Replaying the lesson.")

    def startQuiz(self):
        print("Starting the quiz...")
        self.close()
        self.quiz_window = QuizWindow(self.username, self.lessonChosen)
        self.quiz_window.show()

    def go_back(self):
        self.close()
        from gui.lesson_menu import LessonMenuWindow
        self.lesson_menu_window = LessonMenuWindow(self.username) # Modify this later so that it becomes dynamic
        self.lesson_menu_window.show()
