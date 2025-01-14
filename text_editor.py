import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMessageBox, QFileDialog
from PyQt6.QtCore import Qt

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Text Editor")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        self.text_edit = QTextEdit()
        main_layout.addWidget(self.text_edit)

        open_button = QPushButton("Open")
        open_button.clicked.connect(self.open_file)
        button_layout.addWidget(open_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_file)
        button_layout.addWidget(save_button)

        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.close)
        button_layout.addWidget(quit_button)

        main_layout.addLayout(button_layout)
        central_widget.setLayout(main_layout)

        self.text_changed = False
        self.text_edit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self):
        self.text_changed = True

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    self.text_edit.setPlainText(content)
                    self.text_changed = False
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if filename:
            try:
                with open(filename, 'w') as file:
                    content = self.text_edit.toPlainText()
                    file.write(content)
                    self.text_changed = False
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")

    def closeEvent(self, event):
        if self.text_changed:
            reply = QMessageBox.warning(
                self, "Quit?",
                "You have unsaved changes. Are you sure you want to quit?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                event.ignore()
                return
        event.accept()

app = QApplication(sys.argv)
editor = TextEditor()
editor.show()
sys.exit(app.exec())
