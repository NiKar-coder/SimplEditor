from PyQt6.QtWidgets import QDialog
from blurDialogUI import Ui_BlurDialog


class BlurDialog(QDialog, Ui_BlurDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.abort)
        self.exec()

    def get_value(self):
        return self.slider.value()

    def abort(self):
        self.accept()
