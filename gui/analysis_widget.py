from PyQt6.QtWidgets import (
    QGridLayout,
    QPushButton,
    QLabel,
    QWidget
)

class AnalysisWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.button_analyse = QPushButton("Bild Analysieren")
        self.label_avg_color_text = QLabel("Average Color:")
        self.label_median_color_text = QLabel("Median Color:")
        
        self.widget_avg_color = QWidget()
        self.widget_median_color = QWidget()
        
        layout = QGridLayout()
        layout.addWidget(self.button_analyse,           0, 0, 1, 2)
        layout.addWidget(self.label_avg_color_text,     1, 0)
        layout.addWidget(self.widget_avg_color,         1, 1)
        layout.addWidget(self.label_median_color_text,  2, 0)
        layout.addWidget(self.widget_median_color,      2, 1)
        
        self.setLayout(layout)
        
        self.widget_avg_color.setStyleSheet("background-color: white;")
        self.widget_median_color.setStyleSheet("background-color: white;")

    def set_average_color(self, color_tuple):
        self.label_avg_color_text.setText(f"Average Color: {color_tuple[0]}, {color_tuple[1]}, {color_tuple[2]}")
        hex_color = self._rgb_to_hex(color_tuple)
        self.widget_avg_color.setStyleSheet(f"background-color: {hex_color}")

    def set_median_color(self, color_tuple):
        self.label_median_color_text.setText(f"Median Color: {color_tuple[0]}, {color_tuple[1]}, {color_tuple[2]}")
        hex_color = self._rgb_to_hex(color_tuple)
        self.widget_median_color.setStyleSheet(f"background-color: {hex_color}")

    def _rgb_to_hex(self, rgb):
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
