#3. Определение сотрудников с окладом менее 200 000 руб. с подсчётом среднего оклада по всем сотрудникам

with open("teach_file_5_3_source.txt", "r", encoding='utf_8') as f_obj:
    arr_list = f_obj.readlines()
    if len(arr_list) == 0:
        exit(0)

    avg_salary = 0
    count = 0
    write_list = []

    for i, s in enumerate(arr_list):
        str_list = s.split()
        if len(str_list) < 2:
            continue
        try:
            salary = float(str_list[1])
            avg_salary += salary
            count += 1
            if salary < 20000:
                write_list.append(' '.join(str_list) + '\n')
        except:
            continue

if len(write_list) > 0:
    avg_salary /= count
    write_list.sort()
    write_list.insert(0, f"Средний оклад: {avg_salary:.2f} руб.\n")
    with open("teach_file_5_3_target.txt", "w") as f_obj:
        f_obj.writelines(write_list)
    for s in write_list:
        print(s.rstrip())
