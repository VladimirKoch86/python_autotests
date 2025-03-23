import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0f16899f0e25a0fa73fde3d188a04696'
HEADER = {'Content - Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "generate",
    "photo_id": -1
}
body_name = {
    "pokemon_id": "274112",
    "name": "Marusa",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "274111"
}
response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.json()) 

