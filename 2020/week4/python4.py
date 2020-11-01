from cs1media import *###################################################################################################################################################







def mo(img):
	w, h = img.size()
	for x in range(w/10):
		for y in range(h/10):
			r2,g2,b2 = 0, 0, 0
			for i in range(10):
				for j in range(10):
					r,g,b = img.get(x*10+i, y*10+j)
					r2 += r
					g2 += g
					b2 += b
			r2 /= 100
			b2 /= 100
			g2 /= 100
			for i in range(10):
				for j in range(10):
					img.set(x*10+i, y*10+j, (r2, g2, b2))
	return img
	
trees = load_picture("../week1/photo/trees.jpg")
mo(trees).show()