# Solicitar frase do usuário
frase = input("Digite uma frase: ")

# Definir vogais (maiúsculas e minúsculas)
vogais = "aeiouAEIOU"

# Lista de vogais da frase, ordenada alfabeticamente
lista_vogais = sorted([char for char in frase if char in vogais])

# Lista de consoantes da frase (removendo espaços em branco)
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

# Imprimir resultados
print(f"Vogais: {lista_vogais}")
print(f"Consoantes: {lista_consoantes}")