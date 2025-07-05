from PIL import Image, ImageQt


class Editor:
    def __init__(self):
        pass

    def open_image(self, img_name):
        img = Image.open(img_name)
        img.save(f'data/images/temp/{img_name.split("/")[-1]}')

    def diagonalReflection(self, img_name):
        img = Image.open(img_name).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        img.save(f'data/images/temp/{img_name.split("/")[-1]}')
        return ImageQt.toqpixmap(img)

    def verticalReflection(self, img_name):
        img = Image.open(img_name).transpose(Image.FLIP_LEFT_RIGHT)
        img.save(f'data/images/temp/{img_name.split("/")[-1]}')
        return ImageQt.toqpixmap(img)
