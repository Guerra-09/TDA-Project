import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Gui_Session(QMainWindow):
   
    def __init__(self):
        super().__init__()
        uic.loadUi("QTDesigner.ui", self)

if __name__== '__main__':
    app = QApplication(sys.argv)
    GUI = Gui_Session()
    GUI.show()
    sys.exit(app.exec_())

