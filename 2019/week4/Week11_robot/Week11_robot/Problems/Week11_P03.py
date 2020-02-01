import time
from cs1robots import *

load_world("./worlds/window1.wld")

hubo = Robot(beepers = 100)

# put hubo in front of the door
hubo.turn_left()
for i in range(5):
    hubo.move()
hubo.turn_right()
hubo.move()
time.sleep(1)
hubo.set_trace("blue")
hubo.set_pause(0)


def close_windows():
    hubo.move()
    hubo.drop_beeper()
    hubo.turn_right()
    hubo.move()

    # ADD ADDITIONAL CODE HERE!
    while True:
    	if hubo.front_is_clear():
    		hubo.move()
    		if hubo.right_is_clear():
    			if hubo.on_beeper():
    				break
    			hubo.drop_beeper()
    			hubo.move()

    	else:
    		hubo.turn_left()



close_windows()