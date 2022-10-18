# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 761)
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 607, 741))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.citems_layout = QVBoxLayout()
        self.citems_layout.setObjectName(u"citems_layout")

        self.verticalLayout_3.addLayout(self.citems_layout)


        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cmb_category_filter = QComboBox(MainWindow)
        self.cmb_category_filter.setObjectName(u"cmb_category_filter")

        self.horizontalLayout_4.addWidget(self.cmb_category_filter)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.cmb_sort_by = QComboBox(MainWindow)
        self.cmb_sort_by.addItem("")
        self.cmb_sort_by.addItem("")
        self.cmb_sort_by.setObjectName(u"cmb_sort_by")

        self.horizontalLayout_2.addWidget(self.cmb_sort_by)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.cmb_sort_order_cost = QComboBox(MainWindow)
        self.cmb_sort_order_cost.addItem("")
        self.cmb_sort_order_cost.addItem("")
        self.cmb_sort_order_cost.setObjectName(u"cmb_sort_order_cost")

        self.horizontalLayout_3.addWidget(self.cmb_sort_order_cost)

        self.cmb_sort_order_date = QComboBox(MainWindow)
        self.cmb_sort_order_date.addItem("")
        self.cmb_sort_order_date.addItem("")
        self.cmb_sort_order_date.setObjectName(u"cmb_sort_order_date")

        self.horizontalLayout_3.addWidget(self.cmb_sort_order_date)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.b_new_item = QPushButton(MainWindow)
        self.b_new_item.setObjectName(u"b_new_item")

        self.verticalLayout.addWidget(self.b_new_item)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 4)

        self.retranslateUi(MainWindow)
        self.cmb_category_filter.currentTextChanged.connect(MainWindow.cmb_sort_category_filter_slot)
        self.cmb_sort_by.currentTextChanged.connect(MainWindow.cmb_sort_by_slot)
        self.cmb_sort_order_cost.currentTextChanged.connect(MainWindow.cmb_sort_order_cost_slot)
        self.cmb_sort_order_date.currentTextChanged.connect(MainWindow.cmb_sort_order_date_slot)
        self.b_new_item.clicked.connect(MainWindow.b_new_item_slot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u0448\u0435\u043b\u0435\u043a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u043f\u043e", None))
        self.cmb_sort_by.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0435", None))
        self.cmb_sort_by.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0435", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430 \u043e\u0442", None))
        self.cmb_sort_order_cost.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0431\u043e\u043b\u044c\u0448\u0435\u0433\u043e \u043a \u043c\u0435\u043d\u044c\u0448\u0435\u043c\u0443", None))
        self.cmb_sort_order_cost.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043c\u0435\u043d\u044c\u0448\u0435\u0433\u043e \u043a \u0431\u043e\u043b\u044c\u0448\u043e\u043c\u0443", None))

        self.cmb_sort_order_date.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0440\u0430\u043d\u043d\u0435\u0433\u043e \u043a \u043f\u043e\u0437\u0434\u043d\u0435\u043c\u0443", None))
        self.cmb_sort_order_date.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0437\u0434\u043d\u0435\u0433\u043e \u043a \u0440\u0430\u043d\u043d\u0435\u043c\u0443", None))

        self.b_new_item.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043f\u043e\u043a\u0443\u043f\u043a\u0430", None))
    # retranslateUi

