from persistencia import ler_dados_salvos, salvar_dados_disco

itens_estoque = []

def adicionar_item_estoque():
    nome = input('nome do item: ')
    descriçao = input('descriçao do item: ')
    quantidade = int(input('quantidade de itens: '))

    item = {
        'nome': nome,
        'descriçao': descriçao,
        'quantidade': quantidade
    }

    itens_estoque.append(item)
    print(f"o item {nome} foi adicionado ao estoque")
    print()


def listar_itens_estoque():
    if len(itens_estoque) == 0:
        print('nao ha itens para serem listados')
        print()
        return

    print('#########################')
    for item in itens_estoque:
        print(f'nome: {item["nome"]}')
        print(f'quantidade: {item["quantidade"]}')
        print('###########################')

    print()

if __name__ == "__main__":
    itens_estoque = ler_dados_salvos()
    print('bem vindo ao sistema de estoque ultima')

    opcao = 0
    while opcao != 3:
        print('menu de opçoes:')
        print('===============')
        print('1. adicionar item')
        print('2. listar itens do estoque')
        print('3. sair')

        opcao = int(input('selecione uma opçao: '))

        if opcao == 1:
            adicionar_item_estoque()
        elif opcao == 2:
            listar_itens_estoque()
        elif opcao == 3:
            print('obrigado por usar nosso sistema')
            salvar_dados_disco(itens_estoque)
        else:
            print('opçao invalida. tente novamente\n')