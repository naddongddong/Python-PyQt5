import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

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
        
        self.widget_label_1 = QWidget(self.main_widget)
        self.widget_label_1.setGeometry(0,60,500,70)
        self.widget_label_1.setStyleSheet('background-color: skyblue;')
        
        self.label_1 = QLabel(self.widget_label_1)
        self.label_1.setGeometry(10,20,240, 30)
        self.label_1.setStyleSheet('background-color: white; border:1px solid black;')
        self.label_1.setText('0')
        
    def button_function(self, i):
        print('clicked : '+ str(i))
        self.label_1.setText('Button '+str(i)+' clicked !')
    
def StartGUI():
    app = QApplication(sys.argv)
    temp = Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
