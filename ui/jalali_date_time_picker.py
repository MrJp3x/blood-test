# jalali_date_time_picker.py
import jdatetime
from PySide6.QtWidgets import QDialog, QVBoxLayout, QCalendarWidget, QPushButton

class JalaliDatePicker(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("select date")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        self.ok_button = QPushButton("Confirm")
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_selected_date(self):
        selected_date = self.calendar.selectedDate().toPython()
        jalali_date = jdatetime.date.fromgregorian(date=selected_date)
        return jalali_date.strftime("%Y-%m-%d")
