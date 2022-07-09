#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

is_random_arr = False        # Случайный или отладочный массив
if is_random_arr:
    arr = [random.randint(-1000, 1000) for _ in range(100000)]
else:
    arr = [1, 2, 3, 23, 4, 5, 18, 0, 9]

max_el = arr[0]
min_el = arr[0]
max_el_pos = 0
min_el_pos = 0

for i, el in enumerate(arr):
    if el > max_el:
        max_el = el
        max_el_pos = i
    elif el < min_el:
        min_el = el
        min_el_pos = i

if abs(min_el_pos - max_el_pos) < 2:
    print("\nМежду минимальным и максимальным элементами массива нет других элементов, задача не имеет решения")
    exit(0)

if min_el_pos > max_el_pos:
    min_el_pos, max_el_pos = max_el_pos, min_el_pos

s = 0
for i in range(min_el_pos + 1, max_el_pos):
    s += arr[i]

print(f"\nСумма элементов одномерного массива, находящихся между минимальным и максимальным элементами, равна {s}")