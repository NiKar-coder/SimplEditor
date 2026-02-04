import tempfile
import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow
import qdarktheme
from PyQt6.QtGui import QPalette


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sandbox = tempfile.mkdtemp()
print(sandbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dark_palette = qdarktheme.load_palette()
    palette = app.palette()
    palette.setColor(QPalette.ColorRole.Link, dark_palette.link().color())
    app.setPalette(palette)
    ex = MainWindow(sandbox)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
