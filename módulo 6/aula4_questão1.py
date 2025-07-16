# 1. Todos os números pares entre 20 e 50
pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]
print("1. Números pares entre 20 e 50:")
print(pares_20_50)
print()

# 2. Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in lista_original]
print("2. Quadrados dos valores [1,2,3,4,5,6,7,8,9]:")
print(quadrados)
print()

# 3. Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]
print("3. Números entre 1 e 100 divisíveis por 7:")
print(divisiveis_por_7)
print()

# 4. Para todos os valores em range(0,30,3), escreva "par" ou "ímpar"
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("4. Paridade dos valores em range(0,30,3):")
print(f"Valores: {list(range(0, 30, 3))}")
print(f"Paridade: {paridade}")