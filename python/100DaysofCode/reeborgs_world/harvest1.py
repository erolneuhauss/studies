def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_on_left_wall():
    turn_right()
    move()
    turn_right()

def turn_on_right_wall():
    turn_left()
    move()
    turn_left()

walls = 0
while not wall_in_front():
    move()
    if object_here():
        take()
    elif wall_in_front():
        walls += 1
        if walls % 2 == 0 and walls != 10:
            turn_on_left_wall()
        elif walls % 2 == 1 and walls != 10:
            turn_on_right_wall()
        else:
            done()
