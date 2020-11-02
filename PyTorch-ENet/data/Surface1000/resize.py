from PIL import Image

object = "test/"

def name(k):
  if (k<9):
    return "MP_SEL_SUR_00000"+str(k+1)+"."
  elif (k<99):
    return "MP_SEL_SUR_0000"+str(k+1)+"."
  elif (k<999):
    return "MP_SEL_SUR_000"+str(k+1)+"."
  else:
    return "MP_SEL_SUR_00"+str(k+1)+"."

hole = {113, 134, 159, 171, 186, 216, 220, 239, 243, 259, 286, 290, 302, 322, 366, 486, 500, 551, 743, 840, 969, 982, 1095, 1103, 1109, 1143, 1169, 1171, 1174, 1188, 1216, 1283, 1315, 1366, 1372, 1407, 1438}

for k in range(1201, 1439):
	if ((k+1) in hole):
		continue
	img = Image.open(object+"original/"+name(k)+"jpg")
	img = img.resize((480,360))
	img.save(object+name(k)+"png")
