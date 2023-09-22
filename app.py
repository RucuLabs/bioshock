import sys
import os
import re
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox, QListWidget

import tools.cameras as cameras
import tools.interaction as interaction
import tools.monitoring as monitoring
from tools.art import BANNER

class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, interval, project_name, available_ports):
        super().__init__()
        self.running = False
        self.interval = interval
        self.project_name = project_name
        self.available_ports = available_ports
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run)

    def start(self):
        self.running = True
        self.timer.start(self.interval * 1000)

    def stop(self):
        self.running = False
        self.timer.stop()
        self.finished.emit()

    def run(self):
        
        print("Proyecto:", self.project_name)
        print("Puertos disponibles:", self.available_ports)
        # Tu código de captura de fotos y procesamiento aquí
        pass

def is_valid_project_name(name):
    return re.match(r'^[a-zA-Z0-9_-]+$', name)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = None
        self.available_ports = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Detener ciclo while')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.start_button = QPushButton('Iniciar')
        self.start_button.clicked.connect(self.start_worker)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton('Detener')
        self.stop_button.clicked.connect(self.stop_worker)
        layout.addWidget(self.stop_button)

        self.update_ports_button = QPushButton('Actualizar Puertos')
        self.update_ports_button.clicked.connect(self.update_ports)
        layout.addWidget(self.update_ports_button)

        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText('Intervalo (segundos)')
        layout.addWidget(self.interval_input)

        self.project_name_input = QLineEdit()
        self.project_name_input.setPlaceholderText('Nombre del Proyecto (sin espacios)')
        layout.addWidget(self.project_name_input)

        self.ports_list = QListWidget()
        layout.addWidget(self.ports_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.update_ports()

    def update_ports(self):
        _, self.available_ports, _ = cameras.list_ports()
        self.ports_list.clear()
        self.ports_list.addItems([str(port) for port in self.available_ports])

    def start_worker(self):
        interval_text = self.interval_input.text()
        project_name = self.project_name_input.text()
        
        try:
            interval = int(interval_text)
            if interval <= 0:
                raise ValueError()
        except ValueError:
            # El valor no es un número positivo válido
            return

        if not is_valid_project_name(project_name):
            QMessageBox.critical(self, 'Error', 'El nombre del proyecto no es válido.')
            return

        monitoring_path = f"./monitoring/{project_name}"
        if os.path.exists(project_name):
            QMessageBox.critical(self, 'Error', 'El proyecto "{}" ya existe.'.format(project_name))
            return

        if self.worker:
            self.worker.stop()

        self.worker = Worker(interval, project_name, self.available_ports)
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

    _, working_ports, _ = cameras.list_ports()
    if not working_ports:
        print("Exiting")
        sys.exit(1)

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
