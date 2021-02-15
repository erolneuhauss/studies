def turn_right():
    for step in range(0,3):
        turn_left()

def hurdle_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

if wall_in_front():
    hurdle_jump()
while not at_goal() and front_is_clear():
    move()
    while wall_in_front():
        hurdle_jump()
        if at_goal():
            done()
        elif front_is_clear():
            move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
