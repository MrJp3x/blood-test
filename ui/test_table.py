from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class TestTable(QWidget):
    def __init__(self, edit_test_callback, delete_test_callback):
        super().__init__()
        self.edit_test_callback = edit_test_callback
        self.delete_test_callback = delete_test_callback

        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Test Type", "Result", "Date", "Actions"])
        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_tests(self, tests):
        self.table.setRowCount(0)
        for test in tests:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for i, data in enumerate(test):
                self.table.setItem(row_position, i, QTableWidgetItem(str(data)))

            edit_button = QPushButton("Edit")
            delete_button = QPushButton("Delete")
            edit_button.clicked.connect(lambda _, row=row_position: self.edit_test_callback(row))
            delete_button.clicked.connect(lambda _, row=row_position: self.delete_test_callback(row))

            self.table.setCellWidget(row_position, 4, edit_button)
            self.table.setCellWidget(row_position, 4, delete_button)
