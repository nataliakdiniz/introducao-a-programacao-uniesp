# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque
# e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média
# ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média,
# escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quantAtualEstoque = int(input('Digite a quantidade atual do estoque: '))
quantMaximaEstoque = int(input('Qual a quantidade máxima em estoque: '))
quantMinimaEstoque = int(input('Qual a quantidade mínima em estoque: '))
quantidadeMedia = (quantMaximaEstoque + quantMinimaEstoque) / 2

print("A quantidade média é:", quantidadeMedia)

if quantAtualEstoque >= quantidadeMedia:
    print('Não efetuar a compra!')
else:
    print('Efetuar a compra!')







