import random

num_elementos = random.randint(5, 20)  # Agora é um número inteiro

# Gera 'num_elementos' valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(num_elementos)]

# Imprime a lista original
print("\nLista original:")
print(lista)

# Calcula soma e média
soma = sum(lista)
media = soma / num_elementos

# Exibe os resultados
print(f"\nSoma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
