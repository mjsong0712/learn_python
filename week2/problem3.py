from cs1media import *

def adjust_light(img, factor):
	w, h = img.size()	
	img2 = create_picture(w,h,Color.white)





prisoner = load_picture("./photo/prisoner.jpg")
adjust_light(prisoner, 1.5).show()