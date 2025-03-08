
alunos = [
    ["Ana", 8.5],
    ["Bruna", 7.2],
    ["Carlos", 9.1],
    ["Diego", 6.8]
]


alunos.sort(key=lambda aluno: aluno[1], reverse=True)

print("Notas dos alunos: ")

for i, (nome, nota) in enumerate (alunos, start=1):
    print(f"{i}. {nome} - Nota: {nota}")