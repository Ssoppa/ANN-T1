import matplotlib.pyplot as plt
import numpy as np
import math


def funcao(x):
    # return 1 / (1 + x ** 2)
    # return 1 / (math.sqrt(1 + x ** 2))
    return 2 / (1 + x ** 2)

# pontos_dados = [-2, -1, 1, 2]
# pontos_dados = [-2, -1, 0, 1, 2]
# pontos_dados = [0, 0.3, 0.9, 1.3, 2]
# pontos_dados = [-1.97, -1.16, -0.34, 0.32, 0.38, 0.61, 1.09, 1.44, 1.81, 1.82]
pontos_dados = [-4.65, -4.62, -4.39, -4.25, -4.01, -3.6, -3.52, -2.52, -0.75, 0.47, 0.77, 0.78, 1.44, 2.45, 2.91, 3.06, 3.17, 3.7, 4.49, 4.83]

pontos = [(x, funcao(x)) for x in pontos_dados]
xs, ys = zip(*pontos)
n = len(xs) - 1
h = {k: xs[k+1] - xs[k] for k in range(n)}
a = {k: v for k, v in enumerate(ys)}

matrix = []
first_row = [1] + [0 for _ in range(n)]
matrix.append(first_row)
for i in range(1, n):
    zeros_before = [0 for _ in range(i - 1)]
    zeros_after = [0 for _ in range(i + 1, n)]
    row = zeros_before + [h[i - 1], 2 * (h[i - 1] + h[i]), h[i]] + zeros_after
    matrix.append(row)
last_row = [0 for _ in range(n)] + [1]
matrix.append(last_row)

B = [0] + [3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1]) / h[k-1] for k in range(1, n)] + [0]

solucao = np.linalg.solve(matrix, B)
c = {k: v for k, v in enumerate(solucao)}

b = {k: (a[k+1] - a[k]) / h[k] - h[k] * (2 * c[k] + c[k+1]) / 3 for k in range(n)}

d = {k: (c[k+1] - c[k]) / (3 * h[k]) for k in range(n)}

intvls = {k: [xs[k], xs[k+1]] for k in range(n)}
def sign(x):
    if x < 0:
        return str(x)
    return f'+{x}'

print(intvls)

eq = {k: f'{a[k]}{sign(b[k])}*(x{sign(-xs[k])}){sign(c[k])}*(x{sign(-xs[k])})**2{sign(d[k])}*(x{sign(-xs[k])})**3' for k in range(n)}
polinomios = []
for k, v in eq.items():
    polinomios.append(v)

t = [-4 + i * (8 / 999) for i in range(1000)]
ft = [funcao(i) for i in t]
# plt.plot(t, ft, label="gráfico de $f(x)=\\frac{2}{1 + x^2}$")
plt.plot(t, ft, label="gráfico da função")

for k, p in eq.items():
    def s(x):
        return eval(p)
    a, b = xs[k], xs[k + 1]
    t = np.arange(a, b, 0.01)
    plt.plot(t, s(t), label="polinômio interpolador")
plt.scatter(xs, ys)
plt.legend()
plt.title(f"{n} pontos")
plt.show()

print(polinomios)
