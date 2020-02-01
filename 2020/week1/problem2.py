from cs1media import *
img = load_picture("./photo/prisoner.jpg")
w, h = img.size()

img2 = create_picture(w,h, Color.white)

for x in range(w):
	for y in range(h):
		r, g, b = img.get(x,y)
		img2.set(x, y, (r, g, b))	

img2.show()