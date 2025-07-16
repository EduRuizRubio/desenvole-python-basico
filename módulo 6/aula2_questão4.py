# Lê a primeira lista
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    lista1.append(int(input()))     #.append é usado para adicionar novos valores em uma lista

# Lê a segunda lista
n2 = int(input("\nDigite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    lista2.append(int(input()))

# Intercala as listas
intercalada = []
for i in range(max(n1, n2)):
    if i < n1:
        intercalada.append(lista1[i])
    if i < n2:
        intercalada.append(lista2[i])

# Exibe a lista intercalada
print(f"\nLista intercalada: {' '.join(map(str, intercalada))}")
