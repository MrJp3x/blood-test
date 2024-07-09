import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from _version import get_version

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(f"Medical Test Management v{get_version()}")
    window.show()
    sys.exit(app.exec())
