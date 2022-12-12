from CollectionsContainer import Collections


def delete_item(collection:Collections, current_category:str, sort_by_cost:bool, big_to_small:bool):
    inpt = input("Удалить элемент: ")
    try:
        num = int(inpt)
    except:
        print("Неверный ввод.")
        return

    if sort_by_cost:
        data = collection.get_sorted_category_by_cost(current_category, big_to_small)
    else:
        data = collection.get_sorted_category_by_time(current_category, big_to_small)

    if num <= 0 or num > len(data):
        print("Такого элемента нет в списке.")
        return

    if current_category == "всё":
        element = data[num-1]
        for category in collection.data.values():
            for item in category:
                if item.__hash__() == element.__hash__():
                    category.remove(item)
                    if len(category) == 0:
                        del category

                        for key in collection.data.keys():
                            if len(collection.data[key]) == 0:
                                collection.data.pop(key, None)
                                break

                        return
    else:
        data.remove(data[num-1])
