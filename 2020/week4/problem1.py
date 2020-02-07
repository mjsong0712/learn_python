from cs1media import *

def combine(bg, ob, x1, y1):
	w, h = ob.size()
	w2, h2 = bg.size()
	for x in range(w):
		for y in range(h):
			bg.set(x1+x,y1+y, (ob.get(x, y)))

	return bg

img1 = load_picture("../week1/photo/trees.jpg")
img2 = load_picture("../week1/photo/statue_noframe.jpg")

combine(img1, img2, 100, 100).show()