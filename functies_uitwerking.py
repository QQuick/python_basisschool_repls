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
  
def tekenBlokje (x, y, zijde):
  turtle.up ()
  turtle.goto (x - zijde / 2, y - zijde / 2)
  turtle.down ()
  turtle.color ('black', kleuren [random.randint (0, aantalKleuren - 1)])
  turtle.begin_fill ()
  for teller in range (4):
    turtle.forward (zijde)
    turtle.right (90)
  turtle.end_fill ()
  
def tekenDriehoek (x, y, zijde):
  turtle.up ()
  turtle.goto (x - zijde / 2, y - zijde / 2)
  turtle.down ()
  turtle.color ('black', kleuren [random.randint (0, aantalKleuren - 1)])
  turtle.begin_fill ()
  for teller in range (3):
    turtle.forward (zijde)
    turtle.right (120)
  turtle.end_fill ()
  
grootte = 40
for x in range (-250, 250, 100):
  for y in range (-400, 400, 80):
    tekenBlokje (x + random.randint (0, 200), y, grootte)
    tekenDriehoek (x + random.randint (0, 200), y, grootte)
    tekenBubbel (x + random.randint (0, 100), y, grootte / 2)
    tekenBubbel (x + random.randint (0, 100), y, grootte / 2)
    
    grootte += 20
    if grootte > 140:
      grootte = 40
      

turtle.done ()
