idade = int(input("Digite a idade de candidato: "))
jogos = int(input("Digite quantos jogos já jogou: "))
vitorias = int(input("Digite quantos jogos já venceu: "))

if idade>=16 and idade <=18 and jogos<=3 and vitorias>=1:
    print("True")
else:
    print("False")

