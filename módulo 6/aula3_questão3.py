import random

# Criando lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print(f"Lista original:")
print(lista)
print(f"Tamanho: {len(lista)} elementos")

# Função para encontrar o intervalo com mais números negativos
def encontrar_intervalo_mais_negativos(lista):
    max_negativos = 0
    melhor_inicio = 0
    melhor_fim = 0
    
    # Testando todos os intervalos possíveis
    for inicio in range(len(lista)):
        for fim in range(inicio + 1, len(lista) + 1):
            intervalo = lista[inicio:fim]
            negativos = sum(1 for x in intervalo if x < 0)
            
            # Se encontrou um intervalo com mais negativos
            if negativos > max_negativos:
                max_negativos = negativos
                melhor_inicio = inicio
                melhor_fim = fim
    
    return melhor_inicio, melhor_fim, max_negativos

# Encontrando o melhor intervalo
inicio, fim, qtd_negativos = encontrar_intervalo_mais_negativos(lista)

print(f"\n--- Análise do intervalo ---")
print(f"Intervalo com mais negativos: posições {inicio} até {fim-1}")
print(f"Elementos do intervalo: {lista[inicio:fim]}")
print(f"Quantidade de números negativos: {qtd_negativos}")

# Criando cópia da lista para mostrar o antes/depois
lista_original = lista.copy()

# Deletando o intervalo usando del
print(f"\n--- Deletando intervalo ---")
print(f"Removendo elementos das posições {inicio} até {fim-1}...")

del lista[inicio:fim]

print(f"\nLista após deleção:")
print(lista)
print(f"Tamanho: {len(lista)} elementos")

print(f"\n--- Comparação ---")
print(f"Original:  {lista_original}")
print(f"Editada:   {lista}")
print(f"Elementos removidos: {len(lista_original) - len(lista)}")

# Verificação adicional: mostrar todos os intervalos analisados
print(f"\n--- Detalhes da análise (primeiros 10 intervalos) ---")
count = 0
for inicio_teste in range(len(lista_original)):
    for fim_teste in range(inicio_teste + 1, len(lista_original) + 1):
        if count >= 10:  # Limitar output
            break
        intervalo = lista_original[inicio_teste:fim_teste]
        negativos = sum(1 for x in intervalo if x < 0)
        print(f"Posições [{inicio_teste}:{fim_teste}] = {intervalo} → {negativos} negativos")
        count += 1
    if count >= 10:
        break