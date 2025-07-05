from PIL import Image, ImageQt


class Editor:
    def __init__(self):
        pass

    def diagonalReflection(self, img_name):
        return ImageQt.toqpixmap(Image.open(img_name).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT))

    def verticalReflection(self, img_name):
        return ImageQt.toqpixmap(Image.open(img_name)
                                 .transpose(Image.FLIP_LEFT_RIGHT))
