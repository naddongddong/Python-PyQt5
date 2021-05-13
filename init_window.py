import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Window title")
        self.setGeometry(650,350,500,400)
        self.setFixedSize(500,400)
        
        self.Main_Widget()
        
        self.show()
        
    def Main_Widget(self):
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,500,400)
        self.main_widget.setStyleSheet('background-color: #b0b0b0;')
        
        self.widget_btn_1 = QWidget(self.main_widget)
        self.widget_btn_1.setGeometry(0,0,500,60)
        self.widget_btn_1.setStyleSheet('background-color: white; border-bottom:1px solid blue;')

        self.pb = []
        for i in range(0, 3):
            self.pb.append(QPushButton("Button "+str(i+1), self.widget_btn_1))
            self.pb[i].setGeometry(10 + 90*i, 10,80,40)
            self.pb[i].setStyleSheet('background-color: white; border:1px solid black; color: black;')
            self.pb[i].clicked.connect(lambda _, num=i: self.button_function(num+1))
            #self.pb[i].clicked.connect(lambda num: self.button_function(i+1))  ##wrong
            
    def button_function(self, i):
        print('clicked : '+ str(i))
    
def StartGUI():
    app = QApplication(sys.argv)
    temp = Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
