#!/usr/bin/env python3
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QMessageBox, QPlainTextEdit, QLineEdit, QDialog
from PyQt5.QtGui import QPixmap
import cv2
from src.decode import decode
from src.encode import insert_msg
from src.encode import create_verify_code
from firebase_connection import send_data_to_firebase, get_data_from_firebase

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../edocs'))
sys.path.append(parent_dir)

class NameSurnameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Name and Surname")
        self.layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Name:"))
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        self.layout.addLayout(name_layout)

        surname_layout = QHBoxLayout()
        surname_layout.addWidget(QLabel("Surname:"))
        self.surname_input = QLineEdit()
        surname_layout.addWidget(self.surname_input)
        self.layout.addLayout(surname_layout)

        description_layout = QHBoxLayout()
        description_layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        description_layout.addWidget(self.description_input)
        self.layout.addLayout(description_layout)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        button_layout.addWidget(self.ok_button)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def get_data(self):
        return (
            self.name_input.text(),
            self.surname_input.text(),
            self.description_input.text(),
        )

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_path = None

    def initUI(self):
        self.setWindowTitle("Document Verifier")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.image_label = QLabel()
        self.image_label.setFixedSize(400, 400)

        button_layout = QHBoxLayout()
        browse_button = QPushButton("Browse Document")
        browse_button.clicked.connect(self.browse_image)
        button_layout.addWidget(browse_button)

        encode_button = QPushButton("Embed Random Verification Code")
        encode_button.clicked.connect(self.show_encode_dialog)
        button_layout.addWidget(encode_button)

        decode_button = QPushButton("Show Verification Code")
        decode_button.clicked.connect(self.show_decode_dialog)
        button_layout.addWidget(decode_button)

        self.verification_code_text = QPlainTextEdit()
        self.verification_code_text.setReadOnly(True)

        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.verification_code_text)

    def browse_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", os.path.join(parent_dir, "imgs"), "Image Files (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path, self.image_label)

    def display_image(self, file_path, label):
        pixmap = QPixmap(file_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def show_encode_dialog(self):
        file_path = self.image_path
        if file_path:
            dialog = NameSurnameDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                name, surname, description = dialog.get_data()
                if not name or not surname or not description:
                    QMessageBox.warning(self, "Warning", "Please fill in all fields.")
                    return

                verification_code = create_verify_code()
                insert_msg(file_path, verification_code, debug=True)

                data = {
                    "name": name,
                    "surname": surname,
                    "description": description,
                    "verification_code": verification_code
                }

                send_data_to_firebase(data)

                QMessageBox.information(self, "Verification Code Embedded", f"The verification code '{verification_code}' has been embedded in the image.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")

    def show_decode_dialog(self):
        file_path = self.image_path
        if file_path:
            secret_message = decode(file_path, debug=True)
            self.verification_code_text.setPlainText(secret_message)
            data = get_data_from_firebase(secret_message)
            if data:
                QMessageBox.information(self, "Certificate Found!!", f"Name: {data['name']}\nSurname: {data['surname']}\nDescription: {data['description']}")
            else:
                QMessageBox.warning(self, "Warning", "No data found for the given verification code.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_app = ImageProcessingApp()
    image_app.show()
    sys.exit(app.exec_())
