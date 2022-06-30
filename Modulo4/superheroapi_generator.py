import requests


def get_superhero_info(url, superhero_id):
    resposta = requests.get(url + str(superhero_id))

    superhero_info = resposta.json()

    if 'error' in superhero_info:
        print(f'Error ao recuperar as informaçoes do super heroi: {resposta.content}')
        return

    return superhero_info


def get_valor_null(valor):
    return '0' if valor == 'null' else valor
    
    #return valor if valor != 'null' else '0'
    '''
    if valor == 'null':
        return '0'

    return valor
    # 3 maneiras de fazer
    '''


def superhero_generator(inicio, final): #comparavel 1 B / (inicio=1, final=10): valor default/ (final=10, inicio=1)
    url = 'https://superheroapi.com/api/8088982984445916/' #/search/name
    index = inicio

    while index <= final:
        superhero_dict = get_superhero_info(url, index)

        atributos_dict = superhero_dict['powerstats']

        atributos = {
            'inteligencia': get_valor_null(atributos_dict['intelligence']), # ...ce', '0'], nao deu certo pq retorna string null
            'força': get_valor_null(atributos_dict['strength']),
            'velocidade': get_valor_null(atributos_dict['speed']),
            'durabilidade': get_valor_null(atributos_dict['durability']),
            'poder': get_valor_null(atributos_dict['power']),
            'combate': get_valor_null(atributos_dict['combat'])
        }

        superhero_info = {
            'id': superhero_dict['id'],
            'nome': superhero_dict['name'],
            'atributos': atributos
        } # maneira 2 de fazer
        
        yield superhero_info
        index += 1



for superhero_info in superhero_generator(1, 5): # (15)/ (5, inicio=15)
    print(f'Nome: {superhero_info["nome"]}')
    print(f'Indentificaçao: {superhero_info["id"]}')
    print('-' * 30)
    print('Atributos: ')
    atributos = superhero_info['atributos']
    print(f'Inteligencia: {atributos["inteligencia"]}')
    print(f'Força: {atributos["força"]}')
    print(f'Durabilidade: {atributos["durabilidade"]}')
    print(f'Poder: {atributos["poder"]}')
    print(f'Combate: {atributos["combate"]}')
    print('==================================================')


'''
teste 1:
url = 'https://superheroapi.com/api/8088982984445916/'
superhero_id = 1

print(get_superhero_info(url, superhero_id))
#
# nao serve aqui pois sempre retorna erro 200:
if resposta.status_code != 200:
        print(f'Nao deu bom requisitar a API {resposta.status_code} - {resposta.content}')
        return
'''