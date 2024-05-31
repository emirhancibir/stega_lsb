#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap
import cv2
from src.decode import decode
from src.encode import insert_msg

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
        browse_button = QPushButton("Browse Image")
        browse_button.clicked.connect(self.browse_image)
        button_layout.addWidget(browse_button)

        encode_button = QPushButton("Encode")
        encode_button.clicked.connect(self.show_encode_dialog)
        button_layout.addWidget(encode_button)

        decode_button = QPushButton("Decode")
        decode_button.clicked.connect(self.show_decode_dialog)
        button_layout.addWidget(decode_button)

        main_layout.addWidget(self.image_label)
        main_layout.addLayout(button_layout)

    def browse_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", os.path.join(parent_dir, "imgs"), "Image Files (*.png *.jpg *.bmp *.jpeg)")
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def show_encode_dialog(self):
        file_path = self.image_path
        print("Encode File path: ", file_path)
        if file_path:
            message, ok = QInputDialog.getText(self, "Encode Message", "Enter the message to encode:")
            if ok and message:
                insert_msg(file_path, message,debug=True)
                self.display_image(file_path)
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")

    def show_decode_dialog(self):
        file_path = self.image_path
        print("Decode File path: ", file_path)
        if file_path:
            secret_message = decode(file_path, debug=True)
            QMessageBox.information(self, "Decoded Message", f"The decoded message is: {secret_message}")
        else:
            QMessageBox.warning(self, "Warning", "Please select an image first.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_app = ImageProcessingApp()
    image_app.show()
    sys.exit(app.exec_())

