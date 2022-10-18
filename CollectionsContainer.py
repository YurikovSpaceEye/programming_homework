import calendar
import datetime
import json
from typing import TypeVar, Dict, AnyStr, List, Any


class CollectionItem:
    def __init__(self, name, cost, date):
        self.name:str = name
        self.cost:float = cost
        self.date:datetime.date = date


T = TypeVar("T", CollectionItem, None)


class Collections:
    def __init__(self):
        self.data: Dict[AnyStr, List[CollectionItem]] = dict()

    def add_to_collection(self, category: str, item: CollectionItem):
        if category not in self.data.keys():
            self.data[category] = []

        self.data[category].append(item)

    def get_collection_item(self, category: str, idx: int) -> T:
        if len(self.data[category]) <= idx:
            return None

        return self.data[category][idx]

    def get_all_collection(self, category: str) -> List[CollectionItem]:
        return self.data[category]

    def get_categories(self) -> List[str]:
        return self.data.keys()

    def get_sorted_category_by_cost(self, category: str, btos: bool) -> List[CollectionItem]:
        self.data[category].sort(key=lambda x: x.cost, reverse=btos)
        return self.data[category]

    def get_sorted_category_by_time(self, category:str, btos:bool) -> List[CollectionItem]:
        self.data[category].sort(key=lambda x: calendar.timegm(x.date.timetuple()), reverse=btos)
        return self.data[category]

    # def remove_collection_item(self, category:str, idx: int):
    #     if len(self.data[category]) <= idx:
    #         return
    #
    #     self.data[category].remove(self.data[category][idx])
    #
    #     if len(self.data[category]) == 0:
    #         del self.data[category]

    def remove_collection_item(self, category:str, item:CollectionItem):
        self.data[category].remove(item)

        if len(self.data[category]) == 0:
            del self.data[category]

    def save_to_json_str(self) -> str:
        temp = dict()
        for key in self.data.keys():
            temp[key] = []
            for item in self.data[key]:
                temp[key].append({"date": int(calendar.timegm(item.date.timetuple())),
                                  "cost": item.cost,
                                  "name": item.name})

        return json.dumps(temp)

    def load_from_json(self, json_str:str):
        if (len(json_str) == 0):
            return
        temp: Dict[str, List[Dict[str, Any]]] = json.loads(json_str)

        for key in temp.keys():
            self.data[key] = []
            for item in temp[key]:
                self.data[key].append(CollectionItem(item["name"],
                                                     item["cost"],
                                                     datetime.date.fromtimestamp(item["date"])))
