from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import sys
import gui_base

class GUI(QtWidgets.QMainWindow, gui_base.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    gui = ExampleApp()
    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
    
