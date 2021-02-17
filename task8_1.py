# 1. Реализовать класс «Дата», функция-конструктор которого
# должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        self.data = date

    @classmethod
    def sort(cls, date):
        d, m, y = [int(i) for i in date.split('-')]
        return d, m, y

    @staticmethod
    def valid(date):
        d, m, y = map(int, date.split('-'))
        if d <= 31 and d != 0 and m <= 12 and m != 0:
            return d, m, y


date1 = '17-02-2021'
print(Date.sort(date1))
print(Date.valid(date1))
