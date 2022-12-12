import os

from CollectionsContainer import Collections

from add_item_ui import add_item
from change_sort_ui import change_sort
from delete_item_ui import delete_item
from display_items_ui import display_items

def save_data(collection: Collections):
    data = collection.save_to_json_str()
    with open("data.json", mode="w") as file:
        file.write(data)

def load_data(collection: Collections):
    if os.path.exists("data.json"):
        with open("data.json", mode="r") as file:
            data = file.read()
        collection.load_from_json(data)

        while True:
            for key in collection.data.keys():
                if len(collection.data[key]) == 0:
                    collection.data.pop(key, None)
                    break
            else:
                break
    else:
        save_data(collection)


greeting_str = "" \
               "Это программа для контроля собственных денежных средств. Выберете опцию:\n" \
               "1. Просмотреть записи.\n" \
               "2. Поменять отображение предметов.\n"\
               "3. Добавить запись.\n" \
               "4. Удалить запись.\n" \
               "в. Выйти из программы\n"
def main(collection: Collections):
    load_data(collection)
    current_category = "всё"

    #Если false то сортирует по дате
    sort_by_cost = False
    big_to_small = True

    while True:
        answ = input(greeting_str)
        if answ == "1":
            display_items(collection, current_category, sort_by_cost, big_to_small)
        elif answ == "2":
            current_category, sort_by_cost, big_to_small = change_sort(collection, current_category, sort_by_cost, big_to_small)
            pass
        elif answ == "3":
            add_item(collection)
            save_data(collection)
        elif answ == "4":
            delete_item(collection, current_category, sort_by_cost, big_to_small)
            save_data(collection)
        else:
            save_data(collection)
            return

if __name__ == "__main__":
    collection = Collections()
    try:
        main(collection)
    except KeyboardInterrupt:
        save_data(collection)