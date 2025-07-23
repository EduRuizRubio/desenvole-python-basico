import re

# Abre o arquivo estomago.txt e lÊ
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# - Imprime as primeiras 25 linhas
print("Primeiras 25 linhas do arquivo:\n")
for linha in linhas[:25]:
    print(linha.strip())

# - Número de linhas do arquivo
num_linhas = len(linhas)
print("\nNúmero total de linhas:", num_linhas)

# - Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\nLinha com maior número de caracteres:")
print(linha_maior.strip())
print("Número de caracteres nesta linha:", len(linha_maior))

# - Contagem de menções aos nomes dos personagens

# Junta todas as linhas em um único texto para a contagem dos nomes
texto_completo = ''.join(linhas)

# Conta "Nonato" ignorando maiúsculas/minúsculas
cont_nonato = len(re.findall(r"\bnonato\b", texto_completo, re.IGNORECASE))

# Conta "Íria" ignorando maiúsculas/minúsculas e pegando a letra I acentuada ou não
# Usa classes de acento: [ÍIíi]ria para aceitar variações
cont_iria = len(re.findall(r"\b[ÍIíi]ria\b", texto_completo, re.IGNORECASE))

print("\nNúmero de menções ao personagem 'Nonato':", cont_nonato)
print("Número de menções ao personagem 'Íria':", cont_iria)
