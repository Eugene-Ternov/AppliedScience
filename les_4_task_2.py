#2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена» (использовать код одного из прошлых уроков и попробовать его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена» (вспомнить классический способ проверки числа на простоту).

import numpy as np
import cProfile

# Печать результата поиска простого числа

def show_required_simple_digit(order, val):
    print(f"{order}-е по счёту простое число - {val}")

# Поиск простого числа с номером order по порядку с помощью классического алгоритма

def get_simple_digit_by_order_with_classical_algorithm(order):
    if order == 1:
        return 2                            # 1-е по счёту простое число = 2

    simple_digit = 3                        # 2-е по счёту простое число = 3, с него начинаем цикл проверки
    i = 2                                   # проверку начинаем с простого числа 3, его номер по счёту = 2

    while True:                             # надо находить все простые числа от 2-го до заданного номера по счёту
        root = int(np.sqrt(simple_digit))   # целая часть кв. корня из числа (далее - корень)
        if root % 2 == 1:                   # для вхождения нечётного корня в цикл "in range" увеличим корень на 1
            root += 1
        is_simple = True                    # изначально полагаем проверяемое число простым
        # Проверяем от 3 до корня через 2 (делим только нечётное на нечётное, после корня не проверяем,
        for j in range(3, root, 2):         # т.к. это будут зеркальные повторения либо заведомо не делится нацело)
            if simple_digit % j == 0:       # делится нацело - значит не простое
                is_simple = False           # Проверяемое число разделилось нацело, оно не простое
                break
        if is_simple:
            if i == order:                  # выйти из отработанного цикла во избежание увеличения simple_digit на 2
                return simple_digit
            i += 1                          # счётчик увеличиваем только для простых чисел
        simple_digit += 2                   # Начиная с 3 расстояние до следующего потенциально простого числа кратно 2

# Поиск простого числа с номером order по порядку с помощью решета Эратосфена
# Идея: счётчик найденных простых чисел: увеличиваем на 1 при нахождении очередного простого числа.
# Когда будет достигнуто требуемое значение счётчика, последнее найденное простое число и будет искомым результатом
# Для больших значений порядкового номера искомого простого числа массив создаётся несколько раз: при 1-м проходе
# туда для постепенного замещения на 0 помещаются числа 0, 1, 2, 3, ..., n. Если за один проход простое число
# с заданным порядковым номером не найдено, в массив помещаются числа n+1, n+2, ..., 2n и т.д., пока среди них не
# встретится простое число с заданным порядковым номером


def get_simple_digit_by_order_with_eratosthenes_sieve(order):
    if order < 1:
        order = 1               # Для порядка - последний контур контроля
    cnt = 0                     # Счётчик найденных простых чисел
    arr_len = order * 2         # Длина решета для заполнения числами для замены на 0
    if arr_len < 3:
        arr_len = 3             # 2 доп. позиции для 0 и 1, если для них не хватило места: [0, 1, 2, ...]
    elif arr_len > 2000000:     # Для интереса: малая верхняя граница массива замедляет работу для больших order!
        arr_len = 2000000
    offset = 2                  # Начальная позиция для обхода решета: 2 при 1-м обходе, 0 при последующих
    cycle_cnt = 0               # число циклов заполнений и повторных проходов массива
    first_pass_sieve = []       # копия решета после 1-го обхода для поиска поиска простых чисел (2, 3, 5, 7, 11, ...)

    sieve = [i for i in range(arr_len)].copy()      # 1-е заполнение решета: [0, 1, 2, 3, 4, ..., arr_len - 1]

    while cnt < order:
        for i in range(offset, arr_len):
            if sieve[i] != 0:
                cnt += 1
                if cnt == order:                    # Конец: возвращаем искомое простое число
                    return sieve[i]
                # На уроке оперировали с индексом i, т.к. он совпадал с числом. Здесь же нужно с самим числом!
                # (2 - offset) = 0 при offset = 2 (1-й проход массива) и равно 2 при offset = 0 (последующие обходы)
                for j in range((sieve[i] + 2 - offset) * 2, arr_len + 2 - offset, sieve[i] + 2 - offset):
                    sieve[j - 2 + offset] = 0
        # Подготовка массива к очередному поиску простых чисел с замещением на 0 элементов, кратных ранее найденным
        if cycle_cnt == 0:                  # 1-й обход отличается от последующих обходов массива
            offset = 0
            first_pass_sieve = sieve.copy()

        cycle_cnt += 1
        lo_lim = cycle_cnt * arr_len
        for i in range(arr_len):
            sieve[i] = lo_lim + i

        for i in range(2, arr_len):                      # Здесь со 2-го элемента, как при 1-м проходе: пропуск 0 и 1
            if first_pass_sieve[i] != 0:
                for j in range(i * 2, lo_lim + arr_len, i):     # Индекс i совпадает с числом до lo_lim + arr_len
                    if j >= lo_lim:
                        sieve[j - lo_lim] = 0


# Проверка производительности поиска простого числа с заданным порядковым номером

b_use_cprofile = True
i_switch = 1            # 0 - классический алгоритм, 1 - решето Эратосфена, 2 и иное - обе функции

if not b_use_cprofile:

    try:
        num_order = int(input("Введите порядковый номер простого числа, которое Вы хотите определить: "))
        if num_order < 1:
            num_order = 1
    except:
        num_order = 1

    if i_switch != 1:
        print("Классический алгоритм: ", end="")
        show_required_simple_digit(num_order, get_simple_digit_by_order_with_classical_algorithm(num_order))
    elif i_switch != 0:
        print("Решето Эратосфена:     ", end="")
        show_required_simple_digit(num_order, get_simple_digit_by_order_with_eratosthenes_sieve(num_order))
else:
    num_order = 500000
    s = 0
    if i_switch != 1:
        cProfile.run("s = get_simple_digit_by_order_with_classical_algorithm(num_order)")
        print("Классический алгоритм: ", end="")
        show_required_simple_digit(num_order, s)
    elif i_switch != 0:
        cProfile.run("s = get_simple_digit_by_order_with_eratosthenes_sieve(num_order)")
        print("Решето Эратосфена:     ", end="")
        show_required_simple_digit(num_order, s)

# № простого числа		Классический алгоритм, с		Решето Эратосфена, с        Простое число
# -----------------------------------------------------------------------------------------------
# 	    1000			        0,018				            0,006                   7919
# 	    10000			        0,284				            0,127                   104729
# 	    25000			        0,919				            0,310                   287117
# 	    50000			        2,286				            0,814                   611953
# 	    100000			        6,179				            1,685                   1299709
# 	    200000			        15,921				            3,542                   2750159
# 	    500000			        56,418				            11,043                  7368787

#       Видно, что до 50000-го числа включительно решето Эратосфена быстрее в 3 раза, далее в 4-5 раз
#       Создание массива в авторской модификации решета Эратосфена даёт один рекурсивный вызов, что приемлемо
#       Сложность классического алгоритма квадратичная - из-за деления каждого числа на простые числа от 3 до целой
#       части корня из проверяемого числа
#       Сложность решета Эратосфена линейная; квадратичный компонент при использовании копии массива для больших
#       значений порядкового номера (может быть взята не 2000000, а максимально допустимый размер массива в python.
#       Установлено: малые значения данного массива при большом порядковом номере искомого простого числа, наоборот,
#       замедляют алгоритм решета Эратосфена по сравнению с классическим.


# ============================ Классический алгоритм ==============================

    #          4 function calls in 0.018 seconds

    #    Ordered by: standard name

        # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #    1    0.000    0.000    0.018    0.018 <string>:1(<module>)
        #    1    0.018    0.018    0.018    0.018 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #    1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
        #    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 1000-е по счёту простое число - 7919

    #          4 function calls in 0.284 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    0.283    0.283 <string>:1(<module>)
        #       1    0.283    0.283    0.283    0.283 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000    0.284    0.284 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 10000-е по счёту простое число - 104729

    #          4 function calls in 0.919 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    0.919    0.919 <string>:1(<module>)
        #       1    0.919    0.919    0.919    0.919 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000    0.919    0.919 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 25000-е по счёту простое число - 287117

    #          4 function calls in 2.286 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    2.285    2.285 <string>:1(<module>)
        #       1    2.285    2.285    2.285    2.285 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000    2.286    2.286 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 50000-е по счёту простое число - 611953

    #          4 function calls in 6.179 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    6.179    6.179 <string>:1(<module>)
        #       1    6.179    6.179    6.179    6.179 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000    6.179    6.179 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 100000-е по счёту простое число - 1299709

    #          4 function calls in 15.921 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000   15.921   15.921 <string>:1(<module>)
        #       1   15.921   15.921   15.921   15.921 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000   15.921   15.921 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 200000-е по счёту простое число - 2750159

    #          4 function calls in 56.418 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000   56.418   56.418 <string>:1(<module>)
        #       1   56.418   56.418   56.418   56.418 les_4_task_2.py:17(get_simple_digit_by_order_with_classical_algorithm)
        #       1    0.000    0.000   56.418   56.418 {built-in method builtins.exec}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Классический алгоритм: 500000-е по счёту простое число - 7368787

# ============================ Решето Эратосфена ==============================

    #          7 function calls in 0.006 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        #       1    0.006    0.006    0.006    0.006 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.000    0.000    0.000    0.000 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        #       2    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     1000-е по счёту простое число - 7919

    #          7 function calls in 0.127 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.000    0.000    0.127    0.127 <string>:1(<module>)
        #       1    0.125    0.125    0.127    0.127 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.001    0.001    0.001    0.001 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    0.127    0.127 {built-in method builtins.exec}
        #       2    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     10000-е по счёту простое число - 104729

    #          7 function calls in 0.310 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.001    0.001    0.310    0.310 <string>:1(<module>)
        #       1    0.305    0.305    0.309    0.309 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.003    0.003    0.003    0.003 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    0.310    0.310 {built-in method builtins.exec}
        #       2    0.001    0.001    0.001    0.001 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     25000-е по счёту простое число - 287117

    #          7 function calls in 0.814 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.002    0.002    0.814    0.814 <string>:1(<module>)
        #       1    0.803    0.803    0.812    0.812 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.006    0.006    0.006    0.006 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    0.814    0.814 {built-in method builtins.exec}
        #       2    0.004    0.002    0.004    0.002 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     50000-е по счёту простое число - 611953

    #          7 function calls in 1.685 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.005    0.005    1.685    1.685 <string>:1(<module>)
        #       1    1.660    1.660    1.680    1.680 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.015    0.015    0.015    0.015 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    1.685    1.685 {built-in method builtins.exec}
        #       2    0.006    0.003    0.006    0.003 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     100000-е по счёту простое число - 1299709

    #          7 function calls in 3.542 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.009    0.009    3.542    3.542 <string>:1(<module>)
        #       1    3.488    3.488    3.533    3.533 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.033    0.033    0.033    0.033 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    3.542    3.542 {built-in method builtins.exec}
        #       2    0.012    0.006    0.012    0.006 {method 'copy' of 'list' objects}
        #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     200000-е по счёту простое число - 2750159

    #          7 function calls in 11.043 seconds

    #    Ordered by: standard name

        #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #       1    0.022    0.022    11.043   11.043 <string>:1(<module>)
        #       1   10.901   10.901    11.021   11.021 les_4_task_2.py:44(get_simple_digit_by_order_with_eratosthenes_sieve)
        #       1    0.091    0.091     0.091    0.091 les_4_task_2.py:57(<listcomp>)
        #       1    0.000    0.000    11.043   11.043 {built-in method builtins.exec}
        #       2    0.028    0.014     0.028    0.014 {method 'copy' of 'list' objects}
        #       1    0.000    0.000     0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Решето Эратосфена:     500000-е по счёту простое число - 7368787


