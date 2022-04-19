# Seja criativo ao desenvolver este programa. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
# Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
# Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites.
# Imprima o nome das pessoas que não poderão comparecer.
# Modifique sua lista, substitua os desistentes por novos convidados.
# Exiba um novo convite para cada pessoa que continua presente em sua lista.

celecebridades = ['Oprah', 'Melinda Gates', 'Bil Gates', 'Mark Zuckerberg', 'Jeff Bezos']
for convite in celecebridades:
    print('Hello, how are you {}? I would like to invite you to our annual innovation conference.'
          'The event will be at my home, at the address los angeles avenue - 430.'.format(convite))

negativas = ['Oprah']
del celecebridades[0]
for compareceram in negativas:
    print('unfortunately {} will not be able to attend the event.'.format(negativas[0]))

celecebridades.append('Madona')

for novoConvite in celecebridades:
    print('Hello, how are you {}? I would like to invite you to our annual innovation conference.'
          'The event will be at my home, at the address los angeles avenue - 430.'.format(novoConvite))












