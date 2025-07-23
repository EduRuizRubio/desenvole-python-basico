import random

def encrypt(lista):
    chave = random.randint(1, 10)
    criptografados = []
    for nome in lista:
        criptografado = ''
        for c in nome:
            novo_codigo = 33 + ((ord(c) + chave - 33) % 94)
            criptografado += chr(novo_codigo)
        criptografados.append(criptografado)
    return criptografados, chave
