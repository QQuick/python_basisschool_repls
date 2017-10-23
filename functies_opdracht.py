import turtle
import random

kleuren = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white']
aantalKleuren = len (kleuren)

turtle.speed ('fastest')

def tekenBubbel (x, y, straal):
  turtle.up ()
  turtle.goto (x, y - straal)
  turtle.down ()
  turtle.color ('black', kleuren [random.randint (0, aantalKleuren - 1)])
  turtle.begin_fill ()
  turtle.circle (straal)
  turtle.end_fill ()
  
straal = 20
for x in range (-250, 250, 50):
  for y in range (-400, 400, 50):
    tekenBubbel (x + random.randint (0, 80), y, straal)
    straal += 10
    if straal > 70:
      straal = 20

turtle.done ()
