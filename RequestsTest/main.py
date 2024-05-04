import requests

URL = 'https://api.pokemonbattle.me'
HEADER = {
    'Content-Type': 'application/JSON',
    'trainer_token': '1cc21edff40b6c42cc8f193d4000a8d9'
    }

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/v2/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body = {
    "pokemon_id": "24221",
    "name": "Cookies Pokemon3",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url=f'{URL}/v2/pokemons', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body = {
    "pokemon_id": "24221"
}

response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

