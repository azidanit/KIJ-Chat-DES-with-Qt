from threading import Thread, Lock

from PySide2.QtCore import QObject, Signal, Slot

from Gui import Gui

class ChatApp(QObject):
    def __init__(self):
        self.ui = Gui()

        pass

