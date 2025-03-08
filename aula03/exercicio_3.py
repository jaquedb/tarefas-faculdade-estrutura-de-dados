# EXERCICIO 3: PERCORRENDO LISTAS COM LAÇOS DE REPETIÇÃO

# A) Crie uma lista de cinco números e exiba cada número multiplicado por 2 usando um laço for

# B) Some todos os elementos da lista usando um laço for e exiba o resultado

# C) Peça ao usuário para digitar cinco números e os armazene em uma lista. Em seguida
# exiba os número digitados 

numeros = [10,15,20,15]
print ("Números da lista: ")
for numero in numeros:
    print(numero)

print ()
print (30*"=")
print ()

# NÚMEROS MULTIPLICADOS POR 2
print("Números da lista multiplicado por 2")
for numero in numeros:
    resultado = numero * 2
    print(numero, "X", 2, "=", resultado)

print ()
print (30*"=")
print ()

# SOMANDO TODOS OS ELEMENTOS DA LISTA USANDO FOR
print ("Resultado da soma de todos os elementos da lista: ")
soma = 0
for numero in numeros:
    soma+=numero

print (soma)

print ()
print (30*"=")
print ()

# NUMEROS FORNECIDOS POR USUÁRIO
print("Números fornecido pelo usuário ")

lista_de_numeros = []

for index in range (5):
    numero = int(input("informe um número "))
    lista_de_numeros.append(numero)

print ()
print (30*"=")
print ()

# MOSTRANDO OS NUMEROS DIGITADOS PELO USUÁRIO + OS INDICES EM QUE ESTÃO
print ("Números digitados pelo usuário ")
for index,numero in enumerate (lista_de_numeros):
    print (f" Índice {index} : Numero {numero}" )




