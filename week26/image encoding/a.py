from cs1media import *
def encode(background, cipher):
    w, h = background.size()
    result = create_picture(w, h, Color.white)
    
    for x in range(w):
        for y in range(h):
            r, g, b = background.get(x,y)
            if cipher.get(x,y)[0]>=128:
            	r = (r/2)*2
            else:
            	r = (r/2)*2-1
            result.set(x, y, (r, g, b))
    return result

background = load_picture('./background.png')
cipher = load_picture("./cipher.png")
encoded = encode(background, cipher)
encoded.save_as("./encoded.png")