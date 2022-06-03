'''
8-Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja um prefixo da segunda.
 Exemplo: ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.

print(s.endswith("mundo"))
'''
def contar_prefixo():
    mensagem = input('qual a frase: ')
    prefixo = input('qual o prefixo: ')
    if prefixo in mensagem:
        print(f'a frase é: {mensagem}')
        print(f'caracteres na frase: {len(mensagem)}')
        print(f' o prefixo é: {prefixo}')
        print(f' o prefixo é encontrado na frase: {mensagem.startswith(prefixo)}')
        print(f'quantas vezes o prefixo é encontrado: {mensagem.count(prefixo)}')
    else:
        print(f'a frase é: {mensagem}')
        print(f'caracteres na frase: {len(mensagem)}')
        print(f' o prefixo é: {prefixo}')
        print(f' o prefixo é encontrado na frase: {mensagem.startswith(prefixo)}')
        print("prefixo nao encontrado")
    

contar_prefixo()