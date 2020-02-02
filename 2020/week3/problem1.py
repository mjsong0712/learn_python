from cs1media import *

def invert(img):
	w, h = img.size()
	result = create_picture(w,h, Color.white)
	for x in range(w):
		for y in range(h):
			r, g, b = img.get(x,y)
			result.set(x, y,(255-r,255-g,255-b))
	return result

img = load_picture("../week1/photo/trees.jpg")
invert(img).show()