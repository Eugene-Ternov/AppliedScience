#2. Ввод пользователем элементов для добавления в список и их обмен местами (0-й с 1-м, 2-й с 3-м и т.д.)

my_list = list([])

while True:
    s = input("Введите элемент для добавления в список или 0 для завершения ввода: ").strip()
    if s != '0':
        my_list.append(s)
    else:
        break

print(my_list)
a = len(my_list)
for i in range(a):
    if (i % 2 == 0) and (i + 1 < a):
        my_list[i + 1], my_list[i] = my_list[i], my_list[i + 1]

print(my_list)


