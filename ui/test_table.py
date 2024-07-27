# test_table.py
from PySide6 import QtGui
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QMenu
from PySide6.QtCore import Qt

class TestTable(QTableWidget):
    def __init__(self, edit_callback, delete_callback, refresh_callback):
        super().__init__()
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self.refresh_callback = refresh_callback

        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["ID", "Test Type", "Result", "Date"])
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)


    def load_tests(self, tests):
        self.setRowCount(0)
        for test in tests:
            row_position = self.rowCount()
            self.insertRow(row_position)
            self.setItem(row_position, 0, QTableWidgetItem(str(test[0])))
            self.setItem(row_position, 1, QTableWidgetItem(test[1]))
            self.setItem(row_position, 2, QTableWidgetItem(test[2]))
            self.setItem(row_position, 3, QTableWidgetItem(test[3]))

    def show_context_menu(self, position):
        menu = QMenu()
        refresh_action = menu.addAction("Refresh")
        refresh_action.triggered.connect(self.refresh_callback)
        menu.exec(self.viewport().mapToGlobal(position))
