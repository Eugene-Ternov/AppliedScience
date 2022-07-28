# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Вспомогательная функция: итеративное слияние двух частей

def merge_parts(left, right):
    if not len(left):          # Левая или правая часть пустая - вторая непустая часть уже отсортирована
        return left
    if not len(right):
        return right

    res = []                                # будущие объединённые части
    ind_left = 0                            # левый индекс
    ind_right = 0                           # правый индекс
    total_len = len(left) + len(right)      # итоговая длина объединённых частей

    while len(res) < total_len:                     # цикл до полного объединения элементов
        if left[ind_left] < right[ind_right]:       # сортировка по возрастанию
            res.append(left[ind_left])
            ind_left += 1
        else:
            res.append(right[ind_right])
            ind_right += 1

        if ind_left == len(left) or ind_right == len(right):    # Если левая или правая часть длинее -
            res.extend(left[ind_left:] + right[ind_right:])     # добавляем оставшиеся элементы к результату
            break                                               # (порядок не имеет значения, т.к. один пустой)

    return res

# Основная функция: рекурсивное разделение массива на части с последующим итеративным слиянием

def merge_sort(array, print_steps = True):
    if len(array) < 2:                                  # Один элемент или пустой массив
        return array

    mid = len(array) // 2                               # Середина списка
    left = merge_sort(array[:mid], print_steps)         # Левая часть сортируемого списка (рекурсия)
    right = merge_sort(array[mid:], print_steps)        # Правая часть сортируемого списка (рекурсия)
    merged = merge_parts(left, right)                   # Итеративное слияние левой и правой части
    if print_steps:
        print(f'Левая часть:\t{left}')
        print(f'Правая часть:\t{right}')
        print(f'Объединены в\t{merged}')
    return merged


import random as rnd

print("\nСортировка слиянием (mergesort). Источник: Мюллер Дж. П., Массарон Л. Алгоритмы для чайников: Пер. с англ."
      " - СПб: Диалектика, 2019. - С. 168-170")

size = 11
arr = [rnd.randint(0, 49) for _ in range(size)]
rnd.shuffle(arr)
#arr = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]      # Массив из примера в литературном источнике (мало ли...)
print('\nБыло:\t', arr)

b_print_debug = True                       # Печатать или нет промежуточные разделения и слияния

if b_print_debug:
    print("")

arr = merge_sort(arr, b_print_debug)       # Сортировка слиянием

if b_print_debug:
    print("")
print('Стало:\t', arr)
