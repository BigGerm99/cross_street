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
	print(k)
	img = Image.open(str(k+1)+".png")
	pix = img.load()
	for i in range(480):
		for j in range(360):
			for s in range(len(colors)):
				if ( (pix[i, j]>9) or (pix[i, j] <0)): print("false")

