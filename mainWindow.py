from PyQt6.QtWidgets import QMainWindow, QFileDialog, QGraphicsScene
from mainWindowUI import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from editor import Editor
import shutil


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, temp_dir):
        super().__init__()
        self.temp_dir = temp_dir
        self.img_name = None
        self.editor = Editor(self.temp_dir)
        self.setupUi(self)
        self.showMaximized()
        self.save_btn.clicked.connect(self.save_image)
        self.open_btn.clicked.connect(self.open_image)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        transposing_bar = self.menubar.addMenu("Transposing")
        filters_bar = self.menubar.addMenu("Filters")
        filters_bar.addAction("Blur").triggered.connect(self.blur)
        filters_bar.addAction("Detail").triggered.connect(self.detail)
        filters_bar.addAction("Enhance edges").triggered.connect(
            self.enhanceEdges)
        filters_bar.addAction("Find contours").triggered.connect(
            self.findContours)
        transposing_bar.addAction("Vertical reflection").triggered.connect(
            self.verticalReflection)
        transposing_bar.addAction("Horizontal reflection").triggered.connect(
            self.horizontalReflection)
        transposing_bar.addAction("Diagonal reflection").triggered.connect(
            self.diagonalReflection)

    def open_image(self):
        try:
            self.img_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                        '/home/', "Image files (*.jpg *.jpeg *.png)")[0]
            self.scene.clear()
            self.editor.open_image(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
            self.img_name = f"{self.temp_dir}/{self.img_name.split('/')[-1]}"
        except Exception:
            pass

    def enhanceEdges(self):
        self.scene.clear()
        try:
            self.editor.enhanceEdges(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def blur(self):
        self.scene.clear()
        try:
            self.editor.blur(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def findContours(self):
        self.scene.clear()
        try:
            self.editor.findCountours(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def diagonalReflection(self):
        self.scene.clear()
        try:
            self.editor.diagonalReflection(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def verticalReflection(self):
        self.scene.clear()
        try:
            self.editor.verticalReflection(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def horizontalReflection(self):
        self.scene.clear()
        try:
            self.editor.horizontalReflection(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass

    def closeEvent(self, event):
        shutil.rmtree(self.temp_dir)

    def save_image(self):
        try:
            print(self.img_name)
            path_, _ = QFileDialog.getSaveFileName(self, 'Save file',
                                                   f'/home/{self.img_name.split("/")[-1]}',
                                                   "Image files (*.jpg *.jpeg *.png)")
            self.editor.saveFile(self.img_name, path_)

        except Exception:
            pass

    def detail(self):
        self.scene.clear()
        try:
            self.editor.detail(self.img_name)
            self.scene.addPixmap(
                QPixmap(self.img_name))
        except Exception:
            pass
