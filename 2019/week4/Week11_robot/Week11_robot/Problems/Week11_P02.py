import random
import time

from cs1robots import *
create_world()

hubo = Robot()

# put hubo in random position/direction
for i in range(random.randrange(5,10)):
	hubo.move()
hubo.turn_left()
for i in range(random.randrange(5,10)):
	hubo.move()
for i in range(random.randrange(4)):
	hubo.turn_left()
time.sleep(1)
hubo.set_pause(0.2)
hubo.set_trace("blue")


def return_back():
	while not hubo.facing_north():
		hubo.turn_left()
	hubo.turn_left()
	while hubo.front_is_clear():
		hubo.move()
	hubo.turn_left()
	while hubo.front_is_clear():
		hubo.move()

	# make hubo face west (by turning left)


	# make hubo move while front is clear


	# now, hubo reaches the left wall
	# make hubo face south (by turning left)


	# make hubo move while front is clear


	# make hubo face east (by turning left)



return_back()