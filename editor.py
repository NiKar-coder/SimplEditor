from PIL import Image
import os.path
from PIL.ImageQt import ImageQt


class Editor:
    def __init__(self):
        pass

    def diagonalReflection(self, img_name):
        img = Image.open(os.path.join(os.path.dirname(os.path.abspath(
            __file__)),
            img_name)).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        return ImageQt(img)
