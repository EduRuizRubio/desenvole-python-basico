dinheiro = int(input("Digite o valor para sacar: "))
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

din_aux = dinheiro
n100 = din_aux // 100
din_aux = din_aux - (n100 * 100)
n50 = din_aux // 50
din_aux = din_aux - (n50 * 50)
n20 = din_aux // 20
din_aux = din_aux - (n20 * 20)
n10 = din_aux // 10
din_aux = din_aux - (n10 * 10)
n5 = din_aux // 5
din_aux = din_aux - (n5 * 5)
n2 = din_aux // 2
din_aux = din_aux - (n2 * 2)
n1 = din_aux // 1
din_aux = din_aux - (n1 * 1)

print (n100, 'nota(s) de R$100,00')
print (n50, 'nota(s) de R$50,00')
print (n20, 'nota(s) de R$20,00')
print (n10, 'nota(s) de R$10,00')
print (n5, 'nota(s) de R$5,00')
print (n2, 'nota(s) de R$2,00')
print (n1, 'nota(s) de R$1,00')

