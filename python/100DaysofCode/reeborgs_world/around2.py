def turn_right():
    for step in range(0,3):
        turn_left()

put()
while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
    elif object_here():
        done()
