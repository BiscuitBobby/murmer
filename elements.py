import csv
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout

app = QtWidgets.QApplication([])

button = QtWidgets.QPushButton("Convert")
button.setStyleSheet("color: black; background-color: orange; border-radius: 10px;")

window = QtWidgets.QWidget()

layout = QtWidgets.QVBoxLayout(window)
window.setStyleSheet("background-color: #323232")

current_file_path = QtWidgets.QLabel('drop files here:')
currentFileLayout = QHBoxLayout(window)
current_file = QtWidgets.QLabel('')
currentFileLayout.addWidget(current_file)

frame = QtWidgets.QFrame(window)
frame.setFrameShape(QtWidgets.QFrame.Box)
frame.setStyleSheet("background-color: grey; border-radius: 10px;")
frame.setMinimumSize(420, 340)
frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # set size policy


frame_layout = QtWidgets.QHBoxLayout(frame)  # Add a layout to the frame
frame_layout.setContentsMargins(0, 0, 0, 0)  # Set the margins of the layout to zero
frame_layout.setAlignment(QtCore.Qt.AlignCenter)  # Align the layout to the center of the frame

plus_label = QtWidgets.QLabel("+", parent=frame)
plus_label.setFont(QtGui.QFont("Arial", 50, QtGui.QFont.Bold))
plus_label.setAlignment(QtCore.Qt.AlignCenter)
frame_layout.addWidget(plus_label)  # Add the plus_label to the frame_layout


button.setMinimumSize(200, 50)
layout.addWidget(current_file_path)
layout.addWidget(frame)
layout.addLayout(currentFileLayout)
layout.addWidget(button)
layout.setAlignment(Qt.AlignCenter)

