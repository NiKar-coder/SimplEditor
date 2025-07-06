from PIL import Image, ImageQt


class Editor:
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir

    def open_image(self, img_name):
        img = Image.open(img_name)
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')

    def diagonalReflection(self, img_name):
        img = Image.open(img_name).rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')

    def verticalReflection(self, img_name):
        img = Image.open(img_name).transpose(Image.FLIP_TOP_BOTTOM)
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')

    def horizontalReflection(self, img_name):
        img = Image.open(img_name).transpose(Image.FLIP_LEFT_RIGHT)
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')
