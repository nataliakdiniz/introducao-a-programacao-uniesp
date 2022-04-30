#Faça um algoritmo para ler 20 números e armazenar em um vetor.
# Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

list = []
for cont in range(0, 20):
    list.append(int(input('Digite um valor: ')))
list.sort(reverse=True)
print(list)

