#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random

matrix = []
row = []
rows_count = 6
cols_count = 8

# Формирование матрицы

for i in range(rows_count):
    row.clear()
    for j in range(cols_count):
        row.append(random.randint(-20, 50))
    matrix.append(row.copy())

print("\nМатрица:\n")
for i in range(rows_count):
    for j in range(cols_count):
        print(f'{matrix[i][j]:>5}', end='')
    print("")

print("\nМинимальные элементы столбцов матрицы:\n")

row.clear()
for j in range(cols_count):
    row.append(matrix[0][j])
    for i in range(1, rows_count):
        if matrix[i][j] < row[j]:
            row[j] = matrix[i][j]

max_el = row[0]
for j in range(cols_count):
    print(f'{row[j]:>5}', end='')
    if max_el < row[j]:
        max_el = row[j]

print(f'\n\nМаксимальный элемент среди минимальных элементов столбцов матрицы равен {max_el}')





