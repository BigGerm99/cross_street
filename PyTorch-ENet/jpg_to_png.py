from PIL import Image

img = Image.open("frame1017.jpg")
cropped_img = img.crop((0,320,640,480))
resize_img = cropped_img.resize((480,360))
resize_img.save("frame1017.png")
