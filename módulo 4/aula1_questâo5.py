N = int(input("escreva a quantidade de respondentes: "))

i = 0
idade_total = 0

while i < N:
    print ("Digite a idade do respondente ", i, ": ")
    idade = int(input())
    idade_total = idade_total + idade
    i = i + 1
    
media = idade_total/N

print ("Media das idades: ", media)
