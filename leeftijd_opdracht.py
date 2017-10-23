leeftijd = float (input ('Hoe oud ben je?'))

if leeftijd < 13:
  print ('Als je {} bent, zit je nog niet op de middelbare school'.format (leeftijd))
elif leeftijd < 19:
  print ('Met {} jaar zit je waarschijnlijk op de middelbare school'.format (leeftijd))
else:
  print ('Met {} jaar ben je al een tijdje volwassen'.format (leeftijd))
