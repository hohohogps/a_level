import sys
import random
from PyQt6 import QtCore, QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversion tool.")

        layout = QtWidgets.QFormLayout()

        self.feet_input = QtWidgets.QLineEdit('')
        layout.addRow('Feet',self.feet_input)
        self.meters_label = QtWidgets.QLabel("0.0")
        layout.addRow("Metres", self.meters_label)
        
        self.feet_input.editingFinished.connect(self.on_text_change)
    
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def on_text_change(self):
        try:
            feet = float(self.feet_input.text())
            meters = feet * 0.3048
            self.meters_label.setText(f"{meters:.2f}")
        except ValueError:
            self.meters_label.setText("Invalid input")
            
app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()