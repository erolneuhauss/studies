from library import turn_right, turn_around, jump
# inital solution
steps = 0
while front_is_clear():
    move()
    steps += 1
    if wall_in_front():
        turn_around()
        center = int(steps / 2)
        print(center)
        for center in range(0, center):
            move()
        put()
        done()
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
