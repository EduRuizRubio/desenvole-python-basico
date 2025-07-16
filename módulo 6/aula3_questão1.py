# Solicita até 4 números
lista = []
while len(lista) < 4:
    n = int(input("Digite um número inteiro (mínimo 4 no total): "))
    lista.append(n)

# Permite adicionar mais valores se o usuário quiser
while True:
    opcao = input("Deseja adicionar mais um número? (s/n): ").strip().lower()
    if opcao == 's':
        n = int(input("Digite outro número inteiro: "))
        lista.append(n)
    else:
        break

print("\nLista original:")
print(lista)

print("\nOs 3 primeiros elementos:")
print(lista[:3])

print("\nOs 2 últimos elementos:")
print(lista[-2:])

print("\nLista invertida:")
print(lista[::-1])

print("\nElementos de índice par:")
print(lista[0::2])

print("\nElementos de índice ímpar:")
print(lista[1::2])