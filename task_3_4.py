#4. Функция возведения числа в степень бех pow() и **

def my_func(figure, power):
    try:
        power = int(power)
        if power == 0 or figure == 1:
            return 1
        elif figure == 0 and power < 0:
            return 'Деление на ноль'
        elif figure == 0:
            return 0
        else:
            result = figure
            for i in range(abs(power) - 1):
                result *= figure
            if power < 0:
                result = 1 / result
            return result
    except Exception as exp:
        return exp

figure = 0
power = -3

print(f"Возведение {figure} в степень {power}")
print("Моя функция:", my_func(figure, power))
try:
    print("С использованием **:", figure ** power)
except Exception as exp:
    print("С использованием **:", exp)
