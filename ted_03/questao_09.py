# 9) Determine os resultados obtidos na avaliação das expressões lógicas seguintes,
# sabendo que a, b, c contêm, respectividamente 2, 7, 3.5, e que existe uma variável
# lógica L cujo o valor é false.
# a) b == a * c and l
# b) b > a or b == a^a
# c) l and b % a >= c or not a <= c
# d) b/a == c or b/a != c

a = 2
b = 7
c = 3.5
l = False

valorA = b == a * c and l
valorB = b > a or b == a ^ a
valorC = l and b % a >= c or not a <= c
valorD = b/a == c or b/a != c

print("a) b == a * c and l: ", valorA)
print("b) b > a or b == a^a: ", valorB)
print("c) l and b % a >= c or not a <= c: ", valorC)
print("d) b/a == c or b/a != c: ", valorD)

