'''
Desenvolvedor Python (PD0222)  Semana 1. Iterators e Generators  Atividade M4S1
MÓDULO 15, LIÇÃO 5

Atividade M4S1

Para a atividade desta semana, você deverá criar um interator que irá interar os dados da API (Application Interface) 
da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que 
fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca).

Para trazer esses dados, será necessário interagir com a API da FIPE disponível nesse 
endereço: https://deividfortuna.github.io/fipe/. 

Dicas:

1.Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas 
todas as marcas que a API possui. Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no 
seu código.
2.Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando a 
URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos 
que ela possui.
3.Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca 
selecionada.

Essa atividade possui um grau de dificuldade um pouco maior e será necessário pesquisar como usar a biblioteca 
de JSON (que já vem com a linguagem) e as requests (necessário instalar). Caso encontre muitas dificuldades, 
marque um horário para que um tutor possa te ajudar : )

Agora que você já está utilizando o GitHub, sugerimos manter suas atividades em um repositório.
Para enviar a atividade, por favor compartilhar o link do seu repositório e usar como título “Modulo4-Semana1”.

Digite sua resposta aqui:
"nome": "BMW",
        "codigo": "7"
'''
# FIPEAPI URL = https://deividfortuna.github.io/fipe/

'''
def get_info_marcas(url, marca_id):
    resposta = requests.get(url + str(marca_id))
    resposta_info = resposta.json()

    return resposta_info

url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
index = all

print(get_info_marcas(url, index))

'''

import requests

def get_info_fipe(url, fipe_id):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos'
    headers = {'user-agent': 'MyStudyApp'}
    resposta = requests.get(url, headers=headers)

    if resposta.status_code != 200:
        print(f'status_code: {resposta.status_code}')
        print(f'Error ao recuperar as informaçoes da marca: {resposta.content}')
        return
        

    resposta_info = resposta.json()
    fipe_info = {
        'nome': resposta_info["nome"],
        'id': resposta_info["codigo"]
        }

    return fipe_info['modelos']


class FIPEIterator():
    def __init__(self, inicio, final):
        self.index = inicio
        self.final = final
        self.url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marca}/modelos'

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.final:
            raise StopIteration
        fipe_info = get_info_fipe(self.url, self.index)
        if not fipe_info:
            raise StopIteration
        
        self.index += 1
        return fipe_info

id_marca = 7


for fipe_info in FIPEIterator(0, 100000):
    print(f'Nome: {fipe_info["nome"].capitalize()}')
    print(f'Indentificaçao: {fipe_info["id"]}')
    print('.............................................')