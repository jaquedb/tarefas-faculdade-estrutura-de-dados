numeros = [10,20,30,40,50]

# ADICIONANDO NUMEROS NO FINAL
numeros.append (60)

print (numeros)

print ("=================================")

# INSERIR ELEMENTOS EM UMA POSIÇÃO ESPECIFICA
numeros.insert(2,25) #Insere o numero 25 na posição 2

# REMOVENDO ITEM DA LISTA
numeros.remove(40)

# REMOVENDO O ULTIMO ITEM DA LISTA
numeros.pop()

print (numeros)

print("=================================")

# ACESSANDO O PRIMEIRO E O ULTIMO NUMERO DA LISTA
primeiro_numero = numeros[0]
ultimo_atual = numeros[-1]

print("Primeiro número: " + str(primeiro_numero) + " - Ultimo numero: " + str(ultimo_atual))