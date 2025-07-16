import random

num = random.randint(0,50)
n=-1
while n != num:
    n = int(input('Adivinha o número entre 1 e 50: '))
    if n>num:
        print('Muito alto, tente notavemnte!')
    else:
        if n<num:
            print('Muito baixo, tente notavemnte!')
        else:
            print ('Correto! O número é', num)