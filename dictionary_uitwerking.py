hoofdsteden = {}

hoofdsteden ['Nederland'] = 'Amsterdam'
hoofdsteden ['Frankrijk'] = 'Parijs'
hoofdsteden ['Duitsland'] = 'Berlijn'
hoofdsteden ['Engeland'] = 'Londen'

for teller in range (3):
  for land in hoofdsteden.keys ():
    hoofdstad = ''
    while hoofdstad != hoofdsteden [land]:
      hoofdstad = input ('Wat is de hoofdstad van {}? '.format (land))
    