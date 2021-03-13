def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left() 

    
while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and not right_is_clear():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
