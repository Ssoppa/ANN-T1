import math
# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x

def g(x):
    # return (x + 7 / x) / 2
    # return (x + 11 / x ** 2) / 2
    # return math.sqrt(11 / x)
    # return x - (((x ** 3) - 11) / (3 * (x ** 2)))
    # return math.log(2 * x + 1)
    # return (x + 4) ** (1/3)
    # return (x ** 2 + 5) ** (1 / 4)
    return (math.sin(x) + 4) / 2

n = 10
a, b = [2, 3]
x0 = 2.2
itr = []
for i in range(n):
    xn = g(x0)
    x0 = xn
    itr.append(x0)
    print(i, x0)
print(itr)
