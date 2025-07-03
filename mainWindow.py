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
        self.diagonalReflection_btn.clicked.connect(self.diagonalReflection)
        self.open_btn.clicked.connect(self.open_image)
        self.pixmap = QPixmap('data/images/img.jpeg')
        self.scene = QGraphicsScene()
        self.scene.addPixmap(self.pixmap)
        self.graphicsView.setScene(self.scene)

    def open_image(self):
        self.img_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '/home/', "Image files (*.jpg *.jpeg)")

    def diagonalReflection(self):
        self.scene.addPixmap(
            QPixmap(QImage(self.editor.diagonalReflection(self.img_name))))

    def save_image(self):
        pass
