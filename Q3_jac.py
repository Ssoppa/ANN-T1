# E = [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]]
# E = [[3, 2, 1, 2], [2, 7, 2, -3], [1, 3, 5, 3]]
# E = [[1, 1, -3, 5], [0, -2, 1, -3], [-4, 1, -1, -2]]
E = [[3, 1, 1, 1], [1, -4, 2, 3], [1, -3, 5, -1]]

n = 10
itr = []
chute = [0, 0, 0]
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    itr.append(xn)
    chute = xn

print(itr)
