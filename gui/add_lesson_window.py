from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from gui.add_quiz_window import AddQuizWindow
from mongoDB.db_utils import add_lesson, check_lesson

class AddLessonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Lesson")
        self.initUI()
        self.nOfQuestion = 0 # Variable to keep track of number of questions

    def initUI(self):
        self.layout = QVBoxLayout()
        
        # Lesson Name
        self.lessonNameLabel = QLabel("Lesson Name:")
        self.lessonNameEdit = QLineEdit()
        self.layout.addWidget(self.lessonNameLabel)
        self.layout.addWidget(self.lessonNameEdit)
        
        # Lesson Content
        self.lessonContentLabel = QLabel("Lesson Content:")
        self.lessonContentEdit = QLineEdit()
        self.layout.addWidget(self.lessonContentLabel)
        self.layout.addWidget(self.lessonContentEdit)
        
        # Add Quiz Button
        self.addQuizButton = QPushButton("Add Quiz")
        self.addQuizButton.clicked.connect(self.openAddQuiz)
        self.layout.addWidget(self.addQuizButton)

        # Add Lesson Button
        self.saveLessonButton = QPushButton("Save lesson")
        self.saveLessonButton.clicked.connect(self.saveLesson)
        self.layout.addWidget(self.saveLessonButton)

        self.setLayout(self.layout)


    def openAddQuiz(self):
        self.quiz_window = AddQuizWindow(self.nOfQuestion, self.lessonNameEdit.text())
        self.quiz_window.quiz_saved.connect(self.updateQuizCount)  # Connect to the signal
        self.quiz_window.show()

    def updateQuizCount(self, count, question):
        self.nOfQuestion = count
        infoLabel = QLabel(f"Question {count}: '{question}' has been added!")
        self.layout.addWidget(infoLabel)

    def saveLesson(self):
        lessonName = self.lessonNameEdit.text()
        lessonContent = self.lessonContentEdit.text()
        if not lessonName or not lessonContent:
            QMessageBox.warning(self, "Incomplete Data", "Please enter both lesson name and content.")
            return

        if check_lesson(lessonName):
            QMessageBox.warning(self, "Duplicate Lesson", f"A lesson with the name '{lessonName}' already exists.")
            return

        lesson_id = add_lesson(lessonName, lessonContent)
        QMessageBox.information(self, "Lesson Saved", f"New lesson {lessonName} saved successfully with ID: {lesson_id}")
        self.close()
