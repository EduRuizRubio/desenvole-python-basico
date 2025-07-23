import csv

# Inicializa o dicionário para armazenar a música mais tocada por ano
mais_tocadas = {}

# Abre o arquivo para leitura com encoding latin-1
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)

    # Lê o cabeçalho
    cabecalho = next(leitor)
    print("Cabeçalho:", cabecalho)

    # Processa cada linha do arquivo
    for colunas in leitor:
        try:
            track_name = colunas[0]
            artist_name = colunas[1]
            artist_count = int(colunas[2])
            released_year = int(colunas[3])
            streams = int(colunas[8])

            # Considera apenas músicas lançadas entre 2012 e 2022
            if 2012 <= released_year <= 2022:
                # Se ainda não há música para o ano ou se a atual tem mais streams, atualiza
                if released_year not in mais_tocadas or streams > mais_tocadas[released_year][3]:
                    mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]

        except ValueError:
            # Ignora linhas com dados inválidos de streams
            continue

# Organiza o resultado em uma lista ordenada pelos anos
lista_mais_tocadas = [mais_tocadas[ano] for ano in sorted(mais_tocadas.keys())]

# Imprime o resultado final
print("\nMúsicas mais tocadas de 2012 a 2022:")
for musica in lista_mais_tocadas:
    print(musica)
