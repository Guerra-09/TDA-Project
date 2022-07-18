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

#class Gui(QMainWindow):

#def __init__(self) -> None:
       #super(Gui,self).__init__()
       #uic.loadUi("QtDesiginer.ui", self)
       #self.show()

#def main():
    #app = QApplication([])
    #window = Gui()
    #app.exit()

#if __name__=="__main__":
    #main()


