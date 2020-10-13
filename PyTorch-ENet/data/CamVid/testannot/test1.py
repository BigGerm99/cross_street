from PIL import Image

img = Image.open("0001TP_008580.png")
rgb_img = img.convert('RGB')
pix = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        print(rgb_img.getpixel((i,j)))
