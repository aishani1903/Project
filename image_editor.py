#image editor 
from PIL import Image, ImageEnhance
import os


img1 = Image.open('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.jpg')
#To save the image as png
img1.save('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.png')

#To resize the image
max_size = (250,250)
img1.thumbnail(max_size)
img1.save('resized_doggo.jpg')
img1.show()

#to save multiple .jpg images as .png
for item in os.listdir():
   if item.endswith(".jpg"):
      img1 = Image.open(item)
      fname, extension = os.path.split(item)
      img1.save(f'{fname}.png')
      img1.save()

#sharpness
img1 = Image.open('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(8).save('C:\\Users\\Aishani Anavkar\\Desktop\\doggo_sharped.jpg')
# 0 : blurry
# 1 : original image
# 2 : img with increased sharpness


#color
img1 = Image.open('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(2).save('C:\\Users\\Aishani Anavkar\\Desktop\\doggo_sharped.jpg')
# 0 : B/W
# 1 : Original
# 2 : Increased

#brightness
img1 = Image.open('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(3).save('C:\\Users\\Aishani Anavkar\\Desktop\\doggo_sharped.jpg')

#sharpness
img1 = Image.open('C:\\Users\\Aishani Anavkar\\Desktop\\doggo.jpg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(2).save('C:\\Users\\Aishani Anavkar\\Desktop\\doggo_sharped.jpg')





