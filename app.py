import sys
import os
import re

from PyQt5.QtCore import Qt, QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QListWidget, QGroupBox, QTextEdit


import tools.errors as ERRORS
from tools.art import BANNER
import tools.monitoring as monitoring
import tools.cameras as cameras

MONITORING_PATH = "./monitoring/"
WINDOW_TITLE = "BioShock: Monitoring System for Biomaterials"
class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, interval, monitoring_path, available_ports):
        super().__init__()
        self.running = False
        self.interval = interval
        self.monitoring_path = monitoring_path
        self.available_ports = available_ports
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run)
        self.iteration = 0

    def start(self):
        os.makedirs(self.monitoring_path)
        os.makedirs(self.monitoring_path + "/pictures")
        self.running = True
        self.timer.start(self.interval * 1000)

    def stop(self):
        self.running = False
        self.iteration = 0
        self.timer.stop()
        self.finished.emit()

    def run(self):
        monitoring.monitoring_cycle(monitoring_path=self.monitoring_path, working_ports=working_ports, iteration=self.iteration)
        print(self.iteration)
        self.iteration += 1

def is_valid_project_name(name):
    return re.match(r'^[a-zA-Z0-9_-]+$', name)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = None
        self.available_ports = []
        self.supported_resolutions = []

        self.initUI()

    def initUI(self):

        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # SETTINGS BOX
        settings_box = QGroupBox('Monitoring Settings')
        layout.addWidget(settings_box)
        settings_box.setLayout(QVBoxLayout())
        # SET PROJECT NAME INPUT
        self.project_name_input = QLineEdit()
        self.project_name_input.setPlaceholderText('Project Name')
        settings_box.layout().addWidget(self.project_name_input)
        # SET INTERVAL INPUT
        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText('Interval (seconds)')
        settings_box.layout().addWidget(self.interval_input)

        # CAM BOX
        cam_box = QGroupBox('Available Cameras')
        layout.addWidget(cam_box)
        cam_box.setLayout(QVBoxLayout())
        # AVAILABLE CAMS LIST
        self.ports_list = QListWidget()
        cam_box.layout().addWidget(self.ports_list)
        # UPDATE CAMS BUTTON
        self.update_ports_button = QPushButton('Update Cameras')
        self.update_ports_button.clicked.connect(self.update_ports)
        cam_box.layout().addWidget(self.update_ports_button)

        # CONTROL BOX
        control_box = QGroupBox('Monitoring Control')
        layout.addWidget(control_box)
        control_box.setLayout(QVBoxLayout())
        # START BUTTON
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_worker)
        control_box.layout().addWidget(self.start_button)
        # STOP BUTTON
        self.stop_button = QPushButton('Stop')
        self.stop_button.clicked.connect(self.stop_worker)
        control_box.layout().addWidget(self.stop_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.update_ports()

    def update_ports(self):
        _, self.available_ports, _, self.supported_resolutions = cameras.list_ports()
        self.ports_list.clear()
        item_list = []
        for idx, port in enumerate(self.available_ports):
            item = f"{str(port)} - {str(self.supported_resolutions[idx])}"
            item_list.append(item)
        self.ports_list.addItems(item_list)

    def start_worker(self):
        interval_text = self.interval_input.text()
        project_name = self.project_name_input.text()
        
        try:
            interval = int(interval_text)
            if interval <= 0:
                raise ValueError()
        except ValueError:
            QMessageBox.critical(self, 'NOT_VALID_INTERVAL', ERRORS.NOT_VALID_INTERVAL)
            return

        if not is_valid_project_name(project_name):
            QMessageBox.critical(self, 'NOT_VALID_PROJECT_NAME', ERRORS.NOT_VALID_PROJECT_NAME)
            return

        monitoring_path = MONITORING_PATH + project_name
        if os.path.exists(monitoring_path):
            QMessageBox.critical(self, 'PROJECT_ALREADY_EXISTS', ERRORS.PROJECT_ALREADY_EXISTS)
            return

        if self.worker:
            self.worker.stop()

        self.worker = Worker(interval, monitoring_path, self.available_ports)
        self.worker.finished.connect(self.worker_finished)
        self.worker.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.interval_input.setEnabled(False)
        self.project_name_input.setEnabled(False)

    def stop_worker(self):
        if self.worker:
            self.worker.stop()
            self.worker = None
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.interval_input.setEnabled(True)
        self.project_name_input.setEnabled(True)

    def worker_finished(self):
        pass

if __name__ == '__main__':
    print(BANNER)

    _, working_ports, _, suppored_resolutions = cameras.list_ports()
    if not working_ports:
        print("Exiting")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
