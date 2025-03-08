# EXERCICIO 1: CONCEITOS BÁSICOS DE LISTAS

# A) Criar uma lista chamada "numeros" contendo os valores [10,20,30,40,50] e exiba 
# terceiro elemento.

# B) Adicione o número 60 a lista "números" e exiba a lista atualizada

# C) Remova o número 30 da lista "numeros" e exiba a lista novamente

# D) Exiba o tamanho (Quantidade de elementos) da lista utilizandoa função len().



numeros = [10,20,30,40,50]

# EXIBINDO O TERCEIRO ELEMENTO DA LISTA
print("TERCEIRO ELEMENTO DA LISTA")
print(numeros[2])

print()
print (30*"=")
print()

# ADICIONANDO NUMEROS A LISTA
print("ADICIONANDO NUMEROS NA LISTA")
numeros.append(60)
print(numeros)

print()
print (30*"=")
print()

# REMOVENDO NUMEROS DA LISTA
print("REMOVENDO NUMEROS DA LISTA")
numeros.remove(30)

print (numeros)

print()
print (30*"=")
print()

# EXIBINDO O TAMANHO DA LISTA
print("EXIBINDO O TAMANHO DA LISTA ")
numeros = len(numeros)
print (numeros)




