S = 0
R = 0
C = 0
cobaias_totais = 0

experimentos = int(input("Escreva a quantidade de experimentos realizados: "))

i = 0
while i < experimentos:
    quantidade = int(input("Escreva a quantidade de animais usados no experimentos: "))
    animal = input("Digite o animal do primeiro experimento Sapo, Rato, Coelho (S, R, C) ")
    if animal == 'S':
        S = S + quantidade
    elif animal == 'R':
        R = R + quantidade 
    elif animal == 'C':
        C = C + quantidade 
    else:
        print('Aninmal invalido!')
    cobaias_totais = cobaias_totais + quantidade
    i = i + 1

perc_C = (C / cobaias_totais) * 100
perc_S = (S / cobaias_totais) * 100
perc_R = (R / cobaias_totais) * 100

print ("Total: ", cobaias_totais, " cobaias")
print ("Total de coelhos: ", C)
print ("Total de ratos: ", R)
print ("Total de sapos: ", S)
print ("Percentual de coelhos: ", round(perc_C, 2), "%")
print ("Percentual de ratos: ", round(perc_R, 2), "%")
print ("Percentual de sapos: ", round(perc_S, 2), "%")
