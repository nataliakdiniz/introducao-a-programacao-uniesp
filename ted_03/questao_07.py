# 7) PROGRAMA COTAÇÃO – O usuário digita quanto está valendo o dólar e quanto em reais ele possui. O
# programa exibe quantos dólares vale os reais que o usuário informou.


def converter_real_dolar(dolar, real):
    return dolar * real


dolar = float(input("Digite a cotação atual do dólar: "))
real = float(input("Digite quantos reais você possui: "))
resultado = converter_real_dolar(dolar, real)

print(resultado)
