from threading import Thread, Lock

from PySide2.QtCore import QObject, Signal, Slot, Qt

from DES import DES
from RSA import RSA
from Gui import Gui
from Communication import CommunicationTCP

class ChatApp(QObject):
    def __init__(self):
        self.ui = Gui()
        self.rsa = RSA()
        self.comm = CommunicationTCP()
        self.comm.setPublicKeyRSA(self.rsa.getMyPublicKey())
        self.des = DES()
        self.connectSignalSlot()
        pass

    def connectSignalSlot(self):
        self.comm.getIncomingConnection.connect(self.ui.incomingConnectionSlot)
        # self.comm.getMessageData.connect(self.ui.pushIncomingMsg)
        self.comm.getMessageData.connect(self.receiveMessage)
        self.comm.getAccRSAPubKey.connect(self.getAccRSAPubKey)

        # self.ui.message_textEdit.
        self.ui.send_pushButton.clicked.connect(lambda state: [self.sendMessage(self.ui.message_textEdit.toPlainText()),
                                                               self.ui.pushMsgToTextBrowser(self.ui.message_textEdit.toPlainText(), True)])
        self.ui.disconnect_all_pushButton.clicked.connect(self.comm.disconnectAllComm)
        self.ui.connect_to_client_pushButton.clicked.connect(self.comm.connectToServer)

        self.ui.host_lineEdit.editingFinished.connect(lambda : [self.comm.changeHostToConnect(self.ui.host_lineEdit.text())])
        self.ui.port_lineEdit.editingFinished.connect(lambda : [self.comm.changePortToConnect(self.ui.port_lineEdit.text())])
        self.ui.myport_lineEdit.editingFinished.connect(lambda : [self.comm.changeMyPortToConnect(self.ui.myport_lineEdit.text())])

    def getAccRSAPubKey(self, list_key):
        print("APP: ",list_key)
        self.rsa.setAcrossPublicKey((int(list_key[1]), int(list_key[2])))
        encrypted_msg = self.rsa.encryptMsg("DES_KEY" + self.des.getDesKey())
        print("APP : SENDING DES KEY", self.des.getDesKey())
        self.comm.sendMessage(encrypted_msg)

    # def getDESKey(self, key_):
    #     self.des.setDesKey(key_)

    def sendMessage(self, msg):
        print("APP : SENDING MSG TO ENC")
        encrypted_msg = self.des.encryptIntoString(msg)
        # encrypted_msg = self.rsa.encryptMsg(msg)
        self.comm.sendMessage(encrypted_msg)
        pass

    @Slot(str)
    def receiveMessage(self, msg):
        print("APP : RECEIVING MSG TO DEC")

        decrypted_msg_for_key = self.rsa.decryptMsg(msg)
        if decrypted_msg_for_key[:7] == "DES_KEY" and len(decrypted_msg_for_key) == 15:
            print("APP : GET DECODED DES KEY", decrypted_msg_for_key[7:])
            self.des.setDesKey(decrypted_msg_for_key[7:])
        else:
            decrypted_msg = self.des.decryptIntoString(msg)
            self.ui.pushIncomingMsg(decrypted_msg)
        pass