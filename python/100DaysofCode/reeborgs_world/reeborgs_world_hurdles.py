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
# first solution which fits all hurdles
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
# efficient solution
while not at_goal():
    if wall_in_front():
        hurdle_jump()
    else:
        move()

# around1 - variable solution
put()
while front_is_clear():
    move()
    if wall_in_front():
        turn_left()
    elif object_here():
        done()

# around1 - apple
while front_is_clear():
    move()
    if object_here() and wall_in_front():
        take()
        turn_left()
    elif object_here():
        take()
    elif wall_in_front() and at_goal():
        done()
    elif wall_in_front():
        turn_left()

# center 1
steps = 0
while not wall_in_front():
    move()
    steps += 1
    if wall_in_front():
        print(steps)
        center = int(steps / 2)
        print(center)
        turn_left()
        turn_left()
        for step in range(0, center):
            move()
        put()
        done()
