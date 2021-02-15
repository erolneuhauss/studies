while not at_goal():
    if object_here():
        take()
        move()
        put()
    move()
