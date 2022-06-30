'''
6- Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.

def contar_letras(letras):
    mensagem = "ola mundo"
    if letras in mensagem:
        print(mensagem)
        print(letras)
        print(len(letras))
    else:
        print(mensagem)
        print(letras)
        print("letra nao encontrada")

def contar_letras(letras):
    mensagem = "ola mundo"
    if letras in mensagem:
        print(mensagem)
        print(letras)
        print(mensagem.startswith(letras))
    else:
        print(mensagem)
        print(letras)
        print("letra nao encontrada")
    
    
'''




def contar_letras(letras):
    mensagem = "ola mundo"
    if letras in mensagem:
        print(mensagem)
        print(len(mensagem))
        print(letras)
        print(mensagem.count(letras))
    else:
        print(mensagem)
        print(letras)
        print("letra nao encontrada")
    

contar_letras('o')