import view
import model
import PhoneBook

pb = PhoneBook.PBManager('phone.txt')

functionList = []
functionList.insert(0, "Ошибка! Попробуйте снова.\n")
functionList.insert(1, pb.showContacts)
functionList.insert(2, pb.searchContact)
functionList.insert(3, pb.addContact)
functionList.insert(4, pb.changeContact)
functionList.insert(5, pb.delContact)
functionList.insert(6, pb.exit)


def start():
    flag = True
    while(flag):
        choice = view.menu()
        match choice:
            case 1 | 2 | 3 | 4 | 5:
                functionList[choice]()
            case 6:
                flag = functionList[choice]()
            case _:
                print(functionList[0])
