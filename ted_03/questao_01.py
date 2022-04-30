# 1) Escreva um algoritmo que, com base nas dimensões de um retângulo (base e altura),
# vai calcular e escrever a área do retângulo.

def calcular_dimensao_retangulo(base, altura):
    return base * altura


base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
dimensao = calcular_dimensao_retangulo(base, altura)

print(dimensao)
