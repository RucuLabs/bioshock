import os
import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import tools.cameras as camera

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

        self.setWindowTitle("BioShock: Monitoring System 4 BioMaterials")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.list_cameras_button = QPushButton("List Cameras")
        self.list_cameras_button.clicked.connect(self.list_cameras)
        self.layout.addWidget(self.list_cameras_button)

        self.camera_dropdown = QComboBox()
        self.layout.addWidget(self.camera_dropdown)

        self.resolution_dropdown = QComboBox()
        self.resolution_dropdown.addItems(list(RESOLUTIONS_16_9.keys()))
        self.layout.addWidget(self.resolution_dropdown)

        self.test_cameras_button = QPushButton("Test Selected Camera")
        self.test_cameras_button.clicked.connect(self.test_selected_camera)
        self.layout.addWidget(self.test_cameras_button)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_test_image)

        self.cameras = None
        self.selected_test_camera = None
        self.selected_resolution = None

    def list_cameras(self):
        self.cameras = camera.detect()
        self.camera_dropdown.addItems(self.cameras)

    def test_selected_camera(self):
        self.selected_resolution = RESOLUTIONS_16_9.get(self.resolution_dropdown.currentText())
        self.selected_test_camera = self.camera_dropdown.currentText()
        if self.selected_resolution:
            camera.take_picture(path="./", 
                                resolution=self.selected_resolution, 
                                cam_name=self.selected_test_camera, 
                                filename='test_image.jpg')
            pixmap = QPixmap('test_image.jpg')
            self.image_label.setPixmap(pixmap)
        else:
            print('No selected resolution or camera')

    def update_test_image(self):
        pass

if __name__ == "__main__":
    if os.path.exists('test_image.jpg'):
        os.remove('test_image.jpg')
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec_())
