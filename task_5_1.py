#1. Создать программно текстовый файл и записать в него построчно данные, вводимые пользователем, до пустой строки.

s_list = []
s_file = "teach_file_5_1.txt"
b_start = True
b_print = True

while True:
    s = input("Введите строку для записи в файл или нажмите Enter для прекращения ввода строк: ")
    s_list = s.split()
    if len(s_list) == 0:
        break
    s = ' '.join(s_list)
    if b_start == True:
        f_obj = open(s_file, "w")
        b_start = False
    if b_print:
        print(s, file=f_obj)
    else:
        f_obj.write(s + '\n')
    b_print = not b_print

if not (b_start or f_obj.closed):
    f_obj.close()
