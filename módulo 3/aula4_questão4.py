distancia = int(input('Digite a distância do frete: '))
peso = int(input('Digite o peso do produto: '))
preco = 0
if peso>10:
    preco = 10
else:
    if distancia <= 100:
        preco = preco + peso
    elif distancia>100 and distancia<=300:
        preco = preco + peso * 1.5
    else:
        preco = preco + peso * 2

print('Para ', distancia, 'km e ', peso, 'kg, o frete será de: R$', preco)