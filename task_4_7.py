#7. Вычисление факториала при помощи функции, возвращающей yield

# Вычисление факториала от аргумента arg

def fac_int(arg):
    result = 1
    for i in range(1, arg + 1):
        result *= i
    return result

# Формирование массива факториалов от 1! до arg!

def fac(arg):
    fac_list = [fac_int(i) for i in range(1, arg + 1)]
    for el in fac_list:
        yield el

# Главная функция

print("Массив факториалов от 1! до 5!")
for el in fac(5):
    print(f"\t{el}", end = '')
