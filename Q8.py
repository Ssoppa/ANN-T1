import math


def f(x):
    # return math.cos(x ** x)
    # return math.sin(x)
    # return x ** math.cos(x)
    return math.e ** -(x ** 2)


def f1(x0, h):
    return (f(x0) - f(x0 - h)) / h


def f2(x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)


def f3(x0, h):
    return (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)


hs = [0.1, 0.05, 0.025, 0.0125]
x0 = 1
res = []
for h in hs:
    valor = f3(x0, h)
    res.append(valor)
    print('aprox:', valor)

import sympy as sy

x = sy.Symbol('x')
# string = 'cos(x ** x)'
# string = 'sin(x)'
# string = 'x ** cos(x)'
string = 'E ** -(x ** 2)'
func = sy.sympify(string)
df = sy.diff(func, x, 1).subs(x, x0)
print('exact:', df.evalf())

print()
print(res)
