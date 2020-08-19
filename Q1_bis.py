import math


# uma função qualquer
def f(x):
    # return x ** 5 - 8 * x - 2
    # return math.cos(x ** 2) - x
    # return math.log(x) + x ** 2
    # return math.log(x ** 2) + 2 * x
    # return math.cos(math.sin(x ** 2)) + x ** 3 - 2
    return (math.e ** math.cos(x)) + math.log(x ** 2)
    # return (math.e ** math.cos(x)) + math.log(x ** 2)
    # return ((x ** 2) * math.cos(x)) + x - 1
    # return 2 * math.cos(math.e ** x) - x
    # return x ** 3 + x ** 2 + 0.001


# método da bisseção
a, b = [1, 2]
n = 10  # número de iterações
raizes = []
for i in range(n):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0:  # teorema de Bolzano
        b = m
    else:
        a = m
    print(i, m, f(2.2375640774059926))
    raizes.append(m)

print(raizes)
