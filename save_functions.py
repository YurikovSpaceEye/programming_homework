import os

from CollectionsContainer import Collections


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
