import json


def ler_dados_salvos():
    arquivo = open('estoque.json', 'r')
    dados_json = arquivo.read()
    arquivo.close

    dados_python = json.loads(dados_json)
    print('lendo os itens no banco de dados do estoque')
    return dados_python


def salvar_dados_disco(itens_estoque):
    itens_estoque_json = json.dumps(itens_estoque)

    arquivo = open('estoque.json', 'w')
    arquivo.write(itens_estoque_json)

    arquivo.close()
    print('salvando itens do estoque no disco')