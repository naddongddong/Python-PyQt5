import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setWindowTitle("Create new window")
        self.setFixedSize(500,400)
        self.setWindowIcon(QIcon('icon.png'))
        
        self.mainUI()
        self.show()
    
    def mainUI(self):
        self.btn = QPushButton("button", self)
        self.btn.clicked.connect(self.button_func)
    
    def button_func(self):
        self.new_widget = QWidget()
        self.new_widget.setWindowIcon(QIcon('icon.png'))
        self.new_widget.setFixedSize(400,300)
        self.new_widget.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
