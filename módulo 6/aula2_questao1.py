import random

# Gera 20 valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Imprime a lista ordenada
print("Lista ordenada (sem alterar a original):")
print(sorted(lista))

# Imprime a lista original
print("\nLista original:")
print(lista)

# Encontra o índice do maior valor
indice_maior = lista.index(max(lista))

# Encontra o índice do menor valor
indice_menor = lista.index(min(lista))

# Exibe os índices
print(f"\nÍndice do maior valor ({max(lista)}): {indice_maior}")
print(f"Índice do menor valor ({min(lista)}): {indice_menor}")
