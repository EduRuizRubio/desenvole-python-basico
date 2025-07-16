import random

# Gera duas listas com 20 números aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria a lista de interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Exibe as listas
print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"Interseccao = {interseccao}")

# Contagem de ocorrências
print("Contagem")
for valor in interseccao:
    count1 = lista1.count(valor)
    count2 = lista2.count(valor)
    print(f"{valor}: (lista1={count1}, lista2={count2})")


