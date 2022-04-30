# 6) PROGRAMA QUADRADO 2.0 – O usuário informa três números inteiros, o programa soma esses três
# valores e depois mostra o quadrado do resultado obtido.

def calcular_divisao(numero1, numero2, numero3):
    soma = numero1 + numero2 + numero3
    return soma * soma


numero1 = int(input("Digite a número 1: "))
numero2 = int(input("Digite a número 2: "))
numero3 = int(input("Digite a número 3: "))
resultado = calcular_divisao(numero1, numero2, numero3)

print(resultado)
