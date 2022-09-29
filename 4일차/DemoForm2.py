# DemoForm2.py 
# Demoform2.ui (화면단)-> Demoform.py (로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#화면로딩
form_class = uic.loadUiType("Demoform2.ui")[0]
#클래스정의(부모 클래스변경)
class DemoFrom(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    #시그널을 처리하는 슬롯메서드
    def firstClick(self):
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoFrom()
    demoWindow.show()
    app.exec_()

