# image transformations

from PIL import Image
from PIL import ImageFilter

pic1 = Image.open("pic1.jpg") # open object and convert to a pillow object
blur = pic1.filter(ImageFilter.BLUR)
details = pic1.filter(ImageFilter.DETAIL)
edges = pic1.filter(ImageFilter.FIND_EDGES)



blur.show()
details.show()
edges.show()
