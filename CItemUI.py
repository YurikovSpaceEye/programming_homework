# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CItemUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CItem(object):
    def setupUi(self, CItem):
        if not CItem.objectName():
            CItem.setObjectName(u"CItem")
        CItem.resize(400, 300)
        self.verticalLayout = QVBoxLayout(CItem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_name = QLineEdit(CItem)
        self.le_name.setObjectName(u"le_name")

        self.verticalLayout.addWidget(self.le_name)

        self.le_cost = QLineEdit(CItem)
        self.le_cost.setObjectName(u"le_cost")

        self.verticalLayout.addWidget(self.le_cost)

        self.cmb_category = QComboBox(CItem)
        self.cmb_category.setObjectName(u"cmb_category")

        self.verticalLayout.addWidget(self.cmb_category)

        self.dt_edit = QDateTimeEdit(CItem)
        self.dt_edit.setObjectName(u"dt_edit")

        self.verticalLayout.addWidget(self.dt_edit)

        self.b_delete_item = QPushButton(CItem)
        self.b_delete_item.setObjectName(u"b_delete_item")

        self.verticalLayout.addWidget(self.b_delete_item)


        self.retranslateUi(CItem)
        self.cmb_category.currentTextChanged.connect(CItem.cmb_category_slot)
        self.le_cost.editingFinished.connect(CItem.le_cost_slot)
        self.le_name.editingFinished.connect(CItem.le_name_slot)
        self.dt_edit.dateTimeChanged.connect(CItem.dt_edit_slot)
        self.b_delete_item.clicked.connect(CItem.b_delete_item_slot)

        QMetaObject.connectSlotsByName(CItem)
    # setupUi

    def retranslateUi(self, CItem):
        CItem.setWindowTitle(QCoreApplication.translate("CItem", u"Form", None))
        self.b_delete_item.setText(QCoreApplication.translate("CItem", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

