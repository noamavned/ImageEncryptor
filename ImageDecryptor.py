from funcs import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QRadioButton, QTextEdit, QGroupBox, QSizePolicy
from PyQt5.QtCore import Qt
from pathlib import Path
from error import raise_error

class ImageDecryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        image_group_box = QGroupBox('')
        image_layout = QHBoxLayout()

        self.image_path_label = QLabel('Path:')
        self.image_path_edit = QLineEdit(self)
        self.image_path_button = QPushButton('Browse', self)
        self.image_path_button.clicked.connect(self.get_image_path)

        image_layout.addWidget(self.image_path_label)
        image_layout.addWidget(self.image_path_edit)
        image_layout.addWidget(self.image_path_button)
        image_group_box.setStyleSheet(r"QGroupBox{border:0;}")
        image_group_box.setLayout(image_layout)
        image_group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.extract_button = QPushButton('Extract text from image', self)
        self.extract_button.clicked.connect(self.dec_text)

        space_group = QGroupBox('')
        space_group.setStyleSheet("border:0;")
        space_group_layout = QHBoxLayout()
        space_group.setLayout(space_group_layout)
        space_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setTextInteractionFlags(
            self.text_edit.textInteractionFlags() & ~Qt.TextEditable)

        btns_group_box = QGroupBox('')
        btns_layout = QHBoxLayout()

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_text)
        self.copy_button = QPushButton('Copy', self)
        self.copy_button.clicked.connect(self.copy_text)

        btns_layout.addWidget(self.save_button)
        btns_layout.addWidget(self.copy_button)
        btns_group_box.setStyleSheet(r"QGroupBox{border:0;}")
        btns_group_box.setLayout(btns_layout)
        btns_group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        main_layout = QVBoxLayout()
        main_layout.addWidget(image_group_box)
        main_layout.addWidget(self.extract_button)
        main_layout.addWidget(space_group)
        main_layout.addWidget(self.text_edit)
        main_layout.addWidget(btns_group_box)

        self.setLayout(main_layout)
        self.setMinimumWidth(450)
        self.setMinimumHeight(500)
        self.setWindowTitle('Image Decryptor')

        self.show()

    def get_image_path(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.gif)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.image_path_edit.setText(selected_files[0])

    def save_text(self):
        text_to_save = self.text_edit.toPlainText()
        if not text_to_save:
            raise_error("No text to save!")
            return
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0]
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text_to_save)
            except Exception as e:
                raise_error(f"Error saving file: {str(e)}")

    def copy_text(self):
        text_to_copy = self.text_edit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text_to_copy)

    def dec_text(self):
        image_path = self.image_path_edit.text()
        if not image_path:
            raise_error(
                "Not all fields were filled!\nMake sure you filled everything :D")
            return
        if not Path(image_path).is_file():
            raise_error(
                "Given image path does not exist!")
            return
        extracted = extract_text_from_image(image_path)
        if extracted:
            text = dec(extracted)
            self.text_edit.setPlainText(text)