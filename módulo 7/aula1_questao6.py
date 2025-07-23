frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

from collections import Counter

contador_objetivo = Counter(objetivo.lower())
palavras = frase.split()
anagramas = []

for palavra in palavras:
    if Counter(palavra.lower()) == contador_objetivo:
        anagramas.append(palavra)

print("Anagramas:", anagramas)
