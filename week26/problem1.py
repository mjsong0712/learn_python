from cs1media import *
def luminance(p):
	r, g, b = p
	return int(0.299*r + 0.587*g + 0.114*b)

def luminance2(p):
	r, g, b = p
	return int((r+g+b)/3.0)

def bw(img):
	w,h = img.size()
	for i in range(h):
		for j in range(w):
			v = luminance(img.get(j, i))
			img.set(j, i, (v, v, v))
	return img

img = load_picture("../week25/photo/trees.jpg")
bw(img).save_as("./1.png")