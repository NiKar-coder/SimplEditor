from PIL import Image, ImageFilter
from blurDialog import BlurDialog


class Editor:
    def __init__(self, temp_dir):
        self.temp_dir = temp_dir

    def save(self, img, img_name):
        img.save(f'{self.temp_dir}/{img_name.split("/")[-1]}')

    def open_image(self, img_name):
        img = Image.open(img_name)
        self.save(img, img_name)

    def diagonalReflection(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def verticalReflection(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.transpose(Image.FLIP_TOP_BOTTOM)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def horizontalReflection(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.transpose(Image.FLIP_LEFT_RIGHT)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def blur(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.filter(ImageFilter.BLUR)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def gaussianBlur(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        blurDialog = BlurDialog()
        value = blurDialog.get_value()
        print(value)
        img = img_.filter(ImageFilter.GaussianBlur(value))
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def findCountours(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.filter(ImageFilter.CONTOUR)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def saveFile(self, img_name, path):
        img = Image.open(img_name)
        img.save(path)

    def detail(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.filter(ImageFilter.DETAIL)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')

    def enhanceEdges(self, img_name):
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.filter(ImageFilter.EDGE_ENHANCE)
        img_.save(f'{self.temp_dir}/{img_n}_old.{img_e}')
        img.save(f'{self.temp_dir}/{img_n}.{img_e}')
