#3. Функция, принимающая 3 позиционных аргумента с возвратом суммы 2-х наибольших

def my_func(arg1, arg2, arg3):
    """
    Функция my_func(arg1, arg2, arg3)
    Принимает 3 аргумента
    На выходе: сумма 2-х наибольших аргументов или текст исключения, например, при нечисловых аргументах
    """
    try:
        return max(arg1 + arg2, arg1 + arg3, arg2 + arg3)   # попарное сложение всех аргументов, т.к. 2 наибольших
    except Exception as exp:
        return exp

def my_func_alt(*args):      # Для произвольного числа аргументов задачу можно упростить
    """
    Функция my_func_alt(arg1, arg2, arg3)
    Принимает произвольное число аргументов как кортеж *arg
    На выходе: сумма 2-х наибольших аргументов или текст исключения, например, при нечисловых аргументах и др.
    """
    try:
        my_list = list(args)
        my_list.sort(reverse=True)
        return my_list[0] + my_list[1]
    except Exception as exp:
        return exp

print(my_func.__doc__)
print(my_func_alt.__doc__)
a = 5
b = 21
c = 7
print("Результат my_func:", my_func(a, b, c))
print("Результат my_func_alt:", my_func_alt(a, b, c))
