import random

# Função para imprimir o estágio do enforcado
def imprime_enforcado(erros, enforcado):
    print("\n".join(enforcado[erros]))

# Lê as palavras do gabarito_forca.txt
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f.readlines()]

# Escolhe uma das palavras aleatoriamente
palavra = random.choice(palavras).lower()

# Lê os estágios do enforcado do arquivo
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    estagios = conteudo.strip().split("\n\n")

# Converte cada estágio em lista de linhas para imprimir corretamente
enforcado = [estagio.split("\n") for estagio in estagios]

# Inicializa variáveis do jogo
tentativas = 0
letras_corretas = ["_" for _ in palavra]
letras_usadas = []

print("Bem-vindo ao jogo da Forca!")
print("A palavra tem", len(palavra), "letras.")

# Loop para funcionar o jogo
while tentativas < 6 and "_" in letras_corretas:
    print("\nPalavra:", " ".join(letras_corretas))
    letra = input("Digite uma letra: ").lower()
    
    if letra in letras_usadas:
        print("Você já tentou essa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        print("Acertou!")
        for i, l in enumerate(palavra):
            if l == letra:
                letras_corretas[i] = letra
    else:
        print("Errou!")
        tentativas += 1
        imprime_enforcado(tentativas, enforcado)

# Verifica resultado final
if "_" not in letras_corretas:
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)
