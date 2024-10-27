def get_matrix (n, m, valuo):
    matrix = []
# внешний цикл для добавления строки
    for i in range(n):
        row = [valuo] * m
        for i in range (m):
            matrix.append (valuo)

        matrix.append (row)
        return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
