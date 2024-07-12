from PySide6.QtWidgets import QWidget, QVBoxLayout, QDateTimeEdit, QPushButton
from PySide6.QtCore import QDateTime


class DateTimePicker(QWidget):
    def __init__(self, save_callback):
        super().__init__()
        self.save_callback = save_callback

        layout = QVBoxLayout()

        self.date_time_edit = QDateTimeEdit(self)
        self.date_time_edit.setCalendarPopup(True)
        self.date_time_edit.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.date_time_edit)

        save_button = QPushButton("Save DateTime")
        save_button.clicked.connect(self.save_date_time)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_date_time(self):
        selected_datetime = self.date_time_edit.dateTime()
        self.save_callback(selected_datetime.toString("yyyy-MM-dd HH:mm:ss"))
