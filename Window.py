from os.path import isfile, dirname

import PySide2
from PySide2 import QtWidgets

from CollectionsContainer import Collections
from MainWindowUI import Ui_MainWindow
from CItem import CItemWidget, CItemManager

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.collections = Collections()
        self.manager = CItemManager(self.ui.citems_layout, self.collections)

        self.data_path = dirname(__file__) + "/data.json"

        self.load_sequence()

    def load_sequence(self):
        if not isfile(self.data_path):
            open(self.data_path, mode="w")

        with open(self.data_path, mode="r") as file:
            self.collections.load_from_json(file.read())

        self.manager.reload_widgets()

    def save_state(self):
        json_str = self.collections.save_to_json_str()
        with open(self.data_path, mode="w") as file:
            file.write(json_str)

    def update_state(self):
        self.save_state()
        self.manager.reload_widgets()

    # ==================== Slots ====================

    def cmb_sort_category_filter_slot(self, s):
        pass

    def cmb_sort_by_slot(self, s):
        pass

    def cmb_sort_order_cost_slot(self, s):
        pass

    def cmb_sort_order_date_slot(self, s):
        pass

    def b_new_item_slot(self):
        self.manager.new_widget()
        pass

    # ==================== Events ====================

    def closeEvent(self, event:PySide2.QtGui.QCloseEvent) -> None:
        self.save_state()

        self.close()
