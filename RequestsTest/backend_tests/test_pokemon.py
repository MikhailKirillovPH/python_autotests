import requests
import pytest

URL = 'https://api.pokemonbattle.me'

def test_pokemon():
    '''
    KTI-1. Gat trainers
    '''
    response = requests.get(url=f'{URL}/v2/trainers', params={"trainer_id": 3553})
    assert response.status_code == 200, 'Error'


def test_pokemon_by_id():
    '''
    KTI-2. Gat trainers ID
    '''
    response = requests.get(url=f'{URL}/v2/trainers', params={"trainer_id": 3553})
    assert response.status_code == 200, 'Error'
    assert response.json()["trainer_name"] == "Cookie"