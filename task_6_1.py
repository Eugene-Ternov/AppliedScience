#1. Класс светофора: работа сигналов по sleep(), выразительные средства - консоль. И усложнённое учебное ООП

from time import sleep
from datetime import datetime as dt
import random

class Light:                                            # Единичный сигнал светофора

    def __init__(self, color):
        self.__on_color = color
        self.__off_color = "-" * len(color)
        self.switch_off()

    def switch_on(self):
        self.__curr_color = self.__on_color

    def switch_off(self):
        self.__curr_color = self.__off_color

    def get_current_color(self):
        return self.__curr_color


class TrafficLight:                                     # Автомобильный светофор (горизонтальное расположение)

    def __init__(self, stop_color, stop_delay, ready_color, ready_delay, run_color, run_delay, start_offset = 0):
        self.__lights = [Light(stop_color)]
        self.__lights.append(Light(ready_color))
        self.__lights.append(Light(run_color))

        self.__cycle_time = stop_delay + 2 * ready_delay + run_delay    # Время полного цикла
        self.__stop_max_time = stop_delay                               # Переключение в жёлтый после красного
        self.__go_ready_time = stop_delay + ready_delay                 # Переключение в зелёный
        self.__go_max_time = self.__go_ready_time + run_delay           # Переключение в жёлтый после зелёного

        self.__start_offset = start_offset # Запуск не обязательно с красного света, а возможно с более позднего состояния
        self.stop()

    # Запуск светофора

    def running(self, single_cycle_mode = False, reset_start_offset = False):
        self.__is_running = True
        self.__single_cycle_mode = single_cycle_mode
        if reset_start_offset:
            self.__start_offset = 0
        self.__start_time = dt.now()

    # Остановка светофора

    def stop(self):
        for l in self.__lights:
            l.switch_off()
        self.__is_running = False

    # Отработка одного шага модельного времени (равно физическому) - режим односекционного автомобильного светофора

    def pass_model_time_step(self):
        if not self.__is_running:
            passed = True
        else:
            passed = False
            self.__pass_time = (dt.now() - self.__start_time).seconds + self.__start_offset
            if self.__pass_time < self.__stop_max_time:         # Красный
                self.__lights[0].switch_on()
                self.__lights[1].switch_off()
                self.__lights[2].switch_off()
            elif self.__pass_time < self.__go_ready_time:       # Красный и жёлтый вместе - переход к зелёному
                self.__lights[0].switch_on()
                self.__lights[1].switch_on()
                self.__lights[2].switch_off()
            elif self.__pass_time < self.__go_max_time:         # Зелёный
                self.__lights[0].switch_off()
                self.__lights[1].switch_off()
                self.__lights[2].switch_on()
            elif self.__pass_time < self.__cycle_time:          # Жёлтый после зелёного - переход к красному
                self.__lights[0].switch_off()
                self.__lights[1].switch_on()
                self.__lights[2].switch_off()
            else:                                               # Пора зажигать красный сигнал после жёлтого
                if self.__single_cycle_mode:                    # Однократное прохождение цикла
                    self.stop()
                else:                                           # Непрерывная работа
                    self.__start_time = dt.now()
                    self.__start_offset = 0                     # Стартовое смещение в авторежиме - только при запуске
                passed = True

        return [passed, [l.get_current_color() for l in self.__lights], self.__pass_time]

# Прогоны 2-х светофоров (вывод их текущих сигналов в одной общей строке )

count = 3       # Количество циклов для прогона - в непрерывном либо однопроходном режиме
i1 = 0
i2 = 0

tl_1 = TrafficLight("Красный", 7, "Жёлтый", 2, "Зелёный", 7)
tl_2 = TrafficLight("Красный", 5, "Жёлтый", 3, "Зелёный", 4, 2)     # Как бы запущен на 2 секунды раньше первого

b1 = True               # Пусть цикл 1-го светофора перезапускается принудительно
b2 = False              # Пусть цикл 2-го светофора перезапускается автоматически
tl_1.running(b1)
tl_2.running(b2)

let_failure = True     # Установить в True для разрешения имитации ошибки; False - ошибка имитироваться не будет

print("")

s1 = ''
s2 = ''

# Элемент итоговой строки для печати цветов светофора

def str_to_print(arg1, arg2, arg3):
    res_str = f"\tСветофор {arg1}:"
    for el in arg2:
        res_str += f" [{el}]"
    res_str += f"\t00:{arg3:02d}"
    return res_str

while True:
    # Определение текущих цветов всех светофоров сразу после пуска и далее через задержку sleep()
    d_1 = tl_1.pass_model_time_step()
    d_2 = tl_2.pass_model_time_step()

    # Имитация ошибки:  2 цикла будет без ошибок - понаблюдать за правильной работой

    if let_failure and i1 > 1 and i2 > 1 and (random.randint(0, 100) % 4 == 0):
        # Лучше бы конечно подпрограммой, но здесь это не суть важно
        mask_1 = 0
        mask_2 = 0
        for i, el in enumerate(d_1[1]):
            if el.find('-') < 0:
                mask_1 += (2 ** i)
        for i, el in enumerate(d_2[1]):
            if el.find('-') < 0:
                mask_2 += (2 ** i)
        if random.randint(mask_1 - 1, mask_1) != mask_1 and random.randint(mask_1, mask_1 + 1) != mask_1:
            print("")
            print("\tНарушение очерёдности сигнала светофора 1 (не детализируем). Программа остановлена")
            exit(0)
        if random.randint(mask_2 - 1, mask_2) != mask_2 and random.randint(mask_2, mask_2 + 1) != mask_2:
            print("")
            print("\tНарушение очерёдности сигнала светофора 2 (не детализируем). Программа остановлена")
            exit(0)
    # Конец имитации ошибки
    # Отображение сигналов светофора с использованием сравнения с предыдущей строкой, чтобы избежать эффекта рябления
    s2 = f"\r{str_to_print(1, d_1[1], d_1[2])}{str_to_print(2, d_2[1], d_2[2])}"
    if s2 != s1:
        s1 = s2
        print(s2, end= '')
    # Проверка на отработку заданного количества циклов с перезапуском, если был режим однократного прохождения цикла
    if d_1[0]:
        i1 += 1
        if i1 < count and b1:
            tl_1.running(True, True)
    if d_2[0]:
        i2 += 1
        if i2 < count and b2:
            tl_2.running(True, True)
    # Оба светофора с учётом разности индивидуальных задержек отработали не менее count циклов
    if i1 >= count and i2 >= count:
        tl_1.stop()
        tl_2.stop()
        print("")
        break

    sleep(0.25)     # Для точности отсчётов времени. Но можно и 0.5 - работает одинаково





