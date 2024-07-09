from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class TestForm(QWidget):
    def __init__(self, add_test_callback):
        super().__init__()
        self.add_test_callback = add_test_callback

        layout = QVBoxLayout()

        self.test_type_combo = QComboBox()
        self.test_type_combo.addItems(["PT INR", "CBC"])
        self.result_input = QLineEdit()
        self.date_input = QLineEdit()

        layout.addWidget(QLabel("Test Type"))
        layout.addWidget(self.test_type_combo)
        layout.addWidget(QLabel("Result"))
        layout.addWidget(self.result_input)
        layout.addWidget(QLabel("Date"))
        layout.addWidget(self.date_input)

        add_button = QPushButton("Add Test")
        add_button.clicked.connect(self.add_test)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_test(self):
        test_type = self.test_type_combo.currentText()
        result = self.result_input.text()
        date = self.date_input.text()
        self.add_test_callback(test_type, result, date)
