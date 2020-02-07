from cs1media import *

def dist(c1, c2):
	return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5

def combine(bg, ob, x1, y1):
	w, h = ob.size()
	w2, h2 = bg.size()
	for x in range(w):
		for y in range(h):
			c = ob.get(x,y)
			if dist(c,(30,60,128))>80:
				bg.set(x1+x,y1+y,c)

	return bg

img1 = load_picture("../week1/photo/trees.jpg")
img2 = load_picture("../week1/photo/statue_noframe.jpg")

combine(img1, img2, 100, 100).show()