#1. Сложение 2-х матриц с перегрузкой оператора "+" (при неравенстве размеров по-простому вернём None)

from random import randint

class Matrix:
    def __init__(self, list_arg):
        self.__matrix = list(list_arg)

    def __str__(self):
        return f"{self.__matrix}"

    def __add__(self, other):
        try:                        # для больших размерностей лучше сначала по размерам пробежаться, наверное
            result = []
            for i in range(len(self.__matrix)):
                result.append([])
                for j in range(len(self.__matrix[i])):
                    result[i].append(self.__matrix[i][j] + other.__matrix[i][j])
            return Matrix(result)
        except:
            return None



row_count = randint(1, 5)       # число строк
col_count = randint(1, 5)       # число столбцов

print('')
A = Matrix([[randint(-15, 15) for j in range(col_count)] for i in range(row_count)])
B = Matrix([[randint(-15, 15) for j in range(col_count)] for i in range(row_count)])
print(f"A = {A}")
print(f"\nB = {B}")
print(f"\nA + B = {A + B}")
