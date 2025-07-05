from PyQt6.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene
from mainWindowUI import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from editor import Editor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.img_name = None
        self.editor = Editor()
        self.setupUi(self)
        self.showMaximized()
        self.save_btn.clicked.connect(self.save_image)
        self.open_btn.clicked.connect(self.open_image)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        transposing_bar = self.menubar.addMenu("Transposing")
        transposing_bar.addAction("Diagonal reflection").triggered.connect(
            self.diagonalReflection)
        transposing_bar.addAction("Vertical reflection").triggered.connect(
            self.verticalReflection)

    def open_image(self):
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '/home/', "Image files (*.jpg *.jpeg)")[0]
        self.scene.clear()
        self.scene.addPixmap(
            QPixmap(self.img_name))

    def diagonalReflection(self):
        self.scene.clear()
        try:
            self.scene.addPixmap(
                self.editor.diagonalReflection(self.img_name))
        except Exception:
            pass

    def verticalReflection(self):
        self.scene.clear()
        try:
            self.scene.addPixmap(
                self.editor.verticalReflection(self.img_name))
        except Exception:
            pass

    def save_image(self):
        pass
