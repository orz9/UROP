from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QButtonGroup

class LessonMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lesson Menu')
        layout = QVBoxLayout()

        label = QLabel('Please select your lesson', self)
        layout.addWidget(label)

        self.buttonGroup = QButtonGroup(self)
        lessons = ['Lesson 1 Kinemetics', 'Lesson 2 Motion', 'Lesson 3 Newton\'s Law', 'Lesson 4 Thermodynamics']
        for lesson in lessons:
            btn = QRadioButton(lesson, self)
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
