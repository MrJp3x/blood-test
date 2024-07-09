from PySide6.QtWidgets import QDialog, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ChartWindow(QDialog):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Test Results Chart")
        self.setGeometry(200, 200, 800, 600)

        self.db = db
        layout = QVBoxLayout()

        figure = Figure()
        self.canvas = FigureCanvas(figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)
        self.plot_chart()

    def plot_chart(self):
        data = self.db.fetch_tests()
        dates = [row[3] for row in data]
        results = [float(row[2]) for row in data]

        ax = self.canvas.figure.add_subplot(111)
        ax.clear()
        ax.plot(dates, results, marker='o')
        ax.set_title("Test Results Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Result")
        ax.grid(True)

        self.canvas.draw()
