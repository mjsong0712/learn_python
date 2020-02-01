from cs1media import *

def adjust_light(img, factor):
	w, h = img.size()	
	result = create_picture(w,h,Color.white)
	for x in range(w):
		for y in range(h):
			r, g, b = img.get(x,y)
			r = int(r * factor)
			if r > 255: r = 255
			g = int(g * factor)
			if g > 255: g = 255
			b = int(b * factor)
			if b > 255: b = 255
			result.set(x, y, (r, g, b))
	return result

prisoner = load_picture("../week25/photo/prisoner.jpg")
adjust_light(prisoner, 0.6).show()