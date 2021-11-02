from PySide2.QtGui import QTextCursor

# from kij_chat_form import Ui_Form
from PySide2.QtWidgets import QMessageBox

from chat_form_ui_resp import Ui_Form

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Slot, Signal

# from kij_chat_Ui import Ui_MainWindow

class Gui(Ui_Form):
    def __init__(self):
        super().__init__()
        self.Form = QtWidgets.QWidget()
        # self.Mw = QtWidgets.QMainWindow()
        self.setupUi(self.Form)
        # self.Mw.show()
        self.connectWidget()
        self.message_textBrowser.clear()
        self.Form.show()

        self.alignment_msg = 0
        self.counter = 1

    def connectWidget(self):
        # self.send_pushButton.clicked.connect(self.sendMsg)
        # self.host_lineEdit.textChanged.connect(lambda x: print("TEXT HOST ", x))
        pass

    # def sendMsg(self):
    #     # print("SENDING MSG ", end='')
    #     # print(self.message_textEdit.toPlainText())
    #     # self.pushMsgToTextBrowser("DSASD", True)
    #     # self.pushMsgToTextBrowser("DSASD", False)
    #     pass

    @Slot(str)
    def pushIncomingMsg(self, msg):
        self.pushMsgToTextBrowser(msg, False)

    def pushMsgToTextBrowser(self, msg, is_from_me):
        # self.message_textBrowser.text
        if is_from_me:
            self.message_textBrowser.append(msg + str(self.counter))
            cursor = self.message_textBrowser.textCursor()
            textBlockFormat = cursor.blockFormat()
            textBlockFormat.setAlignment(QtCore.Qt.AlignRight)
            cursor.mergeBlockFormat(textBlockFormat)
            self.message_textBrowser.setTextCursor(cursor)
            print(msg)

        else:
            self.message_textBrowser.append(msg + str(self.counter))
            cursor = self.message_textBrowser.textCursor()
            textBlockFormat = cursor.blockFormat()
            textBlockFormat.setAlignment(QtCore.Qt.AlignLeft)
            cursor.mergeBlockFormat(textBlockFormat)
            self.message_textBrowser.setTextCursor(cursor)
            print(msg)

        self.counter += 1

    @Slot(str)
    def incomingConnectionSlot(self, ip_client):
        print("GUI : SLOT INCOMING CONN", ip_client)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setIcon(Warning)
        msg.setText("Ada Koneksi Masuk..")
        msg.setInformativeText(str(ip_client))
        msg.setWindowTitle("Koneksi Baru")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)

        retval = msg.exec_()
