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

# derivada de f
def df(x):
    # return 5 * x ** 4 - 8
    # return -2 * x * math.sin(x ** 2) - 1
    # return 2 * x + 1 / x
    # return (2 / x) + 2
    # return x * (3 * x - 2 * math.sin(math.sin(x ** 2)) * math.cos(x ** 2))
    # return (-2 * math.e ** (-x ** 2) - 2) * x
    # return (2 / x) - (math.sin(x) * (math.e ** math.cos(x)))
    # return (x ** 2) * (-math.sin(x)) + 2 * x * math.cos(x) + 1
    # return -2 * math.e ** x * math.sin(math.e ** x) - 1
    return x * (3 * x + 2)

x0 = -2
n = 10
itr = []
itr.append(x0)
for i in range(1, n):
    itr.append(x0 - f(x0) / df(x0))
    x0 = itr[i]

print(itr)
