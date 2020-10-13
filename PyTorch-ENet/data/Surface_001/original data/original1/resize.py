from PIL import Image

def name(k):
  if (k<9):
    return "MP_SEL_SUR_00000"+str(k+1)+".png"
  elif (k<99):
    return "MP_SEL_SUR_0000"+str(k+1)+".png"
  else:
    return "MP_SEL_SUR_000"+str(k+1)+".png"

colors = [0, 55, 110, 128, 138, 198, 217, 230, 255]
for k in range(112):
	img = Image.open(name(k))
	img_resize = img.resize((480,360))
	img_r, g, b = img.split()
	pix = img_r.load()
	for i in range(480):
		for j in range(360):
			for s in range(len(colors)):
				if colors[s] == pix[i, j]:
					pix[i, j] = (s)
	img_r.save(str(k+1)+".png")

