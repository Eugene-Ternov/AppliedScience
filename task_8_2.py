#2. Пользовательский класс исключения при делении на нуль

class OwnZeroDivide(Exception):
    def __init__(self, message):
        self.message = message


while (True):
    s = input("Введите любое число: ").strip()
    try:
        a = float(s)
    except ValueError:
        print("Это было не число. Ещё раз, пожалуйста.")
    else:
        print("Вы ввели", a)
        break

while (True):
    s = input("Введите ноль или другое число: ").strip()
    try:
        b = float(s)
        if b == 0:
            raise OwnZeroDivide("Вы предотвратили деление на ноль!")
    except ValueError:
        print("Это было не число. Ещё раз, пожалуйста.")
        continue
    except OwnZeroDivide as err:
        print(err)
    else:
        print (f"Результат деления {a} : {b} = {a / b:.1f}")
    break
