tafelNr = float (input ('Welke tafel? '))
print ('')

for regelNr in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  print ('{} x {} = {}'.format (regelNr, tafelNr, regelNr * tafelNr))
  
print ('')

for regelNr in range (1, 11):
  print ('{} x {} = {}'.format (regelNr, tafelNr, regelNr * tafelNr))

print ('')

for regelNr in range (1, 11, 2):
  print ('{} x {} = {}'.format (regelNr, tafelNr, regelNr * tafelNr))

print ('')