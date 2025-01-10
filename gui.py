import sys
import random
from PyQt6 import QtCore, QtWidgets, QtGui


# Subclass QMainWindow to customise your application's main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Widget Demo")
        layout.addWidget(self.label)
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItems(['One', 'Two', 'Three'])
        layout.addWidget(self.combo_box)
        self.check_box_1 = QtWidgets.QCheckBox('choose this')
        self.check_box_2 = QtWidgets.QCheckBox('and this?')
        layout.addWidget(self.check_box_1)
        layout.addWidget(self.check_box_2)
        self.line_edit = QtWidgets.QLineEdit('Type here')
        layout.addWidget(self.line_edit)
        self.radio_button_1 = QtWidgets.QRadioButton('This one?')
        self.radio_button_2 = QtWidgets.QRadioButton('Or this one?')
        layout.addWidget(self.radio_button_1)
        layout.addWidget(self.radio_button_2)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)
        self.button_1 = QtWidgets.QPushButton('Ok')
        self.button_2 = QtWidgets.QPushButton('Cancel')
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.