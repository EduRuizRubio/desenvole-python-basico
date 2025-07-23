import re #biblioteca para usar o re.


# Abre o arquivo e lê
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Encontra as palavras feitas apenas por letras (ignora pontuação e números)
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", conteudo)

# Abre o arquivo palavras.txt para escrita e salva cada palavra em uma linha
with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Imprime o conteúdo do arquivo palavras.txt
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
