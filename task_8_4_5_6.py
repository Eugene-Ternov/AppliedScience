#4, 5, 6. Склад оргтехники (аналог примера с библиотекой)

import random
from abc import ABC

class DeviceException(Exception):
    pass

class Warehouse:
    def __init__(self):
        self._unit_types = ("принтеры", "ксероксы", "сканеры")
        self._printer_dict = {}
        self._scanner_dict = {}
        self._xerox_dict = {}
        self._in_division_dict = {}

    @property
    def printer_count(self):
        return len(self._printer_dict.items())

    @property
    def scanner_count(self):
        return len(self._scanner_dict.items())

    @property
    def xerox_count(self):
        return len(self._xerox_dict.items())

    @property
    def total_count(self):
        return self.printer_count + self.scanner_count + self.xerox_count

# Переключение словарей в зависимости от типа оборудования

    def _switch_device_type(self, unit):
        if isinstance(unit, Printer):
            self._dev_dict = self._printer_dict
        elif isinstance(unit, Xerox):
            self._dev_dict = self._xerox_dict
        elif isinstance(unit, Scanner):
            self._dev_dict = self._scanner_dict

# Переключение словарей в зависимости от запроса на выдачу техниеи

    def _switch_device_type_by_command(self, cust_choice):
        if cust_choice == 1:
            self._dev_dict = self._printer_dict
        elif cust_choice == 2:
            self._dev_dict = self._xerox_dict
        elif cust_choice == 3:
            self._dev_dict = self._scanner_dict

# Переключение словарей в зависимости от запроса на выдачу техниеи

    def propose_available_units(self, cust_choice):
        self._switch_device_type_by_command(cust_choice)
        if len(self._dev_dict.items()) == 0:
            print("Оборудование запрошенного типа отсутствует")
            return 0
        print(f"Доступные {self._unit_types[cust_choice - 1]}:")
        for i, item in enumerate(self._dev_dict.values()):
            print(f"{(i + 1):2d}: {item}")
        return len(self._dev_dict.items())

# Приём оборудования

    def get_device(self, unit, division = None):
        self._switch_device_type(unit)
        if not self._dev_dict.get(unit.inv_no):
            self._dev_dict.update({unit.inv_no: unit})
        if division and not isinstance(self, FirmDivision): # только класса WareHouse - списали с подразделения
            if self._in_division_dict.get(unit.inv_no):
                self._in_division_dict.pop(unit.inv_no)
            self.__print_given_device()

# Выдача оборудования

    def give_device(self, unit_type, cust_choice, division = None):
        self._switch_device_type_by_command(unit_type)
        keys = list(self._dev_dict.keys())
        inv_no = keys[cust_choice - 1]
        unit = self._dev_dict.get(inv_no)
        if unit:
            self._dev_dict.pop(inv_no)
            # задел "учётной политики" - куда ушло оборудование (далее не используется)
            if division and not isinstance(self, FirmDivision):  # только класса WareHouse - записали на подразделение
                if not self._in_division_dict.get(inv_no):
                    self._in_division_dict.update({inv_no: division.name})
                self.__print_given_device()
        return unit

    def __print_given_device(self):
        if len(self._in_division_dict.items()) > 0:
            print("\tЧто на ком числится:")
            for key, value in self._in_division_dict.items():
                print(f'\tИнв. номер: {key}\t- {value}')

class OfficeEquipment(ABC):
    _DeviceCount = 0
    def __init__(self, *args):
        self.inv_no = ""               # Инвентарный номер (сразу пустой, присваивается на складе)
        self._place = ""                # Место, где будет находиться (пустая строка, если на складе)
        self._kind = args[0]            # Тип устройства
        arg_list = list(args[1])        # Список его характеристик
        self._model = arg_list[0]       # 1-я (всегда): модель
        self._doc_size = arg_list[1]    # 2-я (всегда): размер бумаги


    # При печати выводятся тип, модель и инвентарный номер (если он присвоен)

    def __str__(self):
        if self.inv_no != "":
            s = 'Инв. № ' + self.inv_no
        return f"'{self._kind} {self._model} {s}'".rstrip()


class Printer(OfficeEquipment):
    Models = {1: ["Canon PIXMA iX6840", "A3", "color", "inkjet"], 2: ["Epson L805", "A4", "color", "inkjet"]}
    def __init__(self, *args):
        super().__init__("принтер", *args)


class Scanner(OfficeEquipment):
    Models = {1: ["BearPaw 2448TA Plus", "A4"], 2: ["Epson WorkForce DS-70000", "A3"], 3: ["Canon DR-M1060", "A3"]}
    def __init__(self, *args):
        super().__init__("сканер", *args)


class Xerox(OfficeEquipment):
    Models = {1: ["Xerox WorkCentre 3225DNI", "A4", "b/w", "laser"], 2: ["Brother MFC-J2720", "A3", "color", "inkjet"]}
    def __init__(self, *args):
        super().__init__("ксерокс", *args)
        arg_list = list(args[0])
        self._print_mode = arg_list[2]
        self._print_type = arg_list[3]

# для простоты - подразделение в данной задаче - то же, что склад для иллюстрации механизма приёма/передачи

class FirmDivision(Warehouse):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

# Количество свободной техники на складе

def print_warehouse_state():
    print(f"Количество свободной техники на складе: принтеры - {wh.printer_count},"
          f" ксероксы - {wh.xerox_count}, сканеры - {wh.scanner_count}; всего устройств: {wh.total_count}.")

d = None    # Подразделение, с которым ведёт диалог склад

# Вспомогательная реализация цикла опроса в подпрограмме

def pass_request_cycle(input_message, max_range = 3):
    while True:
        s = input(input_message)
        try:
            result = int(s)
            if result not in range(0, max_range + 1):
                raise()
        except:
            print("Пожалуйста, сделайте предлагаемый выбор")
        else:
            return result

# Возврат техники на склад

def return_to_warehouse():
    global d
    while True:
        unit_type = pass_request_cycle("Что-то желаете сдать: принтер (1), ксерокс (2), сканер (3)? Для отказа нажмите 0: ")
        if unit_type == 0:
            return False
        # Предложение подразделения
        choice = d.propose_available_units(unit_type)
        if choice == 0:
            continue
        elif choice == 1:
            s = "1"
        else:
            s = f"от 1 до {choice}"
        choice = pass_request_cycle(f"Введите {s}. Для возврата к выбору типа оборудования нажмите 0: ", choice)
        if choice != 0:
            break
    dev = d.give_device(unit_type, choice)
    if dev:
        wh.get_device(dev, d)
        print(f"{d.name.capitalize()}: принтеры - {d.printer_count},"
              f" ксероксы - {d.xerox_count}, сканеры - {d.scanner_count}; всего устройств: {d.total_count}.")

    return True

# Взятие техники со склада

def take_from_warehouse():
    global d, wh
    while True:
        unit_type = pass_request_cycle("Что-то желаете взять: принтер (1), ксерокс (2), сканер (3)? Для отказа нажмите 0: ")
        if unit_type == 0:
            return False
        # Предложение склада
        choice = wh.propose_available_units(unit_type)
        if choice == 0:
            continue
        elif choice == 1:
            s = "1"
        else:
            s = f"от 1 до {choice}"
        choice = pass_request_cycle(f"Введите {s}. Для возврата к выбору типа оборудования нажмите 0: ", choice)
        if choice != 0:
            break
    dev = wh.give_device(unit_type, choice, d)
    if dev:
        d.get_device(dev)
        print(f"{d.name.capitalize()}: принтеры - {d.printer_count},"
              f" ксероксы - {d.xerox_count}, сканеры - {d.scanner_count}; всего устройств: {d.total_count}.")

    return True

# Основная программа

print("")

wh = Warehouse()                                    # склад (будет глобальной переменной)
div_adm = FirmDivision('приёмная')                  # 1-е подразделение
div_eng = FirmDivision('инженерный отдел')          # 2-е подразделение
div_acc = FirmDivision('бухгалтерия')               # 3-е подразделение

div_list = [div_adm]                                # Для дальнейшего обращения по номеру 1...3
div_list.append(div_eng)
div_list.append(div_acc)


print_warehouse_state()         # До поступления техники.

# на склад поступает новое оборудование: 3 ксерокса (МФУ), 5 принтеров, 2 сканера

print("На склад поставлено новое оборудование:")
print("\nПринтеры:")
print("---------")
for i in range(5):
    dev = Printer(Printer.Models.get(random.randint(1, len(Printer.Models))))
    dev.inv_no = 'p' + str(i + 1)                                      # Упрощённое присвоение инв. номера
    print(dev)
    wh.get_device(dev)  # Подразделение не указано, условно - со стороны (не детализируем)

print("\nКсероксы (МФУ):")
print("---------------")
for i in range(3):
    dev = Xerox(Xerox.Models.get(random.randint(1, len(Xerox.Models))))
    dev.inv_no = 'x' + str(i + 1)                                      # Упрощённое присвоение инв. номера
    print(dev)
    wh.get_device(dev)  # Подразделение не указано, условно - со стороны (не детализируем)

print("\nСканеры:")
print("--------")
for i in range(2):
    dev = Scanner(Scanner.Models.get(random.randint(1, len(Scanner.Models))))
    dev.inv_no = 's' + str(i + 1)                                      # Упрощённое присвоение инв. номера
    print(dev)
    wh.get_device(dev)  # Подразделение не указано, условно - со стороны (не детализируем)

print_warehouse_state()         # После поступления техники

# Демонстрация получения техники в подразделение со склада и возврат на склад

while True:
    choice = pass_request_cycle(f"Выберите подразделение по номеру: {div_adm} (1), {div_eng} (2),"
                                f" {div_acc} (3); для выхода нажмите 0: ")
    if choice == 0:
        print("\nВ целом так выглядит процедура приёма/выдачи. На этом пока можно остановиться")
        exit(0)

    elif choice == 1:
        d = div_adm
    elif choice == 2:
        d = div_eng
    elif choice == 3:
        d = div_acc
    print(f"Здравствуйте, {d}! ", end='')

    # Техники на складе нет совсем

    if wh.total_count == 0:
        d1 = None
        d2 = None
        for el in div_list:
            if el == d:
                continue
            elif d1 == None:
                d1 = el
            else:
                d2 = el
        print(f"К сожалению, сейчас ничего нет. Нужно, чтобы {d1} или {d2} что-нибудь вернули на склад.")
        # Если техника есть у обратившегося - предлагается что-нибудь вернуть
        if d.total_count > 0:
            if return_to_warehouse():
                print_warehouse_state()
        continue

    # Техника на складе есть (какая-то). Печатается количество и предлагается что-нибудь взять

    print_warehouse_state()
    if take_from_warehouse():
        print_warehouse_state()                         # Количество техники на складе изменилось
    # Если в подразделении что-то есть - предлагается что-то сдать
    if d.total_count > 0 and return_to_warehouse():
        print_warehouse_state()                         # Количество техники на складе изменилось
