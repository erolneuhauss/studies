def hurdle_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# inefficent way of doing things
while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_right()
        move()
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        move()

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

# efficent approach  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
