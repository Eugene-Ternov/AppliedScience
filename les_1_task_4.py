#4. Определить, какое число в массиве встречается чаще всего.


import random

arr_len = 50
arr = [random.randint(-5, 5) for _ in range(arr_len)]
arr_unique = set(arr)
arr_dict = {}

for el in arr_unique:                   # Словарь "уникальный элемент - количество вхождений в массив"
    arr_dict.update({el:arr.count(el)})

print(f"\nИсходный массив:\n\n{arr}")
print("\nУникальные элементы, образующие массив:" + (" " * 20), end='')

for key in arr_dict.keys():
    print(f'{key:>4}', end='')

print("\nЧисло вхождений элемента в массив:" + (" " * 25), end='')

for val in arr_dict.values():
    print(f'{val:>4}', end='')

#Наиболее часто встречающиеся числа в массиве (в общем случае больше одного)

max_count = 0

for val in arr_dict.values():               # 1-й проход - максимальное количество вхождений любого элемента в массив
    if max_count == 0 or val > max_count:
        max_count = val

arr_unique.clear()                          # Сюда будем добавлять элементы (напомним, они уникальны)

for key, val in arr_dict.items():           # 2-й проход - какие элементы входят максимальное число раз
    if val == max_count:
        arr_unique.add(key)

print(f"\n\nНаиболее часто с числом вхождений {max_count} в массиве встречаются элементы {arr_unique}")