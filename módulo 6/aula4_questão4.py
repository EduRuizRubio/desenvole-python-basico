alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Versão com compreensão de listas
aprovados = [aluno for aluno, nota in zip(alunos, notas) if nota >= 60]

print("\nCom compreensão de listas:")
print(aprovados)
