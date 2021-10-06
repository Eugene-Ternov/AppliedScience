#6.2. Повторение элементов списка вызовом итератора с завершением по условию

from random import randrange
from itertools import cycle

chr_list = [chr(randrange(ord('a'), ord('z'), i)) for i in range(1, 11)]
print("Список элементов для повторения:", chr_list)

iter = cycle(chr_list)

print("Начальные единичные вызовы итератора (next()) - 3 шт.:")
for i in range(0, 3):
    print(f"\t{next(iter)}", end = '')

print("\nЦиклические вызовы итератора (in cycle([]) - 20 шт.:")

i = 1
for el in cycle(chr_list):
    print(f"\t{el}", end = '')
    if i == 20:
        break
    elif i == 10:
        print("")
    i += 1

print("\nПромежуточные единичные вызовы итератора (next()) - 3 шт.:")
for i in range(0, 3):
    print(f"\t{next(iter)}", end = '')

print("\nЦиклические вызовы итератора (in cycle([]) - 7 шт.:")

i = 1
for el in cycle(chr_list):
    print(f"\t{el}", end = '')
    if i > 7:
        break
    i += 1

print("\nЗавершающие единичные вызовы итератора (next()) - 8 шт.:")
for i in range(0, 8):
    print(f"\t{next(iter)}", end = '')

print("\nТаким образом, вызовы next() начинаются с 1-го элемента списка и далее продолжаются с очередной позиции,")
print("переходя через границу списка. Это происходит независимо от промежуточных вызовов итератора при помощи")
print("конструкции for in cycle(), в которой вызов начинается с 1-го элемента списка и заканчивается")
print("прозвольной позицией.")



