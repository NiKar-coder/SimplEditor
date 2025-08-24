import tempfile
import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow
import qdarktheme
from file import File
from PyQt6 import QtGui


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sandbox = tempfile.mkdtemp()
print(sandbox)

if __name__ == '__main__':
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark", corner_shape="sharp",
                           custom_colors={"primary": "#FFFFFF"})
    app.setWindowIcon(QtGui.QIcon(File('data/icons/icon.png').resource_path()))
    ex = MainWindow(sandbox)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
