#5. Задача о накапливающейся сумме. Немного усложним для использования sum() - урок был о функциях

total_sum = 0
my_list = []
b_exit = False

while (True):
    s = input("Введите строку произвольных чисел, разделённых пробелами, или 'stop' для выхода (можно между чисел): ")
    a = s.lower().find('stop')      # После stop всё игнорируем
    if a > -1:
        s = s[:a]
        b_exit = True

    my_list.clear()
    my_list.extend(s.split())       # Заполнили список элементами строки
    for i, item in enumerate(my_list):
         try:
             a = float(item)
             my_list[i] = a
         except:
             my_list[i] = 0

    total_sum += round(sum(my_list), 3)

    print(f'Накопленная сумма: {total_sum:.3f}')  # Печатается, даже если ничего не прибавилось

    if b_exit == True:                    # Если в строке было 'stop'
        break
