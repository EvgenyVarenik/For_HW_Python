"""
 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам 

Вывод:
Парам пам-пам
"""
def rhytm(text):
    text = text.lower().split()
    glasnie = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
    if len(set(map(lambda x: len([i for i in x if i in glasnie]), text))) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'

print(rhytm(text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'))

