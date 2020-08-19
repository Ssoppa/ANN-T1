import numpy as np
import math

# pontos = [(x, x ** x) for x in [0.99, 1, 1.01]]
pontos = [(x, math.cos(x)) for x in [0.99, 1, 1.01, 1.02]]
# pontos = [(x, math.e ** x) for x in [0.98, 0.99, 1, 1.01]]
n = len(pontos)
def vandermond(pontos):
    xs, ys = zip(*pontos)
    A = [[x ** k for k in range(n)] for x in xs]
    B = ys
    a = np.linalg.solve(A, B)
    return a

a = vandermond(pontos)

def p(x):
    px = sum([a[k] * x ** k for k in range(n)])
    return px

def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

def equation(pontos):
    eq = ""
    eq += "".join([f'{sign(a[k])}*x**{k}' for k in range(n)])
    return eq

eq = equation(pontos)

x0 = 1

def f_der1(x0, h):
    x = x0 + h
    valor = eval(eq)
    x = x0 - h
    valor -= eval(eq)
    return valor / (2 * h)

def f_der2(x0, h):
    x = x0 - h
    valor = eval(eq)
    x = x0
    valor -= 2 * eval(eq)
    x = x0 + h
    valor += eval(eq)
    return valor / h ** 2

def f_der3(x0, h):
    x = x0 + (-2 * h)
    valor = (-1 / 2) * eval(eq)
    x = x0 + (-1 * h)
    valor += eval(eq)
    x = x0 + (1 * h)
    valor -= eval(eq)
    x = x0 + (2 * h)
    valor += (1 / 2) * eval(eq)
    return valor / (h ** 3)


res = []
hs = [0.1, 0.05, 0.025, 0.0125]
for h in hs:
    valor = f_der3(x0, h)
    res.append(valor)
    print('aprox:', valor)

import sympy as sy

x = sy.Symbol('x')
# string = 'x ** x'
string = 'cos(x)'
# string = 'E ** x'
f = sy.sympify(string)
df = sy.diff(f, x, 3).subs(x, x0)
print('exact:', df.evalf())
print()
print(res)
print(eq)
