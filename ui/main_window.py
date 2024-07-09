from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QToolBar, QPushButton
from db_controler import DatabaseController
from ui.test_form import TestForm
from ui.test_table import TestTable
from ui.chart_window import ChartWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Test Management")
        self.setGeometry(100, 100, 800, 600)

        self.db = DatabaseController("medical_tests.db")

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New Test", self)
        file_menu.addAction(new_action)
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(new_action)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Input form
        self.test_form = TestForm(self.add_test)
        layout.addWidget(self.test_form)

        # Search field
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.search_tests)
        layout.addWidget(self.search_input)

        # Test table
        self.test_table = TestTable(self.edit_test, self.delete_test)
        layout.addWidget(self.test_table)

        # Show Chart button
        chart_button = QPushButton("Show Chart")
        chart_button.clicked.connect(self.show_chart)
        layout.addWidget(chart_button)

        central_widget.setLayout(layout)
        self.load_tests()

    def add_test(self, test_type, result, date):
        self.db.insert_test(test_type, result, date)
        self.load_tests()

    def load_tests(self):
        tests = self.db.fetch_tests()
        self.test_table.load_tests(tests)

    def search_tests(self):
        query = self.search_input.text()
        results = self.db.search_tests(query)
        self.test_table.load_tests(results)

    def show_chart(self):
        chart_window = ChartWindow(self.db)
        chart_window.exec()

    def edit_test(self, row):
        test_id = int(self.test_table.table.item(row, 0).text())
        test_type = self.test_form.test_type_combo.currentText()
        result = self.test_form.result_input.text()
        date = self.test_form.date_input.text()
        self.db.update_test(test_id, test_type, result, date)
        self.load_tests()

    def delete_test(self, row):
        test_id = int(self.test_table.table.item(row, 0).text())
        self.db.delete_test(test_id)
        self.load_tests()

    def closeEvent(self, event):
        self.db.close()
        event.accept()
