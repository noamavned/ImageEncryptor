from PyQt5.QtWidgets import QMessageBox

class SuccessWindow(QMessageBox):
    def __init__(self, parent=None):
        super(SuccessWindow, self).__init__(parent)
        self.setWindowTitle('Success')
        self.setIcon(QMessageBox.Information)
        self.setText('Success')
        self.setDetailedText('Detailed success information goes here.')

        self.close_and_stay_button = self.addButton(
            'Close and Stay', QMessageBox.AcceptRole)
        self.close_and_quit_button = self.addButton(
            'Close and Quit', QMessageBox.RejectRole)
        self.close_and_stay_button.clicked.connect(self.close_and_stay)
        self.close_and_quit_button.clicked.connect(self.close_and_quit)

    def close_and_stay(self):
        self.accept()

    def close_and_quit(self):
        self.reject()
        exit()


def success_message(msg):
    suc_window = SuccessWindow()
    suc_window.setDetailedText(msg)
    result = suc_window.exec_()