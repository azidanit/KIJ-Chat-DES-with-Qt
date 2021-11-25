# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kij_chat_form_resp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(897, 745)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.to_connect = QHBoxLayout()
        self.to_connect.setObjectName(u"to_connect")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.host_lineEdit = QLineEdit(Form)
        self.host_lineEdit.setObjectName(u"host_lineEdit")
        font = QFont()
        font.setPointSize(11)
        self.host_lineEdit.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.host_lineEdit)


        self.to_connect.addLayout(self.formLayout_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.port_lineEdit = QLineEdit(Form)
        self.port_lineEdit.setObjectName(u"port_lineEdit")
        self.port_lineEdit.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.port_lineEdit)


        self.to_connect.addLayout(self.formLayout_2)

        self.connect_to_client_pushButton = QPushButton(Form)
        self.connect_to_client_pushButton.setObjectName(u"connect_to_client_pushButton")

        self.to_connect.addWidget(self.connect_to_client_pushButton)


        self.verticalLayout.addLayout(self.to_connect)

        self.our_2 = QHBoxLayout()
        self.our_2.setObjectName(u"our_2")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.myhost_ip_lineEdit = QLineEdit(Form)
        self.myhost_ip_lineEdit.setObjectName(u"myhost_ip_lineEdit")
        self.myhost_ip_lineEdit.setEnabled(True)
        self.myhost_ip_lineEdit.setFont(font)
        self.myhost_ip_lineEdit.setReadOnly(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.myhost_ip_lineEdit)


        self.our_2.addLayout(self.formLayout_6)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.myport_lineEdit = QLineEdit(Form)
        self.myport_lineEdit.setObjectName(u"myport_lineEdit")
        self.myport_lineEdit.setFont(font)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.myport_lineEdit)


        self.our_2.addLayout(self.formLayout_7)

        self.disconnect_all_pushButton = QPushButton(Form)
        self.disconnect_all_pushButton.setObjectName(u"disconnect_all_pushButton")

        self.our_2.addWidget(self.disconnect_all_pushButton)


        self.verticalLayout.addLayout(self.our_2)

        self.message_textBrowser = QTextBrowser(Form)
        self.message_textBrowser.setObjectName(u"message_textBrowser")
        font1 = QFont()
        font1.setPointSize(12)
        self.message_textBrowser.setFont(font1)

        self.verticalLayout.addWidget(self.message_textBrowser)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.message_textEdit = QTextEdit(Form)
        self.message_textEdit.setObjectName(u"message_textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_textEdit.sizePolicy().hasHeightForWidth())
        self.message_textEdit.setSizePolicy(sizePolicy)
        self.message_textEdit.setMaximumSize(QSize(16777215, 50))
        self.message_textEdit.setFont(font1)

        self.horizontalLayout_3.addWidget(self.message_textEdit)

        self.send_pushButton = QPushButton(Form)
        self.send_pushButton.setObjectName(u"send_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.send_pushButton.sizePolicy().hasHeightForWidth())
        self.send_pushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.send_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Chat Dengan DES", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Host", None))
        self.label.setText(QCoreApplication.translate("Form", u"Port", None))
        self.port_lineEdit.setText(QCoreApplication.translate("Form", u"5557", None))
        self.connect_to_client_pushButton.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"IP ADDRESS ANDA", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Port Koneksi Ke Komputer Anda", None))
        self.myport_lineEdit.setText(QCoreApplication.translate("Form", u"5556", None))
        self.disconnect_all_pushButton.setText(QCoreApplication.translate("Form", u"Disconnect All", None))
        self.message_textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:14pt;\">ASDSADSA</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-size:14pt;\">dddddd</span></p></body></html>", None))
        self.send_pushButton.setText(QCoreApplication.translate("Form", u"Kirim", None))
    # retranslateUi

