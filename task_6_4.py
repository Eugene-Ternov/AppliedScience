#4. Создание классов автомобилей

import random

class Car:
    def __init__(self, color, name, is_police = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0
        self._dir = {1: "Налево", 2: "Направо", 3: "На разворот"}

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Приехали")
        self.speed = 0

    def turn(self, direction):
        try:
            return self._dir[direction]
        except:
            return "Потеря управления"

    def show_speed(self):
        print(f"{self.speed} км/ч")

class TownCar(Car):

    def go(self):
        print("Поехали. Эх, прокачу!")

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Потише, пожалуйста. Снизьте скорость до 60 км/ч")

class SportCar(Car):

    def go(self):
        print("Поехали. Вперёд! 'Don't stop me now!' (c)")

    def stop(self):
        print("Приехали! 'We are champions, my friend!' (c)")
        self.speed = 0

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости! Снизьте скорость до 40 км/ч и менее!")

class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, True)
        self._dir = {1: "Нале-во!", 2: "Напра-во!", 3: "Кру-гом!"}

    def stop(self):
        print("Стой! Раз-два. 'Наша служба и опасна, и трудна' (с)")
        self.speed = 0

    def go(self):
        print("По коням! Тыг-дыг, тыг-дыг, тыг-дыг!")

pc = PoliceCar('серо-голубой', 'Молния')
sc = SportCar('бежевый', 'БМВ-кабриолет')
wc = WorkCar('оранжевый', 'Изыскательская')
tc = TownCar('серебристо-синий', 'Ласточка')

car_list = [pc, sc, wc, tc]
print("\nХарактеристики:\tкласс\tцвет\tнаименование\tтранспорт МВД")
print("-" * 80)
for el in car_list:
    print(f"{str(type(el)):<30}\t{el.color:<20}\t{el.name:<19}\t{el.is_police}")

print("\nОтработка изменения направления движения (1...4)")
print("-" * 80)
for el in car_list:
    print(f"{str(type(el)):<30}\t{str(el.turn(1)):<10}\t{str(el.turn(2)):<10}"
          f"\t{str(el.turn(3)):<15}\t{str(el.turn(4))}")

print("\nНачало, текущая скорость и завершение движения ('go', 'show_speed' and 'stop')")
print("-" * 80)
for el in car_list:
    print(f"\n{str(type(el))}")
    el.go()
    el.speed = random.randint(61, 80)
    el.show_speed()
    el.stop()