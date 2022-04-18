import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first_login', self)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    Yury = Program()
    Yury.show()
    sys.exit(app.exec_())