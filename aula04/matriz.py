
import random

def gerar_matriz(linhas, colunas, aleatoria=True):
    """Gera uma matriz de tamanho linhas x colunas, com valores entre 1 e 10."""
    if aleatoria:
        return [[random.randint(1, 10) for _ in range(colunas)] for _ in range(linhas)]
    else:
        return [[int(input(f"Digite o valor [{i}][{j}]")) for j in range(colunas)] for i in range(linhas)]

def exibir_matriz(matriz):
    """Exibe a matriz formatada."""
    for linha in matriz:
        print(" ".join(f"{x:3}" for x in linha))
    print()

def somar_matrizes(A, B):
    """Soma duas matrizes do mesmo tamanho"""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrizes(A, B):
    """Multiplica duas matrizes"""
    if len(A[0]) != len(B):
        raise ValueError("O número de colunas de A deve ser igual ao número de linhas de B")
    resultado = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    return resultado

def simetrica(matriz):
    """Verifica se uma matriz é simétrica"""
    tamanho = len(matriz)
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def determinante_3x3(matriz):
    """Calcula o determinante de uma matriz 3x3"""
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("A matriz deve ser 3x3")
    return (
        matriz[0][0] * matriz[1][1] * matriz[2][2] +
        matriz[0][1] * matriz[1][2] * matriz[2][0] +
        matriz[0][2] * matriz[1][0] * matriz[2][1] -
        matriz[0][2] * matriz[1][1] * matriz[2][0] -
        matriz[0][0] * matriz[1][2] * matriz[2][1] -
        matriz[0][1] * matriz[1][0] * matriz[2][2]
    )

print("Gerar matriz")
A = gerar_matriz(3, 3)
exibir_matriz(A)

print("Gerar matriz")
B = gerar_matriz(3, 3)
exibir_matriz(B)

print("Soma A e B")
exibir_matriz(somar_matrizes(A, B))

print("Multiplicação")
exibir_matriz(multiplicar_matrizes(A, B))

print("A matriz A é simétrica?", simetrica(A))

if len(A) == 3 and len(A[0]) == 3:
    print("Determinante de A:", determinante_3x3(A))
