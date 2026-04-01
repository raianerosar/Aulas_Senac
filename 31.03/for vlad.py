#1. Crie um programa em python que:
#Peça ao usuário digitar 10 números inteiros.
# Armazene esses números em uma lista, use um laço FOR para percorrer a lista.
# Para cada número classifique como:
 
numeros = []
 
for i in range(3):
    nms = int(input(f"Digite {i+1}º número: "))
    numeros.append(nms)
    print(numeros)
 
for n in (numeros):
 
    if n == 10:
        print(f"Número {n} é igual a 10. \n")
    elif n > 10:
        print(f"Número {n} é maior que 10! \n")
    else:
        print(f"Número {n} é menor que 10! \n")