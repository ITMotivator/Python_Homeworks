path = 'L8/phone.txt'


def showContacts():
    with open(path, 'r', encoding='UTF-8') as data:
        lines = data.read()
        if lines == '':
            lines = "Книга пуста"
    print(lines)
    print()


def searchContact():
    contact = input("Введите фамилию или должность с большой буквы ")
    with open(path, 'r', encoding='UTF-8') as data:
        lines = data.readlines()
        count = len(lines)
        flag = False
        for i in range(1, count):
            item = lines[i].split()
            if item[1] == contact or item[4] == contact:
                print(lines[i])
                flag = True
        if flag == False:
            print("Контакт не найден\n")


def addContact():
    nameContact = input("Введите фамилию и имя с большой буквы через пробел ")
    phoneNum = input("Введите номер телефона в формате +7-ХХХ-ХХХ-ХХ-ХХ ")
    position = input("Введите должность с большой буквы ")
    contact = nameContact + " " + phoneNum + " " + position
    print(f"Вы хотите добавить в справочник контакт:\n{contact}")
    check = input("Сохранить: нажмите 1 / Отменить: нажмите 0\n")
    if check == "1":
        with open(path, 'r+', encoding='UTF-8') as data:
            lines = data.readlines()
            count = len(lines)
            contact = "\n" + str(count) + " " + contact
            data.write(contact)
            print("Сохранение прошло успешно!")


def changeContact():
    while (True):
        contactInd = int(input(
            "Введите индекс контакта, который хотите изменить (для выхода нажмите 0) "))
        with open(path, 'r', encoding='UTF-8') as data:
            lines = data.readlines()
            count = len(lines)
        if contactInd == 0:
            break
        elif contactInd > 0 and contactInd <= count:
            print("Что вы хотите поменять?\n" +
                  "1. Фамилия/имя 2. Телефон 3. Должность")
            num = input()
            if num == "1":
                newName = input(
                    "Введите фамилию и имя с большой буквы через пробел ")
                item = lines[contactInd].split()
                item[1] = newName
                lines[contactInd] = item[0] + " " + \
                    item[1] + " " + item[3] + " " + item[4]
                with open(path, 'w', encoding='UTF-8') as data:
                    data.write("№ Фамилия Имя Телефон Должность\n")
                with open(path, 'a', encoding='UTF-8') as data:
                    for i in range(1, count):
                        data.write(lines[i])
            elif num == "2":
                newPhone = input(
                    "Введите номер телефона в формате +7-ХХХ-ХХХ-ХХ-ХХ ")
                item = lines[contactInd].split()
                item[3] = newPhone
                lines[contactInd] = ' '.join(item) + "\n"
                with open(path, 'w', encoding='UTF-8') as data:
                    data.write("№ Фамилия Имя Телефон Должность\n")
                with open(path, 'a', encoding='UTF-8') as data:
                    for i in range(1, count):
                        data.write(lines[i])
            elif num == "3":
                newPosition = input("Введите должность с большой буквы ")
                item = lines[contactInd].split()
                item[4] = newPosition
                lines[contactInd] = ' '.join(item) + "\n"
                with open(path, 'w', encoding='UTF-8') as data:
                    data.write("№ Фамилия Имя Телефон Должность\n")
                with open(path, 'a', encoding='UTF-8') as data:
                    for i in range(1, count):
                        data.write(lines[i])
            else:
                print("Ошибка! Попробуйте снова\n")
        else:
            print("Ошибка! Попробуйте снова\n")


def delContact():
    while (True):
        contactInd = int(input(
            "Введите индекс контакта, который хотите удалить (для выхода нажмите 0) "))
        with open(path, 'r', encoding='UTF-8') as data:
            lines = data.readlines()
            count = len(lines)
        if contactInd == 0:
            break
        elif contactInd > 0 and contactInd <= count:
            lines.pop(contactInd)
            count -= 1
            with open(path, 'w', encoding='UTF-8') as data:
                data.write("№ Фамилия Имя Телефон Должность\n")
            with open(path, 'a', encoding='UTF-8') as data:
                for i in range(1, count):
                    item = lines[i].split()
                    item[0] = str(i)
                    lines[i] = ' '.join(item) + "\n"
                    data.write(lines[i])
        else:
            print("Ошибка! Попробуйте снова\n")


functionList = []
functionList.insert(0, "Ошибка! Попробуйте снова.\n")
functionList.insert(1, showContacts)
functionList.insert(2, searchContact)
functionList.insert(3, addContact)
functionList.insert(4, changeContact)
functionList.insert(5, delContact)
choiceList = [1, 2, 3, 4, 5]


def menu():
    print("Добро пожаловать в справочник контактов компании Ругугл:\n")
    while (True):
        print("1. Показать все контакты\n" +
              "2. Найти контакт\n" +
              "3. Добавить контакт\n" +
              "4. Изменить контакт\n" +
              "5. Удалить контакт\n" +
              "6. Выход\n")
        choice = int(input("Выберите пункт меню "))
        if choice in choiceList:
            functionList[choice]()
        elif choice == 6:
            print("Работа завершена. До скорых встреч!")
            break
        else:
            print(functionList[0])


menu()
