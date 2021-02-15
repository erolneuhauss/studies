from library import turn_right, turn_around, jump

loops = 0
put()
while True:
    loops += 1
    if loops > 10 and object_here():
        done()
    elif wall_in_front():
        turn_left()
    elif front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()