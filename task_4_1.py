#1. Скрипт с параметрами - расчёт почасового вознаграждения с премиальными (параметры - в конфигурации)

from sys import argv

try:
    script_name, hour_salary, work_time, bonus = argv
    money = round(float(hour_salary) * float(work_time) + float(bonus), 2)
    print(f"{'Почасовая ставка':<20} - {hour_salary} руб./ч")
    print(f"{'Отработанное время':<20} - {work_time} ч")
    print(f"{'Премиальная выплата':<20} - {bonus} руб.")
    print(f"\nСумма вознаграждения: {money} руб.")
except:
    print('Не все параметры заданы либо являются числами.')
    print(f'Пример запуска: {argv[0]} HS WT BN')
    print('HS - почасовая ставка, руб./ч')
    print('WT - отработанное время, ч')
    print('BN - премиальная выплата, руб.')
