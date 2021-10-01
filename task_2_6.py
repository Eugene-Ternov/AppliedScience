# 6. Аналитика о товарах. Чуть усложним задачу: если ввести существующие наименование и цену - суммируется количество

goods = []
product = {}
cnt = 1

while True:
    s1 = input("Введите наименование товара или stop для завершения ввода сведений о товарах: ").strip().lower()
    if s1.find('stop') > -1:      # Завершаем ввод и переходим к статистике
        break
    while True:                   # Цена товара
        s2 = input("Введите цену товара, руб.: ").strip()
        try:
            cost = abs(float(s2))
        except:
            print("Это было не число. Пожалуйста, ещё раз.")
        else:
            break
    while True:                   # Количество единиц товара
        s2 = input("Введите количество единиц товара, шт.: ").strip()
        try:
            amount = abs(int(float(s2)))
        except:
            print("Это было не число. Пожалуйста, ещё раз.")
        else:
            break

    b_new = True
    for item in goods:
        product = dict(item[1])
        if product.get('название') == s1 and product.get('цена') == cost:
            product.update({'количество': amount + product.get('количество')})
            item[1] = product.copy()
            b_new = False
            break

    if b_new == True:
        product.update({'название': s1, 'цена': cost, 'количество': amount, 'ед.': 'шт.'})
        goods.append([cnt, product])
        cnt += 1

    print('\r')
    for item in goods:
        print(item)
    print('\r')

if len(goods) == 0:     # Список товаров не сформирован
    exit(0)

# Формирование списка товаров завершено, его элементы становятся кортежами (read-only)

print('\nИтоговый список товаров:')
for item in goods:
    item = tuple(item)
    print(item)

result_dict = {}
for item in goods:
    product = dict(item[1])
    for key, value in product.items():
        if not result_dict.get(key):
            result_dict[key] = [value]
        else:
            result_dict[key].append(value)

# Финализируем только единицы, чтобы не нарушить уникальности пар "название-цена"
if result_dict.get('ед.') != None:      # не нужно, но для обучения
    result_dict['ед.'] = list(set(result_dict.get('ед.')))
    print('\nАналитика о товарах:')
    print(result_dict)




