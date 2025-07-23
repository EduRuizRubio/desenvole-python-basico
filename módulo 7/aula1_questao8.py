def validar_cpf(cpf):
    cpf_numeros = [int(c) for c in cpf if c.isdigit()]
    if len(cpf_numeros) != 11 or len(set(cpf_numeros)) == 1:
        return "Inválido"

    soma1 = sum(cpf_numeros[i] * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    dig1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = sum(cpf_numeros[i] * (11 - i) for i in range(9)) + dig1 * 2
    resto2 = soma2 % 11
    dig2 = 0 if resto2 < 2 else 11 - resto2

    if cpf_numeros[9] == dig1 and cpf_numeros[10] == dig2:
        return "Válido"
    return "Inválido"

cpf = input("Digite um CPF (XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf))
