# EXERCICIO 2: OPERAÇÕES E MANIPULAÇÃO DE LISTAS

# A) Crie uma lista chamada "frutas" contendo ["maça, "banana", "laranja", "Uva"]

# B) Inverta a ordem dos elementos da lista e exiba o resultado

# C) Ordene  a lista em ordem alfabética e exiba o resultado

# D) Verifique se a palavra morango esta na lista e exiba a palavra apropriada


# LISTA DOS ELEMENTOS
frutas = ["Maça", "Banana", "Laranja", "Uva"]
print ()
print ("LISTA DE FRUTAS ")
print ()
for fruta in frutas:
    print (fruta)

print()
print (30*"=")
print()


# INVERTENDO A ORDEM DOS ELEMENTOS DA LISTA
print("ORDEM INVERTIDA DOS ELEMENTOS ")
frutas.reverse()
print()
for fruta in frutas:
    print(fruta)

print ()
print (30*"=")
print()

# LISTA DOS ELEMENTOS EM ORDEM ALFABÉTICA
print ("LISTA DE FRUTAS ORDEM ALFABÉTICA")
print()
frutas.sort()

for fruta in frutas:
    print(fruta)

print ()
print (30*"=")
print ()

# VERIFICANDO SE HÁ MORANGOS NA LISTA

if "Morango" in frutas:
    print ("Sim, há morango na lista")
else:
    print ("Não há morango na lista")