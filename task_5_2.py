#2. Подсчёт слов в каждой строке текстового файла (создан руками); знак "-" за слово не считается

with open("teach_file_5_2_source.txt", "r", encoding='utf_8') as f_obj:
    arr_list = f_obj.readlines()
    if len(arr_list) == 0:
        exit(0)
    for i, s in enumerate(arr_list):
        str_list = s.split()
        count = len(str_list)
        if count > 0:
            count -= str_list.count('-')
        if i == 0:
            f_target = open("teach_file_5_2_target.txt", "w")
            print(f'Число строк в файле "{f_obj.name}": {len(arr_list)}', file= f_target)
            print(f'Число строк в файле "{f_obj.name}": {len(arr_list)}')
        print(f'Строка {i + 1}\tЧисло слов: {count}', file= f_target)
        print(f'Строка {i + 1}\tЧисло слов: {count}')

    f_target.close()
