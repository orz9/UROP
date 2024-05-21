# add_quiz_window.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from mongoDB.db_utils import add_quiz
from PyQt5.QtCore import pyqtSignal

class AddQuizWindow(QWidget):
    quiz_saved = pyqtSignal(int, str)

    def __init__(self, nOfQuestion):
        super().__init__()
        self.nOfQuestion = nOfQuestion
        self.setWindowTitle("Add Quiz")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.questionLabel = QLabel("Question:")
        self.questionEdit = QLineEdit()
        layout.addWidget(self.questionLabel)
        layout.addWidget(self.questionEdit)
        
        self.option1Label = QLabel("Option 1:")
        self.option1Edit = QLineEdit()
        layout.addWidget(self.option1Label)
        layout.addWidget(self.option1Edit)
        
        self.option2Label = QLabel("Option 2:")
        self.option2Edit = QLineEdit()
        layout.addWidget(self.option2Label)
        layout.addWidget(self.option2Edit)
        
        self.option3Label = QLabel("Option 3:")
        self.option3Edit = QLineEdit()
        layout.addWidget(self.option3Label)
        layout.addWidget(self.option3Edit)
        
        self.answerLabel = QLabel("Answer:")
        self.answerEdit = QLineEdit()
        layout.addWidget(self.answerLabel)
        layout.addWidget(self.answerEdit)
        
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.saveData)
        layout.addWidget(self.saveButton)
        
        self.setLayout(layout)

    def saveData(self):
        question = self.questionEdit.text()
        option1 = self.option1Edit.text()
        option2 = self.option2Edit.text()
        option3 = self.option3Edit.text()
        answer = self.answerEdit.text()
        
        if not all([question, option1, option2, option3, answer]):
            QMessageBox.warning(self, "Incomplete Data", "Please fill in all fields.")
            return
        
        quiz_id = add_quiz(question, option1, option2, option3, answer)
        QMessageBox.information(self, "Quiz Saved", f"Quiz question saved successfully with ID: {quiz_id}")
        
        self.nOfQuestion += 1
        self.quiz_saved.emit(self.nOfQuestion, self.questionEdit.text())  # Emit the signal with updated data
        # QMessageBox.information(self, "Saved", f"Question {self.nOfQuestion}: {self.questionEdit.text()} has been added!")
        self.close()
