# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input('Enter time in seconds: '))

seconds = user_time % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

if minutes < 10 or seconds < 10 or hour < 10:
    print(f'{0}{hour}:{0}{minutes}:{0}{seconds}')
else:
    print(f'{hour}:{minutes}:{seconds}')

print(f'{hours:02}') #  где 02 - количество позиций  !!!