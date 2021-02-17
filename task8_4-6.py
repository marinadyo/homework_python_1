# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. ---  В ОРГТЕХНИКЕ
# Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании.  --- ДЕТИ - ПОДРАЗДЕЛЕНИЯ
# Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать
# в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#

"""
Хотелось распределять вводимые пользователем товары по категориям, выводить с помощью одноименных классов.
Например, пользователь выбирает в меню 1, это Принтер. Мы запрашиваем у него данные, записываем их в общую базу,
но так же добавляем их в конкретную категорию, из которой позже можем их вызвать (к примеру, если захотим посмотреть,
сколько принетров у нас осталось на складе. Как это сделать, не разобралась =(
"""


class Storage:
    def __init__(self):
        self.all_items = []
        self.printer = []
        self.scanner = []
        self.xerox = []

    def supply(self):
        while input('Would you like to add an item? (yes/no) ') == 'yes'.lower():
            try:
                a = int(input(f'Which one?\n 1 -- Printer\n 2 -- Scanner\n 3 -- Xerox\n'))
                if a == 1:
                    printer_name = input("Enter printer's name: ")
                    printer_price = int(input("Enter printer's price: "))
                    printer_quantity = int(input("Enter printer's amount: "))
                    product_dict = {'Printer': printer_name, 'Quantity': printer_price, 'Cost': printer_quantity}
                    self.all_items.append(product_dict)
                    self.printer.append(product_dict)
                    print(f'You added a printer: {self.printer}')
                elif a == 2:
                    scanner_name = input("Enter scanner's name: ")
                    scanner_price = int(input("Enter scanner's price: "))
                    scanner_quantity = int(input("Enter scanner's amount: "))
                    product_dict = {'Scanner': scanner_name, 'Quantity': scanner_price, 'Cost': scanner_quantity}
                    self.scanner.append(product_dict)
                    self.all_items.append(product_dict)
                    print(f'You added a scanner: {self.scanner}')
                elif a == 3:
                    xerox_name = input("Enter xerox's name: ")
                    xerox_price = int(input("Enter xerox's price: "))
                    xerox_quantity = int(input("Enter xerox's amount: "))
                    product_dict = {'Xerox': xerox_name, 'Quantity': xerox_price, 'Cost': xerox_quantity}
                    self.xerox.append(product_dict)
                    self.all_items.append(product_dict)
                    print(f'You added a xerox: {self.xerox}')

            except ValueError:
                print('Enter valid data')


class Goods(Storage):
    def __str__(self):
        return 'Welcome to '


class Printer(Goods):
    def __str__(self):
        return 'I\'m Printer! I can print stuff!'


class Scanner(Goods):
    def __str__(self):
        return 'I\'m Scanner! I can scan things.'


class Xerox(Goods):
    def __str__(self):
        return 'I am Xerox. I can xerox documents...'


item1 = Storage()
equipment = Goods()
printer = Printer()
scanner = Scanner()
xerox = Xerox()
print(equipment)
print(printer)
print(scanner)
print(xerox)

print(item1.supply())
print(item1.all_items)