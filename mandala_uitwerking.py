# Inspired by "Georgia's Spirals"

import turtle

turtle.speed ('fastest')

turtle.begin_fill ()
turtle.color ('black', 'black')
turtle.goto (0, -250)
turtle.circle (250)
turtle.goto (0, 0)
turtle.end_fill ()

for lijst in [
    ['green', 1, 25, 82, 6],       
    ['red', 1, 30, 84, 8], 
    ['white', 2, 50, 98, 5],
    ['yellow', 2, 50, 70, 5],
    ['blue', 2, 70, 97, 5],
    ['orange', 2, 69, 87, 17],
    ['pink', 3, 60, 102, 17],  
]:
    turtle.color (lijst [0])
    turtle.pensize (lijst [1])
    for teller in range (10):
        for straal in range (lijst [2], lijst [3], lijst [4]):
            turtle.circle (straal)
        turtle.right (36)
        
turtle.done ()
