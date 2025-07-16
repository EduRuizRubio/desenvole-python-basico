import random
import math

n = int(input('Digite a quantidade de valores: '))
soma = 0
i=0
for i in range(n):
    aux = random.randint(0,100)
    soma = soma + aux
    print ('Valor n', i+1, ': ', aux)

print('Soma das raízes:', round(math.sqrt(soma),2))