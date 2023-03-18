import view
import model

functionList = []
functionList.insert(0, "Ошибка! Попробуйте снова.\n")
functionList.insert(1, model.showContacts)
functionList.insert(2, model.searchContact)
functionList.insert(3, model.addContact)
functionList.insert(4, model.changeContact)
functionList.insert(5, model.delContact)
functionList.insert(6, model.exit)


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
