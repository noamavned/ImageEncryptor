from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from ImageDecryptor import ImageDecryptorApp
from ImageEncryptor import ImageEncryptorApp

cho = None
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        message_label = QLabel("Hello!\nClick the desired button to continue.")
        main_layout.addWidget(message_label)
        buttons_layout = QHBoxLayout()
        quit_button = QPushButton('Quit', self)
        encrypt_button = QPushButton('Encrypt', self)
        decrypt_button = QPushButton('Decrypt', self)
        quit_button.clicked.connect(self.quit_clicked)
        encrypt_button.clicked.connect(self.encrypt_clicked)
        decrypt_button.clicked.connect(self.decrypt_clicked)
        buttons_layout.addWidget(quit_button)
        buttons_layout.addWidget(encrypt_button)
        buttons_layout.addWidget(decrypt_button)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        self.setWindowTitle('Main Window')
        self.setFixedSize(250, 75)
        self.show()

    def quit_clicked(self):
        exit()

    def encrypt_clicked(self):
        global cho
        cho = 0
        self.close()

    def decrypt_clicked(self):
        global cho
        cho = 1
        self.close()


app = QApplication([])
window = Main()
app.exec_()

if cho == 1:
    app1 = QApplication([])
    ex = ImageDecryptorApp()
    app1.exec_()
elif cho != None:
    app1 = QApplication([])
    ex = ImageEncryptorApp()
    app1.exec_()
# pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/Noam Avned/Downloads/encryption-icon-15203-Windows.ico" --name "ImageEncryptor" --add-data "C:/Users/Noam Avned/Documents/imageHider/env;env/" --add-data "C:/Users/Noam Avned/Documents/imageHider/error.py;." --add-data "C:/Users/Noam Avned/Documents/imageHider/funcs.py;." --add-data "C:/Users/Noam Avned/Documents/imageHider/ImageDecryptor.py;." --add-data "C:/Users/Noam Avned/Documents/imageHider/ImageEncryptor.py;." --add-data "C:/Users/Noam Avned/Documents/imageHider/success.py;."  "C:/Users/Noam Avned/Documents/imageHider/app.py"