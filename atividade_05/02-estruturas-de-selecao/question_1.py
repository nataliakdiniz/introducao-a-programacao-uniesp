# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior
# ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor)
# e informar o valor digitado pelo usuário.

number = float(input('Primeiro valor: '))

if number <= 10:
    print('Menor que 10, número digitado: ', number)
else:
    print('Maior que 10, número digitado: ', number)
