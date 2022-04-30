# 3) Escreva um algoritmo que peça dois números ao usuário e realize a SUBTRAÇÃO entre eles.

def calcular_subtracao(numero1, numero2):
    return numero1 - numero2


numero1 = float(input("Digite a número 1: "))
numero2 = float(input("Digite a número 2: "))
resultado = calcular_subtracao(numero1, numero2)

print(resultado)
