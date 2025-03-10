import requests, json

class Pokemon:

	def __init__(self):
		
		self.base_url = 'https://pokeapi.co/api/v2/pokemon/'
	
	def _get(self, pokemon_name):

		request_url = self.base_url + pokemon_name
		r = requests.get(request_url)
		
		if r.ok:
			print(r.json())
			return r.json()
		else:
			print('Pokemon name invalid')

	def get_pokemon(self, pokemon):
		data = self._get(pokemon.lower())
		height = data['height']
		weight = data['weight']
		print(f'{pokemon.title()} is {height} feet tall and {weight} lbs.')
		print(f'Height: {height} ft')
		print(f'Weight: {weight} lbs')


pokedex = Pokemon()

pokedex.get_pokemon('pikachu')