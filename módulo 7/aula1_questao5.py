frase = input("Digite uma frase: ")
indices = [i for i, letra in enumerate(frase) if letra.lower() in "aeiou"]
print(len(indices), "vogais")
print("Índices", indices)
