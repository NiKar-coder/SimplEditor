import tempfile
import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow
import qdarktheme
from PyQt6.QtGui import QIcon


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sandbox = tempfile.mkdtemp()
print(sandbox)

if __name__ == '__main__':
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark", corner_shape="sharp",
                           custom_colors={"primary": "#FFFFFF"})
    app.setWindowIcon(QIcon('data/icons/icon.png'))
    ex = MainWindow(sandbox)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
