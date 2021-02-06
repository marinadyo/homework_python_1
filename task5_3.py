# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

"""Использовала текстовые файлы из архива"""

with open('text_3.txt', 'r') as salary:
    lines = salary.readlines()

salary_list = []
for line in lines:
    key, value = line.split()
    salary_list.append(float(value))
    if float(value) < 20000:
        print(key)
print(sum(salary_list) / len(salary_list))
