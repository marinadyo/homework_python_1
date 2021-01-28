
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
#
#
income = int(input('enter your income '))
outcome = int(input('enter your outcome '))
workers = int(input('how many workers do you have? '))

if income > outcome:
    proceeds = (income - outcome)
    efficiency = (income / proceeds)
    salary = (proceeds // workers)
    print('Your profit is:', proceeds, 'your efficiency is:', efficiency, 'each worker gets:', salary)

elif income < outcome:
    print('You have no profit.')
