leeftijd = float (input ('Hoe oud ben je?'))

# Keuze uit meerdere mogelijkheden

if leeftijd < 20:
  print ('Als je {} jaar bent, zit je waarschijnlijk nog op school.'.format (leeftijd))
elif leeftijd < 30:
  print ('Met {} jaar zit je niet meer op school, maar heb je misschien ook nog geen kinderen.'.format (leeftijd))
elif leeftijd < 50:
  print ('Als je {} bent, heb je misschien al een partner en eventueel ook kinderen.'.format (leeftijd))
elif leeftijd < 60:
  print ('Als je kinderen hebt en je bent {} zijn ze waarschijnlijk al volwassen.'.format (leeftijd))
else:
  print ('Als je {} bent, heb je misschien al kleinkinderen.'.format (leeftijd))
  
# Keuze binnen andere keuze
  
if leeftijd < 50:
  print ('Abraham nog niet gezien.')
  if leeftijd < 25:
    print ('Voornamelijk aan het leren.')
  else:
    print ('Voornamelijk aan het werk.')
else:
  print ('Abraham al wel gezien.')
  if leeftijd < 65:
    print ('Nog steeds aan het werk.')
  else:
    print ('Misschien met pensioen.')
  