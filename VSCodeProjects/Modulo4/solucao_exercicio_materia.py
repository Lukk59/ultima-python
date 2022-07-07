import requests


def get_modelos_veiculos(id_marca):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos'
    headers = {'user-agent': 'MyStudyApp'}
    # Necessário criar esse header para fazer a requisição adequada na API
    resposta = requests.get(url, headers=headers)

    if resposta.status_code != 200:
        print('Houve um erro na requisição!!')
        return []

    resposta_json = resposta.json()
    return resposta_json['modelos']



class ListaFipe():
    def __init__(self, id_marca):
        self.id_marca = id_marca
        self.indice = 0
        self.modelos = []

    def __iter__(self):
        self.modelos = get_modelos_veiculos(self.id_marca)
        return self

    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration

        modelo = self.modelos[self.indice]
        self.indice += 1
        return modelo



id_marca = 22 # Pode ser qualquer ID

lista_fipe = ListaFipe(id_marca)

for veiculo in lista_fipe:
    print(f'Nome: {veiculo["nome"]}')
    print(f'ID: {veiculo["codigo"]}')
    print('==========================')
