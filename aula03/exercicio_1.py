# EXERCICIO 1: CONCEITOS BÁSICOS DE LISTAS

# A) Criar uma lista chamada "numeros" contendo os valores [10,20,20,40,50] e exiba 
# terceiro elemento.

# B) Adicione o número 60 a lista "números" e exiba a lista atualizada

# C) Remova o número 30 da lista "numeros" e exiba a lista novamente

# D) Exiba o tamanho (Quantidade de elementos) da lista utilizandoa função len().



numeros = [10,20,30,40,50]

# ADICIONANDO NUMEROS A LISTA
numeros.append(60)
print(numeros)
print (30*"=")

# REMOVENDO NUMEROS DA LISTA
numeros.remove(30)

print (numeros)
print (30*"=")

numeros = len(numeros)
print (numeros)




