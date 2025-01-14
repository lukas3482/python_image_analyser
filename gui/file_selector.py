from pathlib import Path

from PyQt6.QtWidgets import (
    QFileDialog,
    QVBoxLayout,
    QPushButton,
    QWidget
)
from PyQt6.QtGui import (
    QPixmap,
)
from PyQt6.QtCore import Qt

from gui.image_widget import ImageWidget


class FileSelectorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        #Default Image
        self.selected_file = Path("C:\\Users\\lukas\\OneDrive\\#Studium\\#FHV\\1. Semester\\Wissenschaftliches Rechnen mit Python\\Projekt\\img\\bild_4.png")
        
        self.button_select_file = QPushButton("Select Img")
        self.image_label = ImageWidget(str(self.selected_file))
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_select_file)
        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)
        
        self.button_select_file.clicked.connect(self._open_file_dialog)

    def _open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Images (*.png *.jpg)")
        #Default File Location
        dialog.setDirectory("C:\\Users\\lukas\\OneDrive\\#Studium\\#FHV\\1. Semester\\Wissenschaftliches Rechnen mit Python\\Projekt\\img\\")

        if dialog.exec():
            file_paths = dialog.selectedFiles()
            if file_paths:
                self.selected_file = Path(file_paths[0])
                pixmap = QPixmap(str(self.selected_file))
                pixmap = pixmap.scaled(450, 500, Qt.AspectRatioMode.KeepAspectRatio)
                self.image_label.setPixmap(pixmap)

    def update_image(self, file_path: Path):
        self.selected_file = file_path
        pixmap = QPixmap(str(self.selected_file))
        pixmap = pixmap.scaled(450, 500, Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)