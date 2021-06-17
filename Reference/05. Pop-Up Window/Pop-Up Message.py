import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        
        self.btn = QPushButton("pop-up message",self)
        self.btn.setGeometry(160,160,200,30)
        self.btn.clicked.connect(self.button_function)
        
        self.show()
       
    def button_function(self):
        self.pop_up_message('Hello')
        
    def pop_up_message(self, str):
        msg = QMessageBox()
        msg.setWindowTitle("Pop-Up Message")
        msg.setText(str)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
