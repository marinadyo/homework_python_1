# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go-go-go mofucker!')

    def stop(self):
        print('The car has stopped.')

    def turn(self):
        turns = {1: 'right', 2: 'left', 3: '180 deg'}
        x = random.choice(list(turns))
        if x == 1:
            print(f'{self.name} turns: {turns[1]}')
        elif x == 2:
            print(f'{self.name} turns: {turns[2]}')
        elif x == 3:
            print(f'{self.name} turns: {turns[3]}')

    def show_speed(self):
        print(f'Current speed: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Your speed is too high!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Your speed is too high!')


class PoliceCar(Car):
    is_police = True


town_car = TownCar(70, 'beige', 'Lexus', False)
print(town_car.name)
town_car.go()
town_car.show_speed()
town_car.turn()

print('-' * 80)
police_car = PoliceCar(45, 'black&white', 'Toyota')
print(police_car.name)
police_car.go()
police_car.show_speed()
print(police_car.is_police)
town_car.turn()

print('-' * 80)
sport_car = SportCar(120, 'blue', 'Mazda')
print(sport_car.name)
print(sport_car.is_police)
sport_car.go()
sport_car.turn()

print('-' * 80)
work_car = WorkCar(80, 'gold', 'BMW')
print(work_car.name)
print(work_car.is_police)
work_car.go()
work_car.turn()
