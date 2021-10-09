# 7. Чтение данных о фирмах из текстового файла и преобразование их в json-объект с сохранением в json-файл

import json

avg_profit = 0
count = 0
firm_dict = {}
with open("teach_file_5_7.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        data = line.split()
        print(data)
        profit = int(data[3])
        lost = int(data[4])
        profit = profit - lost
        if profit > 0:
            avg_profit += profit
            count += 1
        firm_dict.update({data[0]: profit})

    if count > 0:
        avg_profit /= count
    result_list = [firm_dict]
    result_list.append({"average_profit": round(avg_profit, 2)})
    print(result_list)

    with open("teach_file_5_7.json", "w") as f_obj:
        json.dump(result_list, f_obj)

    with open("teach_file_5_7.json", "r") as f_obj:
        r = json.load(f_obj)
        print(r)



