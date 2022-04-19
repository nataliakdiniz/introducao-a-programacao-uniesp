# Faça um programa que mostre as tabuadas dos números de 1 a 10.

number = int(input("Qual o número que quer que se faça a tabuada? "))
for valor in range(0,11):
    resultado = valor * number
    print("{} x {} = {}".format(number, valor, resultado))



