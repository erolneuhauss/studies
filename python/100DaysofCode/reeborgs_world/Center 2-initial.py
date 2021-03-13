def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()

if wall_in_front():
    turn_left()
while front_is_clear:
    move()
    steps += 1
    if wall_in_front():
        turn_around()
        halfway = int(steps / 2)
        for center in range(0, halfway):
            move()
        if right_is_clear():
            turn_right()
            steps = 0
            while front_is_clear:
                move()
                steps += 1
                if wall_in_front():
                    turn_around()
                    halfway = int(steps / 2)
                    for center in range(0, halfway):
                        move()
                    put()
                    done()
        put()
        done()
