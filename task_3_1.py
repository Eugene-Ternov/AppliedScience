#1. Функция с 2-мя позиционными параметрами и обработкой ситуации деления на ноль

def simple_division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return 'Деление на ноль'
    except Exception as exp:        # Не обрабатываемые явно типы исключений должны идти в конце
        return exp

print(f"{simple_division(3.1416, 0.9182):.4f}")
print(simple_division('Евгений', 3))
print(simple_division(False, True))
print(simple_division(True, False))
print(simple_division('Евгений', 3))
print(simple_division(5, 0))
