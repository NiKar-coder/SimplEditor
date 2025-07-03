from PIL import Image
import os.path


def mirror():
    Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.jpeg')).rotate(
        90).transpose(Image.FLIP_LEFT_RIGHT).save("res.jpg")


mirror()
