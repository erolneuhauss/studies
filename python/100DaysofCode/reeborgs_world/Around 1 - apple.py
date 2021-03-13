def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#put()
while front_is_clear():
    move()
    if object_here() and wall_in_front():
        take()
        turn_left()
    if object_here():
        take()
    elif at_goal():
        done()
    elif wall_in_front():
        turn_left()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
