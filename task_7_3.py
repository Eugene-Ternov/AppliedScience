#3. Немного о загадке жизни: размножение и дробление клеток (с перегрузкой операторов класса и с учётом рядов)
#   Для науки: переменные уровня класса аналогичны статическим членам класса в С++

class BioCellChain:
    InheritRows = False        # Если True - к результату арифметической операции применится make_order
                               # с минимальной длиной ряда у одного из двух операндов
    def __init__(self, count):
        self.__cell_count = count if count > 0 else 1
        self.__clear_chain()

    # Очистка рядов в цепочке клетке

    def __clear_chain(self):
        self.__chain = '*' * self.__cell_count
        self.__row_size = self.__cell_count
        return self  # На случай вызова _BioCellChain__clear_chain() через точку после конструктора не помешало бы

    # Разделение цепочки клеток на ряды заданной длины

    def make_order(self, row_size):
        if not (row_size == self.__row_size or row_size < 0):
            self.__clear_chain()
            if not (row_size == 0 or row_size >= self.__cell_count):
                self.__row_size = row_size
                self.__chain = ''
                for i in range(self.__cell_count // self.__row_size):
                    self.__chain += ('*' * self.__row_size) + '\\n'
                self.__chain += ('*' * (self.__cell_count % self.__row_size))
                if self.__chain[-1] == 'n':
                    self.__chain = self.__chain[: -2]
        return self

    # Перегруженные операторы печати и арифметических действий

    def __str__(self):
        return self.__chain

    def __add__(self, other):
        if not BioCellChain.InheritRows:
            return BioCellChain(self.__cell_count + other.__cell_count)
        else:
            return BioCellChain(self.__cell_count + other.__cell_count).make_order(min(self.__row_size, other.__row_size))

    def __sub__(self, other):
        if self.__cell_count <= other.__cell_count:
            return None
        elif not BioCellChain.InheritRows:
            return BioCellChain(self.__cell_count - other.__cell_count)
        else:
            return BioCellChain(self.__cell_count - other.__cell_count).make_order(min(self.__row_size, other.__row_size))

    def __mul__(self, other):
        if not BioCellChain.InheritRows:
            return BioCellChain(self.__cell_count * other.__cell_count)
        else:
            return BioCellChain(self.__cell_count * other.__cell_count).make_order(min(self.__row_size, other.__row_size))

    def __truediv__(self, other):
        if self.__cell_count < other.__cell_count:
            return None
        elif not BioCellChain.InheritRows:
            return BioCellChain(round(self.__cell_count / other.__cell_count))
        else:
            return BioCellChain(round(self.__cell_count / other.__cell_count)).make_order(min(self.__row_size, other.__row_size))

# Печать результатов операций над цепочками

def illustrate_chain_operations(chain_1, chain_2):
    print(f"Цепочка клеток 1 (далее [1]): {chain_1}\t\tЦепочка клеток 2 (далее [2]): {chain_2}")
    print(f"[1] + [2] = {chain_1 + chain_2}\t\t[1] * [2] = {chain_1 * chain_2}")

    if chain_1 - chain_2 != None:
        print(f"[1] - [2] = {chain_1 - chain_2}")
    else:
        print("[1] - [2]: операция не разрешена, поскольку число клеток в [1] не превышает число клеток в [2]")

    if chain_2 - chain_1 != None:
        print(f"[2] - [1] = {chain_2 - chain_1}")
    else:
        print("[2] - [1]: операция не разрешена, поскольку число клеток в [2] не превышает число клеток в [1]")

    if chain_1 / chain_2 != None:
        print(f"[1] / [2] = {chain_1 / chain_2}")
    else:
        print("[1] / [2]: операция не разрешена, поскольку число клеток в [2] превышает число клеток в [1]")

    if chain_2 / chain_1 != None:
        print(f"[2] / [1] = {chain_2 / chain_1}")
    else:
        print("[2] / [1]: операция не разрешена, поскольку число клеток в [1] превышает число клеток в [2]")

# ------------------------------------ Основная программа ------------------------------------------------

BioCellChain.InheritRows = False

print('\nОперации с цепочками, не разделёнными на ряды; результаты не наследуют минимальную длину ряда:')
print('----------------------------------------------------------------------------------------------')
chain_1 = BioCellChain(8)
chain_2 = BioCellChain(3)
illustrate_chain_operations(chain_1, chain_2)

BioCellChain.InheritRows = True

print('\nОперации с цепочками, не разделёнными на ряды; результаты наследуют минимальную длину ряда:')
print('-------------------------------------------------------------------------------------------')
chain_1 = BioCellChain(8)
chain_2 = BioCellChain(3)
illustrate_chain_operations(chain_1, chain_2)

BioCellChain.InheritRows = False

print('\nОперации с цепочками, разделёнными на ряды; результаты не наследуют разделение:')
print('-------------------------------------------------------------------------------')
chain_1 = BioCellChain(8).make_order(4)
chain_2 = BioCellChain(3).make_order(2)
illustrate_chain_operations(chain_1, chain_2)

BioCellChain.InheritRows = True

print('\nОперации с цепочками, разделёнными на ряды; результаты наследуют минимальную длину ряда:')
print('----------------------------------------------------------------------------------------')
chain_1 = BioCellChain(8).make_order(4)
chain_2 = BioCellChain(3).make_order(2)
illustrate_chain_operations(chain_1, chain_2)

