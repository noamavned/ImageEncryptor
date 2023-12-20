from funcs import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QRadioButton, QTextEdit, QGroupBox, QSizePolicy
from PyQt5.QtCore import Qt
from pathlib import Path
from error import raise_error
from success import success_message

class ImageEncryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        image_group_box = QGroupBox('Image')
        image_layout = QHBoxLayout()

        self.image_path_label = QLabel('Path:')
        self.image_path_edit = QLineEdit(self)
        self.image_path_button = QPushButton('Browse', self)
        self.image_path_button.clicked.connect(self.get_image_path)

        image_layout.addWidget(self.image_path_label)
        image_layout.addWidget(self.image_path_edit)
        image_layout.addWidget(self.image_path_button)
        image_group_box.setLayout(image_layout)
        image_group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        text_type_group_box = QGroupBox('Text Type')
        text_type_layout = QVBoxLayout()

        self.text_type_group = QRadioButton('Direct Input', self)
        self.text_type_file = QRadioButton('Text File', self)
        self.text_type_group.setChecked(True)

        self.text_type_group.toggled.connect(self.toggle_text_input)
        self.text_type_file.toggled.connect(self.toggle_text_input)

        text_type_layout.addWidget(self.text_type_group)
        text_type_layout.addWidget(self.text_type_file)
        text_type_group_box.setLayout(text_type_layout)
        text_type_group_box.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        text_group_box = QGroupBox('Text')
        text_layout = QHBoxLayout()

        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText('Enter text here...')
        self.text_edit.setHidden(True)

        text_layout.addWidget(self.text_edit)

        self.text_file_path_label = QLabel('Path:')
        self.text_file_path_edit = QLineEdit(self)
        self.text_file_path_button = QPushButton('Browse', self)
        self.text_file_path_button.setHidden(True)
        self.text_file_path_button.clicked.connect(self.get_text_file_path)

        text_layout.addWidget(self.text_file_path_label)
        text_layout.addWidget(self.text_file_path_edit)
        text_layout.addWidget(self.text_file_path_button)
        text_layout.setAlignment(Qt.AlignTop)
        text_group_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        text_group_box.setLayout(text_layout)

        output_group_box = QGroupBox('Output')
        output_layout = QVBoxLayout()

        output_path_group_box = QGroupBox('')
        output_path_layout = QHBoxLayout()

        output_name_group_box = QGroupBox('')
        output_name_layout = QHBoxLayout()

        self.output_path_label = QLabel('Path:')
        self.output_path_edit = QLineEdit(self)
        self.output_path_button = QPushButton('Browse', self)
        self.output_path_button.clicked.connect(self.get_output_path)
        self.output_name_label = QLabel('Name:')
        self.output_tooltip_label = QLabel('ⓘ')
        self.output_tooltip_label.setToolTip("No extension!")
        self.output_name_edit = QLineEdit(self)

        output_path_layout.addWidget(self.output_path_label)
        output_path_layout.addWidget(self.output_path_edit)
        output_path_layout.addWidget(self.output_path_button)
        output_path_group_box.setStyleSheet(r"QGroupBox{border:0;}")
        output_path_group_box.setLayout(output_path_layout)
        output_path_group_box.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        output_name_layout.addWidget(self.output_name_label)
        output_name_layout.addWidget(self.output_name_edit)
        output_name_layout.addWidget(self.output_tooltip_label)
        output_name_group_box.setStyleSheet(r"QGroupBox{border:0;}")
        output_name_group_box.setLayout(output_name_layout)
        output_name_group_box.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

        output_group_box.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)
        output_layout.addWidget(output_path_group_box)
        output_layout.addWidget(output_name_group_box)

        output_group_box.setLayout(output_layout)

        space_group = QGroupBox('')
        space_group.setStyleSheet("border:0;")
        space_group_layout = QHBoxLayout()
        space_group.setLayout(space_group_layout)
        space_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.hide_button = QPushButton('Encrypt and hide text in image', self)
        self.hide_button.clicked.connect(self.hide_text)

        space_group1 = QGroupBox('')
        space_group1.setStyleSheet("border:0;")
        space_group_layout1 = QHBoxLayout()
        space_group1.setLayout(space_group_layout1)

        main_layout = QVBoxLayout()
        main_layout.addWidget(image_group_box)
        main_layout.addWidget(text_type_group_box)
        main_layout.addWidget(text_group_box)
        main_layout.addWidget(output_group_box)
        main_layout.addWidget(space_group)
        main_layout.addWidget(self.hide_button)
        main_layout.addWidget(space_group1)

        self.setLayout(main_layout)
        self.setMinimumWidth(450)
        self.setMinimumHeight(500)
        self.setWindowTitle('Image Encryptor')

        self.toggle_text_input()

        self.show()

    def toggle_text_input(self):
        self.text_edit.clear()
        self.text_file_path_edit.clear()
        self.text_edit.setHidden(not self.text_type_group.isChecked())
        self.text_file_path_edit.setHidden(not self.text_type_file.isChecked())
        self.text_file_path_button.setHidden(
            not self.text_type_file.isChecked())
        self.text_file_path_label.setHidden(
            not self.text_type_file.isChecked())

    def get_image_path(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.gif)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.image_path_edit.setText(selected_files[0])

    def get_text_file_path(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text Files (*.txt)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            self.text_file_path_edit.setText(selected_files[0])

    def get_output_path(self):
        dir = QFileDialog.getExistingDirectory()
        self.output_path_edit.setText(dir)

    def hide_text(self):
        image_path = self.image_path_edit.text()
        output_path = self.output_path_edit.text()
        output_path = output_path.replace("\\", "/")
        output_name = self.output_name_edit.text()
        idt, iok = True, True
        if self.text_type_group.isChecked():
            text = self.text_edit.toPlainText()
            idt = False
        else:
            text = self.text_file_path_edit.text()

        if (not image_path) or (not output_path) or (not text) or (not output_name):
            raise_error(
                "Not all fields were filled!\nMake sure you filled everything :D")
        else:
            if idt:
                p = text
                if not Path(p).is_file():
                    raise_error(
                        "Something is wrong with the text file's path!\nPlease check it and try again")
                    iok = False
                if iok:
                    with open(p) as f:
                        text = f.read().strip()
            if iok:
                try:
                    text = enc(text)
                except:
                    raise_error(
                        "Something went wrong while encrypting the text.\nPlease try again")
                    iok = False
            if iok and (not Path(image_path).is_file()):
                raise_error(
                    "Image's path does not exist!")
                iok = False
            if iok and (not Path(output_path).is_dir()):
                raise_error(
                    "Output's path does not exist!")
                iok = False
            if iok and (not Path(output_path+"/"+output_name+".jpg")):
                v = 1
                while (not Path(output_path+"/"+output_name+f'{v}'+".jpg")):
                    v += 1
                output_name += f'{v}'
            if iok:
                text = "/scb325/" + text + "/scb325/"
                output_name += ".jpg"
                full_output_path = os.path.join(output_path, output_name).replace("/", "\\")
                hide_text_in_jpeg(image_path, text, full_output_path)
                success_message(f'Hid text in {full_output_path}')