# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

"""Использовала текстовые файлы из архива"""

from textblob import TextBlob

with open('text_4.txt') as eng_text:
    text = eng_text.read()
    blob = TextBlob(text)
    rus_text = str(blob.translate(to='ru'))
    print(rus_text)
    with open('task5_4_result.txt', 'w') as rus_tx:
        rus_tx.write(rus_text)
