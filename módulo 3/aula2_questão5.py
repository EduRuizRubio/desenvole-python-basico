genero = input("Escreva o gênero do usuário(M ou F): ")
idade = int(input("Digite a idade do usuário: "))
tempo = int(input("Digite o tempo de serviço do usuário: "))

if genero=='F' and idade>=60:
    aposentadoria = True
else:
    if genero=='M' and idade>=65:
        aposentadoria = True
    else:
        if tempo>=30:
            aposentadoria = True
        else:
            if idade>=65 and tempo>=25:
                aposentadoria = True
            else:
                aposentadoria = False

print ('A aposentadoria é: ',aposentadoria)
