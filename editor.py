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
        tmp = img_name.split("/")[-1].split(".")
        img_n = tmp[0]
        img_e = tmp[-1]
        img_ = Image.open(img_name)
        img = img_.rotate(
            90).transpose(Image.FLIP_LEFT_RIGHT)
        self.save(img_, f'{img_n}_old.{img_e}')
        img.save(img, f'{img_n}.{img_e}')

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

    def saveFile(self, img_name, path):
        img = Image.open(img_name)
        img.save(path)

    def detail(self, img_name):
        img = Image.open(img_name).filter(ImageFilter.DETAIL)
        self.save(img, img_name)

    def enhanceEdges(self, img_name):
        img = Image.open(img_name).filter(ImageFilter.EDGE_ENHANCE)
        self.save(img, img_name)
