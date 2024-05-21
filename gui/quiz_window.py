from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QPushButton, QMessageBox)
from mongoDB.db_utils import get_quiz_questions, update_student_performance

class QuizWindow(QWidget):
    def __init__(self, username, lessonChosen):
        super().__init__()
        self.username = username
        self.lessonChosen = lessonChosen
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quiz for " + self.lessonChosen)
        self.layout = QVBoxLayout(self)

        self.questions = get_quiz_questions(self.lessonChosen)
        self.questionWidgets = []
        self.buttonGroups = []
        self.studentScore = 0
        self.totalQuestions = len(self.questions)

        for question in self.questions:
            questionLayout = QVBoxLayout()
            questionLabel = QLabel(question['question'])
            questionLayout.addWidget(questionLabel)

            buttonGroup = QButtonGroup(self)
            self.buttonGroups.append(buttonGroup)

            for option in ['option1', 'option2', 'option3']:
                radioButton = QRadioButton(question[option])
                buttonGroup.addButton(radioButton)
                questionLayout.addWidget(radioButton)

            self.questionWidgets.append(questionLayout)
            self.layout.addLayout(questionLayout)

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submitAnswers)
        self.backButton = QPushButton('Back')
        self.backButton.clicked.connect(self.go_back)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.submitButton)
        buttonLayout.addWidget(self.backButton)
        self.layout.addLayout(buttonLayout)

    def submitAnswers(self):
        allAnswered = True
        score = 0

        for idx, group in enumerate(self.buttonGroups):
            selected = group.checkedButton()
            if not selected:
                allAnswered = False
                break
            if selected.text() == self.questions[idx]['answer']:
                score += 1

        if not allAnswered:
            QMessageBox.warning(self, "Incomplete", "Please answer all questions.")
            return

        QMessageBox.information(self, "Score", f"Your score: {score}/{self.totalQuestions}")
        update_student_performance(self.username, self.lessonChosen, score, self.totalQuestions)
    
    def go_back(self):
        self.close()
        from gui.lesson_window import LessonWindow
        self.lesson_window = LessonWindow(self.lessonChosen, self.username)
        self.lesson_window.show()

