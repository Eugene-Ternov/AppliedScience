#2. Генерирование списка и Вывод его элементов, значения которых больше предыдущего элемента

from random import randint as rnd

source_list = [rnd(1, 99) for i in range(15)]
target_list = [item for i, item in enumerate(source_list) if i > 0 and item > source_list[i - 1]]
print("Исходный список:", source_list)
print("Целевой список: ", target_list)
