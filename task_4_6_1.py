#6.1. Итератор, генерирующий целые числа, начиная с указанного c заданным шагом (выход из цикла по условию)

from itertools import count

i = 1
start_value = 7
step_value = 6
i_max = 18
stop_value = 100

for el in count(start_value, step_value):
    if el >= stop_value or i > i_max:
        print(f"Пройдено итераций: {i - 1}, последнее значение итератора: {el - step_value}")
        break
    else:
        print(el)
    i += 1

