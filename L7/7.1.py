# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в
# порядке и “Пам парам”, если с ритмом все не в порядке

vowelsList = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ы' 'ю', 'я']
# poem = input("Enter Winnie's rhyme ")
poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
phraseList = poem.split(' ')
print(phraseList)


def countVowels(list1, list2):
    count = 0
    countList = []
    for word in list1:
        for letter in word:
            if letter in list2:
                count += 1
        countList.append(count)
        count = 0
    return countList


numOfVows = countVowels(phraseList, vowelsList)
print(numOfVows)


def checkRhyme(someList):
    x0 = someList[0]
    if len(someList) == len(list(filter(lambda x: x == x0, someList))):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


res = checkRhyme(countVowels(phraseList, vowelsList))
print(res)
