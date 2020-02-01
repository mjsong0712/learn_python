from cs1media import *

def reverse(img):
	w, h = img.size()
	result = create_picture(w,h,Color.white)
	for x in range(w):
		for y in range(h):
			r, g, b = img.get(x, y)
			result.set(w-1-x, y, (r, g, b))
	return result

up = load_picture("../week25/photo/up.jpg")
reverse(up).show()