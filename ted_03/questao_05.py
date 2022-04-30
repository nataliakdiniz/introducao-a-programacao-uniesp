# 5) Escreva um algoritmo que peça dois números ao usuário e realize a DIVISÃO entre eles.

def calcular_divisao(numero1, numero2):
    return numero1 / numero2


numero1 = float(input("Digite a número 1: "))
numero2 = float(input("Digite a número 2: "))
resultado = calcular_divisao(numero1, numero2)

print(resultado)
