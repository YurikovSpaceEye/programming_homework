from CollectionsContainer import Collections


def change_sort(collection: Collections, current_category, sort_by_cost, big_to_small):
    inpt = input("Поменять категорию? д/н. ")
    available_categories = ["всё"]
    available_categories += collection.get_categories()

    if inpt.lower() == "д":
        print("Доступные категории:")
        for i, item in enumerate(available_categories):
            print(f"{i + 1}. {item}")

        print(f"Текущая категория: {current_category}")

        inpt = input("Поменять на: ")
        try:
            num = int(inpt)
        except:
            print("Неверный ввод.")
            return current_category, sort_by_cost, big_to_small
        if num <= 0 or num > len(available_categories):
            print("Неверная позиция.")
            return current_category, sort_by_cost, big_to_small
        current_category = available_categories[num-1]

    inpt = input("Поменять тип сортировки? д/н. ")
    if inpt.lower() == "д":
        inpt = input("1. Сортировка по цене.\n2. Сортировка по дате.\n")
        if inpt == "1":
            sort_by_cost = True
        elif inpt == "2":
            sort_by_cost = False
        else:
            print("Неверный ввод.")
            return current_category, sort_by_cost, big_to_small

    inpt = input("Поменять порядок сортровки? д/н. ")
    if inpt.lower() == "д":
        if sort_by_cost:
            inpt = input("1. Сортировка от большего к меньшему.\n2. Сортировка от меньшего к большему.\n")
        else:
            inpt = input("1. Сортировка от ближайшей даты к дальней.\n2. Сортировка от дальней даты к ближайшей.\n")
        if inpt == "1":
            big_to_small = True
        elif inpt == "2":
            big_to_small = False
        else:
            print("Неверный ввод.")
            return current_category, sort_by_cost, big_to_small

    return current_category, sort_by_cost, big_to_small
