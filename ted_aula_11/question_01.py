# Consutra uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Depois: Imprima o resultado da soma de todos os valores da matriz no terminal;
# E, crie uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint

matrizA = []
for linha in range(10):
    linha = []
for coluna in range(10):
    linha.append(randint(0, 100))
    matrizA.append(linha)
print(matrizA)
somaTotal = 0
for linha in range(len(matrizA)):
        for coluna in range(len(matrizA)):
            somaTotal += matrizA[linha][coluna]
print('Temos aqui a soma total da matriz A: ', somaTotal)
