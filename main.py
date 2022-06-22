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
    print(f"o item {nome} foi adicionado ao estoque\n")
    #print()

if __name__ == "__main__":
    print('bem vindo ao sistema de estoque ultima')

    opcao = 0
    while opcao != 2:
        print('menu de opçoes:')
        print('===============')
        print('1. adicionar item')
        print('2. sair')

        opcao = int(input('selecione uma opçao: '))

        if opcao == 1:
            adicionar_item_estoque()
        elif opcao == 2:
            print('obrigado por usar nosso sistema')
        else:
            print('opçao invalida. tente novamente\n')