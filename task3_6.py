# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских
# букв и возвращающую его же, но с
# прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием.
# В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое
# слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

"""Сложный путь в попытке написать код, или как написать программу,
которая делает вывод латинских слов с заглавной буквы отсеивая слова с кириллицей."""


def my_func(entered_word):
    small_letter = entered_word[0]
    big_letter = chr(ord(small_letter) - ord('a') + ord('A'))
    return big_letter + entered_word[1:]


my_words = input('Enter something: ').split()
list_of_words = []
for word in my_words:
    list_of_words.append(my_func(word))
    for i in list_of_words:
        if 65 < ord(i[0]) and ord(i[0]) > 122:
            list_of_words.remove(i)

print(' '.join(list_of_words))
