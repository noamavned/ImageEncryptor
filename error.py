from PyQt5.QtWidgets import QMessageBox

class ErrorWindow(QMessageBox):
    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent)
        self.setWindowTitle('Error')
        self.setIcon(QMessageBox.Critical)
        self.setText('An error occurred')
        self.setDetailedText('Detailed error information goes here.')
        self.addButton(QMessageBox.Close)


def raise_error(err):
    error_window = ErrorWindow()
    error_window.setDetailedText(err)
    result = error_window.exec_()