
class PBManager:
    def __init__(self, path: str):
        self.path = path

    def showContacts(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            lines = data.read()
            if lines == '':
                lines = "Книга пуста"
        print(lines)


    def searchContact(self):
        contact = input("Введите фамилию или должность с большой буквы ")
        with open(self.path, 'r', encoding='UTF-8') as data:
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

    def addContact(self):
        nameContact = input("Введите фамилию и имя с большой буквы через пробел ")
        phoneNum = input("Введите номер телефона в формате +7-ХХХ-ХХХ-ХХ-ХХ ")
        position = input("Введите должность с большой буквы ")
        contact = nameContact + " " + phoneNum + " " + position
        print(f"Вы хотите добавить в справочник контакт:\n{contact}")
        check = input("Сохранить: нажмите 1 / Отменить: нажмите 0\n")
        if check == "1":
            with open(self.path, 'r+', encoding='UTF-8') as data:
                lines = data.readlines()
                count = len(lines)
                contact = "\n" + str(count) + " " + contact
                data.write(contact)
                print("Сохранение прошло успешно!")


    def changeContact(self):
        while (True):
            contactInd = int(input(
                "Введите индекс контакта, который хотите изменить (для выхода нажмите 0) "))
            with open(self.path, 'r', encoding='UTF-8') as data:
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
                    with open(self.path, 'w', encoding='UTF-8') as data:
                        data.write("№ Фамилия Имя Телефон Должность\n")
                    with open(self.path, 'a', encoding='UTF-8') as data:
                        for i in range(1, count):
                            data.write(lines[i])
                elif num == "2":
                    newPhone = input(
                        "Введите номер телефона в формате +7-ХХХ-ХХХ-ХХ-ХХ ")
                    item = lines[contactInd].split()
                    item[3] = newPhone
                    lines[contactInd] = ' '.join(item) + "\n"
                    with open(self.path, 'w', encoding='UTF-8') as data:
                        data.write("№ Фамилия Имя Телефон Должность\n")
                    with open(self.path, 'a', encoding='UTF-8') as data:
                        for i in range(1, count):
                            data.write(lines[i])
                elif num == "3":
                    newPosition = input("Введите должность с большой буквы ")
                    item = lines[contactInd].split()
                    item[4] = newPosition
                    lines[contactInd] = ' '.join(item) + "\n"
                    with open(self.path, 'w', encoding='UTF-8') as data:
                        data.write("№ Фамилия Имя Телефон Должность\n")
                    with open(self.path, 'a', encoding='UTF-8') as data:
                        for i in range(1, count):
                            data.write(lines[i])
                else:
                    print("Ошибка! Попробуйте снова\n")
            else:
                print("Ошибка! Попробуйте снова\n")


    def delContact(self):
        while (True):
            contactInd = int(input(
                "Введите индекс контакта, который хотите удалить "))
            with open(self.path, 'r', encoding='UTF-8') as data:
                lines = data.readlines()
                count = len(lines)
            if contactInd > 0 and contactInd <= count:
                lines.pop(contactInd)
                count -= 1
                with open(self.path, 'w', encoding='UTF-8') as data:
                    data.write("№ Фамилия Имя Телефон Должность\n")
                with open(self.path, 'a', encoding='UTF-8') as data:
                    for i in range(1, count):
                        item = lines[i].split()
                        item[0] = str(i)
                        lines[i] = ' '.join(item) + "\n"
                        data.write(lines[i])
                break
            else:
                print("Ошибка! Попробуйте снова\n")


    def exit(self):
        print("Работа завершена. До скорых встреч!")
        return False
