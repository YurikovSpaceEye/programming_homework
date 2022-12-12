from CollectionsContainer import Collections


def display_items(collection: Collections, category: str, sort_by_cost: bool, big_to_small:bool):
    if sort_by_cost:
        data = collection.get_sorted_category_by_cost(category, big_to_small)
    else:
        data = collection.get_sorted_category_by_time(category, big_to_small)

    print(f"Категория: {category}."
          f" Сортировка по {'цене' if sort_by_cost else 'дате'}."
          f" В {'уменьшающейся' if big_to_small else 'увеличивающейся'} последовательности.")
    for i, item in enumerate(data):
        print(f"{i+1}. {item.name} | Цена: {item.cost} | Дата добавления: {item.date}")
