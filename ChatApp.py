from threading import Thread, Lock

from PySide2.QtCore import QObject, Signal, Slot

from Gui import Gui
from Communication import CommunicationTCP

class ChatApp(QObject):
    def __init__(self):
        self.ui = Gui()
        self.comm = CommunicationTCP()

        self.connectSignalSlot()
        pass

    def connectSignalSlot(self):
        self.comm.getIncomingConnection.connect(self.ui.incomingConnectionSlot)
        self.comm.getMessageData.connect(self.ui.pushIncomingMsg)

        self.ui.send_pushButton.clicked.connect(lambda state: [self.comm.sendMessageToClient(self.ui.message_textEdit.toPlainText()),
                                                               self.ui.pushMsgToTextBrowser(self.ui.message_textEdit.toPlainText(), True)])

        self.ui.host_lineEdit.textChanged.connect(self.comm.changeHostToConnect)
        self.ui.port_lineEdit.textChanged.connect(self.comm.changePortToConnect)
