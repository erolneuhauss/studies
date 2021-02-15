from library import turn_right, turn_around, jump
def find_the_center():
    steps = 0 
    while not wall_in_front():
        move()
        steps += 1
    turn_around()

    center = int(steps / 2)
    while center > 0:
        move()
        center -= 1

if wall_in_front():
    turn_left()

find_the_center()

if right_is_clear():
    turn_right()
    find_the_center()
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