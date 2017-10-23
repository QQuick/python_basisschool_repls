hoofdsteden = {}

hoofdsteden ['Nederland'] = 'Amsterdam'
hoofdsteden ['Frankrijk'] = 'Parijs'
hoofdsteden ['Duitsland'] = 'Berlijn'
hoofdsteden ['Engeland'] = 'Londen'

print ('De volgende landen zijn in dit programma bekend:')
print ('')
for land in hoofdsteden.keys ():
  print (land)
print ('')

while True:
  land = input  ('Van welk land wil je de hoofdstad weten? ')
  hoofdstad = hoofdsteden [land]
  print ('De hoofdstad van {} is {}.'.format (land, hoofdstad))
  print ('')
