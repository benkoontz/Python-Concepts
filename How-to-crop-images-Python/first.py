# how to crop images

from PIL import Image # use Pillow module

img = Image.open("pic1.jpg") # open object and convert to a pillow object

area = (100,100, 300, 500) # start at 100 over and 100 down, make image 300 wide by 375 tall
cropped_img = img.crop(area)

img.show() # open the image to view
cropped_img.show()
