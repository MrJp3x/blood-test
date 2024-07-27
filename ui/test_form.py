# test_form.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from .jalali_date_time_picker import JalaliDatePicker


test_type = ["INR", "Blood Test", "Urine Test", "X-Ray", "MRI"]


class TestForm(QWidget):
    def __init__(self, add_test_callback):
        super().__init__()
        self.add_test_callback = add_test_callback
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Test type
        self.test_type_combo = QComboBox()
        self.test_type_combo.addItems(test_type)
        layout.addWidget(QLabel("Test Type"))
        layout.addWidget(self.test_type_combo)

        # Result
        self.result_input = QLineEdit()
        layout.addWidget(QLabel("Result"))
        layout.addWidget(self.result_input)

        # Date and Jalali date picker button
        date_layout = QHBoxLayout()
        self.date_input = QLineEdit()
        self.date_input.setPlaceholderText("Date (YYYY-MM-DD)")
        date_layout.addWidget(QLabel("Date"))
        date_layout.addWidget(self.date_input)

        self.jalali_date_button = QPushButton("Select Jalali Date")
        self.jalali_date_button.clicked.connect(self.open_jalali_date_picker)
        date_layout.addWidget(self.jalali_date_button)

        layout.addLayout(date_layout)

        # Add button
        self.add_button = QPushButton("Add Test")
        self.add_button.clicked.connect(self.add_test)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def open_jalali_date_picker(self):
        date_picker = JalaliDatePicker(self)
        if date_picker.exec():
            self.date_input.setText(date_picker.get_selected_date())

    def add_test(self):
        test_type = self.test_type_combo.currentText()
        result = self.result_input.text()
        date = self.date_input.text()
        self.add_test_callback(test_type, result, date)
