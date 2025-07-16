print ('Notas de 0 a 100\n')
n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

m = ((n1 + n2+ n3)/3)

if m >= 60:
    print ('Aprovado')
else:
    if m >= 40:
        print ('Recuperação')
    else:
        print ('Reprovado')

print ('Fim')