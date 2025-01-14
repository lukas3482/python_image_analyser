from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImageWidget(QLabel):
    def __init__(self, file):
        super().__init__()
        self.setGeometry(0, 25, 400, 400)
        image = QPixmap(file)
        image = image.scaled(450, 700, Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(image)
        self.update()
        pass