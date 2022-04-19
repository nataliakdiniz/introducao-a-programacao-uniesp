# Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

number = int(input("Qual o número que quer que se faça a tabuada: "))
for inicio in range(0,101):
    resultado = inicio * number
    print("{} x {} = {}".format(number, inicio, resultado))




