# 8) PROGRAMA TEMPERATURA – O usuário digita a temperatura em graus Célsius e o programa exibe o
# valor em graus Fahrenheit. A conversão é dada pela seguinte fórmula: F   (9 * C + 160) / 5


def converter_celsius_fahrenheit(celsius):
    return (9 * celsius + 160) / 5


celsius = float(input("Digite a temperatura em célsius: "))
resultado = converter_celsius_fahrenheit(celsius)

print(resultado)
