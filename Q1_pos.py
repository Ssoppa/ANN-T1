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
a, b = [-2, -1.5]
itr = []
for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(xn) == 0:
        print('A raiz é:', xn)
    elif f(a) * f(xn) < 0:
        b = xn
    else:
        a = xn
    itr.append(xn)

print(itr)
