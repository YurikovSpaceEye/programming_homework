import calendar
import datetime
import json
from typing import TypeVar, Dict, AnyStr, List, Any


class CollectionItem:
    def __init__(self, name, cost, date):
        self.name:str = name
        self.cost:int = cost
        self.date:datetime.datetime = date


T = TypeVar("T", CollectionItem, None)


class Collections:
    def __init__(self):
        self.data: Dict[AnyStr, List[CollectionItem]] = dict()

    def add_to_collection(self, category: str, item: CollectionItem):
        if category not in self.data.keys():
            self.data[category] = []

        self.data[category].append(item)

    def get_collection(self, category: str) -> List[CollectionItem]:
        if category != "всё":
            return self.data[category]
        else:
            values = self.data.values()
            data = []
            for value in values:
                data += value
            return data

    def get_categories(self) -> List[str]:
        data = []
        for key in self.data.keys():
            data.append(key)
        return data

    def get_sorted_category_by_cost(self, category: str, btos: bool) -> List[CollectionItem]:
        data = self.get_collection(category)
        data.sort(key=lambda x: x.cost, reverse=btos)
        return data

    def get_sorted_category_by_time(self, category:str, btos:bool) -> List[CollectionItem]:
        data = self.get_collection(category)
        data.sort(key=lambda x: calendar.timegm(x.date.timetuple()), reverse=btos)
        return data

    def save_to_json_str(self) -> str:
        temp = dict()
        for key in self.data.keys():
            temp[key] = []

            for item in self.data[key]:
                date = {}
                date["year"] = item.date.year
                date["month"] = item.date.month
                date["day"] = item.date.day
                date["hour"] = item.date.hour
                date["minute"] = item.date.minute
                date["second"] = item.date.second

                temp[key].append({"date": date,
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
                                                     datetime.datetime(
                                                         item["date"]["year"],
                                                         item["date"]["month"],
                                                         item["date"]["day"],
                                                         item["date"]["hour"],
                                                         item["date"]["minute"],
                                                         item["date"]["second"],
                                                     )))
