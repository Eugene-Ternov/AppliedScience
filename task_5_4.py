#5. Замена числительных (алгоритм приемлем для файла малого размера, иначе можно было бы исключать повторные проверки)

with open("teach_file_5_4_source.txt", "r") as f_obj:
    str_list = f_obj.readlines()

write_list = []

for el in str_list:
    s = el.lower()
    pos = s.find(' -')
    if pos < 0:
        continue
    if s.find("one") > -1:
        s1 = "Один"
    elif s.find("two") > -1:
        s1 = "Два"
    elif s.find("three") > -1:
        s1 = "Три"
    elif s.find("four") > -1:
        s1 = "Четыре"

    write_list.append(s1 + s[pos:])

with open("teach_file_5_4_target.txt", "w") as f_obj:
    f_obj.writelines(write_list)


