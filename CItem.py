import datetime
import time
import calendar

from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtCore import QDateTime, QDate, QCalendar
import PySide2

from CItemUI import Ui_CItem
from PySide2.QtWidgets import QWidget

from CollectionsContainer import CollectionItem, Collections
from ExtraFuctions import process_le_to_number

from typing import TypeVar, Dict, AnyStr, List

class CItemWidget(QWidget):
    def __init__(self,
                 item: CollectionItem,
                 collections: Collections,
                 del_function,
                 category: str):
        super(CItemWidget, self).__init__()

        self.ui = Ui_CItem()
        self.ui.setupUi(self)

        self.item = item
        self.collections = collections
        self.category = category
        self.del_function = del_function

        self.init_ui()

    def init_ui(self):
        self.ui.le_name.setText(self.item.name)
        self.ui.le_cost.setText(str(self.item.cost))
        self.ui.dt_edit.setDate(self.item.date)

    def cmb_category_slot(self, s:str):
        self.collections.remove_collection_item(self.category, self.item)
        self.collections.add_to_collection(s, self.item)
        self.category = s
        pass

    def le_cost_slot(self):
        self.item.cost = process_le_to_number(self.ui.le_cost.text(),
                                              float,
                                              self.item.cost)

        self.ui.le_cost.setText(str(self.item.cost))
        pass

    def le_name_slot(self):
        self.item.name = self.ui.le_name.text()
        pass

    def dt_edit_slot(self, dt:PySide2.QtCore.QDateTime):
        self.item.date = dt.date().toPython()
        pass

    def b_delete_item_slot(self):
        self.del_function(self, self.category)
        pass

class CItemManager:
    def __init__(self, layout:PySide2.QtWidgets.QVBoxLayout, collections: Collections):
        self.layout = layout
        self.collections = collections
        self.layout_widgets: Dict[str, List[CItemWidget]] = dict()
        self.categories = ["all"]
        self.btos = False
        self.sort_by_time = True

        self.selected_category = "all"

        self.layout_widgets[self.categories[0]] = []

    def process_delete(self, item: CItemWidget, category:str):
        self.layout_widgets[category].remove(item)
        if len(self.layout_widgets) == 0:
            del self.layout_widgets[category]

        self.collections.remove_collection_item(category, item.item)
        self.layout.itemAt(item).widget().deleteLater()

    def new_widget(self):
        item = CollectionItem("Напишите имя", 0, datetime.date.fromtimestamp(time.time()))
        self.collections.add_to_collection(self.categories[0], item)
        new_widget = CItemWidget(item, self.collections, self.process_delete, self.categories[0])
        self.layout.addWidget(new_widget)

        self.layout_widgets[self.categories[0]].append(new_widget)

    def hide_all(self):
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().hide()

    def show_all(self):
        for i in range(self.layout.count()):
            self.layout.itemAt(i).widget().show()

    def sort_category_by_cost(self, category: str, btos: bool):
        self.layout_widgets[category].sort(key=lambda x: x.item.cost, reverse=btos)

    def sort_category_by_time(self, category:str, btos:bool):
        self.layout_widgets[category].sort(key=lambda x: calendar.timegm(x.item.date.timetuple()), reverse=btos)

    def sort_category(self):
        if self.sort_by_time:
            self.sort_category_by_time(self.selected_category, self.btos)
        else:
            self.sort_category_by_cost(self.selected_category, self.btos)

    def update_items_visibility(self):
        self.hide_all()

        if (self.selected_category == self.categories[0]):
            self.show_all()
            return

        self.sort_category()

        widgets = self.layout_widgets[self.selected_category]

        for widget in widgets:
            widget.show()

    def reload_widgets(self):
        self.hide_all()
        for key in self.layout_widgets.keys():
            for widget in self.layout_widgets[key]:
                widget.deleteLater()

        self.layout_widgets = dict({"all":[]})
        self.layout = QVBoxLayout()

        for key in self.collections.data.keys():
            self.layout_widgets[key] = []
            for item in self.collections.data[key]:
                new_widget = CItemWidget(item, self.collections, self.process_delete, key)
                new_widget.ui.le_name.setText(item.name)
                new_widget.ui.le_cost.setText(str(item.cost))
                new_widget.ui.dt_edit.setDate(QDate(item.date.year,
                                                    item.date.month,
                                                    item.date.day
                                                    ))
        self.update_items_visibility()
