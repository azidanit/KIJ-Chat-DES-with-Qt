# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kij_chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(530, 416)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 10, 91, 17))
        self.message_textBrowser = QTextBrowser(self.centralwidget)
        self.message_textBrowser.setObjectName(u"message_textBrowser")
        self.message_textBrowser.setGeometry(QRect(20, 40, 481, 251))
        self.message_textEdit = QTextEdit(self.centralwidget)
        self.message_textEdit.setObjectName(u"message_textEdit")
        self.message_textEdit.setGeometry(QRect(20, 300, 411, 70))
        self.send_pushButton = QPushButton(self.centralwidget)
        self.send_pushButton.setObjectName(u"send_pushButton")
        self.send_pushButton.setGeometry(QRect(440, 300, 61, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.message_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ASDSADSA</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dddddd</p></body></html>", None))
        self.send_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kirim", None))
    # retranslateUi

