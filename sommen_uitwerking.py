import random

antwoord = 1
a = 1
b = 1

while antwoord > 0:
  if antwoord == a * b:
    a = random.randint (1, 10)
    b = random.randint (1, 10)
  
  antwoord = float (input ('Hoeveel is {} x {}? '.format (a, b)))
  
  if antwoord == a * b:
    print ('Goed')
  elif antwoord > 0:
    print ('Fout, probeer het nog eens...')
    