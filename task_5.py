#5. Вставка элемента в монотонно убывающий набор натуральных чисел (перед первым меньшим)

my_rating = [9, 9, 6, 5, 4, 4, 3, 2, -1, -1, -3]        # С "антирейтингом" в минусе; предв. сортировка по убыванию
my_list = list([])

print(f'Исходный рейтинг: {my_rating}')
print('\r')
b_exit = False

while (True):
    s = input("Введите строку произвольных чисел, разделённых пробелами, или 'stop' для выхода (можно между чисел): ")
    a = s.lower().find('stop')      # После stop всё игнорируем
    if a > -1:
        s = s[:a]
        b_exit = True

    my_list.clear()                 # Подготовили список с учётом цикла
    my_list.extend(s.split())       # Заполнили список элементами строки
    for item in my_list:
        try:
            a = round(float(item))  # Дробное округлить до целого + особенности преобразования строки в число
        except:
            continue
        else:
            #Вставка элемента строки в список рейтинга
            b_append = True
            for i, rate in enumerate(my_rating):
                if a > rate:
                    my_rating.insert(i, a)
                    b_append = False
                    break

            if b_append == True:
                my_rating.append(a)

    print(f'Новый рейтинг: {my_rating}')  # Печатается в любом случае

    if b_exit == True:                    # Если в строке было 'stop'
        break
