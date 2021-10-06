#4. Определить элементы списка чисел, не имеющие повторений, и вывести их в порядке следования в исходном списке

from random import randint as rnd

source_list = [rnd(1, 99) for i in range(15)]
target_list = [item for item in source_list if source_list.count(item) == 1]
print("Исходный список:", source_list)
print("Целевой список: ", target_list)
