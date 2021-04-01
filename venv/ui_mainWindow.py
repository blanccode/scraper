# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import scraper



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 433)
        MainWindow.setMinimumSize(QSize(640, 433))
        MainWindow.setMaximumSize(QSize(640, 433))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color:rgb(40, 42, 54);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 581, 281))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(
            u"background-color: rgb(32, 33, 43);\n"
            "border-style:outset;\n"
            "border-width: 2px;\n"
            "border-color: rgb(181, 137, 238);\n"
            "border-radius: 3px;"
        )
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 451, 20))
        self.label.setStyleSheet(u"border:none;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 350, 111, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(
            u"border-color: rgb(155, 120, 203);\n"
            "color: rgb(243, 243, 237);\n"
            "border-style:outset;\n"
            "border-width: 1px;\n"
            "border-radius: 5px;\n"
            "background-color: rgb(32, 33, 43);\n"
            ""
        )
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.clicked.connect(self.clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet(u"background-color:rgb(40, 42, 54);")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet(u"background-color:rgb(40, 42, 54);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def clicked(self):
        scraper.makeRequest()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                u'<html><head/><body><p><span style=" color:#f8f8f2;">all systems are up and running..</span></p></body></html>',
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Start Scraping", None)
        )
        # scraper.scrapeMediamarkt()

    # retranslateUi
