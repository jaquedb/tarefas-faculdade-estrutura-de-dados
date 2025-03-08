# EXERCICIO 5: APLICAÇÃO PRÁTICA 

# A) Escreva um programa que receba as notas de 4 alunos em uma matriz 4X3 (4 alunos e 3 provas)
# e calcule a média de cada aluno 

# B) Desenvolva um programa que cria uma matriz 3X3 preenchida automaticamente com números
# aleatórios entre 1 e 100. Depois exiba a matriz e a soma de todos os elementos.

#NOTAS DE ALUNOS E MÉDIA

notas = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range (4):
    for j in range (3):
        notas [i][j] = int(input(f" Informe os valores para as posições {i} e {j} "))

print (30*"=")

print("NOTAS DIGITADAS")
print ()

for nota in notas:
    print (nota)

print (30*"=")

print("MÉDIA")
print ()

for index, linha in enumerate (notas, start=1):
    resultado = (sum(linha)/3)
    print(f"Aluno {index}: {resultado}")

print (30*"=")

# MATRIZ ALEATÓRIA

print ("MATRIZ ALEATÓRIA")
print ()

import random

matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(4):
    for j in range(4):
        matriz = [[random.randint(1, 100) for _ in range(i)] for _ in range(j)]

print ()

for mat in matriz:
    print (mat)

print (30*"=")
# SOMA DA MATRIZ

print("SOMA DA MATRIZ ALEATÓRIA")
print()

soma = 0

for linha in matriz:
    soma+=sum(linha)


print ("Total: ",soma)


