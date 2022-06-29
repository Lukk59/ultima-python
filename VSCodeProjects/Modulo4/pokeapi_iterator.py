# pokeAPI URL = https://pokeapi.co/

import requests


def get_info_pokemon(url, pokemon_id):
    resposta = requests.get(url + str(pokemon_id))
    if resposta.status_code != 200:
        print(f'status_code: {resposta.status_code}')
        return

    resposta_info = resposta.json()
    tipos = resposta_info['types']
    pokemon_info = {
        'nome': resposta_info['name'],
        'tipo': ', '.join([tipo['type']['name'] for tipo in tipos]),
        'numero': resposta_info['id']
        }

    return pokemon_info


class PokemonIterator():
    def __init__(self, inicio, final):
        self.index = inicio
        self.final = final
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > self.final:
            raise StopIteration
        pokemon_info = get_info_pokemon(self.url, self.index)
        if not pokemon_info:
            raise StopIteration
        
        self.index += 1
        return pokemon_info


'''
def __init__(self):
    pass
def __next__(self):
    raise StopIteration

url = 'https://pokeapi.co/api/v2/pokemon/'
index = 1 #1 bulbassaur e 25 pikachu

print(get_info_pokemon(url, index))
905 pok na lista
'''

for pokemon_info in PokemonIterator(1, 27):
    print(f'Nome: {pokemon_info["nome"].capitalize()}')
    print(f'Tipo: {pokemon_info["tipo"]}')
    print(f'Numero: {pokemon_info["numero"]}')
    print('.............................................')