# Lista de URLs fornecida
URLs = ["www.google.com", "www.gmail.com", "www.github.com", 
        "www.reddit.com", "www.yahoo.com"]

print("URLs originais:")
print(URLs)

# Criando lista de domínios usando fatiamento de strings
dominios = []

for url in URLs:
    # Remove "www." do início (4 primeiros caracteres) e ".com" do final (4 últimos caracteres)
    dominio = url[4:-4]
    dominios.append(dominio)

print("\nDomínios: ")
print(dominios)