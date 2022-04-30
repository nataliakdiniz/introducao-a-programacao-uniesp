# Solicite ao usuário um valor numérico, inteiro ou real,
# e escrever se é positivo ou negativo (considere o valor zero como positivo).

number = float(input('Número: '))

if number >= 0:
    print('Número positivo', number)
else:
    print('Número Negativo', number)
