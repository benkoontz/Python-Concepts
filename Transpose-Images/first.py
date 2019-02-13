# image transformations

from PIL import Image

pic1 = Image.open("pic1.jpg") # open object and convert to a pillow object
square_img = pic1.resize((250,250))
flip = pic1.transpose(Image.FLIP_LEFT_RIGHT)
spin = pic1.transpose(Image.ROTATE_90)

pic1.show()
square_img.show()
flip.show()
spin.show()
