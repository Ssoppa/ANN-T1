import sympy as sy
import math

n = 4  # ordem do erro
x0 = 1
h = .1
p = 2


def f(x):
    # return math.cos(x ** x)
    # return math.sin(x)
    # return x ** math.cos(x)
    return math.e ** -(x ** 2)


def F1_1(h):
    return (f(x0) - f(x0 - h)) / h


def F1_2(h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)


def F1_3(h):
    return (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)



def Fk(h, n, p):
    # I'm recursive :)
    if n == 1:
        return F1_3(h)
    n -= 1
    return (2 ** (n * p) * Fk(h/2, n, p) - Fk(h, n, p)) / (2 ** (n * p) - 1)


print('aprox:', Fk(h, n, p))

x = sy.Symbol('x')
# string = 'cos(x ** x)'
# string = 'sin(x)'
# string = 'x ** cos(x)'
string = 'E ** -(x ** 2)'
func = sy.sympify(string)
df = sy.diff(func, x, 1).subs(x, x0).evalf()
print('exact:', df)
