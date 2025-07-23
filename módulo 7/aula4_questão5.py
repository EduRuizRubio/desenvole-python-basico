# Lista de livros com título, autor, ano de publicação e número de páginas
livros = [
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],  # edição única
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Star Wars: Herdeiro do Império", "Timothy Zahn", 1991, 416],  # primeiro da trilogia Thrawn
    ["As Crônicas de Nárnia", "C.S. Lewis", 1950, 768],  # volume único
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Código Da Vinci", "Dan Brown", 2003, 480],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, 400],
    ["O Alquimista", "Paulo Coelho", 1988, 208]
]

# Cria o arquivo meus_livros.csv para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escreve a primeira linha com os títulos da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escreve as informações de cada livro
    for livro in livros:
        linha = ",".join([str(item) for item in livro])
        arquivo.write(linha + "\n")

print("Arquivo meus_livros.csv criado com sucesso!")
