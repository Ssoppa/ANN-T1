# matriz = [[4, 1, 1, 6], [2, 5, 2, 3], [1, 2, 4, 11]]
# matriz = [[3, 2, 1, 2], [2, 7, 2, -3], [1, 3, 5, 3]]
# matriz = [[1, 1, -3, 5], [0, -2, 1, -3], [-4, 1, -1, -2]]
matriz = [[3, 1, 1, 1], [1, -4, 2, 3], [1, -3, 5, -1]]

col = len(matriz[0])
linha = len(matriz)

for i in range(linha):
    if (matriz[i][i] == 0):
        for j in range(i + 1, linha):
            if (matriz[j][i] != 0):
                aux = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = aux
                break
        else:
            print("Matriz impossível de ser escalonada!")
            break
    for j in range(i + 1, linha):
        a = -matriz[j][i] / matriz[i][i]
        print(f"{a} * L{i} + L{j}")
        for k in range(i, col):
            matriz[j][k] += matriz[i][k] * a

print()
for row in matriz:
    print(row)
