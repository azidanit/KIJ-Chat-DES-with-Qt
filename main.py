from PySide2 import QtCore, QtGui, QtWidgets

from ChatApp import ChatApp


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chat_app = ChatApp()
    # Form = QtWidgets.QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    sys.exit(app.exec_())