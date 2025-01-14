from PyQt6.QtWidgets import (
    QMainWindow, 
    QVBoxLayout,
    QWidget
    )
from analyser.image_analyser import *
from gui.image_widget import *
from gui.analysis_widget import *
from gui.file_selector import *
from gui.chart_widget import *
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bildanalyse mit Python")
        self.setGeometry(700, 100, 800, 900)

        self.file_selector_widget = FileSelectorWidget()
        self.analysis_widget = AnalysisWidget()
        self.chart_widget = ChartWidget()

        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        layout.addWidget(self.file_selector_widget)
        layout.addWidget(self.analysis_widget)
        layout.addWidget(self.chart_widget)

        self.analysis_widget.button_analyse.clicked.connect(self._analyse_image)

    def _analyse_image(self):
        selected_file = self.file_selector_widget.selected_file
        if(selected_file.is_file()):
            analyser = ImageAnalyser(str(selected_file))

            print(f"UniqueColors: {analyser.uniqueColors()}")
            print(f"Most Common: {analyser.findMostCommonColor()}")

            avg_color = analyser.calcAverage()
            median_color = analyser.calcMedian()
            
            print(f"Average: {avg_color[0]}, {avg_color[1]}, {avg_color[2]}")
            print(f"Median: {median_color[0]}, {median_color[1]}, {median_color[2]}")

            self.analysis_widget.set_average_color(avg_color)
            self.analysis_widget.set_median_color(median_color)

            most_common_colors = analyser.findMostCommonColor(5)
            self.chart_widget.set_most_common_colors(most_common_colors)
        else:
            print("Es wurde noch kein Bild ausgewählt.")