# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# мой код до разбора дз:
#1
month = int(input('What month is it? '))
dict_month = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

if month == 1 or month == 2 or month == 12:
    print(dict_month.get(1))
elif month == 3 or month == 4 or month == 5:
    print(dict_month.get(2))
elif month == 6 or month == 7 or month == 8:
    print(dict_month.get(3))
elif month == 9 or month == 10 or month == 11:
    print(dict_month.get(4))
else:
    print('There is no such month')
#2
month = int(input('What month is it? '))
months = ['winter', 'spring', 'summer', 'autumn']
if month == 1 or month == 2 or month == 12:
    print(months[0])
elif month == 3 or month == 4 or month == 5:
    print(months[1])
elif month == 6 or month == 7 or month == 8:
    print(months[2])
elif month == 9 or month == 10 or month == 11:
    print(months[3])
else:
    print('There is no such month')

# код после разбора дз
season = int(input('Enter season using numbers from 1 to 4: '))
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
season_list = ['winter', 'spring', 'summer', 'autumn']

if season in season_dict:
    print(f'{season} is {season_dict[season]}')
    print(f'{season} is {season_list[season - 1]}')
