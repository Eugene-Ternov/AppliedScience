#7. Комплексные числа

class ComplexNumber:
    AfterDecPoint = 0                   # Сколько знаков после запятой отображать на печати (для интереса)
    def __init__(self, re, im):
        try:
            self.__after_dec_point = 2
            self.__re = float(re)
            self.__im = float(im)
        except ValueError:
            self.__re = 0
            self.__im = 0

    def __str__(self):
        if self.__re == 0:
            if self.__im == 0:
                return "0"
            elif self.__im == 1:
                return "i"
            elif self.__im == -1:
                return "-i"
        return f"({self.__re:.{self.AfterDecPoint}f}, {self.__im:.{self.AfterDecPoint}f})"

    def __add__(self, other):
        return ComplexNumber(self.__re + other.__re, self.__im + other.__im)

    def __sub__(self, other):
        return ComplexNumber(self.__re - other.__re, self.__im - other.__im)

    def __mul__(self, other):
        return ComplexNumber(self.__re * other.__re - self.__im * other.__im,
                             self.__re * other.__im + other.__re * self.__im)

    def __truediv__(self, other):
        if other.__re == 0 and other.__im == 0:
            return None
        else:
            if __name__ == "__main__":
                ComplexNumber.AfterDecPoint = 2     # тут будет явная дробь
            return ComplexNumber((self.__re * other.__re + self.__im * other.__im) /
                                 (other.__re ** 2 + other.__im ** 2),
                                 (self.__im * other.__re - self.__re * other.__im) /
                                 (other.__re ** 2 + other.__im ** 2))


# Основная программа

print('')
a = ComplexNumber(1, 5)
b = ComplexNumber(2, -3)

print(f"Даны комплексные числа a = {a} и b = {b}")
print(f"Сложение: {a} + {b} = {a + b}")
print(f"Умножение: {a} * {b} = {a * b}")
print(f"Вычитание: {a} - {b} = {a - b}")

a = ComplexNumber(3, 1)
print("-------------------------------------")
print(f"Пусть a = {a}, b = {b}")
print(f"Деление: {a} / {b} = {a / b}")
print("Ответы сходятся с примерами из учебника")



