from library import turn_right
from library import turn_around

window = 6
while window != -5:
    move()
    window -=1
    if window == 0:
        build_wall()
        turn_around()
