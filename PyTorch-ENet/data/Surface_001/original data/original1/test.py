from PIL import Image

def name(k):
	if (k<9):
		return "MP_SEL_SUR_00000"+str(k+1)+".png"
	elif (k<99):
		return "MP_SEL_SUR_0000"+str(k+1)+".png"
	else:
		return "MP_SEL_SUR_000"+str(k+1)+".png"


colors = []
colors.append((-1,-1,-1))
for k in range(112):
	img = Image.open(name(k))
	img_pix = img.load()
	for i in range(img.size[0]//10):
		for j in range(img.size[1]//10):
			rgb = img_pix[i*10, j*10]
			len_colors = len(colors)
			print(len(colors))
			l = 0
			for n in range(len_colors):
				if ( (colors[n][0] != rgb[0]) and (colors[n][1] != rgb[1]) and (colors[n][2] != rgb[2]) ): l = l +1
			if (l == len(colors)): colors.append(rgb)
				
print(colors)
				

