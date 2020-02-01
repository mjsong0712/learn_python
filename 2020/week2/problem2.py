from cs1media import *
def bw(img):
	w,h = img.size()
	result = create_picture(w,h, Color.white)
	for i in range(h):
		for j in range(w):
			
			r, g, b = img.get(j, i)
			if r + g + b >= 128*3:
				v = 255
			else:
				v = 0	
			result.set(j, i, (v, v, v))
	return result


img = load_picture("../week25/photo/trees.jpg")
bw(img).show()