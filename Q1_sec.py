import math

# uma função qualquer
def f(x):
    # return x ** 5 - 8 * x - 2
    # return math.cos(x ** 2) - x
    # return math.log(x) + x ** 2
    # return math.log(x ** 2) + 2 * x
    # return math.cos(math.sin(x ** 2)) + x ** 3 - 2
    # return (math.e ** (-x ** 2)) - (x ** 2) + 5
    # return (math.e ** math.cos(x)) + math.log(x ** 2)
    # return ((x ** 2) * math.cos(x)) + x - 1
    # return 2 * math.cos(math.e ** x) - x
    return x ** 3 + x ** 2 + 0.001

n = 10
x0, x1 = [-2, -1.5]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
for i in range(n):
    try:
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # a - f(a) / ((f(b) - f(a))/ (b - a))
    except:
        raise ValueError(f"Divisão por zero para {a}, {b} na iteração {i}")
    itr[i + 2] = xn
    a, b = b, xn

lista = []
for k, v in itr.items():
    lista.append(v)

print(lista)