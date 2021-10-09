#5. Запись строк чисел в файл с вычислением суммы всех введённых чисел (похожа на задачу 5 из урока 3)

total_sum = 0
my_list = []
b_exit = False

with open("teach_file_5_5.txt", "w") as f_obj:
    while (True):
        s = input("Введите строку произвольных чисел, разделённых пробелами, или '#' для выхода (можно между чисел): ")
        pos = s.find('#')      # После "#" всё игнорируем
        if pos > -1:
            s = s[:pos]
            b_exit = True
        f_obj.write(s + '\n')
        if b_exit:
            break

total_sum = 0       # Расчёт суммы всех чисел из файла

with open("teach_file_5_5.txt", "r") as f_obj:
    for line in f_obj:
        for item in line.split():
            try:
                total_sum += float(item)
            except:
                pass

print(f'Сумма записанных в файл "{f_obj.name}" чисел: {round(total_sum, 3)}')
