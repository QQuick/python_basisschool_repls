import random

antwoord = 1

while antwoord > 0:
  a = random.randint (1, 10)
  b = random.randint (1, 10)
  
  antwoord = float (input ('Hoeveel is {} x {}? '.format (a, b)))
  
  if antwoord == a * b:
    print ('Goed')
  elif antwoord > 0:
    
    
    print ('Fout, {} x {} = {}'.format (a, b, a * b))
    