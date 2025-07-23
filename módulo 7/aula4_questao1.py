import os

frase = input("Digite uma frase: ")

#  encoding= 'uft-8' (recomendado para utilizar acentos)
with open('frase.txt', 'w', encoding='utf-8') as f:
    f.write(frase)


caminho_completo = os.path.abspath("frase.txt")
print(f"Frase salva em {caminho_completo}")
