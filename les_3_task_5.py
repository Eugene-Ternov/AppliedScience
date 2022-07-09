#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random

arr_len = 100000
arr = [random.randint(-1000, 1000) for _ in range(arr_len)]
max_neg_el = 0
max_neg_pos = -1

for i, el in enumerate(arr):
    if el < 0 and (max_neg_el == 0 or max_neg_el < el):
        max_neg_el = el
        max_neg_pos = i

print(f'\nМаксимальное отрицательное число в массиве из {arr_len} элементов {max_neg_el}, его позиция {max_neg_pos}')
