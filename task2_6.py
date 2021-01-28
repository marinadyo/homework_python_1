# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена,
# количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название,
# а значение — список значений-характеристик,
# например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# код до разбора дз

goods = []
item = 'Название:'
value = 'Цена:'
amount = 'Количество:'
features_1 = {}
features_2 = {}
while input('Would you like to add an item? ').lower() == 'yes':
    name_1 = input("Enter name: ")
    price_1 = input("Enter price: ")
    number_1 = int(input("Enter amount: "))
    features_1[item] = name_1
    features_1[value] = price_1
    features_1[amount] = number_1
    print(features_1)
    break
while input('Would you like to add another one? ').lower() == 'yes':
    name_2 = input("Enter name: ")
    price_2 = input("Enter price: ")
    number_2 = int(input("Enter amount: "))
    features_2[item] = name_2
    features_2[value] = price_2
    features_2[amount] = number_2
    break
goods.append(tuple([features_1, features_2]))
# print(goods)
analytics = {
    item: [features_1[item], features_2[item]],
    value: [features_1[value], features_2[value]],
    amount: [features_1[amount], features_2[amount]]
}
print(analytics)



