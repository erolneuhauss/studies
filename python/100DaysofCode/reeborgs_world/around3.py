# works with around1 and around2 as well
from library import turn_right
from library import turn_around
loops = 0
put()
while True:
    loops += 1
    if loops > 2 and object_here():
        done()
    if wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
