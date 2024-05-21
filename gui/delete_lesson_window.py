from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox
from mongoDB.db_utils import get_lessons, delete_lesson

class DeleteLessonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Lesson")
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.lessonCheckboxes = []

        # Fetch lessons from database
        lessons = get_lessons()  # This function is used fetch lesson data including in the 'topic'
        for lesson in lessons:
            cb = QCheckBox(lesson['topic'], self)
            self.lessonCheckboxes.append(cb)
            self.layout.addWidget(cb)

        # Error message label
        self.errorLabel = QLabel('')
        self.layout.addWidget(self.errorLabel)

        # Buttons
        deleteButton = QPushButton('Delete', self)
        deleteButton.clicked.connect(self.confirm_deletion)
        backButton = QPushButton('Back', self)
        backButton.clicked.connect(self.close)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(deleteButton)
        buttonLayout.addWidget(backButton)
        self.layout.addLayout(buttonLayout)

    def confirm_deletion(self):
        selected_lessons = [cb.text() for cb in self.lessonCheckboxes if cb.isChecked()]
        if not selected_lessons:
            self.errorLabel.setText("Error, empty selection")
            QMessageBox.warning(self, 'Error', 'Error, empty selection')
            return

        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Question)
        confirm_msg.setWindowTitle('Confirm Delete')
        confirm_msg.setText("Confirm deleting the following lessons?")
        detail_text = "\n".join(selected_lessons)
        confirm_msg.setDetailedText(detail_text)
        confirm_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_msg.setDefaultButton(QMessageBox.Cancel)
        response = confirm_msg.exec_()

        if response == QMessageBox.Ok:
            self.delete_selected_lessons(selected_lessons)

    def delete_selected_lessons(self):
        selected_lessons = [cb.text() for cb in self.lessonCheckboxes if cb.isChecked()]
        # Delete lessons from the database
        for lesson_topic in selected_lessons:
            delete_lesson(lesson_topic)  # Assumes delete_lesson takes the topic and removes that lesson from the database

        QMessageBox.information(self, 'Success', 'Selected lessons have been deleted.')
        self.close()  # Optionally close this window after deletion
