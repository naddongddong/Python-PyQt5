import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Window title")
        self.setGeometry(650,350,500,400)
        
        self.Main_Widget()
        self.show()
        
    def Main_Widget(self):
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,500,400)
        self.main_widget.setStyleSheet('background-color: white;')
        
        self.pb_1 = QPushButton('Button 1', self)
        self.pb_1.setGeometry(10,10,120,50)
        
        
def StartGUI():
    app = QApplication(sys.argv)
    temp = Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
