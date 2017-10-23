import turtle

turtle.speed (10)

turtle.up ()
turtle.goto (-250, 0)

startPositie = turtle.pos ()

turtle.down ()
turtle.color ('red', 'yellow')
turtle.begin_fill ()
while True:
    turtle.forward (500)
    turtle.right (170)
    turtle.circle (20)
    turtle.circle (-10)
    if turtle.distance (startPositie) < 1:
        break
turtle.end_fill ()
turtle.done ()
