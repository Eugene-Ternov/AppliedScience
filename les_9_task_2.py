# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
from binarytree import bst, Node

# Получение строки направления


def get_path_direction(path: str, direction: bool) -> str:
    if direction:
        return path + "1"
    else:
        return path + "0"

# Получение кода Хаффмана для отдельного символа - листа в дереве Хаффмана
# (обход неупорядоченного бинарного дерева в ширину)


def get_Haffman_code(letter, tree_list=[]) -> str:
    length = len(tree_list)
    if length == 0:                         # Список опустел, символ не найден
        return ""

    for el in tree_list:                    # Проверяем, нет ли нужного узла (листа) в списке
        if el[0].value == letter:           # Это он, поиск завершаем успешно
            res = el[1]
            for item in tree_list:          # Очистка списка поиска, в т.ч. всех его элементов, также списков
                item.clear()
            tree_list.clear()
            return res

    for el in tree_list:                     # Добавляем дочерние деревья и пути к ним в список поиска
        if el[0].left is not None:
            tree_list.append([el[0].left, get_path_direction(el[1], False)])
        if el[0].right is not None:
            tree_list.append([el[0].right, get_path_direction(el[1], True)])

    for i in range(length):         # Удаляем обработанные элементы (первые в списке) - они больше не нужны
        tree_list[0].clear()        # Элемент списка поиска - тоже список, его нужно почистить
        tree_list.pop(0)

    return get_Haffman_code(letter, tree_list)      # Рекурсия с обновлённым списком поиска


# Кодировка всей строки по алгоритму Хаффмана


def code_string_by_Haffman(source: str, is_separated=False) -> str:
    if len(source) == 0:
        return ""

    src_dict = Counter(source)          # Символы в строке и частота их появления

    print(f"\nКодируемая строка: '{src}'\n")
    print(f'Символы в строке и частота их появления: {src_dict}')
    src_arr = sorted(src_dict, key=src_dict.get, reverse=False)     # Символы, отсортированные по возрастанию частоты
    print(f'Символы, отсортированные по возрастанию частоты появления: {src_arr}')

    while True:
        el_1 = src_arr[0]
        if len(src_arr) > 1:        # Можно спокойно обрабатывать пару (символ и дерево в любых сочетаниях)
            el_2 = src_arr[1]
        else:                       # Выделяем случай, когда строка из одного символа - второй для дерева не ищем
            el_2 = None

        src_arr.pop(0)
        if len(src_arr) > 0:
            src_arr.pop(0)

        val_1 = src_dict[el_1]
        if val_1 == 0:
            val_1 = el_1.value

        val_2 = src_dict[el_2]
        if val_2 == 0 and el_2 is not None:     # Учитываем случай, когда строка может быть из одного символа
            val_2 = el_2.value

        c = Node(val_1 + val_2)
        try:                                    # Для удобства: или символ - или дерево
            c.left = Node(el_1)                 # Пытаемся создать узел (лист) дерева с символьным значением
        except:
            c.left = el_1                       # Ошибка создания: el_1 - уже готовое дерево

        if el_2 is not None:                    # Учитываем случай, когда строка может быть из одного символа
            try:                                # Всё, как для el_1
                c.right = Node(el_2)
            except:
                c.right = el_2

        if len(src_arr) == 0:                   # Обработаны все символы, встретившиеся в строке - завершить цикл
            break

        b_append = True                         # Помещение символа или дерева в массив по его приоритету
        for i, el in enumerate(src_arr):
            priority = src_dict[el]             # для дерева будет возвращён ноль, возьмём приоритет из корня дерева el
            if priority == 0:
                priority = el.value
            if priority >= c.value:
                src_arr.insert(i, c)
                b_append = False
                break

        if b_append:
            src_arr.append(c)

    # Дерево Хаффмана получено

    print("Дерево Хаффмана:")
    print(c)
    s = ""
    for char in source:
        s += get_Haffman_code(char, [[c, ""]])
        if is_separated:
            s += " "
    return s.rstrip()


s_task = "к кордильерским крокодилам дилер не приходил"
s_test = "beep boop beer!"
b_separate = True                               # Разделять ли кодированные символы пробелами (False - не разделять)
src = s_test                                    # Задайте s_task или наберите здесь собственную строку,
                                                # можно из одного символа или пустую.
s = code_string_by_Haffman(src, b_separate)
if s == "":
    print('\nКодировать пустую строку не имеет смысла')
else:
    print(f"Строка '{src}' в кодировке Хаффмана", end='')
    if b_separate:
        print(' (с разделительными пробелами между символами)', end='')

    print(f":\n\n{s}")

