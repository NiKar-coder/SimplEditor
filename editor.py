from PIL import Image
# import os.path
from PIL import ImageQt


class Editor:
    def __init__(self):
        pass

    def diagonalReflection(self, img_name):
        return ImageQt.toqpixmap(Image.open(img_name).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT))
