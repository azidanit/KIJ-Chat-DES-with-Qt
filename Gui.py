from PySide2.QtGui import QTextCursor

from kij_chat_form import Ui_Form
from PySide2 import QtCore, QtGui, QtWidgets

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
        self.send_pushButton.clicked.connect(self.sendMsg)
        pass

    def sendMsg(self):
        print("SENDING MSG ", end='')
        print(self.message_textEdit.toPlainText())
        self.pushMsgToTextBrowser("DSASD", True)
        self.pushMsgToTextBrowser("DSASD", False)
        pass

    def pushMsgToTextBrowser(self, msg, is_from_me):
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
