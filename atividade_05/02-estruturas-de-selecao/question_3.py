# As maçãs custam 1,30 cada se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maçãs = int(input('Quantas maçãs você comprou? '))

if maçãs >= 12:
    print('As maçãs custam', maçãs * 1.00)
else:
    print('As maçãs custam', maçãs * 1.30)


