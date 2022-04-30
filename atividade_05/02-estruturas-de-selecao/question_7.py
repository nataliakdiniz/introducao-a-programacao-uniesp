# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

conta = int(input('Digite sua conta: '))
saldo = int(input('Informe seu saldo: '))
debito = int(input('Informe seu débito: '))
credito = int(input('Informe seu crédito: '))
saldo_atual = (saldo - debito + credito)

print("Seu saldo atual é:", saldo_atual)

if saldo_atual >= 0:
    print('Saldo Positivo!')
else:
    print('Saldo Negativo!')





