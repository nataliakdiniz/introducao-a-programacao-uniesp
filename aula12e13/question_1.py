# Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão,
# chame este dicionário de glossário. Pense em cinco palavras relacionada à programação que você
# conheceu nesta disciplina. Use estas palavras como chaves em seu glossário e armazene seus significados como valores.
# Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante.
# Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado,
# ou apresentar a palavra em uma linha e então exibir seu significado identado em uma segunda linha.
# Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par de palavra-significado
# em sua saída.
# Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.

glossario = {
    'Algoritimo': 'É uma sequência de passos.',
    'Dicionario em Python': 'É um objeto que contém mais que um valor.',
    'PyCharm': 'Ambiente de desenvolvimento para linguagem Python.',
    'Python': 'Linguagem de programação.',
    'Variável': 'É usado para armazenar dados de forma simples.'
}
for key, value in glossario.items():
    print(f'{key} : {value} \n -----------------------------------------------------------------')
