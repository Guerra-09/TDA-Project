from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGui(QMainWindow):

    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi("ui/bossFrame.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = MyGui()
    app.exec()

if __name__ == '__main__':
    main()