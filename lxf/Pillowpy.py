
# Pillow, PIL, python image library

# pip install pillow

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017785454949568


# operating the images

from PIL import Image

# open, close, stretch, save

im = Image.open('./thejpg1.jpg')

w, h = im.size
print ('Original image size: %s x %s' % (w, h))

print (type(w))

im.thumbnail((w//2, h//2))

print ('Resized image size: %s x %s' % (w, h))

im.save('thumbnail.jpg', 'jpeg')



# bluring

from PIL import Image, ImageFilter

im = Image.open('./thejpg1.jpg')

for i in range(10):
    im = im.filter(ImageFilter.BLUR)
    im2 = im
im2.save ('blur.jpg', 'jpeg')
# im2.show()

# other stuff

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar(): # random character
    return chr(random.randint(65,90))

def rndColor(): # random color 1 (R,G,B)
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def rndColor2(): # random color 2 (R,G,B)
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))


# 240 X 60 resolution
wdt = 60 * 4
hgt = 60
image = Image.new('RGB', (wdt, hgt), (255, 255, 255))


font = ImageFont.truetype('/Library/Fonts/arial.ttf', 36) # creating Font object
draw = ImageDraw.Draw(image) # creating Draw object

for x in range (wdt): # filling all pixles
    for y in range(hgt):
        draw.point((x,y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image.show()
image.save('code.jpg', 'jpeg')


"""
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/Library/Fonts/arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image.show()
"""