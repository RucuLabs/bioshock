import os
import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

RESOLUTIONS_16_9 = {
    "360p": "640x360",
    "480p": "854x480",
    "540p": "960x540",
    "576p": "1024x576",
    "720p": "1280x720",
    "768p": "1366x768",
    "900p": "1600x900",
    "FullHD": "1920x1080",
    "1440p": "2560x1440",
    "4K": "3840x2160"
}

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BioShock - Monitoring System for Biomaterials")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.list_cameras_button = QPushButton("Listar Cámaras")
        self.list_cameras_button.clicked.connect(self.list_cameras)
        self.layout.addWidget(self.list_cameras_button)

        self.test_cameras_button = QPushButton("Probar Cámaras")
        self.test_cameras_button.clicked.connect(self.test_cameras)
        self.layout.addWidget(self.test_cameras_button)

        self.camera_dropdown = QComboBox()
        self.layout.addWidget(self.camera_dropdown)

        self.resolution_dropdown = QComboBox()
        self.resolution_dropdown.addItems(list(RESOLUTIONS_16_9.keys()))
        self.layout.addWidget(self.resolution_dropdown)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.current_camera = None

    def list_cameras(self):
        # Listar cámaras disponibles
        cameras = [f"Camera {i}" for i in range(1, 5)]  # Supongamos 4 cámaras disponibles
        self.camera_dropdown.addItems(cameras)

    def test_cameras(self):
        # Iniciar la cámara seleccionada
        selected_camera = self.camera_dropdown.currentText()
        if selected_camera:
            self.current_camera = cv2.VideoCapture(0)  # Supongamos que seleccionamos la cámara 0
            self.timer.start(30)  # Actualizar la imagen cada 30 ms

    def update_image(self):
        if self.current_camera:
            ret, frame = self.current_camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytes_per_line = 3 * width
                image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.image_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
