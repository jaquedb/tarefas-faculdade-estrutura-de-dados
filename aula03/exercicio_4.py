# EXERCICIO 4: INTRODUÇÃO A MATRIZES

# A) Crie uma matriz 3X3 representada por uma lista de listas
# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# - Exiba o elemento da segunda linha e terceira coluna
# - Substitua o valor da posição [1][1] pelo numero 99
# - Exiba toda a matriz formatada linha por linha

# B) Peça ao usuário para digitar os elementos de uma matriz 2X2 e armazene-os em 
# uma lista de listas. Depois exiba a matriz.

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Matriz", matriz)
print ()
print (30*"=")
print ()

print ("Elemento da segunda linha e terceira coluna: ", matriz[1][2]) # primeiro linha depois coluna

print ()
print (30*"=")
print ()

# SUBSTITUIÇÃO DE VALORES
print("Substituindo valores")
matriz [1][1] = 99
print("Matriz atualizada", matriz)

print ()
print (30*"=")
print ()

# EXIBINDO MATRIZ FORMATADA
print("Matriz formatada ")
for numero in matriz:
    print(numero)

print ()
print (30*"=")
print ()

#CRIANDO MATRIX COM NÚMERO FORNECIDOS PELO USUÁRIO
print ("Criando matriz com números do usuário ")
print()

matrix =[
    [0,0 ],
    [0,0 ]
]

for i in range(2):
    for j in range (2):
        matrix [i][j] = int(input(f"Informe os valores para a posição: {i} e {j} "))

for linha in matrix:
    print(linha)