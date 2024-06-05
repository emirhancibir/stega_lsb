#!/usr/bin/env python3
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QMessageBox, QPlainTextEdit, QLineEdit
from PyQt5.QtGui import QPixmap
import cv2
from src.decode import decode
from src.encode import insert_msg
from src.encode import create_verify_code
from firebase_connection import send_data_to_firebase

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

class ImageProcessingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_path = None

    def initUI(self):
        self.setWindowTitle("Image Steganography")
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

        name_surname_layout = QHBoxLayout()
        name_surname_layout.addWidget(QLabel("Name:"))
        self.name_input = QLineEdit()
        name_surname_layout.addWidget(self.name_input)
        name_surname_layout.addWidget(QLabel("Surname:"))
        self.surname_input = QLineEdit()
        name_surname_layout.addWidget(self.surname_input)

        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.verification_code_text)
        main_layout.addLayout(name_surname_layout)

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
            verification_code = create_verify_code()
            encoded_image_path = insert_msg(file_path, verification_code, debug=True)
            self.display_image(encoded_image_path, self.image_label)

            name = self.name_input.text()
            surname = self.surname_input.text()

            data = {
                "name": name,
                "surname": surname,
                "verification_code": verification_code
            }

            send_data_to_firebase(data, file_path, encoded_image_path)

            QMessageBox.information(self, "Verification Code Embedded", f"The verification code '{verification_code}' has been embedded in the image.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")

    def show_decode_dialog(self):
        file_path = self.image_path
        if file_path:
            secret_message = decode(file_path, debug=True)
            self.verification_code_text.setPlainText(secret_message)
            QMessageBox.information(self, "Verification Code Decoded", "The verification code has been decoded.")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_app = ImageProcessingApp()
    image_app.show()
    sys.exit(app.exec_())
