from PIL import Image

object = "testannot/"

def name(k):
  if (k<9):
    return "MP_SEL_SUR_00000"+str(k+1)+".png"
  elif (k<99):
    return "MP_SEL_SUR_0000"+str(k+1)+".png"
  elif (k<999):
    return "MP_SEL_SUR_000"+str(k+1)+".png"
  else:
    return "MP_SEL_SUR_00"+str(k+1)+".png"

colors = [0, 55, 110, 128, 138, 198, 217, 230, 255]
img_stand = Image.open("0001TP_008550.png")

hole = {113, 134, 159, 171, 186, 216, 220, 239, 243, 259, 286, 290, 302, 322, 366, 486, 500, 551, 743, 840, 969, 982, 1095, 1103, 1109, 1143, 1169, 1171, 1174, 1188, 1216, 1283, 1315, 1366, 1372, 1407, 1438}

for k in range(1200, 1439):
	if ((k+1) in hole):
		continue	
	img = Image.open(object+"original/"+name(k))
	img_resize = img.resize((480,360))
	img_r, g, b = img_resize.split()
	pix = img_r.load()
	pix_stand = img_stand.load()
	for i in range(480):
		for j in range(360):
			for s in range(len(colors)):
				if colors[s] == pix[i, j]:
					pix_stand[i, j] = (s)
	img_stand.save(object+name(k))

