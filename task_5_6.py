#6. Подсчёт общего количества часов по предмету с формированием словаря и вывода его на экран

hours = {}
with open("teach_file_5_6.txt", "r", encoding='utf_8') as f_obj:
    for line in f_obj:
        pos = line.find(':')
        if pos < 1:
            continue

        key = line[:pos].strip()
        line = line[pos + 1:]
        val = 0
        for s in line.split():
            pos = s.find('(')
            if pos > -1:
                try:
                    val += int(s[:pos])
                except:
                    pass

        hours.update({key: val})

print("Общие часы по предметам:", hours)

