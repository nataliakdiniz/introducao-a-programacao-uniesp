# Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever
# se existem números repetidos no vetor VET e em que posições se encontram.

from collections import defaultdict
duplicates = defaultdict(list)

vet = []
for cont in range(0, 50):
    vet.append(int(input('Digite um valor: ')))

# iterage sobre as posições e os números simultaneamente
for indice, numero in enumerate(vet):
    # acumula as posições com os mesmos números
    # O +1 Adiciona a posição no lugar do indice
    duplicates[numero].append(indice + 1)

resultado = {chave: valor for chave, valor in duplicates.items() if len(valor) > 1}
print(resultado)
