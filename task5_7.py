# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить
# прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

"""Использовала текстовые файлы из архива"""

with open('text_7.txt') as all_firms:
    firms = all_firms.readlines()
    profits = {}
    average_profit = []
    for elem in firms:
        name, form, income, expense = elem.split()
        profit = int(income) - int(expense)
        profits[name] = profit
    if profit > 0:
        average_profit.append(profit)
    average_profit = sum(average_profit) / len(average_profit)
    total = [profits, {'average_profit': average_profit}]
    print(total)

import json
with open('text_7.json', 'w') as total_j:
    json.dump(total, total_j)

