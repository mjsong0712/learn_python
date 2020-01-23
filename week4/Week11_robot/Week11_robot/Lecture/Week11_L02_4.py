from cs1robots import *
load_world("./worlds/wall2_2.wld")

hubo = Robot(beepers = 1)
hubo.set_trace("blue")
hubo.set_pause(0.1)

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        hubo.turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:    # wall reached
        hubo.turn_left()
hubo.pick_beeper()
