import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0f16899f0e25a0fa73fde3d188a04696'
HEADER = {'Content - Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '24498'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_response():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Vladimir K' 