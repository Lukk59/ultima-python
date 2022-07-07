import requests
import json
url = "https://parallelum.com.br/fipe/api/v1/"
params = {"carros":"marcas"}

response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    print(response.text)
else:
    print(f'Error: {response.status_code}')
'''
def get_info_marcas(url, index):
    resposta = requests.get(url + str(index))
    resposta_info = resposta.json()

    return resposta_info

url = 'https://parallelum.com.br/fipe/api/v1/'
index = 'carros/marcas'

print(get_info_marcas(url, index))
'''
'''
def get_info_marcas(url, marca_id):
    resposta = requests.get(url + str(marca_id))
    resposta_info = resposta.json()

    return resposta_info

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
index = all

print(get_info_marcas(url, index))

'''
'''
adicionar as seguintes linhas no arquivo .htaccess:
<IfModule mod_security.c>
   SecFilterEngine Off
   SecFilterScanPOST desativado
</IfModule>
'''
'''
import requests

def get_info_fipe(url, fipe_id):
    resposta = requests.get(url + str(fipe_id))

    if resposta.status_code != 200:
        print(f'status_code: {resposta.status_code}')
        print(f'Error ao recuperar as informaçoes da marca: {resposta.content}')
        return

    resposta_info = resposta.json()
    tipos = resposta_info['types']
    fipe_info = {
        'nome': resposta_info['nome'],
        'id': resposta_info['codigo']
        }

    return fipe_info


class FIPEIterator():
    def __init__(self, inicio, final):
        self.index = inicio
        self.final = final
        self.url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/7/modelos'

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > self.final:
            raise StopIteration
        fipe_info = get_info_fipe(self.url, self.index)
        if not fipe_info:
            raise StopIteration
        
        self.index += 1
        return fipe_info


for fipe_info in FIPEIterator(1, 27):
    print(f'Nome: {fipe_info["nome"].capitalize()}')
    print(f'Indentificaçao: {fipe_info["id"]}')
    print('.............................................')
'''