import datetime
from typing import List

from CollectionsContainer import Collections, CollectionItem


def get_user_cost():
    while True:
        inpt = input("Напишите цену предмета:\n")
        try:
            return int(inpt)
        except:
            print("Неверная цена предмета.\n")


def get_user_date():
    def is_true(text1:str, text2:str, ret):
        inpt = input(text1)
        if inpt.lower() == "д":
            return ret
        else:
            inpt = input(text2)
            try:
                return int(inpt)
            except:
                print("Не число.\n")
                raise Exception
    try:
        now = datetime.datetime.now()
        now = now.replace(
            is_true("Год: "     +str(now.year)  +". д/н. ", "Введите год: ", now.year),
            is_true("Месяц: "   +str(now.month) +". д/н. ", "Введите месяц: ", now.month),
            is_true("День: "    +str(now.day)   +". д/н. ", "Введите день: ", now.day),
            is_true("Час: "     +str(now.hour)  +". д/н. ", "Введите час: ", now.hour),
            is_true("Минута: "  +str(now.minute)+". д/н. ", "Введите минуту: ", now.minute),
            is_true("Секунда: " +str(now.second)+". д/н. ", "Введите секунду: ", now.second),
            0)
        return now
    except:
        print("Неправильна была введена дата.\n")
        raise Exception


def get_user_category(categories: List[str]):
        print(f"Сущестующие категории ({len(categories)}):\n")
        for i, item in enumerate(categories):
            print(f"{i+1}. {item}")
        print("")
        inpt = input("1. Выбрать из сущесвующей категории\n"
                     "2. Создать новую категорию\n")
        if inpt == "1":
            if (len(categories) == 0):
                print("Нет категорий для выбора.")
                raise Exception

            inpt = input("Напишите номер категории: ")
            try:
                num = int(inpt)
            except:
                print("Ввод не число.")
                raise Exception
            if num <= 0  or num > len(categories)+1:
                print("Номер больше чем кол-во категорий.")
                raise Exception
            return categories[num-1]
        elif inpt == "2":
            inpt = input("Напишите новую категорию: ")
            if inpt in categories or inpt == "всё":
                print("Уже есть такая категория.")
                raise Exception
            return inpt
        else:
            print("Неверный выбор.")


def add_item(collection: Collections):
    try:
        name = input("Напишите имя предмета:\n")
        cost = get_user_cost()
        date = get_user_date()
        category = get_user_category(collection.get_categories())

        new_item = CollectionItem(name, cost, date)
        collection.add_to_category(category, new_item)
    except:
        return
