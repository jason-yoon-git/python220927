# DemoForm.py 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

form_class = uic.loadUiType("Demoform.ui")[0]

class DemoFrom(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoFrom()
    demoWindow.show()
    app.exec_()

