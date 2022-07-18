#1. Проанализировать скорость и сложность одного любого алгоритма из домашних заданий первых трёх уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать
# b. написать 3 варианта кода (один у вас уже есть)
# c. проанализировать 3 варианта и выбрать оптимальный
# d. результаты анализа вставить в виде комментариев в файл с кодом (указать, для каких N проведены замеры)
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# В качестве примера используем задачу 4 к уроку 2, т.к. там просматриваются 3 варианта кода, в т.ч. с рекурсией

#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

import timeit
import cProfile

# 1 Рекурсия

def method_1(count):
    if count > 1:
        count -= 1
        return (2 ** -count) * ((-1)**(count % 2)) + method_1(count)
    elif count == 1:
        return 1
    else:
        return 0

# 2 Цикл со степенью

def method_2(count):
    res = 0
    for i in range(count):
        res += (2 ** -i) * ((-1) ** (i % 2))
    return res

# 2 Цикл с делением на 2

def method_3(count):
    if count > 1:
        member = 1
        res = 1
        for i in range(2, count + 1):
            member /= -2
            res += member
        return res
    elif count == 1:
        return 1
    else:
        return 0

n = 984
#s = method_1(n)
cProfile.run("s = method_1(n)")

# Разные методы нахождения суммы 984 элементов ряда (984 < 1000 потому, что вызов timeit снижал на 985...1000 выдавал
# ошибку переполнения стека при рекурсивных вызовах; поэтому это число было сохранено и для проверки с cProfile)
# выполнялись примерно с одинаковой скоростью из-за простоты алгоритма и краткости арифметических операций.
# Сложность константная

#n = 984
#s = method_1(n)
#PS D:\PythonProjects\GeekBrains\algorhytm_homework_4> python -m timeit -n 1000 -s "import les_4_task_1"
#1000 loops, best of 5: 11.3 nsec per loop

#987 function calls (4 primitive calls) in 0.003 seconds

#Ordered by: standard name

# ncalls tottime percall cumtime percall filename:lineno(function)
#     1 0.000 0.000 0.003 0.003 <string>:1(< module >)
# 984/1 0.003 0.000 0.003 0.003 les_4_task_1.py:18(method_1)
#     1 0.000 0.000 0.003 0.003 {built-in method builtins.exec}
#     1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

#s = method_2(n)
#PS D:\PythonProjects\GeekBrains\algorhytm_homework_4> python -m timeit -n 1000 -s "import les_4_task_1"
#1000 loops, best of 5: 11.8 nsec per loop

#4 function calls in 0.001 seconds

#Ordered by: standard name

# ncalls tottime percall cumtime percall filename:lineno(function)
# 1 0.000 0.000 0.001 0.001 <string>:1(<module>)
# 1 0.001 0.001 0.001 0.001 les_4_task_1.py:29(method_2)
# 1 0.000 0.000 0.001 0.001 {built-in method builtins.exec}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

#s = method_3(n)
#PS D:\PythonProjects\GeekBrains\algorhytm_homework_4> python -m timeit -n 1000 -s "import les_4_task_1"
#1000 loops, best of 5: 11.3 nsec per loop

#4 function calls in 0.001 seconds

#Ordered by: standard name

# ncalls tottime percall cumtime percall filename: lineno(function)
# 1 0.000 0.000 0.000 0.000 <string>:1(<module>)
# 1 0.000 0.000 0.000 0.000 les_4_task_1.py:37(method_3)
# 1 0.000 0.000 0.001 0.001 {built-in method builtins.exec}
# 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}
