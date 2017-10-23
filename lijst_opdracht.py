dagmenu = [
  'tomatensoep',
  'aardappels',
  'bloemkool',
  'karbonade',
  'yoghurt'
]

print ('Dagmenu')
print ('------')
teller = 1
for gerecht in dagmenu:
  print ('{}: {}'.format (teller, gerecht))
  teller = teller + 1
print ('')

oudeGroente = dagmenu [2]
dagmenu [2] = 'spinazie'
print ('Aangepast dagmenu, {} in plaats van {}!'.format (dagmenu [2], oudeGroente))
print ('------')
teller = 1
for gerecht in dagmenu:
  print ('{}: {}'.format (teller, gerecht))
  teller = teller + 1
print ('')
