# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша hash(), sha1() или любой другой из модуля hashlib
# задача считается нерешённой.

import hashlib

def get_different_substring_count(text: str, print_intermed=False) -> int:

    subs_set = set()    # В множество помещаются только уникальные значения
    length = len(text)
    cnt = 0
    for i in range(length):
        for j in range(length - 1 if i == 0 else length, i, -1):
            s = text[i:j]
            hsh = hash(s)
            subs_set.add(hsh)
            if print_intermed:
                sp = ' ' * (length + 2 - len(s))
                print(f"{s}{sp} i: {i} j: {j}, хеш: {hsh}")
            cnt += 1

    return len(subs_set), cnt


src = input('\nВведите строку: ')
sl = len(src)
b_print_debug = True

if b_print_debug and sl > 1:
    print('')

set_length, parts_count = get_different_substring_count(src, b_print_debug)

print(f"\nДлина заданной строки '{src}' равна {sl}")
print(f"Количество подстрок в заданой строке (без полной строки): выделено - {parts_count},"
      f" из них уникальных - {set_length}")