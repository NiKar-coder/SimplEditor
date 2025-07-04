from PyQt6.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene
from mainWindowUI import Ui_MainWindow
from PyQt6.QtGui import QPixmap, QImage
from editor import Editor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.img_name = 'data/images/img.jpeg'
        self.editor = Editor()
        self.setupUi(self)
        self.save_btn.clicked.connect(self.save_image)
        self.open_btn.clicked.connect(self.open_image)
        self.pixmap = QPixmap('data/images/img.jpeg')
        self.scene = QGraphicsScene()
        self.scene.addPixmap(self.pixmap)
        self.graphicsView.setScene(self.scene)
        transposing_bar = self.menubar.addMenu("Transposing")
        transposing_bar.addAction("Diagonal reflection").triggered.connect(
            self.diagonalReflection)

    def open_image(self):
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '/home/', "Image files (*.jpg *.jpeg)")

    def diagonalReflection(self):
        self.scene.addPixmap(
            QPixmap(QImage(self.editor.diagonalReflection(self.img_name))))

    def save_image(self):
        pass
