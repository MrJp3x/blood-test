from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit
from jdatetime import datetime as jdatetime

class JalaliDateTimePicker(QWidget):
    def __init__(self, save_callback):
        super().__init__()
        self.save_callback = save_callback

        layout = QVBoxLayout()

        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Enter Jalali DateTime (e.g., 1400-01-01 12:30:00)")
        layout.addWidget(self.date_input)

        save_button = QPushButton("Save Jalali DateTime")
        save_button.clicked.connect(self.save_date_time)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_date_time(self):
        input_text = self.date_input.text()
        try:
            jalali_datetime = jdatetime.strptime(input_text, "%Y-%m-%d %H:%M:%S")
            gregorian_datetime = jalali_datetime.togregorian()
            self.save_callback(gregorian_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        except ValueError:
            print("Invalid date format. Please enter a valid Jalali date and time.")
