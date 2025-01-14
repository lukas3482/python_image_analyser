from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget
    )
from PyQt6.QtCharts import (
    QChart,
    QChartView,
    QBarSet,
    QBarSeries,
    QValueAxis,
)
from PyQt6.QtGui import (
    QPainter,
    QColor,
)
from PyQt6.QtCore import Qt
from analyser.image_analyser import *
from gui.image_widget import *

class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.button_show_chart = QPushButton("Diagramm anzeigen")
        self.chart_view = None
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button_show_chart)
        self.setLayout(self.layout)
        
        self.button_show_chart.clicked.connect(self._toggle_chart)

        self._most_common_colors = []

    def set_most_common_colors(self, most_common_colors):
        self._most_common_colors = most_common_colors
        self._reset_chart()

    def _toggle_chart(self):
        if self.chart_view is None:
            self._create_chart()
        else:
            if self.chart_view.isVisible():
                self.chart_view.setVisible(False)
            else:
                self.setVisible(True)

    def _reset_chart(self):
        if self.chart_view != None:
            self.chart_view.setVisible(False)
        self.chart_view = None

    def _create_chart(self):
        chart = QChart()
        chart.setTitle("Most Common Colors")
        
        series = QBarSeries()
        
        for (rgb, anzahl) in self._most_common_colors:
            bar_set = QBarSet(f"{rgb}")
            bar_set.append(anzahl)
            bar_set.setColor(QColor(rgb[0], rgb[1], rgb[2]))
            series.append(bar_set)

        series.setLabelsVisible(False)
        chart.addSeries(series)

        axis_y = QValueAxis()
        axis_y.setTitleText("Anzahl Pixel")
        
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)
        
        self.chart_view = QChartView(chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        self.layout.addWidget(self.chart_view)