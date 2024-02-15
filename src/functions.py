import time
import speech_recognition as sr
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QDropEvent, QDragEnterEvent
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox, QProgressDialog
from src.elements import *


def dragEnterEvent(event: QDragEnterEvent):
    if event.mimeData().hasUrls():
        event.acceptProposedAction()
        print("file dragged over window")
        frame.setStyleSheet("background-color: #6495ED; border-radius: 10px;")


def dropEvent(event: QDropEvent):
    global filepath

    for url in event.mimeData().urls():
        filepath = url.toLocalFile()
        print(f"File dropped: {filepath}")
    frame.setStyleSheet("background-color: grey; border-radius: 10px;")
    readFile(filepath)


def dragLeaveEvent(event):
    print(event)
    frame.setStyleSheet("background-color: grey; border-radius: 10px;")


def readFile(filepath):
    file = filepath.split("/")[-1]
    current_file_path.setText(file)


class WorkerThread(QThread):
    finished = Signal(object)

    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def run(self):
        output = speach2text(self.filepath)
        self.finished.emit(output)

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("convert")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.start_conversion)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.message_label = QLabel("Convert file?")
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def start_conversion(self):
        self.progress_dialog = QProgressDialog("Converting...", "Cancel", 0, 0, self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.canceled.connect(self.cancel_conversion)

        self.worker_thread = WorkerThread(filepath)
        self.worker_thread.finished.connect(self.conversion_complete)

        self.worker_thread.start()
        self.progress_dialog.exec_()

    def cancel_conversion(self):
        self.worker_thread.terminate()
        self.progress_dialog.close()

    def conversion_complete(self, output):
        self.progress_dialog.close()

        if output is not None:
            self.show_message("Conversion Successful", output)
        else:
            self.show_message("Invalid File", "Failed to convert the file.")

        self.close()

    def show_message(self, title, text):
        QMessageBox.information(self, title, text)


def button_clicked(s):
    global filepath
    print("click", s)
    time.sleep(0.5)
    dlg = CustomDialog(window)
    dlg.setStyleSheet("background-color: #323232;color: white")
    dlg.exec()


def speach2text(filepath):
    recognizer = sr.Recognizer()
    audio_file = filepath

    try:
        # Google API
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("Recognized text:", text)
        return text
    except Exception as e:
        print(str(e))
        return None


button.clicked.connect(lambda: button_clicked(window))
