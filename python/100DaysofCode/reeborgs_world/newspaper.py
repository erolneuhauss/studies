def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def up_three_steps():
    for step in range(0, 3):
        turn_left()
        move()
        turn_right()
        move()
        move()
        
def down_three_steps():
    for step in range(0, 3):
        move()
        move()
        turn_left()
        move()
        turn_right()
        
take()
up_three_steps()
put()
turn_around()
down_three_steps()
