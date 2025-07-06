from PIL import Image, ImageFilter


class Editor:
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir

    def save(self, img, img_name):
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')

    def open_image(self, img_name):
        img = Image.open(img_name)
        self.save(img, img_name)

    def diagonalReflection(self, img_name):
        img = Image.open(img_name).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        self.save(img, img_name)

    def verticalReflection(self, img_name):
        img = Image.open(img_name).transpose(Image.FLIP_TOP_BOTTOM)
        self.save(img, img_name)

    def horizontalReflection(self, img_name):
        img = Image.open(img_name).transpose(Image.FLIP_LEFT_RIGHT)
        self.save(img, img_name)

    def blur(self, img_name):
        img = Image.open(img_name).filter(ImageFilter.BLUR)
        self.save(img, img_name)

    def findCountours(self, img_name):
        img = Image.open(img_name).filter(ImageFilter.CONTOUR)
        self.save(img, img_name)
